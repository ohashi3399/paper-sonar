import json
import argparse
from langchain_community.vectorstores.faiss import FAISS
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEmbeddings


def create_vector_store(
    vector_store_path: str,
    embedding_model_name: str,
) -> FAISS:

    embedding_model = HuggingFaceEmbeddings(
        model_name=embedding_model_name,
    )

    vector_store = FAISS.load_local(
        folder_path=vector_store_path,
        embeddings=embedding_model,
        allow_dangerous_deserialization=True,
    )

    return vector_store


def setup_retriever(
    vector_store: FAISS,
) -> RetrievalQA:
    retriever = vector_store.as_retriever(search_kwargs={"k": 10})
    return retriever


def parse_args():
    parser = argparse.ArgumentParser(description="Benchamrk for sake RAG")
    # parser.add_argument("--model_name", type=str, required=True)
    # parser.add_argument("--embedding_model_name", type=str, required=True)
    # parser.add_argument("--vector_store_path", type=str, required=True)
    # parser.add_argument("--path_benchmark", type=str, required=True)
    parser.add_argument(
        "--model_name",
        type=str,
        default="./model/gemma2-2b-it-jpn/gemma-2-2b-jpn-it-Q8_0.gguf",
    )
    parser.add_argument(
        "--embedding_model_name",
        type=str,
        default="BAAI/bge-m3",
    )
    parser.add_argument(
        "--vector_store_path",
        type=str,
        default="./data/db",
    )
    parser.add_argument(
        "--path_benchmark",
        type=str,
        default="./data/eval/benchmark.jsonl",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    vector_store = create_vector_store(
        args.vector_store_path,
        args.embedding_model_name,
    )
    queries = [
        "Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models"
    ]

    contexts = list()
    for query in queries:
        retriever = setup_retriever(vector_store)

        relevant_docs = retriever.get_relevant_documents(query)
        for relevant_doc in relevant_docs:
            candidate = dict()
            candidate["query"] = query
            # candidate["filename"] = relevant_doc.metadata["source"]
            # candidate["content"] = relevant_doc.page_content
            contexts.append(candidate)


if __name__ == "__main__":
    main()
