def generate_resume(data):
    skills = ", ".join(data["skills"].split(","))

    resume = f"""
{data['name']}
{data['title']}

PROFESSIONAL SUMMARY
Results-driven professional with experience in {skills}. Proven ability to deliver measurable outcomes and contribute to organizational success.

SKILLS
{skills}

PROFESSIONAL EXPERIENCE
{data['experience']}

EDUCATION
{data['education']}
    """

    return resume.strip()
