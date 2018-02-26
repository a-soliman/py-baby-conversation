import random

def get_random_question():
	questions = [
		"Why is the sky blue?",
		"Why do we have to go to school?",
		"why do we have to sleep?"
	]

	rand_num = random.randint(0, len(questions))

	return questions[rand_num]
	

