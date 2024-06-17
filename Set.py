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

    def RallyPorRally(self, time1, time2, mediasTime1, mediasTime2, modalidade):
        time1_em_quadra = []  # Lista para armazenar os jogadores de time1 em quadra
        time2_em_quadra = []  # Lista para armazenar os jogadores de time2 em quadra

        # Escolher jogadores de cada time que iniciarão em quadra
        print(f"Escolha os jogadores de {time1.nome} que iniciarão em quadra (digite 's' para sair):")
        for i, jogador in enumerate(time1.elenco_atual, start=1):
            print(f"{i}. {jogador.nome} - {jogador.posicao}")
        while len(time1_em_quadra) < modalidade.quantidade_jogadores_em_quadra:
            escolha = input("Digite o número do jogador:")
            if escolha.isdigit() and 1 <= int(escolha) <= len(time1.elenco_atual):
                jogador = time1.elenco_atual[int(escolha) - 1]
                if jogador in time1_em_quadra:
                    print("Jogador já selecionado. Tente novamente.")
                else:
                    time1_em_quadra.append(jogador)
            else:
                print("Opção inválida. Tente novamente.")

        print(f"Escolha os jogadores de {time2.nome} que iniciarão em quadra (digite 's' para sair):")
        for i, jogador in enumerate(time2.elenco_atual, start=1):
            print(f"{i}. {jogador.nome} - {jogador.posicao}")
        while len(time2_em_quadra) < modalidade.quantidade_jogadores_em_quadra:
            escolha = input("Digite o número do jogador: ")
            if escolha.isdigit() and 1 <= int(escolha) <= len(time2.elenco_atual):
                jogador = time2.elenco_atual[int(escolha) - 1]
                if jogador in time2_em_quadra:
                    print("Jogador já selecionado. Tente novamente.")
                else:
                    time2_em_quadra.append(jogador)
            else:
                print("Opção inválida. Tente novamente.")

        while True:
            indices_time1_em_quadra = [time1.elenco_atual.index(item) for item in time1_em_quadra]
            indices_time2_em_quadra = [time2.elenco_atual.index(item) for item in time2_em_quadra]

            mediasEmQuadra1 = [mediasTime1[i] for i in indices_time1_em_quadra]
            mediasEmQuadra2 = [mediasTime2[i] for i in indices_time2_em_quadra]

            rally = Rally()
            escolha_randomizar = input("Deseja randomizar o rally? ('s' ou 'n') ")
            if escolha_randomizar == 's':
                rally.JogarRallyRandomizado(time1, time2, time1_em_quadra , time2_em_quadra, mediasEmQuadra1, mediasEmQuadra2)
            else:
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
                    while True:
                        print(f"Jogadores em quadra de {time1.nome}: {', '.join(jogador.nome for jogador in time1_em_quadra)}")
                        jogadores_nao_em_quadra = [jogador for jogador in time1.elenco_atual if jogador not in time1_em_quadra]
                        print(f"Jogadores disponíveis de {time1.nome} para substituição:")
                        for i, jogador in enumerate(jogadores_nao_em_quadra, start=1):
                            print(f"{i}. {jogador.nome} - {jogador.posicao}")
                        numero_jogador_sai = int(input("Digite o número do jogador que sairá (ou '0' para sair): "))
                        if(numero_jogador_sai == 0):
                            break
                        numero_jogador_entra = int(input("Digite o número do jogador que entrará (ou '0' para sair): "))
                        if(numero_jogador_entra == 0):
                            break
                        if 1 <= numero_jogador_sai <= len(time1_em_quadra) and 1 <= numero_jogador_entra <= len(jogadores_nao_em_quadra):
                            jogador_sai = time1_em_quadra[numero_jogador_sai - 1]
                            jogador_entra = jogadores_nao_em_quadra[numero_jogador_entra - 1]
                            time1_em_quadra.remove(jogador_sai)
                            time1_em_quadra.append(jogador_entra)
                        else:
                            print("Opção inválida. Tente novamente.")
                    while True:
                        print(f"Jogadores em quadra de {time2.nome}: {', '.join(jogador.nome for jogador in time2_em_quadra)}")
                        jogadores_nao_em_quadra = [jogador for jogador in time2.elenco_atual if jogador not in time2_em_quadra]
                        print(f"Jogadores disponíveis de {time2.nome} para substituição:")
                        for i, jogador in enumerate(jogadores_nao_em_quadra, start=1):
                            print(f"{i}. {jogador.nome} - {jogador.posicao}")
                        numero_jogador_sai = int(input("Digite o número do jogador que sairá (ou '0' para sair): "))
                        if(numero_jogador_sai == 0):
                            break
                        numero_jogador_entra = int(input("Digite o número do jogador que entrará (ou '0' para sair): "))
                        if(numero_jogador_entra == 0):
                            break
                        if 1 <= numero_jogador_sai <= len(time2_em_quadra) and 1 <= numero_jogador_entra <= len(jogadores_nao_em_quadra):
                            jogador_sai = time2_em_quadra[numero_jogador_sai - 1]
                            jogador_entra = jogadores_nao_em_quadra[numero_jogador_entra - 1]
                            time2_em_quadra.remove(jogador_sai)
                            time2_em_quadra.append(jogador_entra)
                        else:
                            print("Opção inválida. Tente novamente.")
                    break
                elif substituir.upper() == "N":
                    break
                else:
                    print("Opção inválida. Tente novamente.")


    def RallyPorRallyRandomizado(self, time1, time2, mediasTime1, mediasTime2, modalidade):

        # Escolher jogadores de cada time que iniciarão em quadra

        rallysPorSet_time1 = [max(random.gauss(media[4], 0.1),0.00000001) for media in mediasTime1]
        rallysPorSet_time2 = [max(random.gauss(media[4], 0.1),0.00000001) for media in mediasTime2]  

        time1_em_quadra = []  # Lista para armazenar os jogadores de time1 em quadra
        jogadores_disponiveis_time1 = list(time1.elenco_atual)
        rallysPorSet_time1_temp = list(rallysPorSet_time1)
        
        # Restrição: permitir apenas um jogador com posição de libero em quadra por vez
        libero_em_quadra_time1 = False

        for _ in range(min(modalidade.quantidade_jogadores_em_quadra, len(time1.elenco_atual))):
            while True:
                jogador = random.choices(jogadores_disponiveis_time1, weights=rallysPorSet_time1_temp, k=1)[0]
                if jogador.posicao == 'Libero' and libero_em_quadra_time1:
                    continue
                else:
                    if jogador.posicao == 'Libero':
                        libero_em_quadra_time1 = True
                    time1_em_quadra.append(jogador)
                    del rallysPorSet_time1_temp[jogadores_disponiveis_time1.index(jogador)]
                    jogadores_disponiveis_time1.remove(jogador)
                    break

        time2_em_quadra = []  # Lista para armazenar os jogadores de time2 em quadra
        jogadores_disponiveis_time2 = list(time2.elenco_atual)
        rallysPorSet_time2_temp = list(rallysPorSet_time2)

        # Restrição: permitir apenas um jogador com posição de libero em quadra por vez
        libero_em_quadra_time2 = False

        for _ in range(min(modalidade.quantidade_jogadores_em_quadra, len(time2.elenco_atual))):
            while True:
                jogador = random.choices(jogadores_disponiveis_time2, weights=rallysPorSet_time2_temp, k=1)[0]
                if jogador.posicao == 'Libero' and libero_em_quadra_time2:
                    continue
                else:
                    if jogador.posicao == 'Libero':
                        libero_em_quadra_time2 = True
                    time2_em_quadra.append(jogador)
                    del rallysPorSet_time2_temp[jogadores_disponiveis_time2.index(jogador)]
                    jogadores_disponiveis_time2.remove(jogador)
                    break

        # Escolher jogadores de cada time que iniciarão em quadra
        print(f"Jogadores que iniciarão em quadra de {time1.nome}:")
        for jogador in time1_em_quadra:
            print(f"- {jogador.nome} - {jogador.posicao}")
        print(f"Jogadores que iniciarão em quadra de {time2.nome}:")
        for jogador in time2_em_quadra:
            print(f"- {jogador.nome} - {jogador.posicao}")

        while True:

            indices_time1_em_quadra = [time1.elenco_atual.index(item) for item in time1_em_quadra]
            indices_time2_em_quadra = [time2.elenco_atual.index(item) for item in time2_em_quadra]

            mediasEmQuadra1 = [mediasTime1[i] for i in indices_time1_em_quadra]
            mediasEmQuadra2 = [mediasTime2[i] for i in indices_time2_em_quadra]

            rally = Rally()
            rally.JogarRallyRandomizado(time1, time2, time1_em_quadra , time2_em_quadra, mediasEmQuadra1, mediasEmQuadra2)

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

            time1_em_quadra = []  # Lista para armazenar os jogadores de time1 em quadra
            jogadores_disponiveis_time1 = list(time1.elenco_atual)
            rallysPorSet_time1_temp = list(rallysPorSet_time1)
            
            # Restrição: permitir apenas um jogador com posição de libero em quadra por vez
            libero_em_quadra_time1 = False

            for _ in range(min(6, len(time1.elenco_atual))):
                while True:
                    jogador = random.choices(jogadores_disponiveis_time1, weights=rallysPorSet_time1_temp, k=1)[0]
                    if jogador.posicao == 'Libero' and libero_em_quadra_time1:
                        continue
                    else:
                        if jogador.posicao == 'Libero':
                            libero_em_quadra_time1 = True
                        time1_em_quadra.append(jogador)
                        del rallysPorSet_time1_temp[jogadores_disponiveis_time1.index(jogador)]
                        jogadores_disponiveis_time1.remove(jogador)
                        break

            time2_em_quadra = []  # Lista para armazenar os jogadores de time2 em quadra
            jogadores_disponiveis_time2 = list(time2.elenco_atual)
            rallysPorSet_time2_temp = list(rallysPorSet_time2)

            # Restrição: permitir apenas um jogador com posição de libero em quadra por vez
            libero_em_quadra_time2 = False

            for _ in range(min(6, len(time2.elenco_atual))):
                while True:
                    jogador = random.choices(jogadores_disponiveis_time2, weights=rallysPorSet_time2_temp, k=1)[0]
                    if jogador.posicao == 'Libero' and libero_em_quadra_time2:
                        continue
                    else:
                        if jogador.posicao == 'Libero':
                            libero_em_quadra_time2 = True
                        time2_em_quadra.append(jogador)
                        del rallysPorSet_time2_temp[jogadores_disponiveis_time2.index(jogador)]
                        jogadores_disponiveis_time2.remove(jogador)
                        break

            # Escolher jogadores de cada time que iniciarão em quadra
            print(f"Jogadores que iniciarão em quadra de {time1.nome}:")
            for jogador in time1_em_quadra:
                print(f"- {jogador.nome} - {jogador.posicao}")
            print(f"Jogadores que iniciarão em quadra de {time2.nome}:")
            for jogador in time2_em_quadra:
                print(f"- {jogador.nome} - {jogador.posicao}")


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