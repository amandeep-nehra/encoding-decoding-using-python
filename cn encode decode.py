from tkinter import *
import base64
root=Tk()
root.geometry('560x500')
bg = PhotoImage(file='cnimg.png')
canvas1=Canvas(root,width=300,height=300)
canvas1.pack(fill="both",expand=True)
canvas1.create_image(0,0,image=bg,anchor="nw")
root.resizable(0,0)
root.title("Encryption-Decryption")
Label(root,text="ENCRYPTION-DECRYPTION",font="Mistral 25 bold").pack(side=TOP)
Text=StringVar()
private_key=StringVar()
mode=StringVar()
Result=StringVar()
def encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c=key[i % len(key)]
        enc.append(chr(ord(message[i]) + ord(key_c) %256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
def decode(key,enc):
    dec=[]
    enc=base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c=key[i % len(key)]
        dec.append(chr((256 + ord(enc[i]) - ord(key_c)) % 256))
    return "".join(dec)

def Mode():
    if(mode.get() == 'e'):
        Result.set(encode(private_key.get(), Text.get()))    
    elif(mode.get() == 'd'):
        Result.set(decode(private_key.get(), Text.get())) 
    else:
        Result.set("inavlid mode")

def Exit():
    root.destroy() 

def Reset():
    Text.set("") 
    private_key.set("")
    mode.set("")
    Result.set("")
Label (root, font= 'Bazooka 12 bold', text='MESSAGE').place(x= 60,y=60)
Entry(root, font='Bings 10', textvariable = Text, bg= 'ghost white').place(x=290, y = 60) 
Label (root, font= 'Helvetica 12 bold', text='KEY').place(x=60, y = 90)
Entry(root, font='Helvetica 10', textvariable= private_key, bg='ghost white').place(x=290, y = 90)
Label(root, font= 'Helvetica 12 bold', text='MODE (e-encode, d-decode)').place(x=60, y = 120)
Entry(root, font= 'Helvetica 10', textvariable = mode, bg= 'ghost white').place(x=290, y = 120)
Label(root, font= 'Helvetica 12 bold', text='OUTPUT').place(x=60, y = 150)
Entry(root, font='Helvetica 10 bold', textvariable= Result, bg='ghost white').place(x=290, y = 150)
Button(root, font= 'Helvetica 10 bold', text = "RESET", padx= 2,bg ='Gray', command = Reset).place(x=100, y=210)
Button (root, font='Helvetica 10 bold',text ='RESULT', width= 6, command=Mode, bg="LimeGreen", padx=2).place(x=200, y = 210)
Button(root, font= 'Helvetica 10 bold', text= 'EXIT', width=6, command= Exit,bg= 'OrangeRed', padx=2, pady=2).place(x=300,y=210)
root.mainloop()