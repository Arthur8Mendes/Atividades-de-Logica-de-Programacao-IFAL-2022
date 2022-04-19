from gui import *
from db import *

class Album:
    def __init__(self, nome, ano, banda, lancamento):
        self.nome = nome
        self.ano = ano
        self.banda = banda
        self.lancamento = lancamento
        self.entradas = f'{self.nome}|{self.ano}|{self.banda}|{self.lancamento}'
        
    def cadastrar(self):
        banco_de_dados = Db('db.txt')
        banco_de_dados.escrever(self.entradas)

class Busca:
    def cadastros(self):
        albuns = []
        banco_de_dados = Db('db.txt')
        for linha in banco_de_dados.ler():
            album = linha.split('|')
            albuns.append(album)

        return albuns

    def buscar_por_nome(self, nome):
        resultado = []
        for album in self.cadastros():
            if nome.lower() in album[2].lower():
                resultado.append(album)

        return resultado

    def buscar_por_ano(self, metodo, ano):
        resultado = []
        if metodo == 1:
            for album in self.cadastros():
                if int(album[1]) < int(ano):
                    resultado.append(album)
        elif metodo == 2:
            for album in self.cadastros():
                if int(album[1]) > int(ano):
                    resultado.append(album)
        elif metodo == 3:            
            for album in self.cadastros():
                if int(album[1]) == int(ano):
                    resultado.append(album)

        return resultado

if __name__ == '__main__':
    janela_inicial()