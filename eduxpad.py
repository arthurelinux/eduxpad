#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 17:07:57 2018

@author: arthur
"""

from tkinter import *


from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename

import random

class calc():
    def __init__(self):
        self.pyno = Tk()
        self.pyno.title("Eduxpad")
        self.pyno ["bg"] = "white"

        self.pyno.geometry("350x350")
        self.l1 = Label(self.pyno, text="", font="arial 14", bg="white")
        self.l1.pack()
        self.l = Label(self.pyno, text="Bem vido ao Eduxpad", font="arial 14", bg="white")
        self.l.pack()
        self.l2 = Label(self.pyno, text="clique Ok para entrar", font="arial 8", bg="white")
        self.l2.pack()
        self.b = Button(self.pyno, text="OK", command=self.sair)
        self.b.pack()
        
        self.l2 = Label(self.pyno, text="""
        Esse software foi desenvolvido por Arthur Carlos da Silva,
        mais informações acesse educadoresnolinux.blogspot.com
        ou www.educadoresnolinux.top""", font="arial 8", bg="white")
        self.l2.pack()
        
        self.photo = PhotoImage(file="LOGO SITE 300X100.png")
        self.image1 = Label(self.pyno, image = self.photo, bg="white")
        self.image1.pack()

        self.menubar1 = Menu(self.pyno)
            # Aqui criamos os menus:
        self.MENUarquivo1 = Menu(self.menubar1)
        
        
        self.MENUarquivo1.add_command(label="Editar arquivo", command=self.sair)
        self.MENUarquivo1.add_command(label="Calcular", command=self.calcular1)
        self.MENUarquivo1.add_command(label="sobre", command=self.importantea)
        
        self.menubar1.add_cascade(label="Arquivo", menu=self.MENUarquivo1)
        self.pyno.config(menu=self.menubar1)


        self.pyno.mainloop()

    def sair(self):
        
        self.root = Tk()
        self.root.geometry('630x580')
        self.root.title("anotações")
        self.root['bg'] = 'DarkSlateGray'



        self.frame1 = Frame(self.root)
        self.frame1['bg'] = 'DarkSlateGray'
        self.frame = Frame(self.root)
        self.frame['bg'] = 'DarkSlateGray'
        self.frame2 = Frame(self.root)
        self.frame1.pack(expand=YES, fill=BOTH)
        self.frame.pack(expand=YES, fill=BOTH)
        self.frame2.pack(expand=YES, fill=BOTH)



        self.bt1 = Label(self.frame, text="registrar", bg='MidnightBlue', fg="white")
        self.bt1.grid(column=0, row=0)
        self.bt1 = Label(self.frame, text="Visualizar", bg='MidnightBlue', fg="white")
        self.bt1.grid(column=0, row=1)

        self.bt1 = Button(self.frame, text=" ajuda ", bg='MidnightBlue', fg="white", command=self.importantea)
        self.bt1.grid(column=4, row=0)
        self.bt1 = Button(self.frame, text="limpar", bg='MidnightBlue', fg="white", command=self.limpa)
        self.bt1.grid(column=4, row=1)

        self.bt1 = Button(self.frame, text="importante",bg='Brown',fg="white", command=self.importante)
        self.bt1.grid(column=1, row=0)
        self.bt2 = Button(self.frame, text="intermediario", bg='MediumSlateBlue',fg="white", command=self.intermediario)
        self.bt2.grid(column=2, row=0)
        self.bt3 = Button(self.frame, text="Pouco importante", bg='DarkCyan',fg="white", command=self.pouco)
        self.bt3.grid(column=3, row=0)

        self.bt4 = Button(self.frame, text="importante", bg='MidnightBlue',fg="white", command=self.Vimportante)
        self.bt4.grid(column=1, row=1)
        self.bt5 = Button(self.frame, text="intermediario", bg='MidnightBlue',fg="white", command=self.Vintermediario)
        self.bt5.grid(column=2, row=1)
        self.bt6 = Button(self.frame, text="Pouco importante", bg='MidnightBlue',fg="white", command=self.Vpouco)
        self.bt6.grid(column=3, row=1)
        self.bt8 = Button(self.frame, text="Cor", bg='MidnightBlue', fg="white", command=self.cores)
        self.bt8.grid(column=0, row=3)
        
        self.bt81 = Button(self.frame, text="zerar", bg='MidnightBlue', fg="white", command=self.cores1)
        self.bt81.grid(column=1, row=3)


        self.low = Scrollbar(self.frame2)
        self.low.pack(side=RIGHT, fill=Y)


        self.e = Text(self.frame2,font="arial 12",bd=3, pady=20, padx=20)
        self.e.pack(expand=YES, fill=BOTH)
        self.e.config(yscrollcommand=self.low.set)
        self.low.config(command=self.e.yview)

        self.menubar = Menu(self.root)
        self.menubar["bg"] = "DarkBlue"
        self.menubar["fg"] = "white"
            # Aqui criamos os menus:
        self.MENUarquivo = Menu(self.menubar)
        self.MENUarquivo["bg"] = "purple"
        self.MENUarquivo["fg"] = "white"
        self.MENUarquivo.add_command(label="Salvar", command=self.salvara)
        self.MENUarquivo.add_command(label="Abrir", command=self.abrira)
        self.menubar.add_cascade(label="Arquivo", menu=self.MENUarquivo)

        self.MENUajuda = Menu(self.menubar)
        self.MENUajuda["bg"] = "purple"
        self.MENUajuda["fg"] = "white"
        self.MENUajuda.add_command(label="Sobre", command=self.importantea)
        self.MENUajuda.add_command(label="Fonte", command=self.lista_font)
        self.menubar.add_cascade(label="Ajuda", menu=self.MENUajuda)
        
        self.root.config(menu=self.menubar)

        #Text's de vilualização
    def lista_font(self):
        self.tt = Tk()
        self.tt.title ("fontes")
 
        
        self.Lb1 = Listbox(self.tt)
        self.Lb1.insert(1, "Arial", "Verdana")
        self.Lb1.insert(2, "Helvetica")
        self.et = Entry(self.tt)
        self.et.pack()
        self.bet = Button(self.tt, text="aplicar", command=self.Fonte)
        self.bet.pack()
        self.let = Label (self.tt, text="fontes suportadas")
        self.let.pack()
        self.Lb1.pack()
        self.bet1 = Button(self.tt, text="amarela", command=self.fonte2)
        self.bet1.pack()
        self.bet2 = Button(self.tt, text="Preta", command=self.fonte3)
        self.bet2.pack()
        self.bet2 = Button(self.tt, text="Azul", command=self.fonte4)
        self.bet2.pack()
        self.tt.mainloop()
        
    def Fonte(self):
        self.fotez = self.et.get()
        self.e ["font"] = self.fotez
        
    def fonte2(self):
        self.e ["fg"] = "yellow"
    def fonte3(self):
        self.e ["fg"] = "black"
    def fonte4(self):
        self.e ["fg"] = "DarkBlue"

    def salvara(self):  # Aqui é a função que salva o arquivo:
        fileName = asksaveasfilename()
        try:
            file = open(fileName, 'w')
            textoutput = self.e.get(0.0, END)
            file.write(textoutput)
        except:
            pass
        finally:
            file.close()

    def abrira(self):  # Aqui é a função que abre um arquivo
        fileName = askopenfilename()
        try:
            file = open(fileName, 'r')
            contents = file.read()

            self.e.delete(0.0, END)
            self.e.insert(0.0, contents)
        except:
            pass

    def cores1(self):
        self.e.delete(0.0, END)
    

     #função para mudar de cor   
    def cores(self):
        cor = ["CadetBlue","DarkSlateGray", "Aquamarine", "LightSteelBlue", "Silver", "White", "Violet"]
        sorteia = random.choice
        sorte = sorteia(cor)

        self.e ["bg"] = sorte
        
    def limpa(self):

        self.jj = Tk()
        self.btt1 = Button(self.jj, text="importante", command=self.limpa_1)
        self.btt1.pack()
        self.btt1 = Button(self.jj, text="intermediario", command=self.limpa_2())
        self.btt1.pack()
        self.btt1 = Button(self.jj, text="menos importante", command=self.limpa_3())
        self.btt1.pack()

        self.jj.mainloop()

    #apagar os arquivos de importancia
    def limpa_1(self):
        self.abrir = open("novo.txt", "w")
        self.abrir.write("")
    def limpa_2(self):
        self.abrir1 = open("inter.txt", "w")
        self.abrir1.write("")

    def limpa_3(self):
        self.abrir2 = open("pouco.txt", "w")
        self.abrir2.write("")

    #função sobre o app
    def importantea(self):
        self.jei = Tk()
        self.jei.title("informações")
        self.jei.geometry("450x450")
        self.vari = ("""Eduxpad
        Suas anotações são classificadas segundo o gráu de importancia para você. Então para salvar corretamente,
