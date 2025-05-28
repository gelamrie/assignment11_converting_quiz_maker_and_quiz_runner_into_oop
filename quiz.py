import random  
from rich.console import Console
from question_displayer import QuestionDisplayer
from answer_prompt import AnswerPrompt

class Quiz: 
    def __init__(self):
        self.console = Console()
        self.question_displayer = QuestionDisplayer()
        self.answer_prompt = AnswerPrompt()
    
    def start_quiz(self, questions):  
        score = 0  
        random.shuffle(questions)  
