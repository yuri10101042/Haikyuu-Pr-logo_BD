from Fase import Fase
from Partida import Partida
import math

class Campeonato:
    def __init__(self, nome,modalidade, TimesParticipantes, fases=None, ClassificacaoTimes=None):
        self.nome = nome
        self.modalidade = modalidade
        self.TimesParticipantes = TimesParticipantes  # Vetor de times que participarão do campeonato
        self.fases = fases if fases is not None else []
        self.ClassificacaoTimes = ClassificacaoTimes if ClassificacaoTimes is not None else []
        self.TotalFases = math.log2(len(TimesParticipantes))

    def criarProximaFase(self):
        if not self.fases:  # Se for a primeira fase, use os times participantes
            nova_fase = Fase(1,self.modalidade)
            nova_fase.criarPartidas(self.TimesParticipantes)
        elif self.fases[-1].todasPartidasConcluidas():
            self.fases[-1].TimesClassificados = [partida.vencedor for partida in self.fases[-1].partidas]
            nova_fase = Fase(len(self.fases) + 1,self.modalidade)
            nova_fase.criarPartidas(self.fases[-1].TimesClassificados)
            if(nova_fase.numero > self.TotalFases):
                    print("Esse campeonato já foi concluído.")
                    return
            if(nova_fase.numero == self.TotalFases):
                timeA= self.fases[-1].partidas[0].perdedor
                timeB= self.fases[-1].partidas[1].perdedor
                partida = Partida(timeA,timeB,self.modalidade)
                nova_fase.partidas.append(partida)
            else:
                nova_fase = Fase(len(self.fases) + 1,self.modalidade)
                nova_fase.criarPartidas(self.fases[-1].TimesClassificados)               
        else:
            print("A fase anterior ainda não foi concluída. Não é possível criar a próxima fase.")
            return

        self.fases.append(nova_fase)

    def JogarCampeonato(self):
        for fase in self.fases:
            if not fase.todasPartidasConcluidas():
                print(f"\nFase {fase.numero} - Partidas:")
                for i, partida in enumerate([partida for partida in fase.partidas if partida.vencedor is None], start=1):
                    print(f"{i}. {partida.time1.nome} vs. {partida.time2.nome}")

                escolha_partida = input("Escolha o número da partida que deseja jogar (ou 's' para sair): ")

                if escolha_partida.lower() == 's':
                    return
                elif escolha_partida.isdigit() and 1 <= int(escolha_partida) <= len([partida for partida in fase.partidas if partida.vencedor is None]):
                    partida_escolhida = [partida for partida in fase.partidas if partida.vencedor is None][int(escolha_partida) - 1]
                    partida_escolhida.SetPorSet()  # Certifique-se de ter uma instância de modalidade definida
                    if fase.numero == self.TotalFases and fase.todasPartidasConcluidas():
                        self.ClassificacaoTimes.append(fase.partidas[0].vencedor.nome)
                        self.ClassificacaoTimes.append(fase.partidas[0].perdedor.nome)
                        self.ClassificacaoTimes.append(fase.partidas[1].vencedor.nome)
                    return
                else:
                    print("Escolha inválida. Tente novamente.")
        print("Não existem Fases com jogos inacabados.")

    def JogarCampeonatoRandomizada(self, mediasTimes):
        for fase in self.fases:
            if not fase.todasPartidasConcluidas():
                print(f"\nFase {fase.numero} - Partidas:")
                for partida in [partida for partida in fase.partidas if partida.vencedor is None]:
                    time1, time2 = partida.time1, partida.time2
                    time1_medias = next((medias for medias in mediasTimes if medias[0] == time1), None)
                    time2_medias = next((medias for medias in mediasTimes if medias[0] == time2), None)
                    if time1_medias and time2_medias:
                        partida.SetPorSetRandomizada(time1_medias[1:], time2_medias[1:])
                        if fase.numero == self.TotalFases and fase.todasPartidasConcluidas():
                            self.ClassificacaoTimes.append(fase.partidas[0].vencedor.nome)
                            self.ClassificacaoTimes.append(fase.partidas[0].perdedor.nome)
                            self.ClassificacaoTimes.append(fase.partidas[1].vencedor.nome)
        print("Não existem Fases com jogos inacabados.")
        
        for fase in self.fases:
            if not fase.todasPartidasConcluidas():
                print(f"\nFase {fase.numero} - Partidas:")
                for partida in [partida for partida in fase.partidas if partida.vencedor is None]:
                    partida.SetPorSetRandomizada(time1_medias, time2_medias)
                    if fase.numero == self.TotalFases and fase.todasPartidasConcluidas():
                        self.ClassificacaoTimes.append(fase.partidas[0].vencedor.nome)
                        self.ClassificacaoTimes.append(fase.partidas[0].perdedor.nome)
                        self.ClassificacaoTimes.append(fase.partidas[1].vencedor.nome)
        print("Não existem Fases com jogos inacabados.")

    def calcularPontosJogadorCampeonato(self, jogador):
        pontos = 0
        print("teste")
        for fase in self.fases:
            pontos += fase.calcularPontosJogadorFase(jogador)
        return pontos

    def calcularBloqueiosJogadorCampeonato(self, jogador):
        bloqueios = 0
        for fase in self.fases:
            bloqueios += fase.calcularBloqueiosJogadorFase(jogador)
        return bloqueios

    def calcularLevantamentosJogadorCampeonato(self, jogador):
        levantamentos = 0
        for fase in self.fases:
            levantamentos += fase.calcularLevantamentosJogadorFase(jogador)
        return levantamentos

    def calcularRecepcoesJogadorCampeonato(self, jogador):
        recepcoes = 0
        for fase in self.fases:
            recepcoes += fase.calcularRecepcoesJogadorFase(jogador)
        return recepcoes
    
    def contar_rallys_do_jogador(self, jogador):
        total_rallys = 0
        for fase in self.fases:
            total_rallys += fase.contar_rallys_do_jogador(jogador)
        return total_rallys

    def jogadorAverageCampeonato(self, jogador):
        total_pontos = self.calcularPontosJogadorCampeonato(jogador)
        total_recepcoes = self.calcularRecepcoesJogadorCampeonato(jogador)
        total_levantamentos = self.calcularLevantamentosJogadorCampeonato(jogador)
        total_bloqueios = self.calcularBloqueiosJogadorCampeonato(jogador)
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
    
    def timeAverageCampeonato(self, time):
        total_average = 0
        total_jogadores = len(time.elenco_atual)

        if total_jogadores == 0:
            return 0  # Retorna 0 se o time não tiver jogadores no elenco atual

        for jogador in time.elenco_atual:
            total_average += self.jogadorAverageCampeonato(jogador)

        return total_average / total_jogadores