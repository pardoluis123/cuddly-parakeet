import os 
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from utilities import load_openai_API
# from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain_openai import OpenAIEmbeddings
import pickle

def RAG_code(input_script):
    '''implement RAG processes if given input code as script

    Parameters
    ----------
    input_script:str|st.file_uploader,default=None,
        Path to an input file or the st.file_uploader object of interest


    Notes
    -----



    Examples
    --------



    Notes
    -----



    '''

    load_openai_API()
    script_content = input_script.getvalue().decode("utf-8")
    script_doc = Document(page_content=script_content, metadata={"source": input_script.name})
    script_docs = [script_doc]
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_docs = splitter.split_documents(script_docs)

    # Embed and index
    embedding_model = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(split_docs, embedding=embedding_model)
    vectorstore.save_local("output/faiss_index_script")

    return


if __name__=='__main__':
    print('running just the rag pipeline to check')

    #first load our API in 
    load_openai_API()

    os._exit(0)


    pdf_path = "C:/Users/jrose01/projects/ai-data-analysis-assistant/basic_epidemiology_chaps234.pdf"
    # pdf_loader = UnstructuredPDFLoader(pdf_path, mode="hi_res")
    pdf_loader = PyMuPDFLoader(pdf_path)
    pdf_docs = pdf_loader.load()

    # check to see if it worked
    print(len(pdf_docs))
    print(pdf_docs[0].page_content)

    # Combine both
    # all_docs = pdf_docs + url_docs

    # Split documents
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_docs = splitter.split_documents(pdf_docs)

    # Create vector store
    embedding_model = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(pdf_docs, embedding=embedding_model)

    # check to see if it worked
    print(vectorstore.index.ntotal)

    # Save vectorstore and metadata
    vectorstore.save_local("vectorstore/faiss_index")
    with open("vectorstore/doc_metadata.pkl", "wb") as f:
        pickle.dump(pdf_docs, f)

    # View the raw vectors (numpy array)
    # Get the FAISS index object
    faiss_index = vectorstore.index

    # How many vectors are stored?
    print(f"Total vectors: {faiss_index.ntotal}")

    # View the raw vectors (numpy array)
    vectors = faiss_index.reconstruct_n(0, faiss_index.ntotal)

    print(f"Shape of embedding matrix: {vectors.shape}")
    print("Sample embedding (first vector):")
    print(vectors[0])

    # save embeddings to an numpy array
    np.save("vectorstore/rag_embeddings.npy", vectors)


    print("✅ Vector store with PDF successfully built and saved.")

    # add reference section from documents to the vector store
    ids = vectorstore.add_documents(documents=pdf_docs)

    # Check pdf references
    results = vectorstore.similarity_search("What are the vector ids?")
    print(results[0])