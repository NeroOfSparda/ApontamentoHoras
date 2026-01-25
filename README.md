Apontamento de Horas - Python

Sistema desktop desenvolvido em Python para apontamento de horas por usuário, com controle de tempo, armazenamento em banco de dados SQLite, geração de gráficos e exportação para Excel.
O projeto foi pensado para uso simples: o usuário faz login, inicia o cronômetro, registra atividades e depois pode visualizar gráficos ou extrair os dados.

Funcionalidades:

Login de usuários
Cronômetro para apontamento de horas

Registro de:

Empresa
Data
Tempo trabalhado

Observações:

Banco de dados separado por usuário
Um arquivo apontamento_<login>.db por login
Gráfico em pizza com o tempo por empresa (por data)
Exportação para Excel
Gera arquivo apontamentos_<login>.xlsx
Interface gráfica com Tkinter
Geração de executável (.exe) com PyInstaller

Cada usuário possui:

Seu próprio banco de dados de apontamentos
Seu próprio arquivo de exportação Excel

Os dados ficam organizados em pastas:

DB/ - bancos de dados
Extract/ - arquivos Excel
Images/ - imagens usadas na interface

Tecnologias Utilizadas:

Python 3
Tkinter (Interface gráfica)
SQLite3 (Banco de dados)
Matplotlib (Gráficos)
OpenPyXL / Pandas (Exportação Excel)
PyInstaller (Geração do executável)

Como Executar (modo desenvolvimento):

Instale as dependências:

pip install matplotlib pandas openpyxl

Execute o sistema:

python main.py

Gerando o Executável (.exe):

pyinstaller --onefile --windowed -- no console --add-data "Images;Images" --add-data "DB;DB" --add-data "Extract;Extract" main.py

O executável será gerado na pasta dist/.

Cada login é isolado:

Não há mistura de dados entre usuários

Este projeto foi desenvolvido com foco em:

Prática de Python desktop
Uso real de SQLite
Organização de dados por usuário
Integração entre interface, banco, gráficos e exportação
Demonstração de arquitetura e boas práticas para portfólio

Possíveis Melhorias Futuras:

Melhoria na Interface
Edição de apontamentos (Update)
Exclusão de registros (Delete)
Filtros avançados por período
Relatórios em PDF
Controle de permissões por usuário

Autor:

André Luiz Ferreira de Souza (NeroOfSparda)
Desenvolvedor Python
