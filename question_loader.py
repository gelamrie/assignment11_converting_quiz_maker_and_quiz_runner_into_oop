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

                category = category_line.split(":", 1)[1].strip()  
                question_text = question_line  
                choices = [line[3:].strip() for line in choice_lines] 

                correct_letter = answer_line.split(":", 1)[1].strip().upper()  
                correct_index = ord(correct_letter) - ord('A')  
                correct_choice = choices[correct_index]  

                question_list.append({  
                    "category": category,
                    "question": question_text,
                    "choices": choices,
                    "answer": correct_choice
                })
            
            except Exception as error:  
                self.console.print(f"[bold red]⚠ Malformed block at line {line_index + 1}: {error}[/bold red]")
            
            line_index += 8  