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