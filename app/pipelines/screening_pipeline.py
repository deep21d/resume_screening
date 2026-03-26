from app.services.resume_service import parse_resume
from app.services.jd_service import parse_jd
from app.services.embedding_service import get_embeddings
from app.services.pinecone_service import init_pinecone, get_index
from app.services.retriever_service import store_resume, search_resume
from app.services.llm_service import get_llm
from app.services.evaluation_service import evaluate_candidate

import hashlib


def generate_candidate_id(resume_text: str) -> str:
    """
    Generates a unique ID for each resume to avoid duplicates.
    """
    return hashlib.md5(resume_text.encode()).hexdigest()


def run_screening_pipeline(resume_path: str, jd_text: str):
    """
    Full pipeline to evaluate resume against job description.
    """

    # 🔹 Step 1: Parse Resume
    resume_text = parse_resume(resume_path)

    # 🔹 Step 2: Generate unique candidate ID
    candidate_id = generate_candidate_id(resume_text)

    # 🔹 Step 3: Parse JD (structured)
    jd_data = parse_jd(jd_text)

    # 🔹 Step 4: Initialize Pinecone (NO index creation here)
    pc = init_pinecone()
    index = get_index(pc)

    # 🔹 Step 5: Load Embeddings
    embeddings = get_embeddings()

    # 🔹 Step 6: Store Resume (with ID to avoid duplicates)
    store_resume(index, embeddings, resume_text, candidate_id)

    # 🔹 Step 7: Retrieve Relevant Chunks
    retrieved_chunks = search_resume(index, embeddings, jd_text, candidate_id)

    # 🔹 Step 8: Initialize LLM
    llm = get_llm()

    # 🔹 Step 9: Evaluate Candidate
    result = evaluate_candidate(
        llm=llm,
        resume_text=resume_text,
        jd_text=jd_text,
        retrieved_chunks=retrieved_chunks
    )

    return {
        "candidate_id": candidate_id,
        "jd_structured": jd_data,
        "evaluation": result
    }