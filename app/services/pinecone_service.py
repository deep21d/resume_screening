import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = "resume-index"


def init_pinecone():
    """
    Initialize Pinecone client
    """
    return Pinecone(api_key=PINECONE_API_KEY)


def create_index_if_not_exists(pc):
    """
    Creates Pinecone index if it does not exist
    """

    existing_indexes = [index.name for index in pc.list_indexes()]

    if INDEX_NAME not in existing_indexes:
        print(f"Creating Pinecone index: {INDEX_NAME}")

        pc.create_index(
            name=INDEX_NAME,
            dimension=768,   # BGE embedding size
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )


def get_index(pc):
    """
    Returns Pinecone index (creates if missing)
    """

    create_index_if_not_exists(pc)

    return pc.Index(INDEX_NAME)