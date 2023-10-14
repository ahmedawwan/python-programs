from question_model import Question
import requests as req



question_bank = []
user_points = 0

def create_question_bank():
    response = req.get('https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean')
    if response.status_code == 200:
        question_data = response.json()
        if 'results' in question_data:
            for question in question_data["results"]:
                new_question = Question(question["question"], question["correct_answer"])
                question_bank.append(new_question)
        else:
            print("Invalid JSON data format: 'results' key not found.")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")


def ask_question(question):
        global user_points
        print(question.text)
        answer = input("True or False? ")
        if answer == question.answer:
            user_points += 1
            print("You're correct!")
        else:
            print("Better luck next time")

def take_quiz():
    for question in question_bank:
         ask_question(question)

    print(f"Your Score: {user_points} / {len(question_bank)}")

def main():
    create_question_bank()
    take_quiz()


if __name__ == "__main__":
    main()