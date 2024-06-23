# LangChain Chatbot with Streamlit GUI

Welcome to the GitHub repository for the LangChain Chatbot with Streamlit GUI! This project offers a thorough guide for building a powerful chatbot capable of website interaction, information extraction, and user-friendly communication through an intuitive interface. By leveraging LangChain 0.1.0 and integrating it with a Streamlit GUI, this repository enhances the user experience for chatbot development.

## Features

### Website Interaction
The chatbot employs the latest version of LangChain to interact with and extract information from various websites. This functionality allows the chatbot to provide real-time responses and accurate data retrieval from the web, enhancing its ability to answer questions and engage with users effectively.

### Large Language Model Integration
This project is compatible with several advanced language models, including GPT-4, Mistral, Llama2, and ollama. While the code defaults to using GPT-4, you can easily modify it to integrate with any other supported model, allowing for flexibility based on specific requirements.

### Streamlit GUI
The chatbot features a clean and intuitive interface built with Streamlit, making it accessible to users of all technical levels. The GUI simplifies interactions, allowing users to engage with the chatbot seamlessly and efficiently.

### Python-Based
The entire project is written in Python, ensuring ease of use and integration with other Python-based tools and libraries. Python's extensive ecosystem of libraries and frameworks further enhances the development and functionality of the chatbot.

## How Retrieval-Augmented Generation (RAG) Works
![](https://github.com/alejandro-ao/chat-with-websites/blob/master/docs/HTML-rag-diagram.jpg)
Retrieval-Augmented Generation (RAG) enhances the knowledge of a large language model (LLM) by incorporating additional information. The process involves:

1. **Vectorizing Text**: All the text intended for use as augmented knowledge is vectorized.
2. **Similarity Search**: The vectorized text is searched to find content most similar to the input prompt.
3. **Prompt Augmentation**: The retrieved similar text is passed to the LLM as a prefix, augmenting its knowledge and improving the relevance and accuracy of its responses.

## How This RAG System Works

This Retrieval-Augmented Generation (RAG) system leverages a Large Language Model (LLM) to create webpages based on user queries and retrieved information. Here's a breakdown of the process:

1. **Data Collection:** Website data is collected, likely using tools like BeautifulSoup for scraping HTML content.

2. **Text Processing:** The collected text is split into smaller chunks and vectorized. Vectorization transforms text into numerical representations for efficient semantic search.

3. **Query Embedding:** The user's query is also vectorized, allowing for semantic comparison with the text chunks.

4. **Semantic Search:** The system searches for text chunks most relevant to the user's query based on vector similarity. This ensures retrieved information aligns with the user's intent. 

5. **Ranked Results:** The retrieved text chunks are ranked based on their relevance scores.

6. **LLM Integration:** The ranked text chunks and the user's query are fed into the LLM. The LLM, trained on a massive dataset of text and code, utilizes this information to generate the final webpage content.

This RAG system offers several advantages:

* **Relevance:** Leverages semantic search to retrieve highly relevant information.
* **Grounded in Reality:** Incorporates real-world information from the website.
* **LLM Power:** Utilizes the capabilities of an LLM for content generation.

By combining these elements, this RAG system aims to provide users with webpages that are both informative and tailored to their specific needs.
## Installation

To set up the project, follow these steps:

1. **Clone the Repository**:
    ```sh
    git clone [repository-link]
    cd [repository-directory]
    ```

2. **Install Required Packages**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**:
    Create a `.env` file with the following content:
    ```plaintext
    OPENAI_API_KEY=[your-openai-api-key]
    ```

## Usage

To run the Streamlit app, use the command:
```sh
streamlit run app.py
```
This will launch the chatbot interface, allowing you to interact with it through your web browser.

## Contributing

This repository supports the accompanying YouTube video tutorial. Contributions for fixing bugs or typos are welcome, but other pull requests are not currently being accepted. This ensures the material remains consistent with the tutorial content.

## License

This project is licensed under the MIT License. For more details, see the LICENSE file included in the repository.

## Note

This project is intended for educational and research purposes. Please ensure compliance with the terms of use and guidelines of the APIs and services utilized within this project.

## Acknowledgments

We hope this repository aids you in exploring AI and chatbot development. For more tutorials and information, visit [Your YouTube Channel].

Happy Coding! 🚀👨‍💻🤖

If you find this repository useful, don’t forget to star it!
