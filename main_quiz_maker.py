from colorama import Fore 
from welcome_display import WelcomeDisplay 
from question_manager import QuestionManager

class MainQuizMaker:
    def run(self):
        welcome_display = WelcomeDisplay()       
        welcome_display.welcome_screen()  

        file_name = input(Fore.LIGHTCYAN_EX + "Enter the file name to save your quiz (e.g., myquiz.txt): ").strip()
        question_manager = QuestionManager(file_name)