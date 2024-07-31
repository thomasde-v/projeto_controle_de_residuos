

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
        print(f"Estratégias de gestão de resíduos: {evento['estrategias']}")
        print(f"Gestor: {evento['gestor']}")
        print(f"Participantes: {evento['participantes']}")
        print(f"Lixeiras necessárias: {evento['lixeiras_necessarias']}")
        print(f"Resíduos gerados: {evento['residuos']}")
        print(f"Funcionários de limpeza necessários: {evento['funcionarios_limpeza']}")
        print("-" * 30)

# Função para excluir um evento pelo nome
def excluir_evento(nome_evento):
    for evento in eventos:
        if evento['nome'] == nome_evento:
            eventos.remove(evento)
            print(f"Evento '{nome_evento}' excluído com sucesso!")
            break
    else:
        print(f"Evento '{nome_evento}' não encontrado.")

# Função para alterar dados de um evento
def alterar_evento(nome_evento, novo_local, nova_data):
    for evento in eventos:
        if evento['nome'] == nome_evento:
            evento['local'] = novo_local
            evento['data'] = nova_data
            print(f"Evento '{nome_evento}' atualizado com sucesso!")
            break
    else:
        print(f"Evento '{nome_evento}' não encontrado.")

while True:
    print("\nMenu:")
    print("1. Adicionar evento")
    print("2. Exibir eventos")
    print("3. Excluir evento")
    print("4. Alterar evento")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome do evento: ")
        local = input("Local do evento: ")
        data = input("Data do evento: ")
        estrategias =  [
    'Coleta seletiva',
    'Parceria com empresa de reciclagem',
    'Campanha de conscientização'
]
        gestor = input("Nome do gestor: ")
        participantes = int(input("Número de participantes: "))
        adicionar_evento(nome, local, data, estrategias, gestor, participantes)
        print("Evento adicionado com sucesso!")

    elif opcao == '2':
        exibir_eventos()

    elif opcao == '3':
        nome_evento = input("Nome do evento a ser excluído: ")
        excluir_evento(nome_evento)

    elif opcao == '4':
        nome_evento = input("Nome do evento a ser alterado: ")
        novo_local = input("Novo local do evento: ")
        nova_data = input("Nova data do evento: ")
        alterar_evento(nome_evento, novo_local, nova_data)

    elif opcao == '5':
        break
