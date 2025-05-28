from rich.console import Console 

class QuestionLoader:  
    def __init__(self):  
        self.console = Console()

    def load_questions_from_text(self, file_path):  
        with open(file_path, 'r', encoding='utf-8') as file:  
            raw_lines = [line.strip() for line in file.readlines()]  

        question_list = []  
        line_index = 0  