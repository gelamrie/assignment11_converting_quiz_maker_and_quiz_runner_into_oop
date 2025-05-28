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