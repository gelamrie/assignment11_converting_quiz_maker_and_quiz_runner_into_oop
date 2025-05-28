from rich.console import Console 

class QuestionLoader:  
    def __init__(self):  
        self.console = Console()

    def load_questions_from_text(self, file_path):  
        with open(file_path, 'r', encoding='utf-8') as file:  
            raw_lines = [line.strip() for line in file.readlines()]  

        question_list = []  
        line_index = 0  

        while line_index + 7 < len(raw_lines):  
            if raw_lines[line_index] == "":  
                line_index += 1
                continue

            try:
                category_line = raw_lines[line_index]  
                question_line = raw_lines[line_index + 1]  
                choice_lines = raw_lines[line_index + 2:line_index + 6]  
                answer_line = raw_lines[line_index + 6] 