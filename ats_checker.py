import re

def load_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().lower()

def extract_keywords(text):
    # Grab words longer than 2 letters, ignore common stopwords
    stopwords = {"and", "the", "for", "with", "a", "to", "in", "of", "on", "at"}
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text)
    return set(w for w in words if w not in stopwords)

def compare_resume_to_jd(resume_text, jd_text):
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    matched = resume_keywords & jd_keywords
    missing = jd_keywords - resume_keywords

    match_score = (len(matched) / len(jd_keywords)) * 100 if jd_keywords else 0

    return match_score, matched, missing

def save_report(score, matched, missing, filename="report.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("ATS Keyword Match Report\n\n")
        f.write(f"Match Score: {score:.2f}%\n\n")
        f.write("✅ Matched Keywords:\n")
        f.write(", ".join(sorted(matched)) + "\n\n")
        f.write("❌ Missing Keywords:\n")
        f.write(", ".join(sorted(missing)) + "\n\n")
        f.write("💡 Suggestion: Add missing keywords naturally into your resume where applicable.")

if __name__ == "__main__":
