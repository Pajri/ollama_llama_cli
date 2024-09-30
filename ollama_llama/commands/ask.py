import time

from langchain_community.vectorstores import Chroma
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from ollama_llama.constants.constants import DB_FOLDER_PATH

llm = Ollama(model="llama3.1")
embedding = FastEmbedEmbeddings()
raw_prompt = PromptTemplate.from_template(
"""
    <s>[INST] Anda adalah asisten yang pandai mencari dokumen. Jika Anda tidak memiliki jawaban dari informasi yang disediakan, katakan demikian. [/INST] </s>
    [INST] {input}
           Konteks: {context}
           Jawaban:
    [/INST]
"""

)

def run(question):
    query = question

    print(f"query: {query}")

    print("Loading vector store")
    vector_store = Chroma(persist_directory=DB_FOLDER_PATH, embedding_function=embedding)
    
    print("Creating chain")
    print("- Retrieve vector store")
    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": 20,
            "score_threshold": 0.1,
        },
    )
    
    print("- Create document chain")
    document_chain = create_stuff_documents_chain(llm, raw_prompt)

    print("- Create retrieval chain")
    chain = create_retrieval_chain(retriever, document_chain)
    
    print('Invoke chain')
    start_time = time.perf_counter()

    result = chain.invoke({"input": query})
 
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")

    print("--------------------------------")
    print("answer:")
    print(result["answer"])
    print("--------------------------------")


    sources = []
    for doc in result["context"]:
        sources.append(
            {"source": doc.metadata["source"]}
        )

    print("--------------------------------")
    print("sources")
    print(sources)
    print("--------------------------------")
    print("result")
    print(result)
    print("--------------------------------") 
    