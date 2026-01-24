import pandas as pd
import openpyxl as xl
import Database as database

def extract_excel(login):

    dados = database.extract_db(login)

    wb = xl.Workbook()
    ws = wb.active
    ws.title = "Extract Data"

    ws.append(["Empresa", "Data", "Tempo", "Observação"])

    agrupados = {}

    for linha in dados:
            empresa = linha[0]
            data = linha[1]
            tempo_total = linha[2]
            observacao = linha[3]

            key = (empresa, data)

            if key not in agrupados:

                agrupados[key] = {"tempo": tempo_total, "observacao": observacao}

            else:
                agrupados[key]["tempo"] += tempo_total
                agrupados[key]["observacao"] += "; " + observacao

    def sec(seg):
        h = seg // 3600
        rm = seg % 3600
        m = rm // 60
        s = rm % 60

        return f"{h:02d}:{m:02d}:{s:02d}"


    for (empresa, data), valores in agrupados.items():
            ws.append([empresa, data, sec(valores["tempo"]), valores["observacao"]])

    wb.save(f"Extract/apontamentos_{login}.xlsx")
