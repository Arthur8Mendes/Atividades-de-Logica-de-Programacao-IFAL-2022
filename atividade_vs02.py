from tkinter import *
from tkinter.ttk import Combobox, Treeview

# -------------------------------------------------------------------------------------
# Cadastrar

def cadastrar(event):
    arquivo = open('informacoes-albuns.txt', 'a', encoding='utf-8')
    informacoes_album = ent_nome_album.get() + '|' + ent_ano_lancamento.get() + '|' + ent_nome_banda_artista.get() + '|' + cb.get()
    arquivo.write(f'{informacoes_album}\n')
    arquivo.close()

# -------------------------------------------------------------------------------------
# Listar cadastros

def listar(event):

    janela = Tk()
    janela.title('Lista de cadastros')
    janela.geometry('900x400+100+100')

    tabela = Treeview(janela, columns=('1', '2', '3', '4'), show='headings')
    tabela.column('1', minwidth=50, width=200)
    tabela.column('2', minwidth=50, width=200)
    tabela.column('3', minwidth=50, width=200)
    tabela.column('4', minwidth=50, width=200)

    tabela.heading('1', text='Nome do álbum')
    tabela.heading('2', text='Ano de lançamento')
    tabela.heading('3', text='Nome da banda/artista')
    tabela.heading('4', text='Álbum de lançamento')

    tabela.place(x=50, y=80)

    albuns = []
    arquivo = open('informacoes-albuns.txt', 'r', encoding='utf-8')
    for album in arquivo:
        album = album.split('|')
        albuns.append(album)
    
    for nome, ano, banda, lancamento in albuns:
        tabela.insert('', END, values=(nome, ano, banda, lancamento))
    
    janela.mainloop()

# -------------------------------------------------------------------------------------
# Buscar por nome

def buscar_por_nome(event):

    def buscar_nome(event):
        for item in tabela.get_children():
            tabela.delete(item)

        caracteres = ent_buscar_por_nome.get()
        albuns = []
        resultado = []
        arquivo = open('informacoes-albuns.txt', 'r', encoding='utf-8')

        for album in arquivo:
            album = album.split('|')
            albuns.append(album)

        for album in albuns:
           
            if caracteres.lower() in album[2].lower():
                resultado.append(album)

        for nome, ano, banda, lancamento in resultado:
            tabela.insert('', END, values=(nome, ano, banda, lancamento))

    janela = Tk()
    janela.title('Buscar por nome')
    janela.geometry('900x400+100+100')

    ent_buscar_por_nome = Entry(janela)
    ent_buscar_por_nome.place(x=50, y=40)

    btn_buscar_por_nome = Button(janela, text='Buscar')
    btn_buscar_por_nome.place(x=200, y=40)

    tabela = Treeview(janela, columns=('1', '2', '3', '4'), show='headings')
    tabela.column('1', minwidth=50, width=200)
    tabela.column('2', minwidth=50, width=200)
    tabela.column('3', minwidth=50, width=200)
    tabela.column('4', minwidth=50, width=200)

    tabela.heading('1', text='Nome do álbum')
    tabela.heading('2', text='Ano de lançamento')
    tabela.heading('3', text='Nome da banda/artista')
    tabela.heading('4', text='Álbum de lançamento')

    tabela.place(x=50, y=80)

    btn_buscar_por_nome.bind('<Button-1>', buscar_nome)

    janela.mainloop()

# -------------------------------------------------------------------------------------
# Buscar por ano

def buscar_por_ano(event):

    def buscar_ano(event):
        for item in tabela.get_children():
            tabela.delete(item)

        rb_selecionado = var.get()
        ano = cb_anos.get()

        albuns = []
        resultado = []

        arquivo = open('informacoes-albuns.txt', 'r', encoding='utf-8')
        for album in arquivo:
            album = album.split('|')
            albuns.append(album)

        if rb_selecionado == 1:
            for album in albuns:
                if int(album[1]) < int(ano):
                    resultado.append(album)

        elif rb_selecionado == 2:
            for album in albuns:
                if int(album[1]) > int(ano):
                    resultado.append(album)

        elif rb_selecionado == 3:
            for album in albuns:
                if int(album[1]) == int(ano):
                    resultado.append(album)
        
        for nome, ano, banda, lancamento in resultado:
            tabela.insert('', END, values=(nome, ano, banda, lancamento))

    janela = Toplevel()
    janela.title('Buscar por ano')
    janela.geometry('900x400+100+100')

    var = IntVar()

    rb_anterior = Radiobutton(janela, text='Anterior a', variable=var, value=1)
    rb_posterior = Radiobutton(janela, text='Posterior a', variable=var, value=2)
    rb_igual = Radiobutton(janela, text='Igual a', variable=var, value=3)

    anos = []
    for ano in range(1950, 2023):
        anos.append(ano)

    cb_anos = Combobox(janela, values=anos)
    cb_anos.current(0)

    tabela = Treeview(janela, columns=('1', '2', '3', '4'), show='headings')
    tabela.column('1', minwidth=50, width=200)
    tabela.column('2', minwidth=50, width=200)
    tabela.column('3', minwidth=50, width=200)
    tabela.column('4', minwidth=50, width=200)

    tabela.heading('1', text='Nome do álbum')
    tabela.heading('2', text='Ano de lançamento')
    tabela.heading('3', text='Nome da banda/artista')
    tabela.heading('4', text='Álbum de lançamento')

    rb_anterior.place(x=50, y=40)
    rb_posterior.place(x=150, y=40)
    rb_igual.place(x=250, y=40)

    cb_anos.place(x=350, y=40)
    cb_anos.bind("<<ComboboxSelected>>", buscar_ano)

    tabela.place(x=50, y=80)

    janela.mainloop()

# -------------------------------------------------------------------------------------
# Janela inicial


janela = Tk()
janela.title('Cadastrar álbum')
janela.geometry('600x400+100+100')

lbl_nome_album = Label(janela, text='Nome do álbum')
ent_nome_album = Entry(janela)
lbl_nome_album.place(x=100, y=50)
ent_nome_album.place(x=300, y=50)

lbl_ano_lancamento = Label(janela, text='Ano de lançamento')
ent_ano_lancamento = Entry(janela)
lbl_ano_lancamento.place(x=100, y=100)
ent_ano_lancamento.place(x=300, y=100)

lbl_nome_banda_artista = Label(janela, text='Nome da banda/artista')
ent_nome_banda_artista = Entry(janela)
lbl_nome_banda_artista.place(x=100, y=150)
ent_nome_banda_artista.place(x=300, y=150)

lbl_album_lancamento = Label(janela, text='Álbum de lançamento')
opcoes = ('Sim', 'Não')
cb = Combobox(janela, values=opcoes)
cb.current(0)
lbl_album_lancamento.place(x=100, y=200)
cb.place(x=300, y=200)

btn_cadastrar = Button(janela, text='Cadastrar')
btn_cadastrar.place(x=100, y=300)

btn_listar_cadastros = Button(janela, text='Listar cadastros')
btn_listar_cadastros.place(x=180, y=300)

btn_buscar_nome = Button(janela, text='Buscar por nome')
btn_buscar_nome.place(x=300, y=300)

btn_buscar_ano = Button(janela, text='Buscar por ano')
btn_buscar_ano.place(x=420, y=300)

btn_cadastrar.bind('<Button-1>', cadastrar)
btn_listar_cadastros.bind('<Button-1>', listar)
btn_buscar_nome.bind('<Button-1>', buscar_por_nome)
btn_buscar_ano.bind('<Button-1>', buscar_por_ano)

janela.mainloop()
