
from Question import Question

#Singelton object
class Questions(object):
    
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(Questions, self).__new__(self)
            self.__question_dictionary = {}
            self.__tags = []
            self.__question_key_words = ["سلام", "دوستان", "بچه", "آیا", "چرا", "کدوم", "کدام"]
            self.__responders = ["a_m_asali", "siavash_askarzadeh", "ashkanvg", "mobinashb", "AmirBabamahmoudi"
, "dannythedaredevil", "radbhdpv", "saharmf6", "nahid_a77"]
        return self.instance

    def is_valid_question(self, question_text, sender):
        if sender not in self.__responders:
            if(question_text.find('?') != -1 or question_text.find('؟') != -1):
                for key_word in self.__question_key_words:
                    if (key_word in question_text):
                        return True   
        
        return False

    def find_question(self, question_id):
        if question_id in self.__question_dictionary.keys():
            return True
        return False

    def __add_tag_in_questions(self, tag):
        for question in self.__question_dictionary.keys():
            question.add_tag(tag)


    def add_question(self, question_text, question_id, sender):
        if self.__question_dictionary.get(question_id) == None and self.is_valid_question(question_text, sender):
            new_question = Question(question_text, question_id)
            new_question.set_sender(sender)
            self.__question_dictionary[question_id] = new_question
            return True
        return False


    def add_tag(self, tag):
        if tag not in self.__tags:
            self.__tags.append(tag)
            self.__add_tag_in_questions(tag)
            return True
        return False

    def add_responder(self, responder):
        if responder not in self.__responders:
            self.__responders.append(responder)
            return True
        return False

    def add_question_key_word(self, new_key_word):
        if new_key_word not in self.__question_key_words:
            self.__question_key_words.append(new_key_word)
            return True
        return False

    def add_answer_to_question(self, question_id, answer):
        if self.__question_dictionary.get(question_id) != None:
            self.__question_dictionary.get(question_id).add_answer(answer)
            return True
        return False

    def get_question(self, question_id):
        return self.__question_dictionary.get(question_id)

    def get_questions(self):
        return list(self.__question_dictionary.values())


    
