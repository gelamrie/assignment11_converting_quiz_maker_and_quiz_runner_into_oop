from colorama import init, Fore, Style         
import time, sys  

init(autoreset=True)

class WelcomeDisplay:
    def typing_effect_centered(self, text, width=60, delay=0.04, color=Fore.RED + Style.BRIGHT):
        centered_text = text.center(width)
        for char in centered_text:
            sys.stdout.write(color + char)
            sys.stdout.flush()
            time.sleep(delay)
        print() 

    def welcome_screen(self):                  
        border_design = (" ★ " + " ♡ ") * 10     
        print(Fore.LIGHTWHITE_EX + Style.BRIGHT + border_design)
        self.typing_effect_centered(" Welcome to the Quiz Creator! ", width=len(border_design))
        print(Fore.LIGHTWHITE_EX + Style.BRIGHT + border_design + "\n")    