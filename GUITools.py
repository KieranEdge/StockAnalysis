"""The purpose of this script is to create the GUI tools for the application"""
import tkinter as tk

class Application(tk.Tk):
    """Creating the main application class"""
    def __init__(self, title, dimensions, *args, **kwargs):
        """Initialising the class and inheriting the key word arguments"""
        super().__init__(title, dimensions, *args, **kwargs)
        self.title(title)
        self.geometry(dimensions)
        self.bg="white"
        self.fg="black"

        # Creating the frames
        self.inFrame = InputFrame(self, bg="white", bd=2, relief=tk.SUNKEN)
        self.inFrame.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.2)


class InputFrame(tk.Frame):
    """Creating the input frame class"""
    def __init__(self, Parent, *args, **kwargs):
        """Initialising the class and inheriting the key word arguments"""
        super().__init__(Parent, *args, **kwargs)

        # Titling the frame
        Title = tk.Label(self, text="User Inputs", bg="white", fg="blue")
        Title.grid(row=0, column=0, columnspan=3)

        # Creating the user inputs
        label = tk.Label(self, text="Choose company", bg="white", fg="blue")
        label.grid(row=1, column=0)
        compInput = tk.Entry(self, width= 40)
        compInput.grid(row=1, column=1, columnspan=2)

        # Creating the user button
        button = tk.Button(self, text="Gather Information")
        button.grid(row=2, column=0, columnspan=3)

class OutputFrame(tk.Frame):
    def __init__(self, Parent, *args, **kwargs):
        """Initialising the class and inheriting the key word arguments"""
        super().__init__(Parent, *args, **kwargs)

        # Titling the frame
        Title = tk.Label(self, text="User Inputs", bg="white", fg="blue")
        Title.grid(row=0, column=0, columnspan=3)

        # Creating the user inputs
        label = tk.Label(self, text="Choose company", bg="white", fg="blue")
        label.grid(row=1, column=0)
        compInput = tk.Entry(self, width=40)
        compInput.grid(row=1, column=1, columnspan=2)

        # Creating the user button
        button = tk.Button(self, text="Gather Information")
        button.grid(row=2, column=0, columnspan=3)

def runProgramme():
    """The main loop for launching the GUI"""
    mainApplication = Application('Stock Market Analysis', '400x600')
    mainApplication.mainloop()