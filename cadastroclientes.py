from ast import Delete
from tkinter import ttk
from tkinter.ttk import *
from tkinter import*
from tkinter import messagebox


from dados import *


# cores ----
co0 = "Black"
co1 = "Grey"
co2 = "White"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "Blue"
co6 = "Red"
co7 = "Green"

# Criando a janela ----

janela = Tk()
janela.title('')
janela.geometry('500x450')
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Frames -----

frame_cima = Frame(janela,width=500, height=50,bg=co3, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela,width=500, height=150,bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_tabela = Frame(janela,width=500, height=248,bg=co2, relief="flat")
frame_tabela.grid(row=2, column=0,columnspan=2,padx=10, pady=1, sticky=NW)

# Configurando frame cima
l_nome = Label(frame_cima, text="Cadastro de Clientes", anchor=NE, font=('arial 25 bold'), bg=co3, fg=co0)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, text='',width=500, anchor=NE, font=('arial 1'), bg=co3, fg=co0)
l_linha.place(x=0, y=46)

global tree
# Configurando frame tabela
def mostrar_dados():

    global tree
    #criando visualizaçao da tabela
    dado_h = ['Nome', 'Sexo', 'Telefone', 'E-mail']

    dados = ver_dados()
    

    tree = ttk.Treeview(frame_tabela, selectmode="extended", columns=dado_h, show="headings")

    #Vertical
    vsb = ttk.Scrollbar(frame_tabela, orient='vertical', command=tree.yview)

    #Horizontal
    hsb = ttk.Scrollbar(frame_tabela, orient='horizontal', command=tree.xview) 

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)


   

    for item in dados:
        tree.insert('', 'end', values=item)
        
mostrar_dados()

# funcao para os botoes

def inserir():
    nome = e_nome.get()
    sexo = c_sexo.get()
    telefone = e_tel.get()
    email = e_email.get()

    dados = [nome, sexo, telefone, email]

    if nome == '' or sexo == '' or telefone == '' or email == '':
        messagebox.showwarning('Dados', 'POR FAVOR PREENCHA TODOS OS CAMPOS')
    else:
        adicionar_dados(dados)
        messagebox.showinfo('Dados', 'OS DADOS FORAM ADICIONADOS COM SUCESSO')

        e_nome.delete(0, 'end')
        c_sexo.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_email.delete(0, 'end')   

        mostrar_dados() 

def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        nome = tree_lista[0]
        sexo = tree_lista[1]
        telefone =str(tree_lista[2])
        email = tree_lista[3]

        e_nome.insert(0,nome)
        c_sexo.insert(0,sexo)
        e_tel.insert(0,telefone)
        e_email.insert(0,email) 

        def confirmar():
            nome = e_nome.get()
            sexo = c_sexo.get()
            telefone_novo = e_tel.get()
            email = e_email.get()

            dados = [telefone,nome, sexo, telefone_novo, email]

            atualizar_dados(dados)             
                    
            messagebox.showinfo('Dados', 'OS DADOS FORAM ATUALIZADOS COM SUCESSO')

            e_nome.delete(0, 'end')
            c_sexo.delete(0, 'end')
            e_tel.delete(0, 'end')
            e_email.delete(0, 'end')

            b_confirmar.destroy() 


            mostrar_dados()            

        b_confirmar = Button(frame_baixo,command=confirmar, text="Confirmar",width=12, font=('Ivy 8 bold'), bg=co0, fg=co2, relief=RAISED, overrelief=RIDGE)
        b_confirmar.place(x=285, y=110) 

    except:
        messagebox.showwarning('Dados', 'POR FAVOR SELECIONE UMA INFORMAÇÃO NA TABELA')

def remover():
     try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        telefone = str(tree_lista[2])

        remover_dados(telefone)

        messagebox.showinfo('Dados', 'OS DADOS FOREM DELETADOS COM SUCESSO')

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        mostrar_dados() 
    
     except:
        messagebox.showwarning('Dados', 'POR FAVOR SELECIONE UMA INFORMAÇÃO NA TABELA')



    
