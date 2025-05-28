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

        