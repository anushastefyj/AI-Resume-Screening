import requests

BASE_URL = "http://localhost:8000"

def test_health():
    print("Testing health endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    print()

def test_extract():
    print("Testing skill extraction...")
    try:
        with open("sample_resume.pdf", "rb") as f:
            response = requests.post(f"{BASE_URL}/extract-skills", files={"file": f})
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
    except FileNotFoundError:
        print("ERROR: sample_resume.pdf not found!")
        print("Please add a sample resume PDF named sample_resume.pdf")
    print()

def test_match():
    print("Testing resume matching...")
    job_desc = "Python Developer with AWS, Docker, Django experience"
    try:
        with open("sample_resume.pdf", "rb") as f:
            response = requests.post(
                f"{BASE_URL}/match-resume",
                files={"file": f},
                data={"job_description": job_desc}
            )
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
    except FileNotFoundError:
        print("ERROR: sample_resume.pdf not found!")
    print()

if __name__ == "__main__":
    print("=" * 50)
    print("RESUME SCANNER API TESTS")
    print("=" * 50)
    test_health()
    test_extract()
    test_match()
    print("Done!")