from tkinter import *
from tkinter.ttk import Combobox, Treeview
from domain import Album, Busca

def janela_inicial():
    global ent_nome_album
    global ent_ano_lancamento
    global ent_nome_banda_artista
    global cb_album_lancamento

    janela_inicial = Tk()
    janela_inicial.title('Cadastrar álbum')
    janela_inicial.geometry('600x400+100+100')

    lbl_nome_album = Label(janela_inicial, text='Nome do álbum')
    ent_nome_album = Entry(janela_inicial)
    lbl_nome_album.place(x=100, y=50)
    ent_nome_album.place(x=300, y=50)

    lbl_ano_lancamento = Label(janela_inicial, text='Ano de lançamento')
    ent_ano_lancamento = Entry(janela_inicial)
    lbl_ano_lancamento.place(x=100, y=100)
    ent_ano_lancamento.place(x=300, y=100)

    lbl_nome_banda_artista = Label(janela_inicial, text='Nome da banda/artista')
    ent_nome_banda_artista = Entry(janela_inicial)
    lbl_nome_banda_artista.place(x=100, y=150)
    ent_nome_banda_artista.place(x=300, y=150)

    lbl_album_lancamento = Label(janela_inicial, text='Álbum de lançamento')
    opcoes = ('Sim', 'Não')
    cb_album_lancamento = Combobox(janela_inicial, values=opcoes)
    cb_album_lancamento.current(0)
    lbl_album_lancamento.place(x=100, y=200)
    cb_album_lancamento.place(x=300, y=200)
    
    btn_cadastrar = Button(janela_inicial, text='Cadastrar')
    btn_cadastrar.place(x=100, y=300)

    btn_listar = Button(janela_inicial, text='Listar')
    btn_listar.place(x=180, y=300)

    btn_buscar_por_nome = Button(janela_inicial, text='Buscar por nome')
    btn_buscar_por_nome.place(x=300, y=300)

    btn_buscar_por_ano = Button(janela_inicial, text='Buscar por ano')
    btn_buscar_por_ano.place(x=420, y=300)

    
    btn_cadastrar.bind('<Button-1>', cadastrar)
    btn_listar.bind('<Button-1>', listar)
    btn_buscar_por_nome.bind('<Button-1>', abrir_janela_buscar_por_nome)
    btn_buscar_por_ano.bind('<Button-1>', abrir_janela_buscar_por_ano)

    Label(text="Autor: Arthur Mendes, Luiz Marcelo, Claudson Lima").place(x=10, y=375)

    janela_inicial.mainloop()

def cadastrar(event):
    
    album = Album(ent_nome_album.get(), ent_ano_lancamento.get(), ent_nome_banda_artista.get(), cb_album_lancamento.get())
    album.cadastrar()
    ent_nome_album.delete(0, 'end') 
    ent_ano_lancamento.delete(0, 'end')
    ent_nome_banda_artista.delete(0, 'end')
    cb_album_lancamento.delete(0, 'end')


def listar(event):
    janela_listar = Tk()
    janela_listar.title('Lista de cadastros')
    janela_listar.geometry('900x400+100+100')
    
    tabela_listar = Treeview(janela_listar, columns=('1', '2', '3', '4'), show='headings')

    tabela_listar.column('1', minwidth=50, width=200)
    tabela_listar.column('2', minwidth=50, width=200)
    tabela_listar.column('3', minwidth=50, width=200)
    tabela_listar.column('4', minwidth=50, width=200)

    tabela_listar.heading('1', text='Nome do álbum')
    tabela_listar.heading('2', text='Ano de lançamento')
    tabela_listar.heading('3', text='Nome da banda/artista')
    tabela_listar.heading('4', text='Álbum de lançamento')
    tabela_listar.place(x=50, y=80)

    dados = Busca()
    albuns = dados.cadastros()

    for nome, ano, banda, lancamento in albuns:
        tabela_listar.insert('', END, values=(nome, ano, banda, lancamento))

    janela_listar.mainloop()

