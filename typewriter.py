import time 

class TypeWriter:
    def type_writer(self, message, delay=0.04): 
        for character in message:  
            print(character, end='', flush=True)  
            time.sleep(delay)  
        print()