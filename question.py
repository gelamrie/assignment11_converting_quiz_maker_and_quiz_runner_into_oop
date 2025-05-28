from colorama import Fore  

class Question:
    def __init__(self):
        self.category = ""
        self.question = ""
        self.choices_dictionary = {}
        self.correct_answer = ""
    
    def get_question_block(self):
        print(Fore.CYAN + "\n=== New Question ===")