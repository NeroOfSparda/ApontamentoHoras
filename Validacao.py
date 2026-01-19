import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, PhotoImage
import InterfaceGrafica as interface

#Cria uma Janela para login

Janela = tk.Tk()
Janela.title("Login")
Janela.geometry("920x680")
Janela.configure(background="#cdcdcd")

logo_valid = tk.PhotoImage(file="Images/Logo_NOS.png")
logo_reduzido2 = logo_valid.subsample(3, 3)

label = tk.Label(Janela, image=logo_reduzido2, bg="#cdcdcd")
label.place(relx= 0.5, rely= 0.2, anchor= tk.CENTER)

#Criação de titulo dos campos para login

label = tk.Label(Janela, text="APONTAMENTO DE HORAS", font=("Arial", 22), bg="#cdcdcd")
label.place(relx= 0.5, rely= 0.4, anchor= tk.CENTER)

label = tk.Label(Janela, text="Login:", font=("Arial", 16), bg="#cdcdcd")
label.place(relx= 0.33, rely= 0.5, anchor= tk.CENTER)

label = tk.Label(Janela, text="Senha:", font=("Arial", 16), bg="#cdcdcd")
label.place(relx= 0.33, rely= 0.6, anchor= tk.CENTER)

#Função para entrada de dados no campo de usuario

def usuario():
      login = tk.Entry(Janela, width=50)
      login.place(relx= 0.53, rely= 0.5, anchor= tk.CENTER, height=30)

#Exibe o valor digitado na tela

print(usuario())

#Função para entrada de dados no campo de senha e exibição de * no lugar da senha

def senha():
      password = tk.Entry(Janela, show= '*', width=50)
      password.place(relx= 0.53, rely= 0.6, anchor= tk.CENTER, height=30)

#Exibe a senha digitada com *

print(senha())

#Função para validar as entradas e abrir a interfacegrafica

def validar():
    interface.InterfaceGrafica()

botao = tk.Button(Janela, text="Validar", command=validar, width=25, height=2)
botao.place(relx= 0.51, rely= 0.7, anchor= tk.CENTER)


Janela.mainloop()