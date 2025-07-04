from educhain import EduChainGenerator

def generate_educational_content(topic):
    generator = EduChainGenerator()
    
    mcqs = generator.generate_mcqs(topic=topic, count=5)
   
    lesson_plan = generator.generate_lesson_plan(topic=topic)
    
    return {
        "mcqs": mcqs,
        "lesson_plan": lesson_plan
    }

if __name__ == "__main__":
    content = generate_educational_content("Python Programming Basics")
    print(content)