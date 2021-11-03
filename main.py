from tkinter import Tk
from dotenv import load_dotenv

from gui import gui

if __name__ == "__main__":
	load_dotenv()
	root = Tk()
	gui(root).draw_ui()
	root.mainloop()
