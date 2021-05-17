from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import time
import datetime
import re
import parser_1
import parser_2


import keep_alive
keep_alive.keep_alive()


vk = vk_api.VkApi
vk = vk_api.VkApi(token="token")
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
				parser_1.init()
			if event.type == VkBotEventType.MESSAGE_NEW:
				peer_id = event.object.message["peer_id"] 
				message = event.object.message["text"].lower()
				id_from =  event.object.message["from_id"]
				user_name = vk.method("users.get", {"user_ids": id_from})[0]["last_name"]
				user_name += " " +vk.method("users.get", {"user_ids": id_from})[0]["first_name"]
				#conversation_id = event.object.message["conversation_message_id"] id сообщения

				print("----------------------------------------------------")
				if (peer_id >= 2000000001):
					try:
						print("Из беседы: " + (vk.method("messages.getConversationsById", {"peer_ids": peer_id})['items'][0]["chat_settings"]["title"]))
					except Exception as e:
						print("А хуй знает что за беседа")
					
					print("Id беседы: " + str(peer_id))
				print("Отправитель: " + str(user_name))
				print("Id отправителя: " + str(id_from))
				print("сообщение: " + str(message))
				
				if (message.lower() == "/погода") or (message.lower() == ".погода") :
					parser_2.init()
					msg(parser_2.output_str)
					msg("Источник:  " + parser_1.url)
				elif (message.lower()) == "/обнови данные":
					parser_1.init()
					msg(parser_1.suc)
					print(parser_1.url)
				elif message.lower() == "sic":
					msg("ss")
				elif message.lower() == ".time" or message.lower() == "/time":
					msg(datetime.datetime.today())
				temp = (message.lower().find("обнови ссылку") != -1)
				if temp == True:
					msg("Обновление ссылки...")
					l = re.findall("(?P<url>https?://[^\s]+)", message)
					if len(l) == 1:
						parser_1.url= l[0]
						msg("ссылка изменена.")
						parser_1.init()
						msg(parser_1.suc)
	except Exception as e:
		print(e)


