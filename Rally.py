import random

class Rally:
    def __init__(self, ponto=False, bloqueios=None, recepcoes=None, levantamentos=None, vencedor_rally=None, EmQuadra=None):
        self.ponto = ponto
        self.bloqueios = bloqueios if bloqueios is not None else []
        self.recepcoes = recepcoes if recepcoes is not None else []
        self.levantamentos = levantamentos if levantamentos is not None else []
        self.vencedor_rally = vencedor_rally
        self.EmQuadra = EmQuadra if EmQuadra is not None else []

    def adicionar_bloqueio(self, jogador):
        self.bloqueios.append(jogador)

    def adicionar_recepcao(self, jogador):
        self.recepcoes.append(jogador)

    def adicionar_levantamento(self, jogador):
        self.levantamentos.append(jogador)

    def JogarRally(self, time1, time2, EmQuadra1, EmQuadra2):
        times = [time1, time2]

        for jogador in EmQuadra1:
            self.EmQuadra.append(jogador)
        
        for jogador in EmQuadra2:
            self.EmQuadra.append(jogador)

        while True:
            print("Escolha a ação:")
            print("1. Ponto")
            print("2. Bloqueio")
            print("3. Levantamento")
            print("4. Recepção")

            escolha = input("Digite o número da opção desejada: ")

            if escolha not in ["1", "2", "3", "4"]:
                print("Opção não válida. Tente novamente.")
                continue

            if escolha == "1":
                print("Em qual time foi o ponto?")
                for i, time in enumerate(times):
                    print(f"{i + 1}. {time.nome}")

                numero_time = input("Digite o número do time: ")

                if not numero_time.isdigit() or int(numero_time) not in range(1, len(times) + 1):
                    print("Opção não válida. Tente novamente.")
                    continue

                elenco_atual = EmQuadra1 if int(numero_time) == 1 else EmQuadra2

                print("Que jogador fez o ponto?")
                for i, jogador in enumerate(elenco_atual):
                    print(f"{i + 1}. {jogador.nome}")
                print(f"{len(elenco_atual) + 1}. Erro do Time Adversário")

                numero_jogador = input("Digite o número do jogador: ")

                if not numero_jogador.isdigit() or int(numero_jogador) not in range(1, len(elenco_atual) + 2):
                    print("Opção não válida. Tente novamente.")
                    continue

                if int(numero_jogador) == len(elenco_atual) + 1:  # Verifica se é "Erro do Time Adversário"
                    self.vencedor_rally = times[int(numero_time) - 1].nome  # Define o time que está pontuando como vencedor
                    self.ponto = False  # Define o ponto como False
                    break

                self.ponto = elenco_atual[int(numero_jogador) - 1].nome
                self.vencedor_rally = times[int(numero_time) - 1].nome
                break

            elif escolha == "2":
                print("Em qual time foi o bloqueio?")
                for i, time in enumerate(times):
                    print(f"{i + 1}. {time.nome}")

                numero_time = input("Digite o número do time: ")

                if not numero_time.isdigit() or int(numero_time) not in range(1, len(times) + 1):
                    print("Opção não válida. Tente novamente.")
                    continue

                elenco_atual = EmQuadra1 if int(numero_time) == 1 else EmQuadra2

                print("Que jogador fez o bloqueio?")
                for i, jogador in enumerate(elenco_atual):
                    print(f"{i + 1}. {jogador.nome}")

                numero_jogador = input("Digite o número do jogador: ")

                if not numero_jogador.isdigit() or int(numero_jogador) not in range(1, len(elenco_atual) + 1):
                    print("Opção não válida. Tente novamente.")
                    continue

                self.adicionar_bloqueio(elenco_atual[int(numero_jogador) - 1].nome)
                continue

            elif escolha == "3":
                print("Em qual time foi o levantamento?")
                for i, time in enumerate(times):
                    print(f"{i + 1}. {time.nome}")

                numero_time = input("Digite o número do time: ")

                if not numero_time.isdigit() or int(numero_time) not in range(1, len(times) + 1):
                    print("Opção não válida. Tente novamente.")
                    continue

                elenco_atual = EmQuadra1 if int(numero_time) == 1 else EmQuadra2

                print("Que jogador fez o levantamento?")
                for i, jogador in enumerate(elenco_atual):
                    print(f"{i + 1}. {jogador.nome}")

                numero_jogador = input("Digite o número do jogador: ")

                if not numero_jogador.isdigit() or int(numero_jogador) not in range(1, len(elenco_atual) + 1):
                    print("Opção não válida. Tente novamente.")
                    continue

                self.adicionar_levantamento(elenco_atual[int(numero_jogador) - 1].nome)
                continue

            elif escolha == "4":
                print("Em qual time foi a recepção?")
                for i, time in enumerate(times):
                    print(f"{i + 1}. {time.nome}")

                numero_time = input("Digite o número do time: ")

                if not numero_time.isdigit() or int(numero_time) not in range(1, len(times) + 1):
                    print("Opção não válida. Tente novamente.")
                    continue

                elenco_atual = EmQuadra1 if int(numero_time) == 1 else EmQuadra2

                print("Que jogador fez a recepção?")
                for i, jogador in enumerate(elenco_atual):
                    print(f"{i + 1}. {jogador.nome}")

                numero_jogador = input("Digite o número do jogador: ")

                if not numero_jogador.isdigit() or int(numero_jogador) not in range(1, len(elenco_atual) + 1):
                    print("Opção não válida. Tente novamente.")
                    continue

                self.adicionar_recepcao(elenco_atual[int(numero_jogador) - 1].nome)
                continue

    def JogarRallyRandomizado(self, time1, time2, EmQuadra1, EmQuadra2, mediasEmQuadra1, mediasEmQuadra2):
        times = [time1, time2]

        for jogador in EmQuadra1:
            self.EmQuadra.append(jogador)
        
        for jogador in EmQuadra2:
            self.EmQuadra.append(jogador)

        # 1- Verifica quantos levantamentos, bloqueios e recepções cada jogador realiza com base nas médias
        levantamentos_time1 = [max(int(random.gauss(media[1], 1)), 0) for media in mediasEmQuadra1]  # Variação de ±0.5 no desvio padrão
        bloqueios_time1 = [max(int(random.gauss(media[2], 1)), 0) for media in mediasEmQuadra1]
        recepcoes_time1 = [max(int(random.gauss(media[3], 1)), 0) for media in mediasEmQuadra1]

        levantamentos_time2 = [max(int(random.gauss(media[1], 1)), 0) for media in mediasEmQuadra2]
        bloqueios_time2 = [max(int(random.gauss(media[2], 1)), 0) for media in mediasEmQuadra2]
        recepcoes_time2 = [max(int(random.gauss(media[3], 1)), 0) for media in mediasEmQuadra2]

        for jogador in EmQuadra1:
            if jogador.posicao == "Libero":
                bloqueios_time1[EmQuadra1.index(jogador)] = 0
            for _ in range(levantamentos_time1[EmQuadra1.index(jogador)]):
                self.adicionar_levantamento(jogador.nome)
            for _ in range(bloqueios_time1[EmQuadra1.index(jogador)]):
                self.adicionar_bloqueio(jogador.nome)
            for _ in range(recepcoes_time1[EmQuadra1.index(jogador)]):
                self.adicionar_recepcao(jogador.nome)

        for jogador in EmQuadra2:
            if jogador.posicao == "Libero":
                bloqueios_time2[EmQuadra2.index(jogador)] = 0
            for _ in range(levantamentos_time2[EmQuadra2.index(jogador)]):
                self.adicionar_levantamento(jogador.nome)
            for _ in range(bloqueios_time2[EmQuadra2.index(jogador)]):
                self.adicionar_bloqueio(jogador.nome)
            for _ in range(recepcoes_time2[EmQuadra2.index(jogador)]):
                self.adicionar_recepcao(jogador.nome)


        # 2- Calcula a média de levantamentos, bloqueios e recepções realizadas por cada time
        media_levantamentos_time1 = sum(levantamentos_time1) / len(levantamentos_time1)
        media_bloqueios_time1 = sum(bloqueios_time1) / len(bloqueios_time1)
        media_recepcoes_time1 = sum(recepcoes_time1) / len(recepcoes_time1)

        media_levantamentos_time2 = sum(levantamentos_time2) / len(levantamentos_time2)
        media_bloqueios_time2 = sum(bloqueios_time2) / len(bloqueios_time2)
        media_recepcoes_time2 = sum(recepcoes_time2) / len(recepcoes_time2)

        # 3- Calcula a média das médias de pontos dos jogadores de cada time
        media_pontos_jogadores_time1 = sum([media[0] for media in mediasEmQuadra1]) / len(mediasEmQuadra1)
        media_pontos_jogadores_time2 = sum([media[0] for media in mediasEmQuadra2]) / len(mediasEmQuadra2)

        # 4- Calcula o score de cada time considerando os levantamentos, bloqueios, recepções e médias de pontos com desvio padrão de 0.1
        score_time1 = max((media_levantamentos_time1 + media_bloqueios_time1 + media_recepcoes_time1 + media_pontos_jogadores_time1 + random.gauss(0, 0.1)), 0)
        score_time2 = max((media_levantamentos_time2 + media_bloqueios_time2 + media_recepcoes_time2 + media_pontos_jogadores_time2 + random.gauss(0, 0.1)), 0)

        probabilidade_time1 = score_time1 / (score_time1 + score_time2)
        probabilidade_time2 = 1 - probabilidade_time1

        # 5- Determina o vencedor do rally com base nas probabilidades
        vencedor_rally = random.choices([time1, time2], weights=[probabilidade_time1, probabilidade_time2])[0]
        self.vencedor_rally = vencedor_rally.nome

