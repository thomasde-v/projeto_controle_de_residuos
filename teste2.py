# Programa para gerenciar a gestão de resíduos em eventos

# Lista para armazenar os eventos e suas estratégias de gestão de resíduos
eventos = []

# Função para adicionar um novo evento
def adicionar_evento(nome, local, data, estrategias, gestor, participantes):
    # Calcula a quantidade de lixeiras necessárias para cada tipo de resíduo
    residuos = calcular_residuos(participantes)
    lixeiras_necessarias = calcular_lixeiras(residuos)
    # Calcula a quantidade de funcionários de limpeza necessários
    funcionarios_limpeza = calcular_funcionarios_limpeza(participantes)
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
    return round(participantes / 50)

# Função para exibir todos os eventos
def exibir_eventos():
    for evento in eventos:
        print(f"Nome: {evento['nome']}")
        print(f"Local: {evento['local']}")
        print(f"Data: {evento['data']}")
        print(f"Gestor: {evento['gestor']}")
        print(f"Participantes: {evento['participantes']}")
        print(f"Lixeiras Necessárias:")
        for tipo, quantidade in evento['lixeiras_necessarias'].items():
            print(f"  - {tipo}: {quantidade} lixeiras")
        print(f"Funcionários de Limpeza Necessários: {evento['funcionarios_limpeza']}")
        print("Estratégias de Gestão de Resíduos:")
        for estrategia in evento['estrategias']:
            print(f"  - {estrategia}")
        print("Tipos de Resíduos:")
        for tipo, quantidade in evento['residuos'].items():
            print(f"  - {tipo}: {quantidade} kg")
        print("-" * 20)

# Função para introdução do usuário
def introducao_usuario():
    nome_gestor = input("Digite seu nome: ")
    email_gestor = input("Digite seu email: ")
    return {'nome': nome_gestor, 'email': email_gestor}

# Introdução do usuário
gestor = introducao_usuario()

# Coletando informações do evento
nome_evento = input("Digite o nome do evento: ")
local_evento = input("Digite o local do evento: ")
data_evento = input("Digite a data do evento (DD/MM/AAAA): ")
participantes_evento = int(input("Digite o número de participantes: "))
estrategias_evento = [
    'Coleta seletiva',
    'Parceria com empresa de reciclagem',
    'Campanha de conscientização'
]

# Adicionando o evento
adicionar_evento(nome_evento, local_evento, data_evento, estrategias_evento, gestor['nome'], participantes_evento)

# Exibindo os eventos
exibir_eventos()
