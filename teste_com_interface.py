import tkinter as tk
from tkinter import messagebox

# Lista para armazenar os eventos e suas estratégias de gestão de resíduos
eventos = []

# Função para adicionar um novo evento
def adicionar_evento():
    nome = entry_nome.get()
    local = entry_local.get()
    data = entry_data.get()
    participantes = int(entry_participantes.get())
    gestor = entry_gestor.get()
    
    residuos = calcular_residuos(participantes)
    lixeiras_necessarias = calcular_lixeiras(residuos)
    funcionarios_limpeza = calcular_funcionarios_limpeza(participantes)
    
    estrategias = [
        'Coleta seletiva',
        'Parceria com empresa de reciclagem',
        'Campanha de conscientização'
    ]
    
    evento = {
        'nome': nome,
        'local': local,
        'data': data,
        'estrategias': estrategias,
        'gestor': gestor,
        'participantes': participantes,
        'lixeiras_necessarias': lixeiras_necessarias,
        'residuos': residuos,
        'funcionarios_limpeza': funcionarios_limpeza
    }
    eventos.append(evento)
    messagebox.showinfo("Sucesso", "Evento adicionado com sucesso!")

# Função para calcular a quantidade de resíduos gerados por tipo
def calcular_residuos(participantes):
    residuos = {
        'Orgânico': participantes * 0.3,
        'Reciclável': participantes * 0.15,
        'Não Reciclável': participantes * 0.05
    }
    return residuos

# Função para calcular a quantidade de lixeiras necessárias para cada tipo de resíduo
def calcular_lixeiras(residuos):
    capacidade_lixeira = 50  # Cada lixeira pode conter até 50 kg de resíduos
    lixeiras_necessarias = {}
    for tipo, quantidade in residuos.items():
        lixeiras_necessarias[tipo] = round(quantidade / capacidade_lixeira)
    return lixeiras_necessarias

# Função para calcular a quantidade de funcionários de limpeza necessários
def calcular_funcionarios_limpeza(participantes):
    return round(participantes / 300)

# Função para exibir todos os eventos
def exibir_eventos():
    eventos_str = ""
    for evento in eventos:
        eventos_str += f"Nome: {evento['nome']}\n"
        eventos_str += f"Local: {evento['local']}\n"
        eventos_str += f"Data: {evento['data']}\n"
        eventos_str += f"Gestor: {evento['gestor']}\n"
        eventos_str += f"Participantes: {evento['participantes']}\n"
        eventos_str += f"Lixeiras Necessárias:\n"
        for tipo, quantidade in evento['lixeiras_necessarias'].items():
            eventos_str += f"  - {tipo}: {quantidade} lixeiras\n"
        eventos_str += f"Funcionários de Limpeza Necessários: {evento['funcionarios_limpeza']}\n"
        eventos_str += "Estratégias de Gestão de Resíduos:\n"
        for estrategia in evento['estrategias']:
            eventos_str += f"  - {estrategia}\n"
        eventos_str += "Tipos de Resíduos:\n"
        for tipo, quantidade in evento['residuos'].items():
            eventos_str += f"  - {tipo}: {quantidade} kg\n"
        eventos_str += "-" * 20 + "\n"
    messagebox.showinfo("Eventos", eventos_str)

# Criação da janela principal
root = tk.Tk()
root.title("Gestão de Resíduos em Eventos")
root.configure(bg="#e0f7fa")

# Criação dos widgets
tk.Label(root, text="Nome do Evento:", bg="#e0f7fa", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_nome = tk.Entry(root, font=("Arial", 12))
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Local do Evento:", bg="#e0f7fa", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_local = tk.Entry(root, font=("Arial", 12))
entry_local.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Data do Evento (AAAA-MM-DD):", bg="#e0f7fa", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_data = tk.Entry(root, font=("Arial", 12))
entry_data.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Número de Participantes:", bg="#e0f7fa", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_participantes = tk.Entry(root, font=("Arial", 12))
entry_participantes.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Nome do Gestor:", bg="#e0f7fa", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_gestor = tk.Entry(root, font=("Arial", 12))
entry_gestor.grid(row=4, column=1, padx=10, pady=5)

tk.Button(root, text="Adicionar Evento", command=adicionar_evento, bg="#00796b", fg="white", font=("Arial", 12)).grid(row=5, column=0, columnspan=2, pady=10)
tk.Button(root, text="Exibir Eventos", command=exibir_eventos, bg="#00796b", fg="white", font=("Arial", 12)).grid(row=6, column=0, columnspan=2, pady=10)

# Inicia o loop principal da interface
root.mainloop()
