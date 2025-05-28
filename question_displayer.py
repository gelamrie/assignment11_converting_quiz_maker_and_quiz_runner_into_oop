from rich.console import Console  
from rich.table import Table  
from rich import box 

class QuestionDisplayer:  
    def __init__(self):  
        self.console = Console()

    def display_question(self, question_data, question_number):  
        self.console.print(f"\n[bold blue]Question {question_number + 1}:[/bold blue] {question_data['question']}")

        choices_table = Table(box=box.SIMPLE)  
        choices_table.add_column("Letter", justify="center")
        choices_table.add_column("Option", justify="left")