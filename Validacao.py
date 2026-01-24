import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, PhotoImage
import InterfaceGrafica as interface
import Login as Login
import Create as create

#Cria uma Janela para login

Window_valid = tk.Tk()
Window_valid.title("Login")
Window_valid.geometry("920x680")
Window_valid.configure(background="#cdcdcd")

#Cria e exibe a Logo na tela

logo_valid = tk.PhotoImage(file="Images/Logo_NOS.png")
logo_reduzido2 = logo_valid.subsample(3, 3)

logo_tela = tk.Label(Window_valid, image=logo_reduzido2, bg="#cdcdcd")
logo_tela.place(relx= 0.5, rely= 0.2, anchor= tk.CENTER)

#Criação dos textos de Titulo, Login e Senha

label_title = tk.Label(Window_valid, text="APONTAMENTO DE HORAS", font=("Arial", 22), bg="#cdcdcd")
label_title.place(relx= 0.5, rely= 0.4, anchor= tk.CENTER)

label_login = tk.Label(Window_valid, text="Login:", font=("Arial", 16), bg="#cdcdcd")
label_login.place(relx= 0.33, rely= 0.5, anchor= tk.CENTER)

label_pass = tk.Label(Window_valid, text="Senha:", font=("Arial", 16), bg="#cdcdcd")
label_pass.place(relx= 0.33, rely= 0.6, anchor= tk.CENTER)


#Criação do campo de entrada de dados para login

entry_login = tk.Entry(Window_valid, width=50)
entry_login.place(relx= 0.53, rely= 0.5, anchor= tk.CENTER, height=30)

#Criação do campo de entrada de dados para senha

entry_pass = tk.Entry(Window_valid, show= '*', width=50)
entry_pass.place(relx= 0.53, rely= 0.6, anchor= tk.CENTER, height=30)

#Função para criar conta

def salvar():

    create.Save()

#Botão para abrir a tela de criação de conta

savebutton = ttk.Button(Window_valid, text="Criar conta", command=salvar)
savebutton.place(relx= 0.51, rely= 0.7, anchor= tk.CENTER)

#Função para validar as entradas e abrir a interfacegrafica

def validar():

    login_valor = entry_login.get()
    password_valor = entry_pass.get()
    verify = Login.select(login_valor, password_valor)

    if verify:
        Window_valid.destroy()
        interface.InterfaceGrafica(login_valor)
    else:
        messagebox.showerror('Erro', "Usuario ou senha incorretos")

#Botão para validar as entradas e abrir a interfacegrafica

button_valid = tk.Button(Window_valid, text="Validar", command=validar, width=25, height=2)
button_valid.place(relx= 0.51, rely= 0.8, anchor= tk.CENTER)


Window_valid.mainloop()