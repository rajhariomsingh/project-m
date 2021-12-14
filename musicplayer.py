from os import close
from pygame import mixer
from tkinter import *
from tkinter import filedialog
import pyttsx3 

currentvol = float(0.5)

def playsong():
        filename=filedialog.askopenfilename(initialdir="C:/",title="sellect a song to play")
        currentsong= filename
        song=filename.split("/")
        song=song[-1]
        try:
                mixer.init()
                mixer.music.load(currentsong)
                mixer.music.set_volume(currentvol)
                mixer.music.play()
                songtitle.config(fg="black",text="now playing: "+str(song))
                vollume.config(fg="black",text="vollume: "+str(currentvol))
        
        except:
                
                songtitle.config(fg="black",text="ERROR PLAYING THE song")

def playmusic():
        try:
             mixer.music.unpause()
        except:
                songtitle.config(fg="black",text="Track not sellected")



def pausemusic():
        try:
             mixer.music.pause()
        except:
                songtitle.config(fg="black",text="Track not sellected")

def reducevol():
        try:
                global currentvol
                if currentvol<=0:
                        vollume.config(fg="black",text="MUTED :(")
                        return
                currentvol=currentvol-float(0.1)      
                currentvol=round(currentvol,1)
                mixer.music.set_volume(currentvol)
                vollume.config(fg="black",text="vollume: "+ str(currentvol))
        except:
                songtitle.config(fg="black",text="Track not sellectd")     

def increasevol():
        try:
                global currentvol
                if currentvol>=1:
                        vollume.config(fg="black",text="MAX VOLLUME o_o")
                        return
                currentvol=currentvol+float(0.1)      
                currentvol=round(currentvol,1)
                mixer.music.set_volume(currentvol)
                vollume.config(fg="black",text="vollume: "+ str(currentvol))
        except:
                songtitle.config(fg="black",text="Track not sellectd")          
# def sound():
    
#         playsound('C:\\Users\\ASUS\\OneDrive\\Desktop\\PROGRAMMING NOTES\\tagd.wav')
        
def click():
        name=textentry.get()
        
        # say = pyttsx3.init()
        # say.say("hello vrooo "+ name)
        # say.runAndWait()
          
        
        
        playing.delete(0.0,END)
        


        vro = "Hello vaiiiii <3 "+name
        playing.insert(END,vro)
        if(name =="abhinav" or name =="hariom" or name =="shubham" or name=="vaibhav" or name=="vaii"or name=="aditya"or name=="aaditya" or name=="h4wkeye" or name=="cat"):
                playsong()
        else:
                exit(0)

        
#main and labels       
Window = Tk()
Window.title("moosic")

Window.configure(background="black")

photo1 = PhotoImage(file="vaii.gif")
Label(Window,image=photo1 ,bg = "black") .grid(row=0,column=0,sticky=W)
Label(Window, text="moosic player dj ",bg="black",fg="white",font="none 48 bold") .grid(row=0, column=1,sticky=N)

Label(Window, text="Enter your name: ",bg="black",fg="white",font="none 20 bold") .grid(row=1, column=0,sticky=N)
songtitle=Label(Window,font=("calibri",12))
songtitle.grid(row=4,column=1,sticky=N)
vollume=Label(Window,font=("calibri",12))
vollume.grid(row=5,column=0,sticky=W)
#  entry box
textentry = Entry(Window, width=20,bg="white")
textentry.grid(row=1,column=1,sticky=W)

# buttons
#Button(Window,text="submit",command=click).grid(row=2,column=0,sticky=W)
Button(Window,text="sellect song",width=40,command=click).grid(row=2,column=1,padx=70,sticky=W)
Button(Window,text="play",width=10,command=playmusic).grid(row=3,column=2,sticky=W)
Button(Window,text="pause",command=pausemusic).grid(row=3,column=0,sticky=W)
Button(Window,text="+",width=15,command=increasevol).grid(row=4,column=0,sticky=W)
Button(Window,text="-",width=15,command=reducevol).grid(row=4,column=2,sticky=W)
#output box
playing= Text(Window,width=20,height=1,wrap=WORD,background="white",fg="black",font=("IMPACT",15))
playing.grid(row=1,column=1,columnspan=2,sticky=N)
Window.maxsize(width=950,height=300)
Window.mainloop()