from app.services.jd_service import parse_jd

job_description = '''
Job Title: QA Automation Engineer (Python)
Role Overview
We are looking for a detail-oriented QA Automation Engineer to ensure the reliability and performance of our codebase. You will be responsible for designing, implementing, and executing automated test suites to catch bugs before they reach production.

Key Responsibilities
Test Suite Development: Build and maintain comprehensive unit, integration, and end-to-end (E2E) tests.

Framework Management: Utilize pytest to develop scalable testing architectures.

Bug Detection: Identify, document, and track software defects and regressions.

CI/CD Integration: Integrate automated tests into our GitHub Actions/GitLab CI pipelines to ensure code health on every push.

Performance Testing: Conduct load testing to ensure the application handles peak traffic efficiently.

Required Skills & Qualifications
Language: Proficiency in Python.

Tools: Experience with pytest, unittest, or Playwright/Selenium.

Environment Management: Familiarity with modern package managers like uv or poetry.

Version Control: Strong command of Git.

Analytical Mindset: Ability to think like a "breaker" to find edge cases that developers might miss.

Preferred Experience
Experience with Mocking and patching external API dependencies.

Knowledge of Docker for containerized testing environments.

Previous experience testing RESTful APIs or FastAPI/Flask applications.
'''


structured_jd = parse_jd(job_description)
print(structured_jd)