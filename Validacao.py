import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, PhotoImage
import InterfaceGrafica as interface
import Login as Login
import Create as create

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

login = tk.Entry(Janela, width=50)
login.place(relx= 0.53, rely= 0.5, anchor= tk.CENTER, height=30)
print(login.get())
#Exibe o valor digitado na tela


#Função para entrada de dados no campo de senha e exibição de * no lugar da senha

password = tk.Entry(Janela, show= '*', width=50)
password.place(relx= 0.53, rely= 0.6, anchor= tk.CENTER, height=30)
print(password.get())

#Exibe a senha digitada com *
def salvar():

    create.Save()


savebutton = ttk.Button(Janela, text="Criar conta", command=salvar)
savebutton.place(relx= 0.51, rely= 0.7, anchor= tk.CENTER)

#Função para validar as entradas e abrir a interfacegrafica

def validar():

    login_valor = login.get()
    password_valor = password.get()
    verify = Login.select(login_valor, password_valor)

    if verify:
        Janela.destroy()
        interface.InterfaceGrafica()
    else:
        messagebox.showerror('Erro', "Usuario ou senha incorretos")

botao = tk.Button(Janela, text="Validar", command=validar, width=25, height=2)
botao.place(relx= 0.51, rely= 0.8, anchor= tk.CENTER)


Janela.mainloop()