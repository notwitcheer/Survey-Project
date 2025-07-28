# survey creation.


def ask_numerical_answer(min, max):
    answer_str = input(f"your answer (between {str(min)} and {str(max)}): ")
    try:
        answer_int = int(answer_str)
        if min <= answer_int <= max:
            return answer_int
        
        print("ERROR: you need to enter a value between", min, "and", max)
    except:
        print("ERROR: please enter a numerical value.")
    return ask_numerical_answer(min, max)


def ask_question(q):
    choice = q[1]
    good_answer = q[2]
    print("question: " + q[0])
    
    for i in range (len(choice)):
        print(i+1,"-", choice[i])

    result_correct_answer = False
    answer_int = ask_numerical_answer(1, len(choice))
    if choice[answer_int-1].lower() == good_answer.lower():
        print("\nCONGRATULATIONS.\n")
        result_correct_answer =  True
    else:
        print("\nWRONG ANSWER.\n")
    return result_correct_answer


def start_survey(survey):
    score = 0
    for q in survey:
        if ask_question(q):
            score += 1
    print(f"final score: {score} on {len(survey)}.")
        


survey = (
    ("what is the capital of France?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris"),
    ("what is the capital of Italie?", ("Milan", "Rome", "Turin", "Naples"), "Rome"),
    ("what is the capital of Spain?", ("Madrid", "Barcelona", "Salamanqua", "Torrente"), "Madrid"),
    ("what is the capital of Russia?", ("Moscow", "Novoss", "Petersbourg", "Lekaterin"), "Moscow"),
)

start_survey(survey)
