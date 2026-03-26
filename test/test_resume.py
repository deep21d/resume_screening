from app.services.resume_service import parse_resume

text = parse_resume("Deependra_CV.pdf")

print(text[:1000])  # print first 1000 chars