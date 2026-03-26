from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()


def get_embeddings():
    """
    Returns FREE embedding model (BGE) instance.
    """

    model_name = "BAAI/bge-base-en-v1.5"

    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={
            "device": "cpu"   # change to "cuda" if you have GPU
        },
        encode_kwargs={
            "normalize_embeddings": True
        }
    )

    return embeddings