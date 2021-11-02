import pandas
import itertools

class Question: 
	def __init__(self, question, answers):
		self.question = question
		self.answers = answers


def get_column(wb, name):
	return pandas.DataFrame(wb, columns=[name]).values.tolist()

def main():
	loc = "/Users/wouter/OneDrive - Hogeschool Leiden/IPOHBO AG 2.1/Challengeweek #fun/stap 3 challenge week.xlsx"
	wb = pandas.read_excel(loc)
	questions = get_column(wb, "question")
	questions = [x for x in questions if not pandas.isna(x)]

	options = list(itertools.chain(get_column(wb, "option")))

	# print(options)

	answers = list(itertools.chain(get_column(wb, "answer")))
	constructed_answers = zip(options, answers)

	ln = 0

	print(list(constructed_answers))

	for q in questions:
		print(q)
		
		
		

if __name__ == '__main__':
	main()
