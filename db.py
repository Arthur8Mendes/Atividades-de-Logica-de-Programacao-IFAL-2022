class Db:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def escrever(self, dados):
        arquivo = open(self.nome_arquivo, 'a', encoding='utf-8')
        arquivo.write(f'{dados}\n')
        arquivo.close()

    def ler(self):
        arquivo = open(self.nome_arquivo, 'r', encoding='utf-8')
        return arquivo.readlines()