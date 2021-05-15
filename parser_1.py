# pip install beautifulsoup4 lxml
import requests
suc ="1"
url="https://rp5.ru/Погода_в_Лесосибирске"

headers = {
	"Accept": "text/css,*/*;q=0.1",
	"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
} 


try:

	reg = requests.get(url)

	src= reg.text
	with open ("index.html" , "w",encoding="utf-8") as file:
		file.write(requests.get(url).text)
	suc="Парсинг успешен"
except Exception as e:
	print(e)

