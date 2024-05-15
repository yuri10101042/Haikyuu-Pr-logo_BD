from Partida import Partida
import random

class Fase:
    def __init__(self, numero, modalidade, partidas=None, TimesClassificados=None):
        self.numero = numero
        self.modalidade = modalidade
        self.partidas = partidas if partidas is not None else []
        self.TimesClassificados = TimesClassificados if TimesClassificados is not None else []

    def criarPartidas(self, times_classificados_fase_anterior):
        times = times_classificados_fase_anterior
        random.shuffle(times)
        partidas = [Partida(times[i], times[i + 1], self.modalidade) for i in range(0, len(times), 2)]
        self.partidas = partidas

    def todasPartidasConcluidas(self):
        return all(partida.vencedor for partida in self.partidas)

    def calcularPontosJogadorFase(self, jogador):
        pontos = 0
        for partida in self.partidas:
            pontos += partida.PontosPorJogadorPartida(jogador)
        return pontos

    def calcularBloqueiosJogadorFase(self, jogador):
        bloqueios = 0
        for partida in self.partidas:
            bloqueios += partida.BloqueiosPorJogadorPartida(jogador)
        return bloqueios

    def calcularLevantamentosJogadorFase(self, jogador):
        levantamentos = 0
        for partida in self.partidas:
            levantamentos += partida.LevantamentosPorJogadorPartida(jogador)
        return levantamentos

    def calcularRecepcoesJogadorFase(self, jogador):
        recepcoes = 0
        for partida in self.partidas:
            recepcoes += partida.RecepcoesPorJogadorPartida(jogador)
        return recepcoes
    
    def contar_rallys_do_jogador(self, jogador):
        total_rallys = 0
        for partida in self.partidas:
            total_rallys += partida.contar_rallys_do_jogador(jogador)
        return total_rallys
    
    def contar_rallys_por_set_do_jogador(self, jogador):
        total_rallys_por_set = 0
        i = 0
        for partida in self.partidas:
            if partida.vencedor != None:
                total_rallys_por_set += partida.contar_rallys_por_set_do_jogador(jogador)
                ++i
        if i!= 0:
            return total_rallys_por_set/i
        else:
            return 0

    def jogadorAverageFase(self, jogador):
        total_pontos = self.calcularPontosJogadorFase(jogador)
        total_recepcoes = self.calcularRecepcoesJogadorFase(jogador)
        total_levantamentos = self.calcularLevantamentosJogadorFase(jogador)
        total_bloqueios = self.calcularBloqueiosJogadorFase(jogador)
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
    
    def timeAverageFase(self, time):
        total_average = 0
        total_jogadores = len(time.elenco_atual)

        if total_jogadores == 0:
            return 0  # Retorna 0 se o time não tiver jogadores no elenco atual

        for jogador in time.elenco_atual:
            total_average += self.jogadorAverageFase(jogador)

        return total_average / total_jogadores