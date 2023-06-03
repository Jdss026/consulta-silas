import tkinter as tk
from tkinter import messagebox
from arq2xls import insert_rows_xls
from req import isRequisitionCompleted
import json

# with open('config.json', 'r') as config_file:
#     config = json.load(config_file)
#     REQ_DIARIA_MAXIMA_SIENGE = config['remaining_requests']
    
REQ_DIARIA_MAXIMA_SIENGE = 100

def validar_inteiro(entrada):
    if entrada.isdigit():
        return True
    elif entrada == "" or entrada.startswith("-"):
        return True
    else:
        messagebox.showerror("Erro", "Por favor, insira apenas números inteiros.")
        return False
    
def obter_numero():
    try:
        global numero_ent_idObra
        numero_ent_idObra = int(caixa_entrada.get())
        numero_ent_uc = float(caixa_entrada_uc.get())
        numero_ent_bdi = float(caixa_entrada_bdi.get())
        numero_ent_encargos = float(caixa_entrada_encargos.get())
        return [numero_ent_idObra, numero_ent_uc, numero_ent_bdi, numero_ent_encargos]
    except ValueError:
        return False
    
# def comBotaoReq():
#     atualizar_texto()
#     ID_OBRA = obter_numero()
#     isRequisitionCompleted(ID_OBRA[0])

def comBotaoxlsx():
    atualizar_texto()
    numeros = obter_numero()
    isRequisitionCompleted(numeros[0])
    insert_rows_xls(numeros[0])

def obter_numreqmax():
    # Exemplo de função que retorna um número (pode ser substituída pela sua própria lógica)
    global REQ_DIARIA_MAXIMA_SIENGE
    if REQ_DIARIA_MAXIMA_SIENGE > 1:
        # with open('config.json', 'w') as config_file:
        #     config = json.load(config_file)
        #     config['remaining_requests'] -= 1
        #     json.dump(config, config_file)
        REQ_DIARIA_MAXIMA_SIENGE -= 1
        # config_file.close()
        return REQ_DIARIA_MAXIMA_SIENGE
    else:
        return 0

def atualizar_texto():
    # Obtém o número da função e atualiza o texto do rótulo
    numero = obter_numreqmax()
    texto_numero.config(text="NUMERO DE REQUISIÇOES DIARIAS RESTANTES: " + str(numero))

def clicar_botao1():
    print("Botão 1 clicado!")

def clicar_botao2():
    print("Botão 2 clicado!")
    messagebox.showinfo("Mensagem", "EXCEL GERADO!")

def clicar_botao3():
    print("Botão 3 clicado!")
    messagebox.showinfo("Mensagem", "PDF GERADO!")

janela = tk.Tk()
janela.title("SIENGE2Excel")

largura = 500
altura = 400

# Centralizar a janela na tela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
posicao_x = (largura_tela - largura) // 2
posicao_y = (altura_tela - altura) // 2
janela.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")

# Texto 1
texto1 = tk.Label(janela, text="Gerador de Excel e PDF para Requisições \nde Orçamento do Sistema Sienge", font=("Arial", 16))
texto1.pack(side=tk.TOP, pady=10)

# Texto 2
texto_numero = tk.Label(janela, text="", font=("Arial", 16))
texto_numero.pack(side=tk.TOP, pady=10)

# entrada de dados
mensagem = tk.Label(janela, text="Por favor, insira o id da Obra:")
mensagem.pack()
validador = janela.register(validar_inteiro)
caixa_entrada = tk.Entry(janela, validate="key", validatecommand=(validador, "%P"))
caixa_entrada.pack()
#botao = tk.Button(janela, text="Obter número", command=obter_numero)
#botao.pack()

# entrada de dados
msg_uc = tk.Label(janela, text="Por favor, insira o Unidade Construtiva da Obra:")
msg_uc.pack()
#validador = janela.register(validar_inteiro)
caixa_entrada_uc = tk.Entry(janela, validate="key")
caixa_entrada_uc.pack()
#botao = tk.Button(janela, text="Obter número", command=obter_numero)
#botao.pack()

# entrada de dados
msg_bdi = tk.Label(janela, text="Por favor, insira o valor BDI (%):")
msg_bdi.pack()
# validador = janela.register(validar_inteiro)
caixa_entrada_bdi = tk.Entry(janela, validate="key")
caixa_entrada_bdi.pack()
#botao = tk.Button(janela, text="Obter número", command=obter_numero)
#botao.pack()

# entrada de dados
msg_encargos = tk.Label(janela, text="Por favor, insira o valor encargos (%):")
msg_encargos.pack()
# validador = janela.register(validar_inteiro)
caixa_entrada_encargos = tk.Entry(janela, validate="key")
caixa_entrada_encargos.pack()
#botao = tk.Button(janela, text="Obter número", command=obter_numero)
#botao.pack()

# Frame para os botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(side=tk.BOTTOM)

# # Botão 1
# botao1 = tk.Button(frame_botoes, text="REQ SIENGE API", command=comBotaoReq, font=("Arial", 18), width=15)
# botao1.grid(row=0, column=0, padx=10)

# Botão 1
botao2 = tk.Button(frame_botoes, text="GERAR EXCEL", command=comBotaoxlsx, font=("Arial", 18), width=15)
botao2.grid(row=0, column=1, padx=10)

# Botão 3
botao3 = tk.Button(frame_botoes, text="GERAR PDF", command=clicar_botao3, font=("Arial", 18), width=15)
botao3.grid(row=0, column=2, padx=10)

janela.mainloop()