import asyncio
from pyrogram import Client

api_id = 21546675
api_hash = '389680699697981ba6c148ac70bc450d'

app = Client("my_account2", api_id=api_id, api_hash=api_hash)

# app.run()
# app = Client("my_account2")

group_ids = [-1001422569087, -1001594675442]
groups_title = ["آقای اپلای(کانادا و آمریکا)"]

@app.on_message()
async def my_handler(client, message):
    if message.chat.id not in group_ids and message.chat.title in groups_title:
        group_ids_file = open("group_ids.txt", "a")
        group_ids.append(str(message.chat.id))
        group_ids_file.write("title: ")
        group_ids_file.write(str(message.chat.title))
        group_ids_file.write("\n")
        group_ids_file.write("id: ")
        group_ids_file.write(str(message.chat.id))
        group_ids_file.write("\n")
        group_ids_file.close()
    



app.run()