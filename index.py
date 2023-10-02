import pygame
import random

# Inicializar pygame
pygame.init()

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
CINZA = (200, 200, 200)

# Dimensões da tela
info_object = pygame.display.Info()
LARGURA = info_object.current_w
ALTURA = info_object.current_h

# Criação da tela e relógio
tela = pygame.display.set_mode((LARGURA, ALTURA), pygame.FULLSCREEN)
pygame.display.set_caption("SUPER ELETRON")
relogio = pygame.time.Clock()


class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.x = LARGURA // 2
        self.rect.y = ALTURA // 4
        self.change_y = 0
        self.init_change_y = 5
        self.verifyCount = 0

    def update(self):
        keys = pygame.key.get_pressed()

        if self.rect.y == ALTURA // 4 or self.rect.y == 3 * ALTURA // 4:

            if self.verifyCount== 0:
                self.verifyCount+=1
                global score
                score+=1
            if keys[pygame.K_UP] and self.rect.y == 3 * ALTURA // 4:
                self.change_y = -self.init_change_y
            if keys[pygame.K_DOWN] and self.rect.y == ALTURA // 4:
                self.change_y = self.init_change_y
        else:
            self.verifyCount=0
            if keys[pygame.K_UP]:
                aux = self.change_y
                self.change_y-=1
                if(self.change_y == 0):
                    self.change_y = aux
            if keys[pygame.K_DOWN]:
                aux = self.change_y
                self.change_y+=1

                if(self.change_y == 0):
                    self.change_y = aux


        self.rect.y += self.change_y

        self.rect.y = max(self.rect.y, ALTURA // 4)
        self.rect.y = min(self.rect.y, 3 * ALTURA // 4)

class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image.fill(VERMELHO)
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(ALTURA // 4 + 40, 3 * ALTURA // 4 - 40)
        self.rect.x = LARGURA
        self.speed = random.randint(3, 6)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.kill()

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

# Função para jogar
def jogar():
    global rodando, score, estado
    jogador = Jogador()
    todos_sprites = pygame.sprite.Group()
    todos_sprites.add(jogador)
    inimigos = pygame.sprite.Group()
    score = 0

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
        text = font.render("Score: " + str(score), True, AZUL)
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
