import pygame
import random

from jogador import Jogador
from inimigo import Inimigo
from cores import *
from configuracoes import *


def menu():
    global rodando, estado
    while estado == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    estado = "jogar"

        tela.fill(BRANCO)
        font = pygame.font.SysFont(None, 50)
        texto = font.render("Pressione ESPAÇO para jogar", True, AZUL)
        tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, ALTURA // 2))
        pygame.display.flip()
        relogio.tick(60)


def jogar():
    global rodando, score, estado
    jogador = Jogador()
    todos_sprites = pygame.sprite.Group()
    todos_sprites.add(jogador)
    inimigos = pygame.sprite.Group()

    while estado == "jogar":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        todos_sprites.update()
        inimigos.update()

        # Gerar inimigos aleatoriamente
        if random.randrange(100) < 3:  # 3% de chance por frame
            inimigo = Inimigo()
            todos_sprites.add(inimigo)
            inimigos.add(inimigo)

        # Checar colisões
        hits = pygame.sprite.spritecollide(jogador, inimigos, False)
        if hits:
            estado = "menu"  # Voltar para o menu após a morte

        tela.fill(BRANCO)
        pygame.draw.rect(tela, CINZA, [0, ALTURA // 4 - 20, LARGURA, 40])  # Plataforma superior
        pygame.draw.rect(tela, CINZA, [0, 3 * ALTURA // 4 - 20, LARGURA, 40])  # Plataforma inferior
        todos_sprites.draw(tela)

        font = pygame.font.SysFont(None, 35)
        text = font.render("Score: " + str(jogador.score.point), True, AZUL)
        tela.blit(text, (10, 10))

        pygame.display.flip()

        relogio.tick(60)

# Variáveis de estado
estado = "menu"
rodando = True
score = 0

# Loop principal
while rodando:
    if estado == "menu":
        menu()
    elif estado == "jogar":
        jogar()

pygame.quit()
