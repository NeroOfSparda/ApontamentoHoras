import matplotlib as mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk

#Função para gerar o Grafico

def graphic():

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
    axes.pie([1,1,1,1], wedgeprops={'width':.6})
    figure.tight_layout()
