from colorama import Fore 
from welcome_display import WelcomeDisplay 
from question_manager import QuestionManager

class MainQuizMaker:
    def run(self):
        welcome_display = WelcomeDisplay()       
        welcome_display.welcome_screen()   