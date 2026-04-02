def main():
        score=0
        print("welcome to animal question game")
        print("="*30)
        q1=input("1.What is the largest land animal on Earth?\na. African Elephant\nb. Giraffe\nc. Hippopotamus\nPlease enter your choice (a/b/c)")
        if q1.strip().upper()=="A":
                print("your are right")
                score+=1
        else:
                print("your are wrong")
        q2=input("\n2.Which of these animals can change colour?\na. Tiger\nb. Chameleon\nc. Lion\nPlease enter your choice (a/b/c)")

        if q2.strip().upper()=="B":
                print("your are right")
                score+=1
        else:
                print("your are wrong")
        q3=input("\n3.Which continent do penguins live on?\na. Asia\nb. Europe\nc. Antarctica\nPlease ebter your choice (a/b/c)")
        if q3.strip().upper()=="C":
                print("your are right")
                score+=1
        else:
                print("your are wrong")
        print("\n"+"="*30)
        print(f"Gameover! your score is {score}/3")
        if score>=3:
                print("Great")
        elif score>=1:
                print("Good")
        else:
                print("Keeping trying")
if __name__ == "__main__":
        main()
