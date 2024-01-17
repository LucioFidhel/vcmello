import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw
import os


def calcular_total():
    try:
        total_camisas = sum(int(entry.get()) for entry in entries.values())
        resultado_var.set(f'Total de camisas: {total_camisas}')
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números nas caixas de entrada.")


def gerar_imagem_png():
    try:
        # Criar uma imagem em branco
        imagem = Image.new("RGB", (1080, 720), "white")
        draw = ImageDraw.Draw(imagem)

        # Adiciona informações da caixa de inputs à imagem
        draw.text((10, 10), f'Nome da Malha: {nome_malha_entry.get()}', fill="black")
        draw.text((10, 30), f'Cor da Malha: {cor_malha_entry.get()}', fill="black")

        y_offset = 50
        for tamanho, entry in entries.items():
            draw.text((10, y_offset), f"Quantidade de Camisas {tamanho}: {entry.get()}", fill="black")
            y_offset += 20

        # Obtém o caminho da pasta Downloads do usuário
        downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        imagem_path = os.path.join(downloads_path, 'resultado_camisas.png')

        # Salva a imagem
        imagem.save(imagem_path)

        # Atualiza a caixa de texto com os resultados
        atualizar_caixa_resultados()

        messagebox.showinfo("Sucesso", f"Imagem PNG gerada com sucesso.\nSalva em: {imagem_path}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar imagem PNG: {str(e)}")


def atualizar_caixa_resultados():
    resultado_text.delete(1.0, tk.END)  # Limpa o conteúdo atual
    resultado_text.insert(tk.END, f"Nome da Malha: {nome_malha_entry.get()}\n")
    resultado_text.insert(tk.END, f"Cor da Malha: {cor_malha_entry.get()}\n")

    for tamanho, entry in entries.items():
        resultado_text.insert(tk.END, f"Quantidade de Camisas {tamanho}: {entry.get()}\n")


# Configuração da interface gráfica
root = tk.Tk()
root.title("Sistema de Controle de Camisas")

# Variáveis de controle
resultado_var = tk.StringVar()
nome_malha_entry = tk.Entry(root)
cor_malha_entry = tk.Entry(root)

# Labels e Entradas
tk.Label(root, text="Nome da Malha:").grid(row=0, column=0, padx=10, pady=5)
nome_malha_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Cor da Malha:").grid(row=1, column=0, padx=10, pady=5)
cor_malha_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Quantidade de Camisas por Tamanho:").grid(row=2, column=0, padx=10, pady=5)

tamanhos = ['P', 'M', 'G', 'GG', '2GG', '3GG', '4GG']
entries = {}

for i, tamanho in enumerate(tamanhos):
    tk.Label(root, text=tamanho).grid(row=3 + i, column=0, padx=10, pady=5)
    entries[tamanho] = tk.Entry(root)
    entries[tamanho].grid(row=3 + i, column=1, padx=10, pady=5)

# Caixa de texto para os resultados
resultado_text = tk.Text(root, height=10, width=40)
resultado_text.grid(row=10, column=0, columnspan=2, pady=10)

# Botões
tk.Button(root, text="Calcular Total", command=calcular_total).grid(row=11, column=0, columnspan=2, pady=10)
tk.Button(root, text="Gerar Imagem PNG", command=gerar_imagem_png).grid(row=12, column=0, columnspan=2, pady=10)

# Resultado
tk.Label(root, textvariable=resultado_var).grid(row=13, column=0, columnspan=2, pady=10)

root.mainloop()
