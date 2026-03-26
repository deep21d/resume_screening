from app.services.llm_service import get_llm
import json
import re


def clean_json(text: str) -> str:
    """
    Extract only JSON part from LLM response.
    """
    match = re.search(r"\{.*\}", text, re.DOTALL)
    return match.group(0) if match else text


def parse_jd(jd_text: str) -> dict:
    """
    Converts raw job description into structured data using LLM.
    """

    llm = get_llm()

    prompt = f"""
You are an expert HR analyst.

Extract structured information from the job description.

Return ONLY valid JSON in this EXACT format:

{{
  "role": "string",
  "required_skills": ["string"],
  "experience_required": "string",
  "responsibilities": ["string"]
}}

STRICT RULES:
- No explanation
- No extra text
- No markdown
- Only JSON

Job Description:
{jd_text}
"""

    response = llm.invoke(prompt)

    content = response.content.strip()

    # Clean possible garbage text
    content = clean_json(content)

    try:
        return json.loads(content)

    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON from LLM",
            "raw_output": content
        }


# ✅ TEST BLOCK (you can run this directly)
# if __name__ == "__main__":
#     job_description = '''
#     Job Title: QA Automation Engineer (Python)

#     Role Overview:
#     We are looking for a detail-oriented QA Automation Engineer...

#     Key Responsibilities:
#     Build and maintain test suites, integrate CI/CD, perform load testing.

#     Required Skills:
#     Python, pytest, Selenium, Git

#     Preferred:
#     Docker, FastAPI testing
#     '''

#     result = parse_jd(job_description)

#     print("\n✅ FINAL OUTPUT:\n")
#     print(json.dumps(result, indent=2))