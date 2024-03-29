from Rally import Rally
import copy
import random

class Set:
    def __init__(self, rallys=None, pontos_time1=0, pontos_time2=0, vencedor_set=None):
        self.rallys = rallys if rallys is not None else []
        self.pontos_time1 = pontos_time1
        self.pontos_time2 = pontos_time2
        self.vencedor_set = vencedor_set

    def adicionar_rally(self, rally):
        obj_copy = copy.deepcopy(rally)
        self.rallys.append(obj_copy)

    def RallyPorRally(self, time1, time2, modalidade):
        time1_em_quadra = []  # Lista para armazenar os jogadores de time1 em quadra
        time2_em_quadra = []  # Lista para armazenar os jogadores de time2 em quadra

        # Escolher jogadores de cada time que iniciarão em quadra
        print(f"Escolha os jogadores de {time1.nome} que iniciarão em quadra (digite 's' para sair):")
        for i, jogador in enumerate(time1.elenco_atual, start=1):
            print(f"{i}. {jogador.nome}")
        while True:
            escolha = input("Digite o número do jogador ou 's' para sair: ")
            if escolha.lower() == 's':
                break
            if escolha.isdigit() and 1 <= int(escolha) <= len(time1.elenco_atual):
                jogador = time1.elenco_atual[int(escolha) - 1]
                time1_em_quadra.append(jogador)
            else:
                print("Opção inválida. Tente novamente.")

        print(f"Escolha os jogadores de {time2.nome} que iniciarão em quadra (digite 's' para sair):")
        for i, jogador in enumerate(time2.elenco_atual, start=1):
            print(f"{i}. {jogador.nome}")
        while True:
            escolha = input("Digite o número do jogador ou 's' para sair: ")
            if escolha.lower() == 's':
                break
            if escolha.isdigit() and 1 <= int(escolha) <= len(time2.elenco_atual):
                jogador = time2.elenco_atual[int(escolha) - 1]
                time2_em_quadra.append(jogador)
            else:
                print("Opção inválida. Tente novamente.")

        while True:
            rally = Rally()
            rally.JogarRally(time1, time2, time1_em_quadra , time2_em_quadra)

            if rally.vencedor_rally == time1.nome:
                self.pontos_time1 += 1
            elif rally.vencedor_rally == time2.nome:
                self.pontos_time2 += 1

            print(f"\nPontos - {time1.nome}: {self.pontos_time1} | {time2.nome}: {self.pontos_time2}")

            self.adicionar_rally(rally)

            if (
                abs(self.pontos_time1 - self.pontos_time2) > 1
                and max(self.pontos_time1, self.pontos_time2) >= modalidade.pontosMaxSet
            ):
                self.vencedor_set = time1 if self.pontos_time1 > self.pontos_time2 else time2
                print(f"Set vencido por {self.vencedor_set.nome}.")
                break

            # Perguntar ao usuário se deseja fazer substituições
            while True:
                substituir = input("Deseja fazer substituições? (S/N): ")
                if substituir.upper() == "S":
                    time_substituir = input("Qual time deseja fazer substituições? (1 para Time 1, 2 para Time 2): ")
                    if time_substituir == "1":
                        print(f"Jogadores em quadra de {time1.nome}: {', '.join(jogador.nome for jogador in time1_em_quadra)}")
                        jogadores_nao_em_quadra = [jogador for jogador in time1.elenco_atual if jogador not in time1_em_quadra]
                        print(f"Jogadores disponíveis de {time1.nome} para substituição:")
                        for i, jogador in enumerate(jogadores_nao_em_quadra, start=1):
                            print(f"{i}. {jogador.nome}")
                        numero_jogador_sai = int(input("Digite o número do jogador que sairá: "))
                        numero_jogador_entra = int(input("Digite o número do jogador que entrará: "))
                        if 1 <= numero_jogador_sai <= len(time1_em_quadra) and 1 <= numero_jogador_entra <= len(jogadores_nao_em_quadra):
                            jogador_sai = time1_em_quadra[numero_jogador_sai - 1]
                            jogador_entra = jogadores_nao_em_quadra[numero_jogador_entra - 1]
                            time1_em_quadra.remove(jogador_sai)
                            time1_em_quadra.append(jogador_entra)
                            break
                        else:
                            print("Opção inválida. Tente novamente.")
                    elif time_substituir == "2":
                        print(f"Jogadores em quadra de {time2.nome}: {', '.join(jogador.nome for jogador in time2_em_quadra)}")
                        jogadores_nao_em_quadra = [jogador for jogador in time2.elenco_atual if jogador not in time2_em_quadra]
                        print(f"Jogadores disponíveis de {time2.nome} para substituição:")
                        for i, jogador in enumerate(jogadores_nao_em_quadra, start=1):
                            print(f"{i}. {jogador.nome}")
                        numero_jogador_sai = int(input("Digite o número do jogador que sairá: "))
                        numero_jogador_entra = int(input("Digite o número do jogador que entrará: "))
                        if 1 <= numero_jogador_sai <= len(time2_em_quadra) and 1 <= numero_jogador_entra <= len(jogadores_nao_em_quadra):
                            jogador_sai = time2_em_quadra[numero_jogador_sai - 1]
                            jogador_entra = jogadores_nao_em_quadra[numero_jogador_entra - 1]
                            time2_em_quadra.remove(jogador_sai)
                            time2_em_quadra.append(jogador_entra)
                            break
                        else:
                            print("Opção inválida. Tente novamente.")
                    else:
                        print("Opção inválida. Tente novamente.")
                elif substituir.upper() == "N":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

    def RallyPorRallyRandomizada(self, time1, time2, modalidade, mediasTime1, mediasTime2):
        time1_em_quadra = []  # Lista para armazenar os jogadores de time1 em quadra
        time2_em_quadra = []  # Lista para armazenar os jogadores de time2 em quadra

        # Escolher jogadores de cada time que iniciarão em quadra com base na média de rallys por set
        for jogador, media_pontos, media_levantamentos, media_bloqueios, _, media_rallys_por_set in mediasTime1:
            if random.random() < media_rallys_por_set * random.uniform(0.8, 1.2):  # Adiciona uma variação de 20%
                time1_em_quadra.append(jogador)
            if len(time1_em_quadra) == 6:
                break

        for jogador, media_pontos, media_levantamentos, media_bloqueios, _, media_rallys_por_set in mediasTime2:
            if random.random() < media_rallys_por_set * random.uniform(0.8, 1.2):  # Adiciona uma variação de 20%
                time2_em_quadra.append(jogador)
            if len(time2_em_quadra) == 6:
                break

        while True:
            rally = Rally()
            rally.JogarRallyRandomizada(time1, time2, time1_em_quadra, time2_em_quadra)

            if rally.vencedor_rally == time1.nome:
                self.pontos_time1 += 1
            elif rally.vencedor_rally == time2.nome:
                self.pontos_time2 += 1

            print(f"\nPontos - {time1.nome}: {self.pontos_time1} | {time2.nome}: {self.pontos_time2}")

            self.adicionar_rally(rally)

            if (
                abs(self.pontos_time1 - self.pontos_time2) > 1
                and max(self.pontos_time1, self.pontos_time2) >= modalidade.pontosMaxSet
            ):
                self.vencedor_set = time1 if self.pontos_time1 > self.pontos_time2 else time2
                print(f"Set vencido por {self.vencedor_set.nome}.")
                break

            # Verifica se deve fazer substituições com base nas médias de rallys em quadra de cada jogador
            for time, em_quadra, medias_time in [(time1, time1_em_quadra, mediasTime1), (time2, time2_em_quadra, mediasTime2)]:
                for jogador in em_quadra:
                    # Calcula a probabilidade de o jogador continuar em quadra
                    probabilidade = medias_time[em_quadra.index(jogador)][5] * random.uniform(0.8, 1.2)
                    if random.random() > probabilidade:  # O jogador sai de quadra
                        jogador_sai = jogador
                        jogadores_disponiveis = [jog for jog in time.elenco_atual if jog not in em_quadra]
                        if jogadores_disponiveis:  # Se houver jogadores disponíveis para substituição
                            jogador_entra = max(jogadores_disponiveis, key=lambda x: medias_time[time.elenco_atual.index(x)][5])
                            em_quadra.remove(jogador_sai)
                            em_quadra.append(jogador_entra)

        # Continua o loop até que os pontos máximos do set sejam alcançados e uma equipe vença

    def PontosPorJogadorSet(self, jogador):
        pontos_jogador = 0
        for rally in self.rallys:
            if rally.ponto != False:
                if rally.ponto == jogador.nome:
                    pontos_jogador += 1
        return pontos_jogador

    def BloqueiosPorJogadorSet(self, jogador):
        bloqueios_jogador = 0
        for rally in self.rallys:
            bloqueios_jogador += rally.bloqueios.count(jogador.nome)
        return bloqueios_jogador

    def LevantamentosPorJogadorSet(self, jogador):
        levantamentos_jogador = 0
        for rally in self.rallys:
            levantamentos_jogador += rally.levantamentos.count(jogador.nome)
        return levantamentos_jogador

    def RecepcoesPorJogadorSet(self, jogador):
        recepcoes_jogador = 0
        for rally in self.rallys:
            recepcoes_jogador += rally.recepcoes.count(jogador.nome)
        return recepcoes_jogador
    
    def contar_rallys_em_quadra(self, jogador):
        total_rallys_em_quadra = 0
        for rally in self.rallys:
            for jogadorIn in rally.EmQuadra:
                if jogadorIn.nome == jogador.nome:
                    total_rallys_em_quadra += 1
                    break
        return total_rallys_em_quadra