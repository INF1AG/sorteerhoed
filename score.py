class score:
	def __init__(self):
		self.score = [0.0, 0.0, 0.0, 0.0]
	
	def add_score(self, score):
		for score_index in range(0, len(score)):
			self.score[score_index] += int(score[score_index])

	def get_score(self):
		return self.score