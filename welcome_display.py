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