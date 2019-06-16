
#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame, time, random
from pygame.locals import *

# Constantes
ANCHO = 1080
ALTO = 720



#Clases
# ---------------------------------------------------------------------
class Snake(object): 
    def __init__(self):
        self.image = pygame.image.load('images/serpiente/CabezaDerecha.png')
        self.image2 = pygame.image.load('images/serpiente/CuerpoH.png')
        self.image3 = pygame.image.load('images/serpiente/ColaDerecha.png')
        
        self.image7 = pygame.image.load('images/serpiente/CuerpoV.png')
        
        self.image4 = pygame.image.load('images/serpiente/CabezaArriba.png')
        self.image5 = pygame.image.load('images/serpiente/CabezaIzquierda.png')
        self.image6 = pygame.image.load('images/serpiente/CabezaAbajo.png')

        
        # posicion
        self.rect = self.image.get_rect()
        self.timetoreload = 0
        self.direccion = ""
        self.body=[[540,360],[540-self.rect.w,360],[540-self.rect.w*2,360]]

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]: 
            self.direccion = "abajo" 
        elif key[pygame.K_UP]: 
            self.direccion = "arriba" 
        if key[pygame.K_RIGHT]: 
            self.direccion = "derecha" 
        elif key[pygame.K_LEFT]: 
            self.direccion = "izquierda"

    def animate(self):
        gotox = self.body[0][0]
        gotoy = self.body[0][1]
        if self.direccion=="abajo":
            self.body[0][1] += self.rect.h
        elif self.direccion=="arriba":
            self.body[0][1] -= self.rect.h
        elif self.direccion=="izquierda":
            self.body[0][0] -= self.rect.w
        elif self.direccion=="derecha":
            self.body[0][0] += self.rect.w

        if self.body[0][0]>ANCHO:
            self.body[0][0]=0
        if self.body[0][0]<0:
            self.body[0][0]=ANCHO

        if self.body[0][1]>ALTO:
            self.body[0][1]=0
        if self.body[0][1]<0:
            self.body[0][1]=ALTO
            
        if self.direccion != "":
            for i in range(1,len(self.body)):
                x=self.body[i][0]
                y=self.body[i][1]
                self.body[i][0]=gotox
                self.body[i][1]=gotoy
                gotox=x
                gotoy=y
        
#    def add(self):
  #      self.body.append([self.body[0][0],self.body[0][1]])#self.body.append(self.body[0].copy())
        
    def draw(self, surface):
        i=0
        for b in self.body:

            if i==0 and self.direccion=="derecha":
                surface.blit(self.image, (b[0], b[1]))
            elif i==0 and self.direccion=="izquierda":
                surface.blit(self.image5, (b[0], b[1]))
            elif i==0 and self.direccion=="arriba":
                surface.blit(self.image4, (b[0], b[1]))
            elif i==0 and self.direccion=="abajo":
                surface.blit(self.image6, (b[0], b[1]))
                
            elif i!=0 and self.direccion=="derecha":
                surface.blit(self.image2, (b[0], b[1]))
            elif i!=0 and self.direccion=="izquierda":
                surface.blit(self.image2, (b[0], b[1]))
            elif i!=0 and self.direccion=="arriba":
                surface.blit(self.image7, (b[0], b[1]))
            elif i!=0 and self.direccion=="abajo":
                surface.blit(self.image7, (b[0], b[1]))

            elif i==0:
                surface.blit(self.image, (b[0], b[1]))
            elif i!=0:
                surface.blit(self.image2, (b[0], b[1]))
            
                       
            i+=1
            
#Main
# ---------------------------------------------------------------------

pygame.init()

screen = pygame.display.set_mode((ANCHO,ALTO))
snake = Snake()

running = True
while running:
    screen.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    snake.handle_keys()
    snake.animate()
    
       

    #if random.random() <  0.05:
      #  snake.add()
    
    snake.draw(screen)
    pygame.display.update()

    time.sleep(0.1)
pygame.display.quit()


