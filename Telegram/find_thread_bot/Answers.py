
from Answer import Answer

#Singelton object
class Answers(object):

    __valuable_responders = ["a_m_asali", "siavash_askarzadeh", "ashkanvg", "mobinashb", "AmirBabamahmoudi"
, "dannythedaredevil", "radbhdpv", "saharmf6", "nahid_a77"]
    __answer_not_contain = ["خواهش میکنم", "خواهش می کنم", "?", "؟", "بفرمایید", "کدوم", "کدام", "آیا", "پیوی", "پی وی"]
    __question_of_answers_dictionary = {}

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(Answers, self).__new__(self)
        return self.instance

    def add_valuable_responder(self, responder):
        if responder not in self.__valuable_responders:
            self.__valuable_responders.append(responder)
            return True
        return False

    def add_word_not_in_answer(self, word):
        if word not in self.__answer_not_contain:
            self.__answer_not_contain.append(word)
            return True
        return False

    def add_question_of_answer(self, answer_id, question_id):
        if answer_id not in self.__question_of_answers_dictionary.keys():
            self.__question_of_answers_dictionary[answer_id] = question_id
            return True
        return False

    def is_valid_answer(self, answer_text, sender):
        if answer_text == "":
            return False
        if sender in self.__valuable_responders:
            return True
        
        for word in self.__answer_not_contain:
            if answer_text.find(word) != -1:
                return False
        return True

    def __does_have_valuable_sender(self, sender):
        if sender in self.__valuable_responders:
            return True
        return False

    def make_answer(self, answer_text, sender):
        if self.is_valid_answer(answer_text, sender) == True:
            new_answer = Answer(answer_text, self.__does_have_valuable_sender(sender))
            return new_answer
        return None

    def get_question_of_answer(self, answer_id):
        return self.__question_of_answers_dictionary.get(answer_id)
        