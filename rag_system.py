from langchain_community.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain.document_loaders import TextLoader
from langchain.chains import RetrievalQA
from langchain.llms import Ollama

def build_rag():

    loader = TextLoader("knowledge_base/job_requirements.txt")
    documents = loader.load()

    embeddings = OllamaEmbeddings(model="llama3")

    db = Chroma.from_documents(documents, embeddings)

    llm = Ollama(model="llama3")

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=db.as_retriever()
    )

    return qa

qa = build_rag()

context = qa.run("What skills are required for this job?")