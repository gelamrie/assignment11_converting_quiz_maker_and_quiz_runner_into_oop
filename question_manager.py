from colorama import Fore 
from question import Question 

class QuestionManager: 
    def __init__(self, file_name):
        if not file_name.endswith(".txt"):    
            file_name += ".txt"
        self.file_name = file_name