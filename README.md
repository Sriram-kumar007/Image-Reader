READ ME


 SETUP:

 This project "Audio" extract text from image and the computer is allowed to 
 read it for you.to.Here you can convert texts in Image to Text file and also 
 hear it.you can also convert text file as an audio file.Here to extract text 
 i used pytesseract and to convert it hearable i used two modules gtts and 
 pyttsx3,because to use gtts module you need internet access so i gave the 
 option of pyttsx3 when there is no internet.Then you an ask me what is the 
 nessecity of gtts? the answer is, with pyttsx3 you can just hear the text 
 and cannot be converted in the mp3 form.To do this you want gtts.Lets see 
 how to install these modules
 
 1. To run this correctly you need pytesseracrt and tesseract application
 	to install pytesseract in cmd use this command - pip install pytesseract

 	To install tesseract application use these links:

 	32 bit - https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.0.0-alpha.20200328.exe

 	64 bit - https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe

 	for more details visit this github account - https://github.com/ub-mannheim/tesseract/wiki

 	You can also search it manually.

 2. To install gtts in cmd use this command - pip install gTTS

 3. To install pyttsx3 in cmd use this command - pip install pyttsx3

 4. To install PIL in cmd use this command - pip install Pillow-PIL

 CODE EXPLAINATION:

 HERE,I HAVE ONLY MENTIONED THE IMPORTANT CODE AND NOT THE REPETATIVE CODE



 import tkinter as tk - importing tkinter to make window

 from gtts import gTTS - importing gtts to convert text to mp3 file

 import os - importing os

 import pyttsx3 - importing pyttsx3 to read text

 import pytesseract as tess - importing pyttsx3 to extract text from image

 from PIL import Image - importing  Image from PIL to access images

 from tkinter import filedialog as fd - importing filedialog from tkinter to 
 										ask the location of files

 root=tk.Tk() - assigning tkinter as root

 root.config(bg="orange") - assigning bg colour

 root.title("Audio") - assigning title

 root.state("zoomed") - assigning the state as zoomed

 tess.pytesseract.tesseract_cmd=r"C:\\Users\\mypc\\AppData\\Local\\Tesseract-OCR\\tesseract.exe" - This is the most important line in this code this code 
 					  says the computer the path of tesseract application. The path i have given is the default path that tesseract takes.Sometimes the computer name that is "mypc" in my case may differ.



 def image_to_text(): - defining function

	root.config(bg="#4d79ff") - changing background
	button.place(x=450,y=20)  - placing button in new position
	button1.destroy() - destroying unneccesary buttons
	button2.destroy() - destroying unneccesary buttons
	label1.destroy() - destroying unneccesary label


	img=Image.open(fd.askopenfilename(defaultextension='.png',filetypes= [('Image (.png file)','.png'),('Image (.JPG file)','.JPG')] )) - asking image location

	text=tess.image_to_string(img) - extracting text from image
	label=tk.Label(root,text=text,bg="#4d79ff",fg="white") - preview the image in text
	label.place(x=350,y=100) - placing label
	label.config(font=("Ariel",20)) - configuring label
	button.place(x=200,y=20) - placing button in new position

	def buttonaenter(event): - This code change the bg of the button when 
							   mouse pointer touches it.This code is just for look 
		buttona.config(bg='black',fg='white')

	def buttonaleave(event):
		buttona.config(bg='white',fg='black')

	def buttonbenter(event):
		buttonb.config(bg='black',fg='white')

	def buttonbleave(event):
		buttonb.config(bg='white',fg='black')

	def save(): - defining function
		
		a=fd.asksaveasfilename() - asking file location to save
		file=open(a,"w") - opening file
		file.write(text) - writing 
		file.close() - closeing file and saveing

	def read(): - defing function
		engine = pyttsx3.init() - assigning engine variable
		engine.say(text) - asking engine to say
		engine. setProperty("rate", 0) - this refers to the speed that the 
										 computer takes to spell each words
		engine.runAndWait() - saying to engine just run and wait



	buttona=tk.Button(root,text="Save as Text file",command=save,width=20,height=2,bg='white')
	buttona.place(x=700,y=20) - Button
	buttona.bind('<Enter>',buttonaenter) - code for calling the`function to change the bg of the button
	buttona.bind('<Leave>',buttonaleave)

	buttonb=tk.Button(root,text="Read Image",command=read,width=20,height=2,bg='white')
	buttonb.place(x=450,y=20)#Buttons
	buttonb.bind('<Enter>',buttonbenter)
	buttonb.bind('<Leave>',buttonbleave)

 def img_to_audio(): - defining function

	root.config(bg="#ff80ff") - changing background colour

	button1.place(x=450,y=20) - changing position of button

	button.destroy() - destroying unneccesary buttons

	button2.destroy() - destroying unneccesary buttons

	label1.destroy() - destroying unneccesary label

	img=Image.open(fd.askopenfilename(defaultextension='.png',filetypes= [('Image (.png file)','.png'),('Image (.JPG file)','.JPG')] )) - asking image location

	text=tess.image_to_string(img) - extracting text from image

	label=tk.Label(root,text=text,bg="#ff80ff",fg="white") - Label

	label.place(x=350,y=100)

	label.config(font=("Ariel",20))

	button1.place(x=200,y=20)


	def convt(): - defining function

		label=tk.Label(root,text="Audio file is saved only when internet is available",bg="#ff80ff",fg="black")

		label.place(x=400,y=70) - labels

		audio=gTTS(text=text,lang="en",slow=False) - assigning a variable audio to gtts
		
		audio.save(fd.asksaveasfilename(defaultextension='.mp3',filetypes= [('audio (.mp3 file)','.mp3')] )) - saving the audio
		
		


def text_to_audio(): - defining function

	
	f=open(fd.askopenfilename(defaultextension='.txt',filetypes= [('text file (.txt file)','.txt')] )).read() - file handling

	label=tk.Label(root,text=f,bg="#66ff33",fg="black")
	label.place(x=350,y=100)
	label.config(font=("Ariel",20)) - label
 - 
	button2.place(x=200,y=20)


	def say():#defining function to read


		engine = pyttsx3.init() - assigning a variable engine to pyttsx3

		engine.say(f) - asking engine to say the handled file

		engine. setProperty("rate", 0) - this refers to the speed that the 
										 computer takes to spell each words
		engine.runAndWait() - asking engine to just run and wait

	def convt(): - defining function to convert txt to mp3 file

		label=tk.Label(root,text="Audio file is saved only when internet is available",bg="#66ff33",fg="black")
		label.place(x=400,y=70)

		audio=gTTS(text=f,lang="en",slow=False) - assigning a variable audio 
												  to gtts
		
		audio.save(fd.asksaveasfilename(defaultextension='.mp3',filetypes= [('audio (.mp3 file)','.mp3')] )) - asking the location to save the 		                                    mp3 file
		

 
 root.mainloop() - mainloop 
 HOW TO USE IT ?

 		I know the installation and setup is quiet long but it is easy to use.


 ADVANTAGES:

 	1. If you are lazy of reading books like me then you can use this 
 	   project.

 	2. If you have any notice in physical form like paper then instead of 
 	   scanning you can also use this and convert to text file.

 	3. I think this simple idea will develop your ideas and let you know a 
 	   new module.

 DISADVANTAGES:

 	1. The main and only disadvantage that i think is you cannot read pdf,i 
 	   mention it here because most of the books are in pdf form ,but you 
 	   can use it after changing it in text format.

 Developer contact: sriramvkumar007@gmail.com

 send me your comments in this gmail account
