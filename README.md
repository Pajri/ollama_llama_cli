# LLM Ollama LLama Console App

This is a console application for text embedding and querying to ollama using  llama3.1 model. <br/>
Source: 
[https://github.com/ThomasJay/RAG/tree/main](https://github.com/ThomasJay/RAG/tree/main)

## Pre Requisite
1. Download ollama: [https://ollama.com/download/windows](https://ollama.com/download/windows)
2. Run model `llama3.1'. <br/>Run this command on terminal
    ```
    ollama run llama 3.1
    ```
    You can check this page for more detailed instruction: [https://github.com/ollama/ollama](https://github.com/ollama/ollama)

## Installation

To install this project, follow these steps:

1. Clone the repository
2. Navigate to the project directory:
3. Create a virtual environment (optional but recommended):
    ```bash 
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows 
        ```bash 
        python -m venv venv
        ```
    - On macOS/Linux
        ```bash 
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
6. Install the console app (`ollama_llama`)
    ```
    pip install .
    ```
## Usage
To run the application, use the following steps:
1. Copy pdf files to `ollama_llama/pdf` folder
    ```
    ollama_llama/
    ├── pdf/
    │   ├── doc1.pdf
    │   ├── doc2.pdf
    │   ├── doc3.pdf
    │   └── ... .pdf
    ```
2. Run this command to do text embedding
    ```bash
    ollama_llama embed
    ```
3. Send query to the console app
    ```bash
    ollama_llama ask query
    ```
    Example:
    ```bash
    ollama_llama ask "give me example of supervised learning"
    ```

