from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import time
import datetime

import keep_alive
keep_alive.keep_alive()

vk = vk_api.VkApi(token="token") #тут нужен ваш токен
vk._auth_token()

p = -1

vk.get_api()

longpoll = VkBotLongPoll(vk, 204221040)
print("Есть коннект!")

def msg(msg):
	vk.method("messages.send", {"peer_id":peer_id, "message": str(msg), "random_id": 0})
	print("Обратка: "+ str(msg) + "\n")



while True:
	try:
		for event in longpoll.listen():
			time=datetime.datetime.today().timetuple()[3]
			if time != p:
				p=time
				from parser_1 import suc
			if event.type == VkBotEventType.MESSAGE_NEW:

				peer_id = event.object.message["peer_id"] 
				message = event.object.message["text"].lower()
				id_from =  event.object.message["from_id"]
				user_name = vk.method("users.get", {"user_ids": id_from})[0]["last_name"]
				user_name += " " +vk.method("users.get", {"user_ids": id_from})[0]["first_name"]
				#conversation_id = event.object.message["conversation_message_id"] id сообщения
				print("----------------------------------------------------")
				if (peer_id >= 2000000001):
					print("Из беседы: " + (vk.method("messages.getConversationsById", {"peer_ids": peer_id})['items'][0]["chat_settings"]["title"]))
					print("Id беседы: " + str(peer_id))
				print("Отправитель: " + str(user_name))
				print("Id отправителя: " + str(id_from))
				print("сообщение: " + str(message))
				
				if (message.lower() == "/погода") or (message.lower() == ".погода") :
					from parser_2 import output_str
					msg(str(output_str))
				elif (message.lower()) == "/обнови данные":
					from parser_1 import suc
					msg(suc)
				elif message.lower() == "?":
					msg("?")
				elif message.lower() == ".time" or message.lower() == "/time":
				  msg(datetime.datetime.today())
        


	except Exception as e:
		print(e)


