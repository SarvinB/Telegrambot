

class Answer:

    def __init__(self, answer_text, sender_value):
        self.__answer_text = answer_text
        self.__sender_value = sender_value
        self.__sender = ""

    def set_sender(self, sender):
        if self.__sender == "":
            self.__sender = sender
            return True
        return False

    def is_valuable_sender(self):
        return self.__sender_value

    def get_answer_text(self):
        return self.__answer_text

    def get_sender(self):
        return self.__sender


    

