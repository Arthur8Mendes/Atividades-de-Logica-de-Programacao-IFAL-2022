# * importa tudo do tkinter
from tkinter import *
from tkinter.ttk import Combobox

def clicked():
    lbl.configure(text="Button was clicked !!")

    
window = Tk() #cria janela window é o nome da variável
window.title("Welcome Nerds") # título
window.geometry('650x400') # tamanho da janela larg x alt
lbl = Label(window, text="",fg='black',font=("Helvetica", 12)) #coloca um texto na tela
lbl.pack( side = TOP ) #coloca no meio da tela - pode usar o place, mas deve posicionar 2 coordenadas
lbl = Label(window, text="Tela de Cadastro de Informações",fg='black',font=("Helvetica", 12)) #coloca um texto na tela
lbl.pack( side = TOP ) #coloca no meio da tela - pode usar o place, mas deve posicionar 2 coordenadas


lbla = Label(window, text="Nome do Álbum:",fg='black',font=("Helvetica", 12))
lbla.place(x=100, y=100)     
txtfld=Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=300, y=100)

lblb = Label(window, text="Ano de Lançamento:",fg='black',font=("Helvetica", 12))
lblb.place(x=100, y=150)     
txtfld=Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=300, y=150)

lblc = Label(window, text="Nome da Banda/Artista:",fg='black',font=("Helvetica", 12))
lblc.place(x=100, y=200)     
txtfld=Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=300, y=200)

lbld = Label(window, text="Álbum de lançamento:",fg='black',font=("Helvetica", 12))
lbld.place(x=100, y=250)     
data=("Selecione a opção","Sim", "Não")
cb= Combobox(window, values=data)
cb.place(x=300, y=250)
cb.current(0)

lbl = Label(window, text="",fg='black',font=("Helvetica", 12)) #coloca um texto na tela
lbl.pack( side = BOTTOM ) #coloca no meio da tela - pode usar o place, mas deve posicionar 2 coordenadas

btn = Button(window, text="Clique Me", command=clicked)
btn.pack(side = BOTTOM)

window.mainloop() #mantém a janela aberta

