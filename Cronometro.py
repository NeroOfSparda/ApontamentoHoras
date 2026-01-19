import time

#Inicia o cronometro em 0

start= ""

#Função de calculo do tempo

def TikTak():

        total = int(time.time() - start)
        h= total // 3600
        rm= total % 3600
        m= rm // 60
        s = rm % 60
        return f"{h:02d}:{m:02d}:{s:02d}".format(h, m, s)

