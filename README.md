import pyttsx3
import time
import sqlite3
from tkinter import *
import random
tts=pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice','ru')
for voice in voices:
    if voice.name == 'Anna':
        tts.setProperty('voice',voice.id)
l1=time.ctime(time.time())        
def say(*c):
    engine = pyttsx3.init()
    engine.say(c)
    engine.runAndWait()
def insert_info(sas):
    cursor.execute('SELECT ID FROM history')
    p3=cursor.fetchall()[-1][0]
    p3+=1
    while True:
        cursor.execute(''' INSERT INTO history(ID,data,action)
VALUES(?,?,?)''',(p3,l1,sas))
        db.commit()
        break
class dengi:
    def __init__(self,balance,currency):
        self.balance=balance
        self.currency=currency
    def top_up_balance(self,num):
        self.balance=num+self.balance
        print('Вы внесли сумму:',num,self.currency)
    def top_down_balance(self,num):
        if self.balance<0:
            raise ValueError('Ты беден')
        self.balance=self.balance-num
        print('Вы сняли сумму:',num,self.currency)
    def info(self):
        z=(str('Ваш баланс: '+str(self.balance)+str(self.currency)))
        return z
class User(dengi):
    def __repr__(self):
        gg=str(input('Введите название кошелька: '))
        return f'{gg}'  
    def exchange(self,gh):
        x={'EUR':{'USD':1.13,
                  'RUB':83.1},
           'USD':{'EUR':0.88,
                  'RUB':73.2},
           'RUB':{'USD':0.014,
                  'EUR':0.012}}
        gg=round(self.balance*x[self.currency][gh],2)
        dengi.__init__(self,balance=gg,currency=gh)
        print('вы успешно сменили волюту на',self.currency,self.balance)
class About(Toplevel,User):
    def __init__(self, parent):
        super().__init__(parent)
        self.button = Button(self, text="Закрыть", command=self.destroy)
        self.button['bg']='#991199'
        self.button['fg']='#ff9218'
        self.button.pack(pady=20, ipadx=2, ipady=2)
class About1(Toplevel,User):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(background='#8b00ff')
        self.label = Label(self, text="Введите сумму которую хотите положить")
        self.entry2=Entry(self,text=0)
        self.label.pack(padx=20, pady=20)
        self.entry2.pack(padx=30,pady=30)
        self.button2=Button(self,  text='Положить', command=self.f1_1)
        self.button2.pack(pady=20,padx=20)
        self.label['bg']='#8b00ff'
        self.label['fg']='#ff9218'
        self.entry2['bg']='#8b00ff'
        self.entry2['fg']='#ff9218' 
        self.button2['bg']='#991199'
        self.button2['fg']='#ff9218'
    def f1_1(self):
        mun=self.entry2.get()
        mun=float(mun)
        dengi.top_up_balance(c,mun)
        sql_update='''Update users set Balance = ? where id= ? '''
        date=(c.balance,1)
        cursor.execute(sql_update,date)
        db.commit()
        self.entry2.delete(0,END)
class About2(Toplevel,User):
     def __init__(self, parent):
        super().__init__(parent)
        self.configure(background='#8b00ff')
        self.label = Label(self, text="Введите сумму которую хотите снять")
        self.entry2=Entry(self,text=0)
        self.label.pack(padx=20, pady=20)
        self.entry2.pack(padx=30,pady=30)
        self.button2=Button(self,  text='Снять', command=self.f1_2)
        self.button2.pack(pady=20,padx=20)
        self.label['bg']='#8b00ff'
        self.label['fg']='#ff9218'
        self.entry2['bg']='#8b00ff'
        self.entry2['fg']='#ff9218'
        self.button2['bg']='#991199'
        self.button2['fg']='#ff9218'
     def f1_2(self):
        mun=self.entry2.get()
        mun=float(mun)
        dengi.top_down_balance(c,mun)
        sql_update='''Update users set Balance = ? where id= ? '''
        date=(c.balance,1)
        cursor.execute(sql_update,date)
        db.commit()
        self.entry2.delete(0,END)
class About3(Toplevel,User):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(background='#8b00ff')
        self.label = Label(self, text="Выбирите валюту из ниже представленных")
        self.button4=Button(self,text='Смена Волюты',command=self.f1_4)
        self.selectName=StringVar(self)
        self.selectName.set('currecy')
        self.nameslist=OptionMenu(self,self.selectName,'USD','EUR','RUB')
        self.nameslist['menu'].config(bg='#8b00ff')
        self.nameslist['menu'].config(fg='#ff9218')
        self.nameslist['fg']='#ff9218'
        self.nameslist['bg']='#8b00ff'
        self.button4['bg']='#991199'
        self.button4['fg']='#ff9218'
        self.label['bg']='#8b00ff'
        self.label['fg']='#ff9218'
        self.nameslist.pack(pady=20,padx=20)
        self.button4.pack(pady=20,padx=20)
    def f1_4(self):
        gj=self.selectName.get()
        sql_update='''Update users set Currency = ? where id= ? '''
        date=(gj,1)
        cursor.execute(sql_update,date)
        db.commit()
        User.exchange(c,gj)
        sql_update1='''Update users set Balance = ? where id= ? '''
        date1=(c.balance,1)
        cursor.execute(sql_update1,date1)
        db.commit()
