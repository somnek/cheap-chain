import pickle

from langchain.document_loaders import OnlinePDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from rich import print


def ingest_doc():
  """Get documents from web pages."""
  loader = OnlinePDFLoader('https://arxiv.org/pdf/2302.08399.pdf')
  raw_documents = loader.load()
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
  )
  documents = text_splitter.split_documents(raw_documents)
  model_name = 'sentence-transformers/all-mpnet-base-v2'
  hf = HuggingFaceEmbeddings(model_name=model_name)
  vectorstore = FAISS.from_documents(documents=documents, embedding=hf)

  # Save vectorstore
  with open('vectorstore.pkl', 'wb') as f:
    pickle.dump(vectorstore, f)

if __name__ == '__main__':
  ingest_doc()
