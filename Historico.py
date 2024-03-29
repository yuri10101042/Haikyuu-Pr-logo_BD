import pickle
from Temporada import Temporada

class Historico:
    def __init__(self):
        self.Temporadas = []
        self.Jogadores = []
        self.Times = []
        self.Modalidades = []

    def adicionar_temporada(self, temporada):
        self.Temporadas.append(temporada)

    def exportar_informacoes(self,nomeArq):
        nome_arquivo = nomeArq
        with open(nome_arquivo, 'wb') as arquivo:
            pickle.dump(self, arquivo)

    def importar_informacoes(self):
        nome_arquivo = "BaseDeDados_Principal.bin"
        with open(nome_arquivo, 'rb') as arquivo:
            historico = pickle.load(arquivo)
            return historico
    
    def encontrar_jogador_por_nome(self, nome_jogador):
        for jogador in self.Jogadores:
            if jogador.nome.lower() == nome_jogador.lower():
                return jogador
        return None

    def encontrar_time_por_nome(self, nome_time):
        for time in self.Times:
            if time.nome.lower() == nome_time.lower():
                return time
        return None
    
        jogadores = []
        for temporada in self.temporadas:
            for campeonato in temporada.campeonatos:
                for time in campeonato.times:
                    for jogador in time.elenco_atual:
                        if jogador.posicao.lower() == posicao.lower():
                            jogadores.append(jogador)
        return jogadores

    def calcularPontosJogadorHistorico(self, jogador):
        total_pontos = 0
        for temporada in self.Temporadas:
            total_pontos += temporada.calcularPontosJogadorTemporada(jogador)
        return total_pontos

    def calcularBloqueiosJogadorHistorico(self, jogador):
        total_bloqueios = 0
        for temporada in self.Temporadas:
            total_bloqueios += temporada.calcularBloqueiosJogadorTemporada(jogador)
        return total_bloqueios

    def calcularLevantamentosJogadorHistorico(self, jogador):
        total_levantamentos = 0
        for temporada in self.Temporadas:
            total_levantamentos += temporada.calcularLevantamentosJogadorTemporada(jogador)
        return total_levantamentos

    def calcularRecepcoesJogadorHistorico(self, jogador):
        total_recepcoes = 0
        for temporada in self.Temporadas:
            total_recepcoes += temporada.calcularRecepcoesJogadorTemporada(jogador)
        return total_recepcoes

    def contar_rallys_do_jogador(self, jogador):
        total_rallys = 0
        for temporada in self.Temporadas:
            total_rallys += temporada.contar_rallys_do_jogador(jogador)
        return total_rallys
    
    def jogadorAverageHistorico(self, jogador):
        total_pontos = self.calcularPontosJogadorHistorico(jogador)
        total_recepcoes = self.calcularRecepcoesJogadorHistorico(jogador)
        total_levantamentos = self.calcularLevantamentosJogadorHistorico(jogador)
        total_bloqueios = self.calcularBloqueiosJogadorHistorico(jogador)
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
    
    def timeAverageHistorico(self, time):
        total_average = 0
        total_jogadores = len(time.elenco_atual)

        if total_jogadores == 0:
            return 0  # Retorna 0 se o time não tiver jogadores no elenco atual

        for jogador in time.elenco_atual:
            total_average += self.jogadorAverageHistorico(jogador)

        return total_average / total_jogadores