class App(Tk): 
    def __init__(self):
        super().__init__()
        self.title('Bank')
        self.configure(background='#8b00ff')
        self.lbl=Label(text='Привет')
        self.lbl.pack(padx=4,pady=4)
        self.button4=Button(self,text='обновить баланс',command=self.f1_3)
        self.output=Message(self,text=0)
        self.button5=Button(self,text='Снять',command=self.open_window2)
        self.button6=Button(self,text='Смена валюты',command=self.open_window3)
        self.f1_3()

        self.output['bg']='#8b00ff'
        self.output['fg']='#ff9218'
        self.button4['bg']='#991199'
        self.button4['fg']='#ff9218'
        self.button6['bg']='#991199'
        self.button6['fg']='#ff9218'
        self.lbl['bg']='#8b00ff'
        self.lbl['fg']='#ff9218'
        self.button5['bg']='#991199'
        self.button5['fg']='#ff9218'
        self.lbl1=Label(text='Введите операцию которую хотите совершить:')
        self.lbl1.pack(padx=10,pady=10)
        self.output.pack(padx=10,pady=10)
        self.lbl1['bg']='#8b00ff'
        self.lbl1['fg']='#ff9218'
        self.button4.pack(pady=20,padx=20)
        self.list=Listbox()
        self.list.pack(pady=20,padx=20,ipadx=50)
        self.list['bg']='#8b00ff'
        self.list['fg']='#ff9218'
        self.but=Button(text='Положить',command=self.open_window1)
        self.but['bg']='#991199'
        self.but['fg']='#ff9218'
        self.but.pack(padx=40,pady=20)
        self.button5.pack(padx=10,pady=10)
        self.but1=Button(text='Очистить',command=self.f2)
        self.but1['bg']='#991199'
        self.but1['fg']='#ff9218'
        self.but1.pack(padx=20,pady=20)
        self.button6.pack(pady=10,padx=10)
        self.lbl=Label(self,text='lol')
    def f1_3(self):
        self.output['text']=dengi.info(c)
        say(self.output['text'])
    def open_window3(self):
        global l1
        ll1=str('Смена валюты ')
        l21=ll1+l1
        insert_info(ll1)
        self.list.insert(END,l21)
        about3=About3(self)
        about3.grab_set()
    def open_window2(self):
        g1=str('Снятие ')
        g21=g1+l1
        insert_info(g1)
        self.list.insert(END,g21)
        about2=About2(self)
        about2.grab_set()
    def open_window1(self):
        h1=str('Пополнение ')
        h21=h1+l1
        insert_info(h1)
        self.list.insert(END,h21)
        about1=About1(self)
        about1.grab_set()
    def open_window(self):
        about = About(self)
        about.grab_set()
    def f2(self):
        self.list.delete(0,END)
with sqlite3.connect('wallet.db') as db:
    cursor=db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
ID integer PRIMARY KEY,
Name text NOT NULL,
Balance real NOT NULL,
Currency text );''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS history(
ID integer PRIMAR KEY,
data text NOT NULL,
action text NOT NULL);''')
    info1 = cursor.execute('SELECT * FROM history WHERE ID=1')
    if info1.fetchone() is None:
        cursor.execute('''INSERT INTO history(ID,data,action)
VALUES(?,?,?)''',('1','None', 'None'))
        #Делаем когда нету человека в бд
    else:
        pass
        #Делаем когда есть человек в бд
    info = cursor.execute('SELECT * FROM users WHERE ID=1')
    if info.fetchone() is None:
        cursor.execute('''INSERT INTO users(ID,Name,Balance,Currency)
VALUES(?,?,?,?)''',('1','User','0','RUB'))
        c=User(0,'RUB')
        say('Привет')               
        app=App()
        app.mainloop()  
        #Делаем когда нету человека в бд
    else:
        #Делаем когда есть человек в бд
        cursor.execute('SELECT Balance FROM users')
        p=cursor.fetchall()[0][0]
        cursor.execute('SELECT Currency FROM users')
        p1=cursor.fetchall()[0][0]
        c=User(p,p1)
        say('Привет')               
        app=App()
        app.mainloop()  


