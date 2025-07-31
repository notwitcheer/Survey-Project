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



class Quiz:
    def __init__(self, questions):
        self.questions = questions

    
    def start_quiz(self):
        score = 0
        for question in self.questions:
            if question.ask():
                score += 1
        print(f"final score: {score} on {len(self.questions)}.")
        return score



class Question:
    def __init__(self, title, options, answer):
        self.title = title
        self.options = options
        self.answer = answer


    def ask(self):
        choice = self.options
        good_answer = self.answer
        print("QUESTION: " + self.title)
        
        for i in range(len(choice)):
            print(i+1, "-", choice[i])

        result_correct_answer = False
        answer_int = ask_numerical_answer(1, len(choice))
        if choice[answer_int-1].lower() == good_answer.lower():
            print("\nCONGRATULATIONS.\n")
            result_correct_answer = True
        else:
            print("\nWRONG ANSWER.\n")
        return result_correct_answer


Quiz([
    Question("what is the capital of France?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris"),
    Question("what is the capital of Italie?", ("Milan", "Rome", "Turin", "Naples"), "Rome"),
    Question("what is the capital of Spain?", ("Madrid", "Barcelona", "Salamanqua", "Torrente"), "Madrid"),
    Question("what is the capital of Russia?", ("Moscow", "Novoss", "Petersbourg", "Lekaterin"), "Moscow"),
]).start_quiz()

