def chunk_text(text, chunk_size=500, overlap=50):
    """
    Splits text into chunks for better retrieval.
    """
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks


def store_resume(index, embeddings, resume_text, candidate_id):
    """
    Stores resume in Pinecone with candidate_id to avoid duplicates.
    """

    # 🔹 Step 1: Chunk resume
    chunks = chunk_text(resume_text)

    # 🔹 Step 2: Create embeddings
    vectors = embeddings.embed_documents(chunks)

    # 🔹 Step 3: Prepare data
    pinecone_data = []

    for i, (chunk, vector) in enumerate(zip(chunks, vectors)):
        pinecone_data.append({
            "id": f"{candidate_id}_{i}",   # 🔥 FIXED ID
            "values": vector,
            "metadata": {
                "text": chunk,
                "chunk_id": i,
                "candidate_id": candidate_id
            }
        })

    # 🔹 Step 4: Upsert (will overwrite if same ID)
    index.upsert(pinecone_data)


def search_resume(index, embeddings, jd_text, candidate_id, top_k=5):
    """
    Searches Pinecone for relevant chunks ONLY for a specific candidate.
    """

    # 🔥 BGE instruction (IMPORTANT)
    query = "Represent this job description for retrieving relevant resumes: " + jd_text

    # 🔹 Step 1: Query embedding
    query_vector = embeddings.embed_query(query)

    # 🔹 Step 2: Search with FILTER (IMPORTANT)
    results = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True,
        filter={"candidate_id": {"$eq": candidate_id}}  # 🔥 KEY FIX
    )

    # 🔹 Step 3: Extract text
    retrieved_chunks = [
        match["metadata"]["text"]
        for match in results["matches"]
    ]

    return retrieved_chunks