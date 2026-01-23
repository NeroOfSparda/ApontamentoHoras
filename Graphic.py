import matplotlib as mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import Database as database
import time
from datetime import datetime

date = datetime.now()
date_now = date.strftime("%d/%m/%Y")

#Função para gerar o Grafico

def graphic():

    empresas = database.agrupar(date_now)

    lista_empresas = []
    lista_tempo = []

    for empresa in empresas:
        if empresa[1] == date_now:
            lista_empresas.append(empresa[0])
            lista_tempo.append(empresa[2])

    total = sum(lista_tempo)

    def sec(seg):
        h = seg // 3600
        rm = seg % 3600
        m = rm // 60
        s = rm % 60

        return f"{h:02d}:{m:02d}:{s:02d}"

    def pct_time(pct):
        seconds = int(pct * total / 100)
        return sec(seconds)

    #Gera uma nova tela
    pie = tk.Toplevel()
    pie.title("Graphic")
    pie.geometry("720x560")

    #Cria o Gráfico
    figure = Figure(figsize=(4, 4), dpi=100)
    image = FigureCanvasTkAgg(figure, pie)
    image.draw()
    get_tk_widget = image.get_tk_widget()
    get_tk_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    axes = figure.add_subplot(111)
    axes.set_title("Grafico de Projetos", fontsize=14)
    axes.pie(lista_tempo,labels= lista_empresas, autopct=pct_time, wedgeprops={'width':.6})
    axes.text(0,0, sec(total), ha="center", va="center", fontsize=14)
    axes.set_xlabel(date_now, fontsize=14)
    figure.tight_layout()

