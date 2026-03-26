from app.pipelines.screening_pipeline import run_screening_pipeline
from project_test.job_description import jd_text

# 🔹 Provide your resume file path
resume_path = r"resumes\Deependra_CV.pdf"

# 🔹 Provide your jd-data
jd_text = jd_text

# 🔹 Run pipeline
result = run_screening_pipeline(resume_path, jd_text)

# 🔹 Print output
print(result)