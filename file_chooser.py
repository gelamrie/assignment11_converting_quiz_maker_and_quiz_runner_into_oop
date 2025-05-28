import tkinter as tk  
from tkinter import filedialog  

class FileChooser:
    def choose_file(self):  
        root = tk.Tk()  
        root.withdraw()  
        file_path = filedialog.askopenfilename(  
            title="Select Quiz Bank File",  
            filetypes=[("Text files", "*.txt")]  
        )
        return file_path