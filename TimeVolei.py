from JogadorVolei import JogadorVolei
from Modalidade import Modalidade

class TimeVolei:
    def __init__(self, nome, pais, regiao, cidade, categoria):
        self.nome = nome
        self.pais = pais
        self.regiao = regiao
        self.cidade = cidade
        self.categoria = categoria
        self.elenco_atual = []

    def adicionar_jogador(self, jogador):
        if jogador not in self.elenco_atual:
            self.elenco_atual.append(jogador)

    def remover_jogador(self, jogador):
        """
        Remove um jogador do elenco do time.
        """
        if jogador in self.elenco_atual:
            self.elenco_atual.remove(jogador)