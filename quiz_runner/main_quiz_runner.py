from rich.console import Console
from typewriter import TypeWriter
from file_chooser import FileChooser
from question_loader import QuestionLoader
from quiz import Quiz 

class MainQuizRunner:  
    def __init__(self):
        self.console = Console()
        self.typewriter = TypeWriter()
        self.file_chooser = FileChooser()
        self.question_loader = QuestionLoader()
        self.quiz = Quiz()

    def run(self):  # feat: main flow of app
        self.typewriter.type_writer(
            "\n🎉 Welcome to the Quiz Game! Test your knowledge and have fun!\n", delay=0.05
        )

        file_path = self.file_chooser.choose_file()  
        if not file_path:
            self.console.print("[bold red]❌ No file selected. Exiting.[/bold red]")  
            return
        
        self.console.print(f"[bold cyan]📂 Loading file:[/bold cyan] {file_path}")

        try:
            questions = self.question_loader.load_questions_from_text(file_path)  
            self.console.print(f"[bold green]📚 {len(questions)} questions loaded. Let's go![/bold green]\n")
            self.quiz.start_quiz(questions) 
        except Exception as error:
            self.console.print(f"[bold red]❌ Error: {error}[/bold red]")  

if __name__ == "__main__":  
    MainQuizRunner().run()