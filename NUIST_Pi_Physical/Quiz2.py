import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GREEN_LED = 17
RED_LED = 18
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.output(GREEN_LED, False)
GPIO.output(RED_LED, False)
def correct_light():
    GPIO.output(GREEN_LED, True)
    time.sleep(1)
    GPIO.output(GREEN_LED, False)
def wrong_light():
    GPIO.output(RED_LED, True)
    time.sleep(1)
    GPIO.output(RED_LED, False)
def quiz():
    print("Welcome to Python Quiz!")
    print("Answer with a/b/c/d/e\n")
    questions = [
        "1. Which is NOT a Python data type? a)int b)float c)rational d)string e)bool\n",
        "2. Which is NOT a built-in operation? a)+ b)% c)abs() d)sqrt()\n",
        "3. Mixed int/float converts: a)float→int b)int→string c)both→string d)int→float\n",
        "4. Best multi-way decision: a)if b)if-else c)if-elif-else d)try\n",
        "5. Loop terminate statement: a)if b)exit c)continue d)break\n"
    ]

    answers = ["c", "d", "d", "c", "d"]
    score = 0

    for i in range(len(questions)):
        user = input(questions[i]).strip().lower()
        if user == answers[i]:
            print("Correct!\n")
            correct_light()
            score +=1
        else:
            print("Incorrect!\n")
            wrong_light()

    print("Quiz finished!")
    print(f"Score: {score}/{len(questions)}")

    GPIO.cleanup()

quiz()
