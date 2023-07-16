from tkinter import *
from tkinter.filedialog import *
from time import sleep
from tkinter import messagebox
import os

form = Tk()
form.title(' Dictionary ')
form.geometry('800x480+400+100')
form.minsize(800,480)
form.maxsize(800,480)
expression = ""
equation = StringVar()
kelime = []
kelimeAnlami = []
cumle = []
counter = 0
counter2 = 0
counterBul = 0
butonkontrol = 0
aramakontrol = 0
bilgikontrol = 0

def main():
    global kelime
    global kelimeAnlami
    global cumle
    global counter2
    global fblue
    global fwhite
    global lb
    global lb2
    equation = StringVar()
    expression = ""

    def on_closing():  
        global expression
        if messagebox.askokcancel("Quit","Do you want to quit?"):
            sleep(0.1)
            form.destroy()
    form.protocol("WM_DELETE_WINDOW", on_closing)

    def press(num):
        global expression
        expression = expression + str(num)
        equation.set(expression)

    def clear():
         global expression
         expression = ""
         equation.set("") 

    def oku():
        global counter2
        global kelime
        global kelimeAnlami
        global cumle
        del kelime 
        del kelimeAnlami
        del cumle
        kelime = []
        kelimeAnlami = []
        cumle = []
        counter2 = 0
        satir = ""
        this=open("Word.txt","a")
        this.close()
        this=open("Word-opposite.txt","a")
        this.close()
        this=open("Sentences.txt","a")
        this.close()
        with open("Word.txt", 'r') as dosya:  
              for satir in dosya:
                  satir=satir.rstrip()
                  kelime.append(satir)
        with open("Word-opposite.txt", 'r') as dosya:  
              for satir in dosya:
                  satir=satir.rstrip()
                  kelimeAnlami.append(satir)
        with open("Sentences.txt", 'r') as dosya:  
              for satir in dosya:
                  satir=satir.rstrip()
                  cumle.append(satir)
        counter2 = len(kelime)

    def kaydet():
        global cumle
        global kelimeAnlami
        global kelime
        global buton4
        global lb
        lb.destroy()
        tut = len(kelime)
        tut2 = ""
        this=open("Word.txt","a")
        tut2 = kelime[tut-1]
        this.write(tut2)
        this.write("\n")
        this.close()
        tut2=""
        tut2 = kelimeAnlami[tut-1]
        this=open("Word-opposite.txt","a")
        this.write(tut2)
        this.write("\n")
        this.close()
        tut2=""
        tut2 = cumle[tut-1]
        this=open("Sentences.txt","a")
        this.write(tut2)
        this.write("\n")
        this.close()
        sleep(0.1)
        bilgi()

    def ekran():
        global cumle
        global etiket2
        global etiket3
        global counter
        global buton3
        global girdi3
        global buton4
        global counter2
        global lb
        cumle.append(girdi3.get())
        counter2 = len(kelime) - int(1)
        if len(girdi3.get()) == 0:
            etiket2.config(text=' '*93)
            etiket2.config(text='No information entered')
            cumle.pop()
        else:
            lb.destroy()
            expression = ""
            equation.set("")
            lb = LabelFrame(fwhite,text = 'Dictionary',width=580,height=240,font='Bold 15',bg='white')
            lb.place(x=10,y=10)
            print(cumle[counter])
            etiket = Label(lb,text = ''+str(kelime[counter2]),font='Bold 15',bg='white') 
            etiket.place(x=10,y=20)
            etiket2 = Label(lb,text = ''+str(kelimeAnlami[counter2]),font='Bold 15',bg='white') 
            etiket2.place(x=10,y=60)
            etiket3 = Label(lb,text = ''+str(cumle[counter2]),font='Bold 15',bg='white')
            etiket3.place(x=10,y=100)
            buton4= Button(fwhite,text ='All Save',fg='black',bg='#C7D11D',command= kaydet)
            buton4.place(x=250,y=200,width=100,heigh=30)
         
    def bilgi3():
        global kelimeAnlami
        global etiket2
        global counter
        global buton2
        global girdi2
        global girdi3
        global buton3
        global lb
        
        kelimeAnlami.append( girdi2.get() )
        if len(girdi2.get()) == 0:
            etiket2.config(text=' '*93)
            etiket2.config(text='No information entered')
            kelimeAnlami.pop()
        else:
            lb.destroy()
            expression = ""
            equation.set("")
            lb = LabelFrame(fwhite,text = 'Dictionary',width=580,height=240,font='Bold 15',bg='white')
            lb.place(x=10,y=10)
            etiket2 = Label(lb,text = 'Sample sentences ',font='Bold 15',bg='white') 
            etiket2.place(x=10,y=60)
            print(kelimeAnlami[counter])
            girdi3 = Entry(lb, textvariable=equation,bg='#A8E3F9')
            girdi3.place(x=100,y=100,width=200,height=30)
            buton3= Button(lb,text ='Save',fg='black',bg='#C7D11D',command= ekran)
            buton3.place(x=150,y=150,width=100,heigh=30)
            
        
    def bilgi2():
        global kelime
        global girdi
        global etiket2
        global buton
        global counter
        global buton2
        global girdi2
        global lb
        
        kelime.append( girdi.get())
        print(counter)
        if len(girdi.get()) == 0:
            etiket2.config(text=' '*93)
            etiket2.config(text='No information entered')
            kelime.pop()
        else:
            lb.destroy()
            expression = ""
            equation.set("")
            lb = LabelFrame(fwhite,text = 'Dictionary',width=580,height=240,font='Bold 15',bg='white')
            lb.place(x=10,y=10)
            etiket2 = Label(lb,text = 'Meaning of the word ',font='Bold 15',bg='white') 
            etiket2.place(x=10,y=60)
            print(kelime[counter])
            girdi2 = Entry(lb, textvariable=equation,bg='#A8E3F9')
            girdi2.place(x=100,y=100,width=200,height=30)
            buton2= Button(lb,text ='Save',fg='black',bg='#C7D11D',command= bilgi3)
            buton2.place(x=150,y=150,width=100,heigh=30)
            
    def bilgi():
        global kelime
        global kelimeAnlami
        global cumle
        global girdi
        global etiket
        global etiket2
        global buton
        global counter
        global lb
        counter = len(kelime)
        lb.destroy()
        expression = ""
        equation.set("")
        lb = LabelFrame(fwhite,text = 'Dictionary',width=580,height=240,font='Bold 15',bg='white')
        lb.place(x=10,y=10)
        etiket = Label(lb,text = 'Information entry',font='Bold 15',bg='white') 
        etiket.place(x=10,y=20)
        etiket2 = Label(lb,text = 'Word to save ',font='Bold 15',bg='white') 
        etiket2.place(x=10,y=60)
        girdi = Entry(lb, textvariable=equation,bg='#A8E3F9')
        girdi.place(x=100,y=100,width=200,height=30)
        buton= Button(lb,text ='Save',fg='black',bg='#C7D11D',command= bilgi2)
        buton.place(x=150,y=150,width=100,heigh=30)

    def bul2():
        global kelime
        global kelimeAnlami
        global cumle
        global counter2
        global girdix
        global lb
        global etiket
        oku()
        k = girdix.get()
        if len(girdix.get()) == 0:
            etiket.config(text=' '*93)
            etiket.config(text='No information entered')
        else:
            for x in range (counter2):
                if(k == kelime[x]):
                    counterBul = int(x)
                    lb.destroy()
                    expression = ""
                    equation.set("")
                    lb = LabelFrame(fwhite,text = 'Dictionary',width=580,height=240,font='Bold 15',bg='white')
                    lb.place(x=10,y=10)
                    
                    etiket = Label(lb,text = ' '*93,font='Bold 15',bg='white') 
                    etiket.place(x=10,y=50)
                    etiket2 = Label(lb,text = ' '*93,font='Bold 15',bg='white') 
                    etiket2.place(x=10,y=100)
                    etiket3 = Label(lb,text = ' '*93,font='Bold 15',bg='white') 
                    etiket3.place(x=10,y=150)
                    etiket = Label(lb,text = ''+str(kelime[counterBul]),font='Bold 15',bg='white') 
                    etiket.place(x=10,y=50)
                    etiket2 = Label(lb,text = ''+str(kelimeAnlami[counterBul]),font='Bold 15',bg='white') 
                    etiket2.place(x=10,y=100)
                    etiket3 = Label(lb,text = ''+str(cumle[counterBul]),font='Bold 15',bg='white')
                    etiket3.place(x=10,y=150)
                    break
                else :
                    etiket.config(text=' '*93)
                    etiket.config(text='Not Found') 
    def bul():
        global kelime
        global kelimeAnlami
        global cumle
        global girdix
        global etiket
        global lb
        lb.destroy()
        lb = LabelFrame(fwhite,text = 'Dictionary',width=580,height=240,font='Bold 15',bg='white')
        lb.place(x=10,y=10)
        etiket = Label(lb,text = 'Search',font='Bold 15',bg='white') 
        etiket.place(x=100,y=50)
        girdix = Entry(lb, textvariable=equation,bg='#A8E3F9')
        girdix.place(x=100,y=100,width=200,height=30)
        butonara= Button(lb,text ='Find',fg='black',bg='#C7D11D',command = bul2)
        butonara.place(x=150,y=150,width=100,heigh=30)

    def sil2():
        global kelime
        global kelimeAnlami
        global cumle
        global counter2
        global girdix
        global lb
        global etiket
        oku()
        boyut = len(kelime)
        print("boyut (silmede kaydetme öncesi) : ",boyut)
        k = girdix.get()
        if len(girdix.get()) == 0:
            etiket.config(text=' '*93)
            etiket.config(text='No information entered')
        else:
            for x in range (boyut):  #boyut-1 i silinen indise counterBul a aktar boyut-1 i sil
                if(k == kelime[x]):
                    counterBul = int(x)
                    lb.destroy()
                    expression = ""
                    equation.set("")
                    lb = LabelFrame(fwhite,text = 'Dictionary',width=580,height=240,font='Bold 15',bg='white')
                    lb.place(x=10,y=10)
                    os.remove("Word.txt")
                    os.remove("Sentences.txt")
                    os.remove("Word-opposite.txt")
                    sleep(0.1)
                    
                    kelime[counterBul] = ""
                    kelimeAnlami[counterBul] = ""
                    cumle[counterBul] = ""
                    kelime[counterBul] = kelime[boyut-int(1)]
                    kelimeAnlami[counterBul] = kelimeAnlami[boyut-int(1)]
                    cumle[counterBul] = cumle[boyut-int(1)]
                    kelime.pop()
                    kelimeAnlami.pop()
                    cumle.pop()
                     
                    tut = len(kelime)
                    for x in range (tut):
                        tut2 = ""
                        this=open("Word.txt","a")
                        tut2 = kelime[x]
                        this.write(tut2)
                        this.write("\n")
                        this.close()
                        tut2=""
                        tut2 = kelimeAnlami[x]
                        this=open("Word-opposite.txt","a")
                        this.write(tut2)
                        this.write("\n")
                        this.close()
                        tut2=""
                        tut2 = cumle[x]
                        this=open("Sentences.txt","a")
                        this.write(tut2)
                        this.write("\n")
                        this.close()
                    sleep(0.1)
                    print("tut (silmede kaydetme sonrasi) : ",tut)
                    
                    etiket = Label(lb,text = ' '*93,font='Bold 15',bg='white') 
                    etiket.place(x=10,y=50)
                    etiket2 = Label(lb,text = ' '*93,font='Bold 15',bg='white') 
                    etiket2.place(x=10,y=100)
                    etiket3 = Label(lb,text = ' '*93,font='Bold 15',bg='white') 
                    etiket3.place(x=10,y=150)
                    etiket = Label(lb,text = 'kelime : '+str(kelime[counterBul]),font='Bold 15',bg='white') 
                    etiket.place(x=10,y=50)
                    etiket2 = Label(lb,text = 'kelime : '+str(kelimeAnlami[counterBul]),font='Bold 15',bg='white') 
                    etiket2.place(x=10,y=100)
                    etiket3 = Label(lb,text = 'kelime : '+str(cumle[counterBul]),font='Bold 15',bg='white')
                    etiket3.place(x=10,y=150)
                    break
                else :
                    etiket.config(text=' '*93)
                    etiket.config(text='Not Found')
  
    def sil():
        print("sistem çalıştı.")
        global kelime
        global kelimeAnlami
        global cumle
        global girdix
        global etiket
        global lb
        lb.destroy()
        lb = LabelFrame(fwhite,text = 'Dictionary',width=580,height=240,font='Bold 15',bg='white')
        lb.place(x=10,y=10)
        etiket = Label(lb,text = 'Remove',font='Bold 15',bg='white') 
        etiket.place(x=100,y=50)
        girdix = Entry(lb, textvariable=equation,bg='#A8E3F9')
        girdix.place(x=100,y=100,width=200,height=30)
        butonara= Button(lb,text ='Delete',fg='black',bg='#C7D11D',command = sil2)
        butonara.place(x=150,y=150,width=100,heigh=30)
        
    def ayar():
        butonbul= Button(lb2,text ='Search',fg='black',bg='#B01641',font='Bold 15',command = bul)
        butonbul.place(x=40,y=100,width=100,heigh=30)
        butonekle= Button(lb2,text ='Add',fg='black',bg='#B01641',font='Bold 15',command = bilgi)
        butonekle.place(x=40,y=150,width=100,heigh=30)
        butonsil= Button(lb2,text ='Delete',fg='black',bg='#B01641',font='Bold 15',command = sil)
        butonsil.place(x=40,y=200,width=100,heigh=30)


    
    fwhite = Frame(form,bg="white",width=600,height=480)
    fwhite.place(x=0,y=0)
    fblue = Frame(form,bg="#A8E3F9",width=200,height=480) #A8E3F9
    fblue.place(x=600,y=0)
    lb = LabelFrame(fwhite,text = 'Dictionary',width=580,height=240,font='Bold 15',bg='white')
    lb.place(x=10,y=10)
    lb2 = LabelFrame(fblue,text = 'Settings',width=180,height=460,font='Bold 15',bg='#A8E3F9')
    lb2.place(x=10,y=10)
    lb3 = LabelFrame(fwhite,text = 'Control Display',width=580,height=180,font='Bold 15',bg='white')
    lb3.place(x=10,y=270)
    oku()
    etiketkontrol = Label(lb3,text = 'Total kayıtlı kelime sayısı : '+str(counter2),font='Bold 15',bg='white') 
    etiketkontrol.place(x=10,y=30)
    ayar()
    bul()

    form.mainloop()

if __name__ == "__main__":
      main()

    
