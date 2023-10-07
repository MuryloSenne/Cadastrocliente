#importando CSV

import csv
import email
from re import I

lista = ['murylo','Masulino','98293600','muh.senne23@gmail.com']


#Função Adicionar
def adicionar_dados(i):
    #acessando CSV  
    with open('dados.csv', 'a+', newline='') as file:
        escrever = csv.writer(file)
        escrever.writerow(i)

   
#FUNCAO VER DADOS   
def ver_dados():
    dados = []
    #Acessando CSV  
    with open('dados.csv') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            dados.append(linha)
    return(dados)


#FUNCAO DELETAR DADOS
def remover_dados(i):
    def adiconar_novalista(j):
        #Acessando csv
         with open('dados.csv', 'w', newline='') as file:
             escrever = csv.writer(file)
             escrever.writerows(j)
             ver_dados() 


    nova_lista = []
    telefone = i
    with open('dados.csv', 'r') as file:
        ler_csv = csv.reader(file)

        for linha in ler_csv:
            nova_lista.append(linha)
            for campo in linha:
                if campo == telefone:
                    nova_lista.remove(linha)
    
    #Adicionar nova lista
    adiconar_novalista(nova_lista)


    
#FUNCAO ATUALIZAR DADOS
def atualizar_dados(i):
    def adiconar_novalista(j):
        #Acessando csv
         with open('dados.csv', 'w', newline='') as file:
             escrever = csv.writer(file)
             escrever.writerows(j)
             ver_dados() 


    nova_lista = []
    telefone = i[0]
    with open('dados.csv', 'r') as file:
        ler_csv = csv.reader(file)

        for linha in ler_csv:
            nova_lista.append(linha)
            for campo in linha:
                if campo == telefone:
                    nome = i[1]
                    sexo = i[2]
                    tel = i[3]
                    email = i[4]

                    dados = [nome, sexo, tel, email]
                    #trocando lista por index    
                    index = nova_lista.index(linha)
                    nova_lista[index] = dados
    
    #Adicionar nova lista
    adiconar_novalista(nova_lista)

#FUNCAO PESQUISAR DADOS   
def pesquisar_dados(i):
    dados = []
    telefone = i
   
    #Acessando CSV  
    with open('dados.csv') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            for campo in linha:
                if campo == telefone:
                    dados.append(linha)
    
    return(dados)

(pesquisar_dados('98293600'))










    



