from colorama import Fore  

class Question:
    def __init__(self):
        self.category = ""
        self.question = ""
        self.choices_dictionary = {}
        self.correct_answer = ""
    
    def get_question_block(self):
        print(Fore.CYAN + "\n=== New Question ===")

        self.category = input(Fore.LIGHTMAGENTA_EX + "Enter a category (e.g., Math, History, Science): ")
        self.question = input(Fore.YELLOW + "Enter the question: ")

        for letter in ['a', 'b', 'c', 'd']:     
            self.choices_dictionary[letter] = input(Fore.BLUE + f"Choice ({letter}): ")

        while True:                               
            self.correct_answer = input(Fore.GREEN + "Which one is the correct answer? (a/b/c/d): ")