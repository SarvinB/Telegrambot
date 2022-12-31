import pytest
from Questions import Questions
from Question import Question
from Answers import Answers
from Answer import Answer

class Test_questions:

    def test_singelton(self):
	    questions1 = Questions()
	    questions2 = Questions()
	    check_singelton = questions1 is questions2
	    assert check_singelton == True

    def test_validate_question(self):
	    questions = Questions()
	    result = questions.is_valid_question("invalid_text", "username")
	    assert result == False

    def test_find_question(self):
	    questions = Questions()
	    result = questions.find_question(-1) #question_id > 0
	    assert result == False

    def test_add_question(self):
	    questions = Questions()
	    result = questions.add_question("کدام?", 1, "username")
	    assert result == True

    def test_add_question_key_word(self):
	    questions = Questions()
	    result = questions.add_question_key_word("کدام")
	    assert result == False

    def test_add_answer_to_question(self):
	    questions = Questions()
	    result = questions.add_answer_to_question(1, "answer")
	    assert result == True

class Test_answers:

	def test_singelton_answers(self):
	    answers1 = Answers()
	    answers2 = Answers()
	    check_singelton = answers1 is answers2
	    assert check_singelton == True

	def test_add_valuable_responder(self):
	    answers = Answers()
	    result = answers.add_valuable_responder("valid responder")
	    assert result == True

	def test_add_word_not_in_answer(self):
	    answers = Answers()
	    result = answers.add_word_not_in_answer("word")
	    assert result == True
	
	def test_add_question_of_answer(self):
	    answers = Answers()
	    result = answers.add_question_of_answer(1, 1)
	    assert result == True

	def test_is_valid_answer(self):
	    answers = Answers()
	    result = answers.is_valid_answer("", "sender")
	    assert result == False

class Test_question:

	def test_add_answer(self):
		question = Question("question_text", 1)
		result = question.add_answer("answer2")
		assert result == True
	
class Test_answer:
	def test_set_sender(self):
		answer = Answer("answer_text", True)
		result = answer.set_sender("sender")
		assert result == True
