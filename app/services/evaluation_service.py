import json
import re
from app.models.prompts import EVALUATION_PROMPT
from app.models.schemas import EvaluationResult


def extract_json(text: str) -> str:
    """
    Extracts JSON object from LLM response.
    """
    match = re.search(r"\{.*\}", text, re.DOTALL)
    return match.group(0) if match else text


def evaluate_candidate(llm, resume_text, jd_text, retrieved_chunks):
    """
    Evaluates candidate using LLM and returns structured result.
    """

    # 🔹 Step 1: Prepare context (limit size for safety)
    context = "\n".join(retrieved_chunks[:5])

    # 🔹 Step 2: Format prompt correctly
    prompt = EVALUATION_PROMPT.format(
        resume=resume_text[:5000],  # prevent huge input
        jd=jd_text,
        context=context
    )

    try:
        # 🔹 Step 3: Call LLM
        response = llm.invoke(prompt)
        response_text = response.content

        # 🔹 Step 4: Extract JSON safely
        clean_text = extract_json(response_text)

        # 🔹 Step 5: Convert to dict
        parsed_output = json.loads(clean_text)

        # 🔹 Step 6: Validate using schema
        validated_output = EvaluationResult(**parsed_output)

        return validated_output.model_dump()

    except Exception as e:
        return {
            "error": "Evaluation failed",
            "details": str(e),
            "raw_output": response_text if 'response_text' in locals() else None
        }