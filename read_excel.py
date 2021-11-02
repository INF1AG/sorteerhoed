from numpy import NaN
from dotenv import load_dotenv
import pandas
import itertools
import os

class Question: 
	def __init__(self, question, answers):
		self.question = question
		self.answers = answers


def get_column(wb, name):
	return pandas.DataFrame(wb, columns=[name]).values.tolist()

def read_question_data(excel_path):
	loc = excel_path
	wb = pandas.read_excel(loc)
	questions = get_column(wb, "question")
	questions = [x for x in questions if not pandas.isna(x)]

	options = list(itertools.chain.from_iterable(get_column(wb, "option")))
	answers = list(itertools.chain.from_iterable(get_column(wb, "answer")))
	points = pandas.DataFrame(wb, columns=["SE", "BDaM", "IaT", "FICT"])
	constructed_answers = list(zip(options, answers, map(lambda x: tuple(x), points.iloc)))

	answer_lists = []

	for i in range(0, len(constructed_answers)):
		if pandas.isna(constructed_answers[i][0]): continue
		if constructed_answers[i][0].startswith("A"):
			answer_lists.append([])
		answer_lists[-1].append(constructed_answers[i])

	qa_pairs = []

	for i in range(0, len(questions)):
		qa_pairs.append(Question(questions[i][0], answer_lists[i]))

	return qa_pairs

if __name__ == '__main__':
	load_dotenv()
	print(read_question_data(os.getenv("EXCEL_PATH")))
