# -*- coding: utf-8 -*-


import tkinter
import tkinter as tk
import tkinter.messagebox
from tkinter import *
import pandas as pd
from tkinter import ttk
import numpy as np
from tkinter import filedialog


class Ml:
    def window1(self):
        window1 = Tk()
        window1.title("REACT WEB APP")
        window1.geometry("700x500+100+10")

        def file_open():
            global loc, df
            loc = filedialog.askopenfile(initialdir="/", filetypes=(("CSV File", "*.csv"), ("ALL Files")))
            df = pd.read_csv(loc)
            print(loc)
            entry7.insert(0, loc)

        label = Label(window1, text="USER PAGE")
        label.pack(pady=20)
        
        label1 = Label(window1, text="Username")
        label1.place(x=80, y=50)
        
        label2 = Label(window1, text="Email")
        label2.place(x=80, y=100)
        
        label3 = Label(window1, text="Gender")
        label3.place(x=230, y=50)
        
        label4 = Label(window1, text="Country")
        label4.place(x=230, y=100)
        
        label5 = Label(window1, text="Age")
        label5.place(x=400, y=50)
        
        label6 = Label(window1, text="City")
        label6.place(x=400, y=100)
        
        entry1 = Entry(window1)
        entry1.place(x=80,y=70)
        
        entry2 = Entry(window1)
        entry2.place(x=80,y=120)
        
        entry3 = Entry(window1)
        entry3.place(x=230, y=70)
                
        entry4 = Entry(window1)
        entry4.place(x=230, y=120)
        
        entry5 = Entry(window1)
        entry5.place(x=400, y=70)
         
        entry6 = Entry(window1)
        entry6.place(x=400, y=120)
        
        button0 = Button(window1, text="UPDATE USER DATA")
        button0.place(x=80, y=150)
        
        
        label7 = Label(window1, text="Input Data")
        label7.place(x=80, y=180)
        
        entry7 = Entry(window1)
        entry7.place(x=80, y=200)

        
        button = Button(window1, text='UPLOAD FILE', command=file_open)
        button.place(x=250, y=200)
        
        button1 = Button(window1, text='UPLOAD', command=f.window2)
        button1.place(x=300, y=350)
        
        window1.mainloop()

    def window2(self):
        global tv1
        window2 = Tk()
        window2.title("React Web App")
        window2.geometry("700x500+100+10")

        frame = Frame(window2)
        frame.pack()
        tv1 = ttk.Treeview(frame)

        tv1["columns"] = list(df.columns)
        print(tv1["columns"])
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            tv1.heading(column, text=column)

        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            tv1.insert("", "end", values=row)
        tv1.pack()
        
    
    
        button3 = Button(window2, text='Logout', command=f.window1)
        button3.place(x=350, y=300)
        window2.mainloop()


   


f = Ml()

f.window1()
