import tkinter as tk
from models.gui import BookTrackerGUI

if __name__ == "__main__" :
    root = tk.Tk()
    app = BookTrackerGUI(root)
    root.mainloop()