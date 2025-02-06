import argparse
from langchain_community.vectorstores.faiss import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader


def parse_args():
    parser = argparse.ArgumentParser(description="build DB")
    parser.add_argument("--data_dir", type=str, default="./data/txt")
    parser.add_argument("--index_path", type=str, default="./data/db")
    parser.add_argument("--model_name", type=str, default="BAAI/bge-m3")
    parser.add_argument("--chunk_size", type=int, default=500)
    parser.add_argument("--chunk_overlap", type=int, default=20)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    loader = DirectoryLoader(args.data_dir)
    embedding_model = HuggingFaceEmbeddings(model_name=args.model_name)

    split_texts = loader.load_and_split(
        text_splitter=RecursiveCharacterTextSplitter(
            chunk_size=args.chunk_size,
            chunk_overlap=args.chunk_overlap,
        )
    )

    index = FAISS.from_documents(
        documents=split_texts,
        embedding=embedding_model,
    )
    index.save_local(folder_path=args.index_path)
