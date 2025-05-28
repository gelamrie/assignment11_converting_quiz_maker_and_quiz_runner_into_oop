from rich.console import Console 
from rich.prompt import Prompt

class AnswerPrompt:  
    def __init__(self):
        self.console = Console()
        
    def prompt_user_for_answer(self):  
        valid_letters = ['A', 'B', 'C', 'D', 'Q'] 
        while True:
            user_input = Prompt.ask("[bold yellow]Your answer (A-D or Q to quit)[/bold yellow]").strip().upper()
            if user_input in valid_letters:  
                return user_input
            self.console.print("[bold red]❗ Invalid input. Choose A, B, C, D, or Q to quit.[/bold red]")