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
            if self.correct_answer in self.choices_dictionary:
                break
            print(Fore.RED + "❌ Invalid input. Please choose from a, b, c, or d.")

        return self.format_question()
    
    def format_question(self):                   
        return (f"Category: {self.category}\n"
                f"Question: {self.question}\n" +
                ''.join(f"{option}) {self.choices_dictionary[option]}\n" for option in ['a', 'b', 'c', 'd']) +
                f"Answer: {self.correct_answer}\n\n")  