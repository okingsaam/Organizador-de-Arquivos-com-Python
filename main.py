import os
from tkinter.filedialog import askdirectory

# Seleciona a pasta base
caminho = askdirectory(title="Selecione uma pasta")

# Lista arquivos dentro da pasta
lista_arquivos = os.listdir(caminho)
print(lista_arquivos)

# Dicionário com os tipos de arquivos
locais = {
    "imagens": [".png", ".jpg", ".jpeg"],
    "planilhas": [".xlsx"],
    "pdfs": [".pdf"],
    "csv": [".csv"],
    "compactados": [".zip", ".rar"],
    "executáveis": [".exe", ".msi", ".jar"],
    "vídeos": [".mp4", ".mov"],
}

# Percorre os arquivos e move conforme a extensão
for arquivo in lista_arquivos:
    # Ignora se for uma pasta
    if os.path.isdir(os.path.join(caminho, arquivo)):
        continue

    nome, extensao = os.path.splitext(arquivo)
    extensao = extensao.lower()  

    for pasta, extensoes in locais.items():
        if extensao in extensoes:
            pasta_destino = os.path.join(caminho, pasta)
            if not os.path.exists(pasta_destino):
                os.mkdir(pasta_destino)

            origem = os.path.join(caminho, arquivo)
            destino = os.path.join(pasta_destino, arquivo)

            # Move o arquivo
            os.rename(origem, destino)
            print(f"Movido: {arquivo} → {pasta_destino}")
