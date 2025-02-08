import argparse
from langchain_community.vectorstores.faiss import FAISS
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
    n: int,
) -> FAISS:
    retriever = vector_store.as_retriever(search_kwargs={"k": n + 1})
    return retriever


def parse_args():
    parser = argparse.ArgumentParser(description="swimmer for paper")
    parser.add_argument(
        "--embedding_model_name",
        type=str,
        default="intfloat/multilingual-e5-large-instruct",
    )
    parser.add_argument("--vector_store_path", type=str, default="./data/db")
    return parser.parse_args()


def main():
    args = parse_args()

    vector_store = create_vector_store(
        args.vector_store_path,
        args.embedding_model_name,
    )

    queries = [
        "Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models",
    ]

    suggestions = list()
    for query in queries:
        retriever = setup_retriever(vector_store, n=10)

        relevant_docs = retriever.get_relevant_documents(query)
        for relevant_doc in relevant_docs:
            content = relevant_doc.page_content
            url = content.split("<BEGIN_URL>")[-1].split("<END_URL>")[0]
            abstract = content.split("\\n")[-1].split("<BEGIN_URL>")[0]
            title = content.split("\\n")[0]

            suggestion = dict()
            suggestion["title"] = title
            suggestion["url"] = url
            suggestion["abstruct"] = abstract
            suggestion["query"] = query
            suggestions.append(suggestion)

    for suggestion in suggestions:
        for key, value in suggestion.items():
            print(f"{key}: {value}")
        print("-" * 50)


if __name__ == "__main__":
    main()
