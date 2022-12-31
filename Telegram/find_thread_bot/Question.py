
from Answer import Answer

class Question:

    __tags = []
    __group_id = None
    __sender = None

    def __init__(self, question_text, question_id):
        self.__question_text = question_text
        self.__question_id = question_id
        self.__answers = []

    def __find_tag(self, tag):
        if self.__question_text.find(tag) != -1:
            return True
        return False

    def add_answer(self, answer):
        if answer not in self.__answers:
            self.__answers.append(answer)
            return True
        return False

    def add_tag(self, tag):
        if tag not in self.__tags:
            self.__tags.append(tag)
            return True
        return False

    def set_group_id(self, group_id):
        if self.__group_id == None:
            self.__group_id = group_id
            return True
        return False

    def set_sender(self, sender):
        if self.__sender == None:
            self.__sender = sender
            return True
        return False
    
    def get_tags(self):
        return self.__tags

    def get_group_id(self):
        return self.__group_id

    def get_question_id(self):
        return self.__question_id

    def get_question_text(self):
        return self.__question_text

    def get_answers(self):
        return self.__answers

    def get_sender(self):
        return self.__sender
    

        

    
