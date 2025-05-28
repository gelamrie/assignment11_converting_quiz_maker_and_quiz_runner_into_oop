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

        for question_number, question_data in enumerate(questions):  
            self.question_displayer.display_question(question_data, question_number)
            user_letter = self.answer_prompt.prompt_user_for_answer()

            if user_letter == "Q":  
                self.console.print("[bold cyan]👋 You chose to quit the quiz early.[/bold cyan]\n")
                break

            user_choice_index = ord(user_letter) - ord('A')  
            user_choice = question_data["choices"][user_choice_index]  
            correct_choice = question_data["answer"]

            if user_choice == correct_choice:  
                self.console.print("[bold green]✅ Correct! Good job![/bold green]\n")
                score += 1
            else:
                correct_index = question_data["choices"].index(correct_choice)  
                correct_letter = chr(correct_index + ord('A'))  
                self.console.print(f"[bold red]❌ Wrong! Correct Answer: {correct_letter}. {correct_choice}[/bold red]\n")

        answered = question_number + 1 if user_letter != "Q" else question_number  
        self.console.rule("[bold cyan]Quiz Finished![/bold cyan]")  
        self.console.print(f"[bold magenta]🔥 Final Score: {score}/{answered}[/bold magenta]") 
        