# 6- Utiliza as médias de pontuação de cada jogador do time vencedor para decidir quem realizou o ponto
        if vencedor_rally in [time1, time2]:
            medias_time_vencedor = mediasEmQuadra1 if vencedor_rally == time1.nome else mediasEmQuadra2
            pontos_jogadores_time_vencedor = [max(random.gauss(media[0], 0.1), 0.00000001) for media in medias_time_vencedor]  # Variação de ±0.1 na média de pontos

            while True:
                if random.random() < 0.1:  # Pequena probabilidade de ser erro do adversário
                    self.ponto = False
                    break
                pontuador = random.choices(EmQuadra1 if vencedor_rally == time1.nome else EmQuadra2, weights=pontos_jogadores_time_vencedor)[0]
                if pontuador.posicao == "Libero":
                    continue
                self.ponto = pontuador.nome
                break
        else:
            self.ponto = False

        print(f"O vencedor do rally é: {self.vencedor_rally}")
        if self.ponto != False:
            print(f"O jogador que realizou o ponto foi: {self.ponto}")
        else:
            print("O ponto foi erro do adversário.")
        print(f"Levantamentos realizados: {', '.join(self.levantamentos)}")
        print(f"Bloqueios realizados: {', '.join(self.bloqueios)}")
        print(f"Recepções realizadas: {', '.join(self.recepcoes)}")

