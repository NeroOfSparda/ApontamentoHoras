import tkinter as tk
import tkinter.ttk as ttk
from calendar import day_abbr
from tkinter import messagebox, PhotoImage
import CodProj as cj
import Cronometro as cronometro
import time
from datetime import datetime
import Graphic as graphic
import Database as database

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

donut = tk.PhotoImage(file="Images/Donuts.png")
donut_reduzido = donut.subsample(10, 10)

logo = tk.Label(novaJanela, image=logo_reduzido, bg="#cdcdcd")
logo.grid(row=0, column=0)

#Criação do titulo dos campos

cronos = tk.Label(novaJanela, text="Cronômetro", font=("Arial", 22), bg="#cdcdcd")
cronos.place(relx=.07, rely=.02)

emp = tk.Label(novaJanela, text="Empresa", font=("Arial", 16), bg="#cdcdcd")
emp.place(relx=.01, rely=.1)

codpj = tk.Label(novaJanela, text="Cod. Proj.", font=("Arial", 16), bg="#cdcdcd")
codpj.place(relx=.3, rely=.1)

obs = tk.Label(novaJanela, text="Observacao", font=("Arial", 16), bg="#cdcdcd")
obs.place(relx=.6, rely=.1)

date_vs = tk.Label(novaJanela, text= date_now, font=("Arial", 22), bg="#cdcdcd")
date_vs.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

initial = tk.Label(novaJanela, text="00:00:00", font=("Arial", 96), bg="#cdcdcd")
initial.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


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


    #if empresa == "" or obs == "":
        #messagebox.showerror("Erro", "Favor digitar a empresa ou observacao.")
    #else:
        #messagebox.showinfo("Iniciar", "Iniciado!")
    cronometro.start= time.time()

        #Função que atualiza o texto com as informações do cronometro

    def atualizar():
        if(iniciar_cronometro == True):
            tempo = cronometro.TikTak()
            initial.config(text= tempo)
            initial.after(1000, atualizar)

    atualizar()


    #Botão para inicio do Cronometro

botaoinit = tk.Button(novaJanela, text="Iniciar", command=Iniciar, width=60)
botaoinit.place(relx=.01, rely=0.8, height=30)

    #Função para encerrar o cronometro

def Parar():
    global iniciar_cronometro
    iniciar_cronometro = False

    empresa_valor = empresa.get()
    observacao_valor = observacao.get()
    data_valor = date_now
    tempo_valor = cronometro.TikTak()

    database.db(
        empresa_valor,
        data_valor,
        tempo_valor,
        observacao_valor
    )

    database.agrupar(
        empresa_valor
        )

    messagebox.showinfo("Parar", "Parado!")
    initial.config(text="00:00:00", font=("Arial", 96), bg="#cdcdcd")
    initial.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

      #Botão para encerrar o cronometro

botaostop = tk.Button(novaJanela, text="Parar", command=Parar, width=60)
botaostop.place(relx=.5, rely=0.8, height=30)

    #Função para Extrair o conteudo

def Extrair():
    messagebox.showinfo("Extrair", "Extraido para a pasta X!")

    #Botão para extrair o conteudo

botaoextract = tk.Button(novaJanela, text="Extrair", command=Extrair, width=50)
botaoextract.place(relx=.5, rely=.9, height=30, anchor=tk.CENTER)

    #Botão para exibir o grafico

botaographic = tk.Button(novaJanela, image=donut_reduzido, command=graphic.graphic, width=50, bg="#cdcdcd", border=0, activebackground="#cdcdcd")
botaographic.place(relx= .9, rely=.05, height=50)

novaJanela.mainloop()