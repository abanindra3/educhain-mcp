import requests

BASE_URL = "http://localhost:5000"

def test_mcq_generation():
    response = requests.post(
        f"{BASE_URL}/generate_mcqs",
        json={"topic": "Python loops", "count": 3}
    )
    print("MCQ Generation:", response.json())

def test_lesson_plan():
    response = requests.post(
        f"{BASE_URL}/generate_lesson_plan",
        json={"subject": "Algebra Basics"}
    )
    print("Lesson Plan:", response.json())

if __name__ == "__main__":
    test_mcq_generation()
    test_lesson_plan()