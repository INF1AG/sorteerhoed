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
	location = excel_path
	workbook = pandas.read_excel(location)
	questions = get_column(workbook, "question")
	questions = [x for x in questions if not pandas.isna(x)]

	options = list(itertools.chain.from_iterable(get_column(workbook, "option")))
	answers = list(itertools.chain.from_iterable(get_column(workbook, "answer")))
	points = pandas.DataFrame(workbook, columns=["SE", "BDaM", "IaT", "FICT"])
	constructed_answers = list(zip(options, answers, map(lambda x: tuple(x), points.iloc)))

	answer_lists = []

	for answer_index in range(0, len(constructed_answers)):
		if pandas.isna(constructed_answers[answer_index][0]): continue
		if constructed_answers[answer_index][0].startswith("A"):
			answer_lists.append([])
		answer_lists[-1].append(constructed_answers[answer_index])

	qa_pairs = []

	for question_index in range(0, len(questions)):
		qa_pairs.append(Question(questions[question_index][0], answer_lists[question_index]))

	return qa_pairs

if __name__ == '__main__':
	load_dotenv()
	print(read_question_data(os.getenv("EXCEL_PATH")))
