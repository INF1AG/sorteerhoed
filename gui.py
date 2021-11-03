import os

from score import score
from tkinter import ttk as tkinter
from read_excel import read_question_data

class gui:
	def __init__(self, root):
		root.title("SorteerHoed")
		self.score = score()
		self.root = root
		self.frame = tkinter.Frame(self.root, padding=30)
		self.frame.grid()
		self.data = read_question_data(os.getenv("EXCEL_PATH"))
		self.current_question = 0

	def draw_ui(self):
		question = self.data[self.current_question]
		tkinter.Label(self.frame, text=question.question).grid(column=0, row=0, columnspan=2, pady=(0,30))

		for answer in range(0, len(question.answers)):
			tkinter.Label(self.frame, text=("%s)" % question.answers[answer][0])).grid(column=0, row=answer+1)
			tkinter.Button(self.frame, text=question.answers[answer][1], command=lambda p = question.answers[answer][2]: self.update_score(p)).grid(column=1, row=answer+1)
	
	def update_score(self, points):
		for ui_item in self.frame.winfo_children():
			ui_item.destroy()

		if(self.current_question+1 == len(self.data)):
			self.show_result()
			return

		self.score.add_score(points)

		self.current_question += 1
		self.draw_ui()
	
	def show_result(self):
		points_with_specification = list(zip(self.score.get_score(), ["SE", "BDaM", "IaT", "FICT"]))
		
		def sorter(elem):
			return elem[0]

		points_with_specification.sort(key=sorter, reverse=True)
		for specification in points_with_specification:
			tkinter.Label(self.frame, text="%s" % specification[1]).grid()