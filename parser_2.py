# pip install beautifulsoup4 lxml
from bs4 import BeautifulSoup
import datetime

weekday=datetime.datetime.today().isoweekday()
time=datetime.datetime.today().timetuple()[3]+7
if time >=24:
  time-=24
  weekday+=1
output_str =""
try:
	with open("index.html", encoding='utf-8') as file:
		src = file.read()
except Exception as e:
	print(e)
	
def weekday_str(x):
	if x >=8:
		x-=7
	if x == 1:
		return("Понедельник")
	elif x == 2: 
		return("Вторник")
	elif x == 3: 
		return("Среда")
	elif x == 4: 
		return("Четверг")
	elif x == 5: 
		return("Пятница")
	elif x == 6: 
		return("Суббота")
	elif x == 7: 
		return("Воскресенье")

def rain_check(a,x):
	for i in range(a,x):
		if str(rain[i]).split("'")[3] != "Явления погоды отсутствуют":
			return(str(rain[i]).split("'")[3])
	return("Явления погоды отсутствуют")

try:
	soup = BeautifulSoup(src,"lxml")

	t = soup.find_all(class_="t_0")
	cur_temperature = t[1]

	all_temperatures = soup.find_all("div",class_="t_0")

	rain = soup.find_all("div",class_="pr_0")



	cur_temperature=cur_temperature.text.strip()
	output_str+=("Температура сейчас: " +cur_temperature + "\n") 



	for i in range(0,23):
		all_temperatures[i] = all_temperatures[i].text.strip()


	td = 4-((time + 5)  // 6)
	temp = 0
	if time < 19: #Прогноз на сегодня

		output_str+=("Прогноз на сегодня: " + "\n")
		output_str+=(rain_check(0,td) + "\n")
		output_str+=("Температура в °C:" + "\n")
		while td >=1:
			output_str+=("в " + str(25-td*6) + "ч. " + all_temperatures[temp]+ "\n")
			td-=1
			temp+=1

	td = 4
	output_str+=("Прогноз на " + weekday_str(weekday+1)+" (завтра):"+ "\n")
	output_str+=(rain_check(temp,td+temp)+ "\n")
	output_str+=("Температура в °C:"+ "\n")
	while td >=1:
			output_str+=("в " + str(25-td*6) + "ч. " + all_temperatures[temp]+ "\n")
			td-=1
			temp+=1

except Exception as e:
	print(e)



