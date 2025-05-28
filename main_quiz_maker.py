from colorama import Fore 
from welcome_display import WelcomeDisplay 
from question_manager import QuestionManager

class MainQuizMaker:
    def run(self):
        welcome_display = WelcomeDisplay()       
        welcome_display.welcome_screen()  

        file_name = input(Fore.LIGHTCYAN_EX + "Enter the file name to save your quiz (e.g., myquiz.txt): ").strip()
        question_manager = QuestionManager(file_name)

        while True:                              
            question_manager.collect_and_save_question()
            add_more_questions = input(Fore.CYAN + "Add another question? (y/n): ").strip().lower()
            if add_more_questions != 'y':
                break

        print(Fore.GREEN + f"\n✅ All questions saved to '{question_manager.file_name}'")
        question_manager.print_session_preview()

if __name__ == "__main__":                       
    MainQuizMaker().run()