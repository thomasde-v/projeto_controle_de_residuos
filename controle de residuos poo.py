class Evento:
    def __init__(self, nome, local, data, estrategias, gestor, participantes):
        self.nome = nome
        self.local = local
        self.data = data
        self.estrategias = estrategias
        self.gestor = gestor
        self.participantes = participantes
        self.residuos = self.calcular_residuos()
        self.lixeiras_necessarias = self.calcular_lixeiras()
        self.funcionarios_limpeza = self.calcular_funcionarios_limpeza()

    def calcular_residuos(self):
        return {
            'Orgânico': self.participantes * 0.3,
            'Reciclável': self.participantes * 0.15,
            'Não Reciclável': self.participantes * 0.05
        }

    def calcular_lixeiras(self):
        capacidade_lixeira = 50
        lixeiras_necessarias = {}
        for tipo, quantidade in self.residuos.items():
            lixeiras_necessarias[tipo] = round(quantidade / capacidade_lixeira)
        return lixeiras_necessarias

    def calcular_funcionarios_limpeza(self):
        return round(self.participantes / 50)

    def exibir_detalhes(self):
        print(f"Nome: {self.nome}")
        print(f"Local: {self.local}")
        print(f"Data: {self.data}")
        print(f"Estratégias de gestão de resíduos: {self.estrategias}")
        print(f"Gestor: {self.gestor}")
        print(f"Participantes: {self.participantes}")
        print(f"Lixeiras necessárias: {self.lixeiras_necessarias}")
        print(f"Resíduos gerados: {self.residuos}")
        print(f"Funcionários de limpeza necessários: {self.funcionarios_limpeza}")
        print("-" * 30)

def excluir_evento(eventos, nome_evento):
    for evento in eventos:
        if evento.nome == nome_evento:
            eventos.remove(evento)
            print(f"Evento '{nome_evento}' excluído com sucesso!")
            break
    else:
        print(f"Evento '{nome_evento}' não encontrado.")

def alterar_evento(eventos, nome_evento, novo_local, nova_data):
    for evento in eventos:
        if evento.nome == nome_evento:
            evento.local = novo_local
            evento.data = nova_data
            print(f"Evento '{nome_evento}' atualizado com sucesso!")
            break
    else:
        print(f"Evento '{nome_evento}' não encontrado.")

eventos = []

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
        estrategias = [
            'Coleta seletiva',
            'Parceria com empresa de reciclagem',
            'Campanha de conscientização'
        ]
        gestor = input("Nome do gestor: ")
        participantes = int(input("Número de participantes: "))
        evento = Evento(nome, local, data, estrategias, gestor, participantes)
        eventos.append(evento)
        print("Evento adicionado com sucesso!")

    elif opcao == '2':
        for evento in eventos:
            evento.exibir_detalhes()

    elif opcao == '3':
        nome_evento = input("Digite o nome do evento a ser excluído: ")
        excluir_evento(eventos, nome_evento)

    elif opcao == '4':
        nome_evento = input("Digite o nome do evento a ser alterado: ")
        novo_local = input("Novo local do evento: ")
        nova_data = input("Nova data do evento: ")
        alterar_evento(eventos, nome_evento, novo_local, nova_data)

    elif opcao == '5':
        break
