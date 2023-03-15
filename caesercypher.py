from tkinter import *
from PIL import ImageTk,Image
#caeser cypher

def encrypt(text,s):
    res=""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            res += chr((ord(char) + s-65) % 26 + 65)
            # Encrypt lowercase characters in plain text
        else:
            res += chr((ord(char) + s - 97) % 26 + 97)
    ans= "Plain Text : "+text+"\nShift Value : "+str(s)+"\nCipher : "+res
    return ans
#check the above function
def create():
    txt=e1.get()
    k=key.get()
    result=encrypt(txt,int(k))
#    lbl4.delete("0.0")
    lbl4.insert(END,result)
def clear():
    e1.delete("0",END)
    key.delete("0",END)
    lbl4.delete("0.0",END)
def clear1():
    de1.delete("0",END)
    Dlbl4.delete("0.0",END)
    
def hack():
    message = de1.get() #encrypted message
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dict={}
    for key in range(len(LETTERS)):
        translated = ''
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
            dict[key] = translated
            
    for i in dict:
        has='Hashkey '+str(i)+' : '+dict[i]+'\n'
        Dlbl4.insert(END,has)
            
root=Tk()
root.title("Caser Cypher")
root.geometry('1000x1000')
m=Frame(root,height=800,width=1000,bg='purple')
m.pack()
lbl=Label(m,text='Caeser Cypher',font='Times 32 bold',bg='purple')
lbl.place(x=150,y=50)
canvas = Canvas(m, width = 400, height = 300,bg= 'purple')  
canvas.place(x=600,y=10) 
img = ImageTk.PhotoImage(Image.open("cypherimage.png"))  
canvas.create_image(20, 20, anchor=NW, image=img)      

frame=Frame(m,bd=10,height=500,width=1000)
frame.place(x=0,y=200)
#Encryption frame
Eframe=Frame(frame,bd=10,height=500,width=500,bg='lightgreen')
Eframe.place(x=0,y=0)
lbl1=Label(Eframe,text='Ecryption', font='Times 24 bold',bg='lightgreen')
lbl1.place(x=150,y=50)
#text entry
lbl2=Label(Eframe,text='Enter Text :',bg='lightgreen', font='Times 12')
lbl2.place(x=100,y=100)
e1=Entry(Eframe)
e1.place(x=250,y=100)
#key entry
lbl3=Label(Eframe,text='Enter Shift Key :', bg='lightgreen', font='Times 12')
lbl3.place(x=100,y=150)
key=Entry(Eframe)
key.place(x=250,y=150)
#display result
lbl4=Text(Eframe,height=10, width=30)
lbl4.place(x=125,y=200)
#Button
button=Button(Eframe,text='Encrypt',bg='red',command = create)
button.place(x=100,y=400)
button=Button(Eframe,text='Reset',bg='red',command = clear)
button.place(x=400,y=400)

#decryption frame
Dframe=Frame(frame,bd=10,height=500,width=500,bg='yellow')
Dframe.place(x=500,y=0)
Dlbl1=Label(Dframe,text='Decryption', font='Times 24 bold',bg='yellow')
Dlbl1.place(x=150,y=50)
#text entry
Dlbl2=Label(Dframe,text='Enter Cypher Text :', font='Times 12',bg='yellow')
Dlbl2.place(x=100,y=100)
de1= Entry(Dframe)
de1.place(x=250,y=100)
#letters
LETTERS = 'Letters : ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Dlbl3=Label(Dframe,text=LETTERS, font='Times 12',bg='yellow')
Dlbl3.place(x=75,y=150)
#display result
Dlbl4=Text(Dframe,height=10,width=30)
Dlbl4.place(x=125,y=200)
#Button
button=Button(Dframe,text='Decrypt',bg='red',command = hack )
button.place(x=100,y=400)
button=Button(Dframe,text='Reset',bg='red',command = clear1)
button.place(x=400,y=400)

root.mainloop()