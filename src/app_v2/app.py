import os
import pandas as pd
import streamlit as st
from langchain_community.vectorstores.faiss import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


st.set_page_config(page_title="ICLR2025 Paper Search", layout="wide")
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"


@st.cache_resource
def create_vector_store(
    vector_store_path: str,
    embedding_model_name: str,
) -> FAISS:
    embedding_model = HuggingFaceEmbeddings(model_name=embedding_model_name)
    vector_store = FAISS.load_local(
        folder_path=vector_store_path,
        embeddings=embedding_model,
        allow_dangerous_deserialization=True,
    )
    return vector_store


def grab_topk(
    input_text: str,
    vector_store: FAISS,
    top_k: int,
    id2paper: dict,
) -> pd.DataFrame:
    retriever = vector_store.as_retriever(search_kwargs={"k": top_k + 1})
    relevant_docs = retriever.get_relevant_documents(input_text)

    abstracts = list()
    titles = list()
    urls = list()
    for relevant_doc in relevant_docs:
        content = relevant_doc.page_content
        id = content.split("<BEGIN_ID>")[-1].split("<END_ID>")[0]
        title = id2paper[id]["title"]["value"]

        abstracts.append(abstract + "...")
        titles.append(title)
        urls.append(url)
    return pd.DataFrame({"title": titles, "abstract": abstracts, "url": urls})


if __name__ == "__main__":
    vector_store_path = "db"
    embedding_model_name = "intfloat/multilingual-e5-large-instruct"
    vector_store = create_vector_store(
        vector_store_path,
        embedding_model_name,
    )

    id2paper = load_id2paper()
    st.markdown("## ICLR2025")
    st.markdown("- list of papers (https://iclr.cc/Downloads/2025)")
    st.markdown(
        "- repository (https://github.com/ohashi3399/paper-sonar?tab=readme-ov-file)"
    )
    input_text = st.text_input(
        "query",
        "",
        placeholder="Enter the keywords you are interested in...",
    )
    top_k = st.number_input("top_k", min_value=1, value=10, step=1)

    if st.button("検索"):
        stripped_input_text = input_text.strip()
        if stripped_input_text.startswith("--name "):
            df = grab_same_authors(
                stripped_input_text,
                vector_store,
                top_k,
                id2paper,
            )
        else:
            df = grab_topk(
                stripped_input_text,
                vector_store,
                top_k,
                id2paper,
            )
        st.table(df)
