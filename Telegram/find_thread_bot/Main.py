from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import arabic_reshaper
from bidi.algorithm import get_display
from Questions import Questions
from Answers import Answers
from Question import Question


    # __api_id = 21546675
    # __api_hash = '389680699697981ba6c148ac70bc450d'


class Thread_finder: 
    def __init__(self, api_id, api_hash):
        self.__api_hash = api_hash
        self.__api_id = api_id
        self.__client =  TelegramClient('anon', api_id, api_hash)
        self.__questions = Questions()
        self.__answers = Answers()
        self.__number_of_message = 30


    def __make_file(self):
        file = open("Thread.txt", "a")
        for question in self.__questions.get_questions():
            file.write("Question: ")
            file.write(question.get_question_text())
            file.write("\n")
            question_answers = question.get_answers()
            file.write("Answers: \n")
            for answer in question_answers:
                file.write(answer.get_answer_text())
                file.write("\n")
            file.write("\n")    
        file.close()



    def __find_question_for_answer(self, message, reply_message):

        question_id = self.__answers.get_question_of_answer(reply_message.id)
        if self.__questions.find_question(reply_message.id):
            new_answer = self.__answers.make_answer(message.text, message.sender.username)
            self.__questions.add_answer_to_question(reply_message.id, new_answer)
            self.__answers.add_question_of_answer(message.id, reply_message.id)
                
        elif question_id != None:
            new_answer = self.__answers.make_answer(message.text, message.sender.username)
            self.__questions.add_answer_to_question(question_id, new_answer)
            self.__answers.add_question_of_answer(message.id, question_id)



    async def thread_finder(self, group_id):
        messages = await client.get_messages(group_id, self.__number_of_message)
        messages.reverse()
        for message in messages:
            if message.text != None and message.sender != None:
                if self.__questions.is_valid_question(message.text, message.sender.username):
                    self.__questions.add_question(message.text, message.id, message.sender.username)

                elif self.__answers.is_valid_answer(message.text, message.sender.username) and message.is_reply:
                    reply_message = await self.__client.get_messages(group_id, ids=message.reply_to_msg_id)
                    self.__find_question_for_answer(message, reply_message)
        
        for question in self.__questions.get_questions():
            await client.send_message('me', "Q&A")
            await client.send_message('me', question.get_question_text())
            question_answers = question.get_answers()
            for answer in question_answers:
                await client.send_message('me', answer.get_answer_text())
            await client.send_message('me', "#######################")
        self.__make_file()

    def get_client(self):
        return self.__client

    def set_number_of_message(self, new_number_of_message):
        self.__number_of_message = new_number_of_message



thread_finder = Thread_finder( 21546675, '389680699697981ba6c148ac70bc450d')
client = thread_finder.get_client()
with client:
    client.loop.run_until_complete(thread_finder.thread_finder(-1001594675442))






