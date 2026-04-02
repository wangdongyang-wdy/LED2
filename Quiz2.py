
import RPi.GPIO as GPIO
import time

def init_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)

def led_feedback(correct):
    if correct:
        GPIO.output(17, GPIO.HIGH)
    else:
        GPIO.output(18, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)

def python_quiz():
    init_gpio()
    print("Welcome to the Python Basic Quiz!")
    print("Answer the following questions (input the option letter only, e.g. a):\n")

    quiz_data = [
        {
            "question": "1. Which of the following is NOT a python data type?",
            "options": "a) int\nb) float\nc) rational\nd) string\ne) bool\n",
            "answer": "c"
        },
        {
            "question": "2. Which of the following is NOT a built-in operation in Python?",
            "options": "a) +\nb) %\nc) abs()\nd) sqrt()\n",
            "answer": "d"
        },
        {
            "question": "3. In a mixed-type expression involving ints and floats, Python will convert:",
            "options": "a) floats to ints\nb) ints to strings\nc) floats and ints to strings\nd) ints to floats\n",
            "answer": "d"
        },
        {
            "question": "4. The best structure for implementing a multi-way decision in Python is:",
            "options": "a) if\nb) if-else\nc) if-elif-else\nd) try\n",
            "answer": "c"
        },
        {
            "question": "5. What statement can be executed in the body of a loop to cause it to terminate?",
            "options": "a) if\nb) exit\nc) continue\nd) break\n",
            "answer": "d"
        }
    ]
    score = 0

    for item in quiz_data:
        print(item["question"])
        user_ans = input(item["options"]).strip().lower()
        if user_ans == item["answer"]:
            print("Correct!")
            score += 1
            led_feedback(correct=True)
        else:
            print(f"Incorrect! The correct answer is {item['answer']}")
            led_feedback(correct=False)
        print("-" * 30)

    total = len(quiz_data)
    print(f"\nQuiz completed! You got {score}/{total} questions correct.")
    GPIO.cleanup()

if __name__ == "__main__":
    python_quiz()
