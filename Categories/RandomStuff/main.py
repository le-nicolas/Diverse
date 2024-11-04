#this code is a simple quiz game that asks the user questions and checks if the answer is correct or not
#the questions are stored in a list of objects of the class Question
#the class Question has two attributes prompt and answer
#the function run_test takes a list of questions and asks the user each question
#it then checks if the answer is correct and increments the score accordingly
#finally it prints the score



from Question import Questions

question_prompts = [
    "What color are apples?\n(a) Red\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Questions(question_prompts[0], "a"),
    Questions(question_prompts[1], "c"),
    Questions(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt).lower()
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

if __name__ == "__main__":
    run_test(questions)
