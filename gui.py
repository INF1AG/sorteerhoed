import os
from tkinter.constants import ANCHOR, CENTER, LEFT, RIGHT
from firebase import send_data
from PIL import ImageTk, Image

from score import score
from tkinter import PhotoImage, ttk as tkinter
from read_excel import read_question_data

class gui:
	def __init__(self, root):
		root.title("SorteerHoed")
		root.geometry("1050x600")
		root.wm_attributes('-transparent', 'True')
		self.score = score()
		self.root = root
		self.frame = tkinter.Frame(self.root)
		self.frame.pack()
		self.data = read_question_data("/Users/wouter/OneDrive - Hogeschool Leiden/IPOHBO AG 2.1/Challengeweek #fun/stap 3 challenge week.xlsx")
		self.current_question = 0
		img = Image.open("/Users/wouter/Desktop/zweinstein.png").resize((1050, 600))
		self.tkimg = ImageTk.PhotoImage(img)
		self.draw_ui()

	def draw_ui(self):
		

		background_label = tkinter.Label(self.root, image=self.tkimg)
		background_label.image = self.tkimg
		background_label.place(x=0, y=0, relheight=1, relwidth=1)

		question = self.data[self.current_question]
		tkinter.Label(self.root, text=question.question, font=('Manrope', 18)).pack(pady=(30, 60))

		for answer in range(0, len(question.answers)):
			wrapper = tkinter.Frame(self.root)
			wrapper.pack(pady=(20,0))
			tkinter.Label(wrapper, text=("%s)" % question.answers[answer][0])).pack(side=LEFT)
			tkinter.Button(wrapper, width=100, text=question.answers[answer][1], command=lambda p = question.answers[answer][2]: self.update_score(p)).pack(side=RIGHT)
	
	def update_score(self, points):
		for ui_item in self.root.winfo_children():
			ui_item.destroy()

		if(self.current_question+1 == len(self.data)):
			self.show_result()
			return

		self.score.add_score(points)

		self.current_question += 1
		self.draw_ui()
	
	def show_result(self):
		background_label = tkinter.Label(self.root, image=self.tkimg)
		background_label.image = self.tkimg
		background_label.place(x=0, y=0, relheight=1, relwidth=1)

		points_with_specification = list(zip(self.score.get_score(), [
			"SE is het beste advies, je hebt een sterk analytisch vermogen en je houdt van ontwerpen/programmeren en daarnaast van slimme oplossingen voor ingewikkelde problemen bedenken.", 
			"BDAM is het beste advies, je bent geïnteresseerd in zowel de technologie als in de business. Je vind het leuk om met data te werken.", 
			"IAT is het beste advies, je vindt het leuk om jezelf steeds uit te dagen, je bent steeds up to date met de nieuwste technologie en aan veel projecten werken vind je niet erg.", 
			"FICT is het beste advies, je bent doelgericht, onderzoekend en je kan de juiste informatie achterhalen."
		]))
		
		def sorter(elem):
			return elem[0]

		points_with_specification.sort(key=sorter, reverse=True)
	
		a = tkinter.Label(self.root, width=100, wraplength=600, text="%s" % points_with_specification[0][1], font=('Manrope', 24))
		a.configure(anchor=CENTER, justify=CENTER)
		a.pack(fill='both', expand=False, pady=(40, 0))

		def send_points(name):
			if name.get() == "":
				return
			send_data(name.get(), self.score.get_score())
			name.destroy()
			button.destroy()
			tkinter.Label(self.root, text="Sent in!").pack()

		fr = tkinter.Frame(self.root)
		fr.pack(pady=(20, 0))
		entry_name = tkinter.Entry(fr)
		entry_name.pack(side=LEFT)

		button = tkinter.Button(fr, text="send", command=lambda p=entry_name: send_points(p))
		button.pack(side=RIGHT)