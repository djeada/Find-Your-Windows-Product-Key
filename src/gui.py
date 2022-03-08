import tkinter as tk
from tkinter import messagebox


class GuiWindow:
    """
    Tkinter window centered on screen.
    Used to display provided text.
    """

    def __init__(self, text):
        self.root = tk.Tk()
        self.root.configure(background="white")
        self.root.title("Your product key")

        self.root.bind("<Escape>", lambda e: self.root.destroy())
        self.root.bind("<Return>", lambda e: self.root.destroy())

        self.label = tk.Label(
            self.root, text=text, font=("Helvetica", "20"), background="white"
        )
        self.label.pack()

        # calculate how much width and height is needed to display the text
        width = self.label.winfo_reqwidth()
        height = self.label.winfo_reqheight()

        # set the size of the window
        self.root.geometry("{}x{}".format(int(width * 1.1), int(height * 1.1)))
        # place text on the center of the screen
        self.root.geometry(
            "+{}+{}".format(
                int(self.root.winfo_screenwidth() / 2 - width / 2),
                int(self.root.winfo_screenheight() / 2 - height),
            )
        )

        # add an event, whenever user clicks on the window, the text should be copied to clipboard
        self.root.bind("<Button-1>", lambda e: self.copy_to_clipboard(text))
        self.root.bind("<Button-2>", lambda e: self.copy_to_clipboard(text))

        self.root.mainloop()

    def copy_to_clipboard(self, text):
        """
        Copy text to clipboard.
        Display a messagebox to inform user that text has been copied.
        """
        self.root.clipboard_clear()
        self.root.clipboard_append(text)

        # display messagebox to inform user that text has been copied
        messagebox.showinfo(
            "Copied to clipboard", "Your product key has been copied to clipboard."
        )