def abrir_janela_buscar_por_nome(event):
    global ent_buscar_por_nome
    global tabela_buscar_por_nome

    janela_buscar_por_nome = Tk()
    janela_buscar_por_nome.title('Buscar por nome')
    janela_buscar_por_nome.geometry('900x400+100+100')

    ent_buscar_por_nome = Entry(janela_buscar_por_nome)
    ent_buscar_por_nome.place(x=50, y=40)

    btn_buscar = Button(janela_buscar_por_nome, text='Buscar')
    btn_buscar.place(x=200, y=40)

    tabela_buscar_por_nome = Treeview(janela_buscar_por_nome, columns=('1', '2', '3', '4'), show='headings')

    tabela_buscar_por_nome.column('1', minwidth=50, width=200)
    tabela_buscar_por_nome.column('2', minwidth=50, width=200)
    tabela_buscar_por_nome.column('3', minwidth=50, width=200)
    tabela_buscar_por_nome.column('4', minwidth=50, width=200)

    tabela_buscar_por_nome.heading('1', text='Nome do álbum')
    tabela_buscar_por_nome.heading('2', text='Ano de lançamento')
    tabela_buscar_por_nome.heading('3', text='Nome da banda/artista')
    tabela_buscar_por_nome.heading('4', text='Álbum de lançamento')
    tabela_buscar_por_nome.place(x=50, y=80)

    btn_buscar.bind('<Button-1>', atualizar_tabela_buscar_por_nome)

    janela_buscar_por_nome.mainloop()

def atualizar_tabela_buscar_por_nome(event):
    dados = Busca()
    albuns = dados.buscar_por_nome(ent_buscar_por_nome.get())

    for linha in tabela_buscar_por_nome.get_children():
        tabela_buscar_por_nome.delete(linha)

    for nome, ano, banda, lancamento in albuns:
        tabela_buscar_por_nome.insert('', END, values=(nome, ano, banda, lancamento))

def abrir_janela_buscar_por_ano(event):
    global rb_selecionado
    global cb_anos
    global tabela_buscar_por_ano

    janela_buscar_por_ano = Toplevel()
    janela_buscar_por_ano.title('Buscar por ano')
    janela_buscar_por_ano.geometry('900x400+100+100')

    rb_selecionado = IntVar()
    rb_anterior = Radiobutton(janela_buscar_por_ano, text='Anterior a', variable=rb_selecionado, value=1)
    rb_anterior.place(x=50, y=40)

    rb_posterior = Radiobutton(janela_buscar_por_ano, text='Posterior a', variable=rb_selecionado, value=2)
    rb_posterior.place(x=150, y=40)

    rb_igual = Radiobutton(janela_buscar_por_ano, text='Igual a', variable=rb_selecionado, value=3)
    rb_igual.place(x=250, y=40)

    anos = []
    for ano in range(1950, 2023): 
        anos.append(ano)

    cb_anos = Combobox(janela_buscar_por_ano, values=anos)
    cb_anos.current(0)
    cb_anos.place(x=350, y=40)

    btn_buscar = Button(janela_buscar_por_ano, text='Buscar')
    btn_buscar.place(x=520, y=40)

    tabela_buscar_por_ano = Treeview(janela_buscar_por_ano, columns=('1', '2', '3', '4'), show='headings')

    tabela_buscar_por_ano.column('1', minwidth=50, width=200)
    tabela_buscar_por_ano.column('2', minwidth=50, width=200)
    tabela_buscar_por_ano.column('3', minwidth=50, width=200)
    tabela_buscar_por_ano.column('4', minwidth=50, width=200)
    
    tabela_buscar_por_ano.heading('1', text='Nome do álbum')
    tabela_buscar_por_ano.heading('2', text='Ano de lançamento')
    tabela_buscar_por_ano.heading('3', text='Nome da banda/artista')
    tabela_buscar_por_ano.heading('4', text='Álbum de lançamento')
    tabela_buscar_por_ano.place(x=50, y=80)

    btn_buscar.bind('<Button-1>', atualizar_tabela_buscar_por_ano)

    janela_buscar_por_ano.mainloop()

def atualizar_tabela_buscar_por_ano(event):
    dados = Busca()
    albuns = dados.buscar_por_ano(rb_selecionado.get(), cb_anos.get())

    for linha in tabela_buscar_por_ano.get_children():
        tabela_buscar_por_ano.delete(linha)

    for nome, ano, banda, lancamento in albuns:
        tabela_buscar_por_ano.insert('', END, values=(nome, ano, banda, lancamento))
