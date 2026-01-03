# 💬 e-commerce chatbot (Gen AI RAG project using LLama3.3 and GROQ)

This is POC of an intelligent chatbot tailored for an e-commerce platform, enabling seamless user interactions by accurately identifying the intent behind user queries. It leverages real-time access to the platform's database, allowing it to provide precise and up-to-date responses.

This chatbot currently supports two intents:

- **faq**: Triggered when users ask questions related to the platform's policies or general information. eg. Is online payment available?
- **sql**: Activated when users request product listings or information based on real-time database queries. eg. Show me all nike shoes below Rs. 3000.


![product screenshot](app/resources/product-ss.png)


## Architecture
![architecture diagram of the e-commerce chatbot](app/resources/architecture-diagram.png)


## 🛠️ Skills & Technologies Used

- **Python**: Core programming language for backend logic.
- **Streamlit**: For building the interactive web UI.
- **LangChain / Semantic Routing**: For intent detection and routing user queries.
- **LLMs (GROQ, LLama3.3)**: For natural language understanding, SQL generation, and answer synthesis.
- **RAG (Retrieval-Augmented Generation)**: For combining LLMs with real-time database querying.
- **SQLite & Pandas**: For efficient data storage, retrieval, and manipulation.
- **dotenv**: For secure management of API keys and environment variables.
- **HuggingFace Transformers**: For semantic encoding and intent classification.
- **Prompt Engineering**: For crafting effective system and user prompts.
- **RESTful API Integration**: For connecting with external LLM services.
- **Version Control (Git & GitHub)**: For project management and collaboration.
- **Markdown**: For documentation and reporting.

### Set-up & Execution

1. Run the following command to install all dependencies. 

    ```bash
    pip install -r app/requirements.txt
    ```

1. Inside app folder, create a .env file with your GROQ credentials as follows:
    ```text
    GROQ_MODEL=<Add the model name, e.g. llama-3.3-70b-versatile>
    GROQ_API_KEY=<Add your groq api key here>
    ```

1. Run the streamlit app by running the following command.

    ```bash
    streamlit run app/main.py
    ```

---
