

Question = tuple("Question", "prompt answer choices correct")

question = [Question("What color are apples?", "a", ["Red", "Purple", "Orange"], "a"), ...]

def quiz():
    score = 0
    for q in question:
        print(q.prompt)
        for i in range(len(q.choices)):
            print(f"({i+1}) {q.choices[i]}")
        answer = input("Enter your answer: ")
        if answer == q.correct:
            score += 1
    print(f"You got {score}/{len(question)} correct")

if __name__ == "__main__":
    quiz()