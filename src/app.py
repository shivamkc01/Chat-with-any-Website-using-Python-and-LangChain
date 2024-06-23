import os
import streamlit as st 
from langchain_core.messages import HumanMessage, AIMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv

load_dotenv()


st.set_page_config(page_title="Chat with websites", page_icon="🕸️",layout="wide")
st.title("🌐 Chat with websites")
st.write("Use LangChain to interact with provided websites via Streamlit.")




def get_vectorstore_from_url(website_url):
  # get the test in document format
  loader = WebBaseLoader(website_url)
  document = loader.load()

  text_splitter = RecursiveCharacterTextSplitter()
  document_chunks=text_splitter.split_documents(document)

  # create a vectorstore from the chunks
  vector_store = Chroma.from_documents(document_chunks,OllamaEmbeddings(model="llama3:8b"))

  return vector_store

def get_context_retriever_chain(vector_store):
  llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama3-70b-8192",
        )
  
  retriever = vector_store.as_retriever()
  prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder('chat_history'),
    ("user", "{input}"),
    ("user", "Given the above converation, generate a search query to look up in order to get information relivent to the converstation.")
  ])

  retriever_chain = create_history_aware_retriever(llm, retriever, prompt)

  return retriever_chain

def get_conversational_rag_chain(retriever_chain):
  llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama3-70b-8192",
        )
  
  prompt = ChatPromptTemplate.from_messages([
    ('system' , "Answer the user's questions based on the below context:\n\n{context}"),
    MessagesPlaceholder('chat_history'),
    ("user", "{input}"),
  ])


  stuff_documents_chain = create_stuff_documents_chain(llm, prompt)
  
  return create_retrieval_chain(retriever_chain, stuff_documents_chain)

def get_response(user_input):
  retriever_chain = get_context_retriever_chain(st.session_state.vector_store)

  conversation_rag_chain = get_conversational_rag_chain(retriever_chain)

  response = conversation_rag_chain.invoke({
    "chat_history" : st.session_state.chat_history,
    "input" : user_input
  })

  return response['answer']


with st.sidebar:
  st.header("Settings")
  website_url = st.text_input("Website URL")

if website_url is None or website_url == "":
  st.info("Please enter a website URL to get started.")
else:
  if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
          AIMessage(content="Hey there! I'm Shivam Bot. How can I assist you with your website today? you can ask me any info from given website") ,
        ]
  
  if "vector_store" not in st.session_state:
    st.session_state.vector_store = get_vectorstore_from_url(website_url)
  # CREATE CONVERSATION STORE

  retriever_chain = get_context_retriever_chain(st.session_state.vector_store)

  conversation_rag_chain = get_conversational_rag_chain(retriever_chain)


  user_query = st.chat_input("Type your message here...")
  # User input
  if user_query is not None and user_query != "":
    response = conversation_rag_chain.invoke({
      "chat_history" : st.session_state.chat_history,
      "input" : user_query
    })
    answer_ai = response['answer']
    # st.write(response)
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    st.session_state.chat_history.append(AIMessage(content=answer_ai))

    # FOR DEBUGGING PURPUSE
    # retrieved_dcomments = retriever_chain.invoke({
    #   "chat_history" : st.session_state.chat_history,
    #   'input' : user_query
    # })

    # st.write(retrieved_dcomments)

  # Conversation
  for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
      with st.chat_message("AI"):
        st.write(message.content)

    elif isinstance(message, HumanMessage):
      with st.chat_message("Human"):
        st.write(message.content)


# DEBUDDING THE CHAT HISTPORY
# with st.sidebar:
#   st.text("Chat History:")
#   st.write(st.session_state.chat_history)