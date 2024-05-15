from Campeonato import Campeonato

class Temporada:
    def __init__(self, ano):
        self.ano = ano
        self.campeonatosValidos = []
        self.campeonatosInvalidos = []    
        self.jogosAvulsosValidos = []
        self.jogosAvulsosInvalidos = []

    def adicionar_campeonatoValido(self, campeonatoValido):
        self.campeonatosValidos.append(campeonatoValido)

    def adicionar_campeonatoInvalido(self, campeonatoInvalido):
        self.campeonatosInvalidos.append(campeonatoInvalido)

    def adicionar_jogosAvulsosValidos(self, jogoAvulsoValido):
        self.jogosAvulsosValidos.append(jogoAvulsoValido)

    def adicionar_jogoAvulsosInvalidos(self, jogoAvulsoInvalido):
        self.jogosAvulsosInvalidos.append(jogoAvulsoInvalido)

    def calcularPontosJogadorTemporada(self, jogador):
        total_pontos = 0
        for campeonato in self.campeonatosValidos:
            total_pontos += campeonato.calcularPontosJogadorCampeonato(jogador)
        for partida in self.jogosAvulsosValidos:
            total_pontos += partida.PontosPorJogadorPartida(jogador)
        return total_pontos

    def calcularBloqueiosJogadorTemporada(self, jogador):
        total_bloqueios = 0
        for campeonato in self.campeonatosValidos:
            total_bloqueios += campeonato.calcularBloqueiosJogadorCampeonato(jogador)
        for partida in self.jogosAvulsosValidos:
            total_bloqueios += partida.BloqueiosPorJogadorPartida(jogador)
        return total_bloqueios

    def calcularLevantamentosJogadorTemporada(self, jogador):
        total_levantamentos = 0
        for campeonato in self.campeonatosValidos:
            total_levantamentos += campeonato.calcularLevantamentosJogadorCampeonato(jogador)
        for partida in self.jogosAvulsosValidos:
            total_levantamentos += partida.LevantamentosPorJogadorPartida(jogador)
        return total_levantamentos

    def calcularRecepcoesJogadorTemporada(self, jogador):
        total_recepcoes = 0
        for campeonato in self.campeonatosValidos:
            total_recepcoes += campeonato.calcularRecepcoesJogadorCampeonato(jogador)
        for partida in self.jogosAvulsosValidos:
            total_recepcoes += partida.RecepcoesPorJogadorPartida(jogador)
        return total_recepcoes


    def contar_rallys_do_jogador(self, jogador):
        total_rallys = 0
        for campeonato in self.campeonatosValidos:
            total_rallys += campeonato.contar_rallys_do_jogador(jogador)
        for partida in self.jogosAvulsosValidos:
            total_rallys += partida.contar_rallys_do_jogador(jogador)
        return total_rallys
    
    def contar_rallys_por_set_do_jogador(self, jogador):
        total_rallys_por_set = 0
        i = 0
        for campeonato in self.campeonatosValidos:
            if campeonato.ClassificacaoTimes != []:
                total_rallys_por_set += campeonato.contar_rallys_por_set_do_jogador(jogador)
                i+=1
        for partida in self.jogosAvulsosValidos:
            if partida.vencedor != None:
                total_rallys_por_set += partida.contar_rallys_por_set_do_jogador(jogador)
                i+=1
        return total_rallys_por_set/i


    def jogadorAverageTemporada(self, jogador):
        total_pontos = self.calcularPontosJogadorTemporada(jogador)
        total_recepcoes = self.calcularRecepcoesJogadorTemporada(jogador)
        total_levantamentos = self.calcularLevantamentosJogadorTemporada(jogador)
        total_bloqueios = self.calcularBloqueiosJogadorTemporada(jogador)
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

    def timeAverageTemporada(self, time):
        total_average = 0
        total_jogadores = len(time.elenco_atual)

        if total_jogadores == 0:
            return 0  # Retorna 0 se o time não tiver jogadores no elenco atual

        for jogador in time.elenco_atual:
            total_average += self.jogadorAverageTemporada(jogador)

        return total_average / total_jogadores