
#importing required modules

import tkinter as tk
from gtts import gTTS
import os
import pyttsx3
import pytesseract as tess
from PIL import Image
from tkinter import filedialog as fd

#creating window

root=tk.Tk()
root.config(bg="orange")
root.title(" Audio")

root.state("zoomed")

#TO DOWNLOAD TESSERACT APP
# USE THIS LINK TO DOWNLOAD FOR 32 BIT https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.0.0-alpha.20200328.exe
# USE THIS LINK TO DOWNLOAD FOR 64 BIT https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe
#feeding the path of the tess app
tess.pytesseract.tesseract_cmd=r"C:\\Users\\mypc\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"

def image_to_text():#defining function
	root.config(bg="#4d79ff")#changing background
	button.place(x=450,y=20)#placing button in new position
	button1.destroy()#destroying unneccesary buttons
	button2.destroy()#destroying unneccesary buttons
	label1.destroy()#destroying unneccesary label


	img=Image.open(fd.askopenfilename(defaultextension='.png',filetypes= [('Image (.png file)','.png'),('Image (.JPG file)','.JPG')] ))#asking image location

	text=tess.image_to_string(img)#extracting text from image
	label=tk.Label(root,text=text,bg="#4d79ff",fg="white")#preview the image in text
	label.place(x=350,y=100)#placing label
	label.config(font=("Ariel",20))#configuring label
	button.place(x=200,y=20)#placing button in new position

	def buttonaenter(event):
		buttona.config(bg='black',fg='white')
	def buttonaleave(event):
		buttona.config(bg='white',fg='black')

	def buttonbenter(event):
		buttonb.config(bg='black',fg='white')
	def buttonbleave(event):
		buttonb.config(bg='white',fg='black')

	def save():#defining function
		
		a=fd.asksaveasfilename(defaultextension='.txt',filetypes= [('Text files (.txt file)','.txt')
		] )#asking file location to save
		file=open(a,"w")#saving file
		file.write(text)
		file.close()

	def read():#defing function
		engine = pyttsx3.init()#assigning engine variable
		engine.say(text)
		engine. setProperty("rate", 0)
		engine.runAndWait()



	buttona=tk.Button(root,text="Save as Text file",command=save,width=20,height=2,bg='white')
	buttona.place(x=700,y=20)#Button
	buttona.bind('<Enter>',buttonaenter)
	buttona.bind('<Leave>',buttonaleave)

	buttonb=tk.Button(root,text="Read Image",command=read,width=20,height=2,bg='white')
	buttonb.place(x=450,y=20)#Buttons
	buttonb.bind('<Enter>',buttonbenter)
	buttonb.bind('<Leave>',buttonbleave)

def img_to_audio():#defining function
	root.config(bg="#ff80ff")#changing background colour
	button1.place(x=450,y=20)#changing position of button
	button.destroy()#destroying unneccesary buttons
	button2.destroy()#destroying unneccesary buttons
	label1.destroy()#destroying unneccesary label

	img=Image.open(fd.askopenfilename(defaultextension='.png',filetypes= [('Image (.png file)','.png'),('Image (.JPG file)','.JPG')] ))#asking image location

	text=tess.image_to_string(img)#extracting text from image
	label=tk.Label(root,text=text,bg="#ff80ff",fg="white")#Label
	label.place(x=350,y=100)
	label.config(font=("Ariel",20))
	button1.place(x=200,y=20)

	def buttonaenter(event):
		buttona.config(bg='black',fg='white')
	def buttonaleave(event):
		buttona.config(bg='white',fg='black')

	

	def convt():#defining function
		label=tk.Label(root,text="Audio file is saved only when internet is available",bg="#ff80ff",fg="black")
		label.place(x=400,y=70)#labels
		audio=gTTS(text=text,lang="en",slow=False)
		
		audio.save(fd.asksaveasfilename(defaultextension='.mp3',filetypes= [('audio (.mp3 file)','.mp3')] ))
		
		



	buttona=tk.Button(root,text="Save Image as audio file",command=convt,width=20,height=2,bg='white')
	buttona.place(x=700,y=20)#buttons
	buttona.bind('<Enter>',buttonaenter)
	buttona.bind('<Leave>',buttonaleave)





def text_to_audio():#defining function
	root.config(bg="#66FF33")
	button2.place(x=450,y=20)
	button.destroy()
	button1.destroy()
	label1.destroy()
	f=open(fd.askopenfilename(defaultextension='.txt',filetypes= [('text file (.txt file)','.txt')] )).read()
	label=tk.Label(root,text=f,bg="#66ff33",fg="black")
	label.place(x=350,y=100)
	label.config(font=("Ariel",20))
	button2.place(x=200,y=20)


	def say():#defining function to read


		engine = pyttsx3.init()
		engine.say(f)
		engine. setProperty("rate", 0)
		engine.runAndWait()

	def convt():#defining function to convert txt to mp3 file
		label=tk.Label(root,text="Audio file is saved only when internet is available",bg="#66ff33",fg="black")
		label.place(x=400,y=70)
		audio=gTTS(text=f,lang="en",slow=False)
		
		audio.save(fd.asksaveasfilename(defaultextension='.mp3',filetypes= [('audio (.mp3 file)','.mp3')] ))
		

	def buttonaenter(event):
		buttona.config(bg='black',fg='white')
	def buttonaleave(event):
		buttona.config(bg='white',fg='black')

	def buttonbenter(event):
		buttonb.config(bg='black',fg='white')
	def buttonbleave(event):
		buttonb.config(bg='white',fg='black')

	buttona=tk.Button(root,text="Read Text file",width=20,height=2,bg='white',command=say)
	buttona.place(x=700,y=20)
	buttona.bind('<Enter>',buttonaenter)
	buttona.bind('<Leave>',buttonaleave)



	buttonb=tk.Button(root,text="Save Text file as Audio file",width=20,height=2,bg='white',command=convt)
	buttonb.place(x=450,y=20)
	buttonb.bind('<Enter>',buttonbenter)
	buttonb.bind('<Leave>',buttonbleave)

def buttonenter(event):
    button.config(bg='black',fg='white')
def buttonleave(event):
    button.config(bg='white',fg='black')
def button1enter(event):
    button1.config(bg='black',fg='white')
def button1leave(event):
    button1.config(bg='white',fg='black')
def button2enter(event):
    button2.config(bg='black',fg='white')
def button2leave(event):
    button2.config(bg='white',fg='black')
def button3enter(event):
    button3.config(bg='black',fg='white')
def button3leave(event):
    button3.config(bg='white',fg='black')

button=tk.Button(root,text="Image To Text",command=image_to_text,width=20,height=2,bg='white')
button.place(x=450,y=160)#buttons
button.bind('<Enter>',buttonenter)
button.bind('<Leave>',buttonleave)


button1=tk.Button(root,text="Image to Audio",width=20,height=2,bg='white',command=img_to_audio)
button1.place(x=450,y=220)#buttons
button1.bind('<Enter>',button1enter)
button1.bind('<Leave>',button1leave)


button2=tk.Button(root,text="Text file to audio",width=20,height=2,bg='white',command=text_to_audio)
button2.place(x=450,y=280)#buttons
button2.bind('<Enter>',button2enter)
button2.bind('<Leave>',button2leave)



label1=tk.Label(root,text="File Reader",bg="orange",fg="black")
label1.place(x=420,y=60)#label
label1.config(font=("Ariel",30))
	

root.mainloop()


#Developer contact: sriramvkumar007@gmail.com
#complete explaination in readme file