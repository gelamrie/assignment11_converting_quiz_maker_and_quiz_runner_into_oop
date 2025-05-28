from colorama import Fore 
from question import Question 

class QuestionManager: 
    def __init__(self, file_name):
        if not file_name.endswith(".txt"):    
            file_name += ".txt"
        self.file_name = file_name
        self.all_questions_this_session = []  

    def collect_and_save_question(self):         
        question = Question()
        question_block = question.get_question_block()
        self.all_questions_this_session.append(question_block)   

        with open(self.file_name, "a", encoding="utf-8") as quiz_file:
            quiz_file.write(question_block)
    
    def print_session_preview(self):            
        print(Fore.YELLOW + "\n📋 Here's a preview of your questions from this session:\n")
        for question in self.all_questions_this_session:
            print(Fore.WHITE + question)
            print(Fore.LIGHTBLACK_EX + "-" * 50)