é necessária clicar na classificação unicamente quando terminar a anotação. Após isso, limpe o que está na tela e poderá anotar 
novamente para outra classificação. Para conferir se foi mesmo salvo recomendamos reiniciar o programa e clicar na parte visualizar
correspondente a sua classificação. 
          
          Essse aplicativo é desenvolvido em Python pelo Blog https://www.educadoresnolinux.top acesse a pagina e ajude a iniciativa.
Você pode fazer uma doação em qualquer valor a partir de 1 real. Ajude-nos. 
Se tiver ainda mais duvidas acesse a pagina e entre em contato. 
          """)

        self.Entrar = Text(self.jei, bd=3, pady=20, padx=20)
        self.Entrar.pack(expand=YES, fill=BOTH)
        self.Entrar.insert(0.0, self.vari)

        self.jei.mainloop()


#salvar o que fora escrito por gráu de importancia.
    def importante(self):

        self.abrir = open("novo.txt", "a")
        self.abrir.write("{}".format(self.e.get(0.0, END)))

    def intermediario(self):
        self.abra = open("inter.txt", "a")
        self.abra.write("{}".format(self.e.get(0.0, END)))
    def pouco(self):
        self.abriu = open("pouco.txt", "a")
        self.abriu.write("{}".format(self.e.get(0.0, END)))

#visualizar o que está dentro dos arquivos de importancia
    def Vimportante(self):
        self.jj3=Tk()
        self.jj3.title("Importante")



        self.low1 = Scrollbar(self.jj3)
        self.low1.pack(side=RIGHT, fill=Y)
        self.e1 = Text(self.jj3, bg="#022047", fg="white", bd=3, pady=20, padx=20)
        self.e1.pack(expand=YES, fill=BOTH)
        self.e1.config(yscrollcommand=self.low1.set)
        self.low1.config(command=self.e1.yview)

        self.abrir1 = open("novo.txt", "r")
        self.x = self.abrir1.read()
        self.e1.insert(0.0, self.x)
        self.jj3.mainloop()



    def Vintermediario(self):
        self.jj2 =Tk()
        self.jj2.title("intermediario")
        self.low2 = Scrollbar(self.jj2)
        self.low2.pack(side=RIGHT, fill=Y)
        self.e2 = Text(self.jj2, bg="#022047", fg="white", bd=3, pady=20, padx=20)
        self.e2.pack(expand=YES, fill=BOTH)
        self.e2.config(yscrollcommand=self.low2.set)
        self.low2.config(command=self.e2.yview)

        self.abra1 = open("inter.txt", "r")
        self.z = self.abra1.read()
        self.e2.insert(0.0, self.z)

        self.jj2.mainloop()



    def Vpouco(self):
        self.jj1 = Tk()
        self.jj1.title("menos importante")
        self.low3 = Scrollbar(self.jj1)
        self.low3.pack(side=RIGHT, fill=Y)
        self.e3 = Text(self.jj1, bg="#022047", fg="white", bd=3, pady=20, padx=20)
        self.e3.pack(expand=YES, fill=BOTH)
        self.e3.config(yscrollcommand=self.low3.set)
        self.low3.config(command=self.e3.yview)


        self.abriu1 = open("pouco.txt", "r")
        self.y = self.abriu1.read()
        self.e3.insert(0.0,self.y)
        self.jj1.mainloop()
    
    #janela do calculo das quadro operações.
    def calcular1(self):
        self.ca = Tk()
        self.ca.geometry("350x350")
        self.ca.title("Quatro operações")
        self.ff = Frame(self.ca)
        self.ff.pack(side=TOP, fill=X)
        self.ff1= Frame(self.ca)
        self.ff1.pack(side=LEFT)
        self.ff2= Frame(self.ca)
        self.ff2.pack(side=RIGHT)

        self.lan = Label(self.ff, text="calcule as quatro operações", fg="white", bg="DarkBlue")
        self.lan.pack(fill=X)


        self.res= Label(self.ff1, text="0", bg="darkblue", fg="white")
        self.res.grid(row=0,column=0)
        self.ent= Entry(self.ff1)
        self.ent.grid(row=1, column=0)
        self.ll= Label(self.ff1, text="+")
        self.ll.grid(row=2,column=0)
        self.ent1= Entry(self.ff1)
        self.ent1.grid(row=3, column=0)
        self.bot = Button(self.ff1, text="=", command=self.soma)
        self.bot.grid(row=4, column=0)

        self.res11= Label(self.ff1, text="0", bg="darkblue", fg="white")
        self.res11.grid(row=5,column=0)
        self.ent11= Entry(self.ff1)
        self.ent11.grid(row=6, column=0)
        self.ll11= Label(self.ff1, text="-")
        self.ll11.grid(row=7,column=0)
        self.ent12= Entry(self.ff1)
        self.ent12.grid(row=8, column=0)
        self.bot11 = Button(self.ff1, text="=", command=self.sub)
        self.bot11.grid(row=9, column=0)

        #FRAME 2
        self.res3= Label(self.ff2, text="0", bg="darkblue", fg="white")
        self.res3.grid(row=0,column=0)
        self.ent3= Entry(self.ff2)
        self.ent3.grid(row=1, column=0)
        self.ll3= Label(self.ff2, text="x")
        self.ll3.grid(row=2,column=0)
        self.ent13= Entry(self.ff2)
        self.ent13.grid(row=3, column=0)
        self.bot3 = Button(self.ff2, text="=", command=self.mult)
        self.bot3.grid(row=4, column=0)

        self.res113= Label(self.ff2, text="0", bg="darkblue", fg="white")
        self.res113.grid(row=5,column=0)
        self.ent113= Entry(self.ff2)
        self.ent113.grid(row=6, column=0)
        self.ll113= Label(self.ff2, text="/")
        self.ll113.grid(row=7,column=0)
        self.ent123= Entry(self.ff2)
        self.ent123.grid(row=8, column=0)
        self.bot113 = Button(self.ff2, text="=", command=self.divis)
        self.bot113.grid(row=9, column=0)



        self.ca.mainloop()

    def soma(self):
        try:
            self.v1 = float(self.ent.get())
            self.v2 = float(self.ent1.get())
            self.z = float(self.v1+self.v2)
            self.res ["text"]= self.z
            self.ent.delete(0,END)
            self.ent1.delete(0,END)
        except ValueError:
            self.res ["text"]= "invalido"

        
    def sub(self):
        try:
            self.v11 = float(self.ent11.get())
            self.v22 = float(self.ent12.get())
            self.z2 = float(self.v11-self.v22)
            self.res11 ["text"]= self.z2
            self.ent11.delete(0,END)
            self.ent12.delete(0,END)
        except ValueError:
            self.res11 ["text"]= "invalido"

    def mult(self):
        try:
            self.v13 = float(self.ent3.get())
            self.v23 = float(self.ent13.get())
            self.z3 = float(self.v13*self.v23)
            self.res3 ["text"]= self.z3
            self.ent3.delete(0,END)
            self.ent13.delete(0,END)
        except ValueError:
            self.res3 ["text"]= "invalido"

    def divis(self):
        try:
            self.v113 = float(self.ent113.get())
            self.v123 = float(self.ent123.get())
            self.z31 = float(self.v113/self.v123)
            self.res113 ["text"]= self.z31
            self.ent113.delete(0,END)
            self.ent123.delete(0,END)
        except ValueError:
            self.res113 ["text"]= "invalido"




calc()

