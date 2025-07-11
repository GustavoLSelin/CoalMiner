import mysql.connector
from colorama import Fore
import os

class conexao_db:

    def criar_conexao(self):
        try:
            cnx = mysql.connector.connect(host='localhost', user='gustavo', password='gustavo', database='test')
            
            if cnx.is_connected():
                return cnx
            
        except Exception as e:
            print(Fore.RED + '\nERROR')
            print(e)
            input('Precione qualquer tecla: ')
            return None

    def fechar_conexao(self, cnx):
        cnx.close()

    def buscar_todos_dados_de_uma_tabela(self, nome_tabela):

        try:
            cnx = self.criar_conexao()
            conexao = cnx.cursor(buffered=True)

            query = ('SELECT * FROM ' + nome_tabela)
            conexao.execute(query)

            array_dados = []

            for ID, NOME, DATA in conexao:
                array_dados.append('ID: ' + str(ID) + ' NOME: ' + NOME + ' DATA: ' + str(DATA)) 

            self.fechar_conexao(cnx)

            return array_dados

        except Exception as e:
            print(Fore.RED + '\nERROR')
            print(e)
            self.fechar_conexao(cnx)
            input('Precione qualquer tecla: ')

    def __init__(self):
        pass