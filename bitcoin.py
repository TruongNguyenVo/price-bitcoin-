import requests
import tkinter as tk
from datetime import datetime
import json

s = requests.Session()
def Show_Price_Bitcoin():
	respone = s.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR')
	# print('------------Giá Bitcoin--------')
	# print('Giá Đô La: ',int(respone.json()['USD']))
	# print('Giá Yên: ',int(respone.json()['JPY']))
	# print('Giá Euro: ',int(respone.json()['EUR']))
	price_usd = respone.json()['USD']
	price_jpy = respone.json()['JPY']
	price_eur = respone.json()['EUR']
	time = datetime.now().strftime('%H:%M:%S')

	#update value for Price
	labelPrice_USD.config(text = 'Giá Đô La: '+ str(price_usd) + "$")
	labelPrice_JPY.config(text = 'Giá Yên: '+ str(price_jpy) + "¥")
	labelPrice_EURO.config(text = 'Giá Euro: '+ str(price_eur) + "€")

	#update value for time
	labelTime.config(text = "Update at: " +time)

	#update value after 2 second
	canva.after(2000,Show_Price_Bitcoin)

canva = tk.Tk() #creat a Form
canva.geometry("400x500") #size
canva.title("Bitcoin Tracker") #title form

#font 
f1 = ('time new roman',24,'bold')
f2 = ('poppins',22,'bold')
f3 = ('time new roman',18,'bold')

#label Title of From
label = tk.Label(canva, text="Bitcoin Price", font=f1)
label.pack(pady = 20)

#label Price USD of Form
labelPrice_USD = tk.Label(canva, font=f2)
labelPrice_USD.pack(pady = 20)

#label Price JPY of Form
labelPrice_JPY = tk.Label(canva, font=f2)
labelPrice_JPY.pack(pady = 20)

#label Price EURO of Form
labelPrice_EURO = tk.Label(canva, font=f2)
labelPrice_EURO.pack(pady = 20)

#label Time of Form
labelTime = tk.Label(canva,font=f3)
labelTime.pack(pady = 20)

Show_Price_Bitcoin()
#show form
canva.mainloop()