# survey creation.

def ask_question(question, r1, r2, r3, r4, good_answer):
    global score
    print(f"question: {question}\n(a) {r1}\n(b) {r2}\n(c) {r3}\n(d) {r4}")
    answer = input("your answer: ")

    if answer == good_answer:
        print("\nCONGRATULATIONS.\n")
        score += 1
    else:
        print("\nWRONG ANSWER.\n")


score = 0
ask_question("what is the capital of France?", "Marseille", "Nice", "Paris", "Nantes", "c")
ask_question("what is the capital of Italie?", "Milan", "Rome", "Turin", "Naples", "b")
ask_question("what is the capital of Spain?", "Madrid", "Barcelona", "Salamanqua", "Torrente", "a")
ask_question("what is the capital of Russia?", "Moscow", "Novoss", "Petersbourg", "Lekaterin", "a")

print(f"final score: {score}.")