# Configurando frame baixo

l_nome = Label(frame_baixo, text="Nome*", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co0)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=('',10), highlightthickness=1)
e_nome.place(x=80, y=20)

l_sexo = Label(frame_baixo, text="Sexo*", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co0)
l_sexo.place(x=10, y=50)
c_sexo = Combobox(frame_baixo, width=27)
c_sexo['value'] = ('','Feminino','Masculino') 
c_sexo.place(x=80, y=50)


l_tel = Label(frame_baixo, text="Telefone*", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co0)
l_tel.place(x=10, y=80)
e_tel = Entry(frame_baixo, width=25, justify='left', font=('',10), highlightthickness=1)
e_tel.place(x=80, y=80)


l_email = Label(frame_baixo, text="E-mail*", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co0)
l_email.place(x=10, y=110)
e_email = Entry(frame_baixo, width=25, justify='left', font=('',10), highlightthickness=1)
e_email.place(x=80, y=110)




b_adicionar = Button(frame_baixo,command=inserir, text="Adicionar",width=14, font=('Ivy 8 bold'), bg=co2, fg=co0, relief=RAISED, overrelief=RIDGE)
b_adicionar.place(x=390, y=50)





def display_data_in_new_window():
    
    new_window = Toplevel()  # Cria nova janela

     # Define o tamanho padrão da janela (largura x altura)
    new_window.geometry("900x600")

    # Visualizaçao da janela
    tree_display_new = ttk.Treeview(new_window, columns=("Nome", "Sexo", "Telefone", "Email"), show="headings")
    tree_display_new.heading("Nome", text="Nome")
    tree_display_new.heading("Sexo", text="Sexo")
    tree_display_new.heading("Telefone", text="Telefone")
    tree_display_new.heading("Email", text="Email")

     # Adiciona um estilo para criar uma borda
    style = ttk.Style()
    style.configure("Treeview", borderwidth=2)
    style.configure("Treeview.Heading", font=('Helvetica', 10, 'bold'))

    # INserir dados na nova janela
    for item in ver_dados():
        tree_display_new.insert('', 'end', values=item)

    for i in range(4):
        tree_display_new.column(i, width=150, anchor='center')

    tree_display_new.pack(expand=YES, fill=BOTH)

    def delete_selected_data():
        try:
            selected_items = tree_display_new.selection()
            for item in selected_items:
                tree_lista = tree_display_new.item(item, 'values')
                telefone = str(tree_lista[2])
                remover_dados(telefone)
                tree_display_new.delete(item)
            messagebox.showinfo('Dados', 'OS DADOS FORAM DELETADOS COM SUCESSO')
        except:
            messagebox.showwarning('Dados', 'POR FAVOR SELECIONE UMA INFORMAÇÃO NA TABELA')

    def search_data():
        query = entry_search.get().lower()
        for item in tree_display_new.get_children():
            if query in str(tree_display_new.item(item)['values']).lower():
                tree_display_new.selection_add(item)
            else:
                tree_display_new.selection_remove(item)

    # Caixa de pesquisa
    entry_search = Entry(new_window, width=20, font=('Ivy 8 bold'))
    entry_search.place(x=10, y=570)  

    # Botão de procura
    b_search = Button(new_window, command=search_data, text="Procurar", width=14, font=('Ivy 8 bold'), bg=co0, fg=co2, relief=RAISED, overrelief=RIDGE)
    b_search.place(x=150, y=570) 

    # Botão para deletar dados
    b_deletar = Button(new_window, command=delete_selected_data, text="Deletar", width=14, font=('Ivy 8 bold'), bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
    b_deletar.place(x=400, y=570)   

    new_window.mainloop()

b_display_data = Button(frame_baixo, command=display_data_in_new_window, text="Lista", width=14, font=('Ivy 8 bold'), bg=co2, fg=co0, relief=RAISED, overrelief=RIDGE)
b_display_data.place(x=390, y=80)



janela.mainloop()

