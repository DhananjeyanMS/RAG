from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI


def process_text(full_text, query):
    # split into chunks
    char_text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
    text_chunks = char_text_splitter.split_text(full_text)

    # create embeddings
    embeddings = OpenAIEmbeddings()
    docsearch = FAISS.from_texts(text_chunks, embeddings)

    llm = OpenAI()
    chain = load_qa_chain(llm, chain_type="stuff")

    # process user query
    docs = docsearch.similarity_search(query)
    response = chain.run(input_documents=docs, question=query)
    return response
