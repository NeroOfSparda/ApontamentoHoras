import tkinter as tk
from tkinter import ttk

import Login as login

def Save():

    CreateWindow = tk.Toplevel()
    CreateWindow.title("Criar Conta")
    CreateWindow.geometry("920x680")
    CreateWindow.configure(background="#cdcdcd")

    logo_valid2 = tk.PhotoImage(file="images/Logo_NOS.png")
    logo_reduzido3 = logo_valid2.subsample(3, 3)

    logoval2 = tk.Label(CreateWindow, image=logo_reduzido3, bg="#cdcdcd")
    logoval2.image = logo_reduzido3
    logoval2.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    apont = tk.Label(CreateWindow, text="CRIAR CONTA", font=("Arial", 22), bg="#cdcdcd")
    apont.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    logincreate = tk.Label(CreateWindow, text="Login:", font=("Arial", 16), bg="#cdcdcd")
    logincreate.place(relx=0.33, rely=0.5, anchor=tk.CENTER)

    passcreate = tk.Label(CreateWindow, text="Senha:", font=("Arial", 16), bg="#cdcdcd")
    passcreate.place(relx=0.33, rely=0.6, anchor=tk.CENTER)

    loginc = tk.Entry(CreateWindow, width=50)
    loginc.place(relx=0.53, rely=0.5, anchor=tk.CENTER, height=30)
    print(loginc.get())
    # Exibe o valor digitado na tela

    # Função para entrada de dados no campo de senha e exibição de * no lugar da senha

    passwordc = tk.Entry(CreateWindow, width=50)
    passwordc.place(relx=0.53, rely=0.6, anchor=tk.CENTER, height=30)
    print(passwordc.get())

    def salvar():

        loginc_valor = loginc.get()
        password_valor = passwordc.get()

        login.acess(loginc_valor, password_valor)
        CreateWindow.destroy()

    createbutton = ttk.Button(CreateWindow, text="Criar Conta", command=salvar, width=25)
    createbutton.place(relx=0.51, rely=0.8, anchor=tk.CENTER)