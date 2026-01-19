import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, PhotoImage
import CodProj as cj
import Cronometro as cronometro
import time
from datetime import datetime

#Cria a variavel para a data

date = datetime.now()
date_now = date.strftime("%d/%m/%Y")

#def InterfaceGrafica():

    #Cria uma nova janela

novaJanela = tk.Tk()

    #Definir Nome da Janela e tamanho da tela

novaJanela.title("Protótipo")
novaJanela.geometry("920x680")
novaJanela.configure(background="#cdcdcd")

#Insere a logo

logo = tk.PhotoImage(file="Images/Logo_NOS.png")
logo_reduzido = logo.subsample(8, 8)

label = tk.Label(novaJanela, image=logo_reduzido, bg="#cdcdcd")
label.grid(row=0, column=0)

#Criação do titulo dos campos

label = tk.Label(novaJanela, text="Cronômetro", font=("Arial", 22), bg="#cdcdcd")
label.place(relx=.07, rely=.02)

label = tk.Label(novaJanela, text="Empresa", font=("Arial", 16), bg="#cdcdcd")
label.place(relx=.01, rely=.1)

label = tk.Label(novaJanela, text="Cod. Proj.", font=("Arial", 16), bg="#cdcdcd")
label.place(relx=.3, rely=.1)

label = tk.Label(novaJanela, text="Observacao", font=("Arial", 16), bg="#cdcdcd")
label.place(relx=.6, rely=.1)

label = tk.Label(novaJanela, text="00:00:00", font=("Arial", 96), bg="#cdcdcd")
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label = tk.Label(novaJanela, text= date_now, font=("Arial", 22), bg="#cdcdcd")
label.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

#Criação dos campos para entrada de dados

empresa = tk.Entry(novaJanela, width=40)
empresa.place(relx=.01, rely=.15, height=30)
print(empresa.get())

codProj= ttk.Combobox(novaJanela, values=(cj.codigos), width=37)
codProj.place(relx=.3, rely=.15, height=30)

observacao = tk.Entry(novaJanela, width=40)
observacao.place(relx=.6, rely=.15, height=30)
print(observacao.get())

# Cria a variavel para iniciar o cronometro

iniciar_cronometro = False

    #Função para Inicio do cronometro

def Iniciar():
    global iniciar_cronometro
    iniciar_cronometro = True
    exibir = empresa.get()
    obs= observacao.get()


    if empresa == "" or obs == "":
        messagebox.showerror("Erro", "Favor digitar a empresa ou observacao.")
    else:
        messagebox.showinfo("Iniciar", "Iniciado!")
        cronometro.start= time.time()

        #Função que atualiza o texto com as informações do cronometro

    def atualizar():
        if(iniciar_cronometro == True):
            tempo = cronometro.TikTak()
            label.config(text= tempo)
            label.after(1000, atualizar)

    atualizar()


    #Botão para inicio do Cronometro

botao = tk.Button(novaJanela, text="Iniciar", command=Iniciar, width=60)
botao.place(relx=.01, rely=0.8, height=30)

    #Função para encerrar o cronometro

def Parar():
    global iniciar_cronometro
    iniciar_cronometro = False
    messagebox.showinfo("Parar", "Parado!")
    label.config(text="Cronometro encerrado!", font=("Arial", 10))
    label.place(relx=0.5, rely=0.9)

      #Botão para encerrar o cronometro

botao = tk.Button(novaJanela, text="Parar", command=Parar, width=60)
botao.place(relx=.5, rely=0.8, height=30)

    #Função para Extrair o conteudo

def Extrair():
    messagebox.showinfo("Extrair", "Extraido para a pasta X!")

    #Botão para extrair o conteudo

botao = tk.Button(novaJanela, text="Extrair", command=Extrair, width=60)
botao.place(relx=.5, rely=.9, height=30, anchor=tk.CENTER)

novaJanela.mainloop()