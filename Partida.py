from Set import Set
import copy

class Partida:
    def __init__(self, time1, time2, modalidade, sets=None, SetsTime1=0, SetsTime2=0, vencedor=None, perdedor=None):
        self.time1 = time1
        self.time2 = time2
        self.modalidade = modalidade
        self.sets = sets if sets is not None else []
        self.SetsTime1 = SetsTime1
        self.SetsTime2 = SetsTime2
        self.vencedor = vencedor
        self.perdedor = perdedor

    def adicionar_set(self, set_obj):
        obj_copy = copy.deepcopy(set_obj)
        self.sets.append(obj_copy)

    def SetPorSet(self, mediasTime1, mediasTime2):
        # Verifica se a partida já foi concluída antes de iniciar um novo set
        if self.vencedor is not None:
            print(f"A partida já foi concluída! O vencedor é: {self.vencedor.nome}")
            return

        while True:
            set_obj = Set()
            escolha_randomizar = input("Deseja randomizar o set? ('s' ou 'n') ")
            if escolha_randomizar == 's':
                set_obj.RallyPorRallyRandomizado(self.time1, self.time2, mediasTime1, mediasTime2, self.modalidade)
            else:
                set_obj.RallyPorRally(self.time1, self.time2, mediasTime1, mediasTime2, self.modalidade)
            if set_obj.vencedor_set == self.time1:
                self.SetsTime1 += 1
            elif set_obj.vencedor_set == self.time2:
                self.SetsTime2 += 1

            print(f"\nSets - {self.time1.nome}: {self.SetsTime1} | {self.time2.nome}: {self.SetsTime2}")

            self.adicionar_set(set_obj)

            if max(self.SetsTime1, self.SetsTime2) > (self.modalidade.setsMax/2):
                print(f"\nPartida vencida por {set_obj.vencedor_set.nome}.")
                self.vencedor = set_obj.vencedor_set;
                self.perdedor = self.time1 if set_obj.vencedor_set == self.time2 else self.time2
                break

    def SetPorSetRandomizado(self,mediasTime1,mediasTime2):
        # Verifica se a partida já foi concluída antes de iniciar um novo set
        if self.vencedor is not None:
            print(f"A partida já foi concluída! O vencedor é: {self.vencedor.nome}")
            return

        while True:
            set_obj = Set()
            set_obj.RallyPorRallyRandomizado(self.time1, self.time2, mediasTime1, mediasTime2, self.modalidade)

            if set_obj.vencedor_set == self.time1:
                self.SetsTime1 += 1
            elif set_obj.vencedor_set == self.time2:
                self.SetsTime2 += 1

            print(f"\nSets - {self.time1.nome}: {self.SetsTime1} | {self.time2.nome}: {self.SetsTime2}")

            self.adicionar_set(set_obj)

            if max(self.SetsTime1, self.SetsTime2) > (self.modalidade.setsMax/2):
                print(f"\nPartida vencida por {set_obj.vencedor_set.nome}.")
                self.vencedor = set_obj.vencedor_set;
                self.perdedor = self.time1 if set_obj.vencedor_set == self.time2 else self.time2
                break

    def PontosPorJogadorPartida(self, jogador):
        pontos_jogador = 0
        for set_obj in self.sets:
            pontos_jogador += set_obj.PontosPorJogadorSet(jogador)
        return pontos_jogador

    def BloqueiosPorJogadorPartida(self, jogador):
        bloqueios_jogador = 0
        for set_obj in self.sets:
            bloqueios_jogador += set_obj.BloqueiosPorJogadorSet(jogador)
        return bloqueios_jogador

    def LevantamentosPorJogadorPartida(self, jogador):
        levantamentos_jogador = 0
        for set_obj in self.sets:
            levantamentos_jogador += set_obj.LevantamentosPorJogadorSet(jogador)
        return levantamentos_jogador

    def RecepcoesPorJogadorPartida(self, jogador):
        recepcoes_jogador = 0
        for set_obj in self.sets:
            recepcoes_jogador += set_obj.RecepcoesPorJogadorSet(jogador)
        return recepcoes_jogador
    
    def contar_rallys_do_jogador(self, jogador):
        total_rallys = 0
        for set_obj in self.sets:
            total_rallys += set_obj.contar_rallys_em_quadra(jogador)
        return total_rallys

    def contar_rallys_por_set_do_jogador(self, jogador):
        total_rallys_por_set = self.contar_rallys_do_jogador(jogador)/len(self.sets)
        return total_rallys_por_set

    def jogadorAveragePartida(self, jogador):
        total_pontos = self.PontosPorJogadorPartida(jogador)
        total_recepcoes = self.RecepcoesPorJogadorPartida(jogador)
        total_levantamentos = self.LevantamentosPorJogadorPartida(jogador)
        total_bloqueios = self.BloqueiosPorJogadorPartida(jogador)
        total_rallys_jogados = self.contar_rallys_do_jogador(jogador)

        posicao = jogador.posicao.lower()

        if(total_rallys_jogados == 0):
            average = 0
        elif posicao == "oposto":
            average = ((total_pontos * 4) + total_recepcoes + total_levantamentos + (total_bloqueios * 2)) / (8 * total_rallys_jogados)
        elif posicao == "levantador":
            average = ((total_pontos * 2) + total_recepcoes + (total_levantamentos * 4) + total_bloqueios) / (8 * total_rallys_jogados)
        elif posicao == "líbero":
            average = (total_recepcoes * 6 + total_levantamentos * 2) / (8 * total_rallys_jogados)
        elif posicao == "central":
            average = ((total_pontos * 2) + total_recepcoes + total_levantamentos + (total_bloqueios * 4)) / (8 * total_rallys_jogados)
        elif posicao == "ponteiro":
            average = ((total_pontos * 3) + (total_recepcoes * 2) + total_levantamentos + (total_bloqueios * 2)) / (8 * total_rallys_jogados)
        else:
            print("Posição do jogador não reconhecida.")
            return None

        return average
    
    def timeAveragePartida(self, time):
        total_average = 0
        total_jogadores = len(time.elenco_atual)

        if total_jogadores == 0:
            return 0  # Retorna 0 se o time não tiver jogadores no elenco atual

        for jogador in time.elenco_atual:
            total_average += self.jogadorAveragePartida(jogador)

        return total_average / total_jogadores