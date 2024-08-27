from tkinter import *
import requests
import json

root = Tk()
root.title('Wheather App')

try:
    api_request = requests.get('api_key')
    api = json.loads(api_request.content)
except Exception as e:
    api = "Error..."

my_label = Label(root, text=api)
my_label.pack()

root.mainloop()
