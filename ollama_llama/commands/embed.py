import os

from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from ollama_llama.constants.constants import DB_FOLDER_PATH

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1024, chunk_overlap=80, length_function=len, is_separator_regex=False
)

embedding = FastEmbedEmbeddings()

def run():
    pdf_folder = "ollama_llama/pdf"  # Directory containing the PDF files

    # List all PDF files in the pdf_folder
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    
    if not pdf_files:
        print("No PDF files found in the folder.")
        return

    all_chunks = []
    all_docs = []

    for pdf_file in pdf_files:
        print('-----------------------------------------')
        # Full path to the current PDF file
        save_file = os.path.join(pdf_folder, pdf_file)
        print(f"Processing file: {save_file}")
        
        # Load the PDF and split it into chunks
        loader = PDFPlumberLoader(save_file)
        docs = loader.load_and_split()
        print(f"Docs length for {save_file} = {len(docs)}")

        chunks = text_splitter.split_documents(docs)
        print(f"Chunks length for {save_file} = {len(chunks)}")

        # Append chunks and docs for later embedding
        all_chunks.extend(chunks)
        all_docs.extend(docs)

        print('-----------------------------------------')

    print(f"Total docs from all PDFs = {len(all_docs)}")
    print(f"Total chunks from all PDFs = {len(all_chunks)}")

    # Start creating the vector store with all chunks from all PDFs
    print('Start creating the vector store')
    vector_store = Chroma.from_documents(
        documents=all_chunks,
        embedding=embedding,
        persist_directory=DB_FOLDER_PATH
    )
    print('Vector store created')

    # Persist the vector store
    print('Persisting the vector store')
    vector_store.persist()
    print('Vector store persisted')

    # Final response
    response = {
        "status": "Successfully Uploaded",
        "total_files": len(pdf_files),
        "total_docs": len(all_docs),
        "total_chunks": len(all_chunks),
    }

    print(f"Status: {response['status']}")
    print(f"Total Files Processed: {response['total_files']}")
    print(f"Total Docs Processed: {response['total_docs']}")
    print(f"Total Chunks Processed: {response['total_chunks']}")
