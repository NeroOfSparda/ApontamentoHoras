import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, PhotoImage
import CodProj as cj
import Cronometro as cronometro
import time


def InterfaceGrafica():

    #Cria uma nova janela

    novaJanela = tk.Toplevel()

    #Definir Nome da Janela e tamanho da tela

    novaJanela.title("Protótipo")
    novaJanela.geometry("950x700")
    novaJanela.configure(background="#cdcdcd")

    logo = tk.PhotoImage(file="Images/Logo_NOS.png")
    logo_reduzido = logo.subsample(8, 8)

    label = tk.Label(novaJanela, image=logo_reduzido, bg="#cdcdcd")
    label.grid(row=0, column=0)

    #Criação do titulo dos campos

    label = tk.Label(novaJanela, text="Empresa", font=("Arial", 11))
    label.grid(column=0, row=1)

    label = tk.Label(novaJanela, text="Cod. Proj.", font=("Arial", 11))
    label.grid(column=0, row=4)

    label = tk.Label(novaJanela, text="Observacao", font=("Arial", 11))
    label.grid(column=0, row=6)

    label = tk.Label(novaJanela, text="Pronto", font=("Arial", 10))
    label.place(relx=0.5, rely=0.9, anchor= tk.CENTER)

    #Criação dos campos para entrada de dados

    empresa = tk.Entry(novaJanela, width=40)
    empresa.grid(column=1, row=1)
    print(empresa.get())

    codProj= ttk.Combobox(novaJanela, values=(cj.codigos), width=37)
    codProj.grid(column=1, row=4)

    observacao = tk.Entry(novaJanela, width=40)
    observacao.grid(column=1, row=6)
    print(observacao.get())

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
                label.config(text=f"Cronômetro iniciado para a empresa {exibir}: {tempo}")
                label.after(1000, atualizar)

        atualizar()


    #Botão para inicio do Cronometro

    botao = tk.Button(novaJanela, text="Iniciar", command=Iniciar)
    botao.grid(column=0, row=8)

    #Função para encerrar o cronometro

    def Parar():
        global iniciar_cronometro
        iniciar_cronometro = False
        messagebox.showinfo("Parar", "Parado!")
        label.config(text="Cronometro encerrado!", font=("Arial", 10))
        label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

      #Botão para encerrar o cronometro

    botao = tk.Button(novaJanela, text="Parar", command=Parar)
    botao.grid(column=1, row=8)

    #Função para Extrair o conteudo

    def Extrair():
        messagebox.showinfo("Extrair", "Extraido para a pasta X!")

    #Botão para extrair o conteudo

    botao = tk.Button(novaJanela, text="Extrair", command=Extrair)
    botao.grid(column=2, row=8)

    novaJanela.mainloop()