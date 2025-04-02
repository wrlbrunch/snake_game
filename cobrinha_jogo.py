import pygame 
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

song_back = pygame.mixer.music.load("songs/BoxCat_Games_-_08_-_CPU_Talk.mp3")
pygame.mixer.music.play(-1)

song_colisao = pygame.mixer.Sound("songs/smw_lemmy_wendy_correct.wav")

morreu = False

altura = 480
largura = 640

x_cobra = largura / 2
y_cobra = altura / 2

velocidade = 4
x_controle = velocidade
y_controle = 0

x_fruta = randint(40, 500)
y_fruta = randint(50, 430)

fonte = pygame.font.SysFont('arial', 40, True, True)
pontos = 0

relogio = pygame.time.Clock()
7
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')

lista_cobra = []
comprimento_inicial = 20


def corpo_cobra(lista_cobra):   #XeY é uma lista com as posições X e Y ;)
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0),  (XeY[0], XeY[1], 20, 20))
        
def reiniciar():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, cabeca_cobra, x_fruta, y_controle, morreu
    pontos = 0
    comprimento_inicial = 20
    x_cobra = largura / 2
    y_cobra = altura / 2
    lista_cobra = []
    cabeca_cobra = []
    x_fruta = randint(40,600)
    y_fruta = randint(50, 430)
    morreu = False

while True:
    relogio.tick(60)
    tela.fill((47, 79, 79))
    mensagem = f'Pontos: {pontos}'
    texto_formt = fonte.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                  x_controle = -velocidade
                  y_controle = 0
                
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                  x_controle = velocidade
                  y_controle = 0
            
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                  y_controle = -velocidade
                  x_controle = 0
            
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                  y_controle = velocidade
                  x_controle = 0
                  
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
 
##    if pygame.key.get_pressed()[K_a]:
##        x_cobra =  x_cobra - 10            

##    if pygame.key.get_pressed()[K_d]:
##        x_cobra =  x_cobra + 10      

##    if pygame.key.get_pressed()[K_w]:
##        y_cobra =  y_cobra - 10    

##    if pygame.key.get_pressed()[K_s]:
##        y_cobra =  y_cobra + 10    

    cobra =   pygame.draw.rect(tela,(0, 255, 0), (x_cobra, y_cobra, 20, 20))
    fruta = pygame.draw.rect(tela,(255, 0, 0), (x_fruta, y_fruta, 20, 20))
    if cobra.colliderect(fruta): 
        x_fruta = randint(40, 500)
        y_fruta = randint(50, 430)
        pontos = pontos + 1
        song_colisao.play()
        comprimento_inicial = comprimento_inicial + 1
    
    cabeca_cobra = []
    cabeca_cobra.append(x_cobra)
    cabeca_cobra.append(y_cobra)
    lista_cobra.append(cabeca_cobra)
   
    if lista_cobra.count(cabeca_cobra) > 1:
        fonte2 = pygame.font.SysFont("arial", 25, True, True)
        mensagem = 'Fim de Jogo! Pressione R para jogar novamente.'
        texto_formt = fonte2.render(mensagem, True, (0, 0, 0))
        ret_texto = texto_formt.get_rect()
        morreu = True
        while morreu:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if  event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar()
            ret_texto.center = (largura//2, largura//2)
            tela.blit(texto_formt, ret_texto)
            pygame.display.update()   
        
    if x_cobra >= largura:
       x_cobra = 0
    if x_cobra <= 0:
       x_cobra = largura - 20
    if y_cobra <= 0:
       y_cobra = altura - 20
    if y_cobra >= altura:
           y_cobra = 0
    
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    corpo_cobra(lista_cobra)
    
    tela.blit(texto_formt, (450, 40))
    pygame.display.update() 