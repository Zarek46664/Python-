
#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame, time, random
from pygame.locals import *

# Constantes
ANCHO = 1080
ALTO = 600

#Funciones
# ---------------------------------------------------------------------

def texto(texto, posx, posy, color=(255, 255, 255), tam=20):
	fuente = pygame.font.Font("images/BLADRMF_.ttf", tam)
	salida = pygame.font.Font.render(fuente, texto, 1, color)
	salida_rect = salida.get_rect()
	salida_rect.centerx = posx
	salida_rect.centery = posy
	return salida, salida_rect

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
        
        self.image9 = pygame.image.load('images/serpiente/ColaDerecha.png')
        self.image10 = pygame.image.load('images/serpiente/ColaIzquierda.png')
        self.image11 = pygame.image.load('images/serpiente/ColaAbajo.png')
        self.image12 = pygame.image.load('images/serpiente/ColaArriba.png')
        
        self.image13 = pygame.image.load('images/serpiente/izqabajo.png')
        self.image14 = pygame.image.load('images/serpiente/derabajo.png')
        self.image15 = pygame.image.load('images/serpiente/izqarriba.png')
        self.image16 = pygame.image.load('images/serpiente/derarriba.png')
        

        

        
        # posicion
        self.rect = self.image.get_rect()
        self.timetoreload = 0
        self.direccion = ""
        self.body=[[540,360],[540-self.rect.w,360],[540-self.rect.w*2,360]]
        self.bodyDireccion=["","",""]
        


        ######        

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]: 
            if self.direccion !="arriba":
                    self.direccion = "abajo"
        
        elif key[pygame.K_UP]:
            if self.direccion !="abajo":
                     self.direccion = "arriba" 

        elif key[pygame.K_RIGHT]:
            if self.direccion !="izquierda":
                     self.direccion = "derecha" 

        elif key[pygame.K_LEFT]:  
            if self.direccion !="derecha":
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
# bordes
        if self.body[0][0]>ANCHO-30:
            self.body[0][0]=0
        if self.body[0][0]<0:
            self.body[0][0]=ANCHO

        if self.body[0][1]>ALTO-30:
            self.body[0][1]=0
        if self.body[0][1]<0:
            self.body[0][1]=ALTO
            
        if self.direccion != "":
            for i in range(1,len(self.body)):
                x=self.body[i][0]
                y=self.body[i][1]
                if x<gotox:
                        self.bodyDireccion[i]="derecha"
                elif x>gotox:
                        self.bodyDireccion[i]="izquierda"
                elif y>gotoy:
                        self.bodyDireccion[i]="arriba"
                elif y<gotoy:
                        self.bodyDireccion[i]="abajo"
                        
                self.body[i][0]=gotox
                self.body[i][1]=gotoy
                gotox=x
                gotoy=y

        self.rect.x = self.body[0][0]
        self.rect.y = self.body[0][1]
        
    def add(self):
        self.body.append([self.body[len(self.body)-1][0],self.body[len(self.body)-1][1]])#self.body.append(self.body[0].copy())
        self.bodyDireccion.append(self.bodyDireccion[len(self.bodyDireccion)-1])

    def muerte(self):
         for i in self.body[1:-1]:
                if  i== self.body[0]:
                        return True

        
    def draw(self, surface):
        i=0
        for b in self.body:
#cabeza
            if i==0 and self.direccion=="derecha":
                surface.blit(self.image, (b[0], b[1]))
            elif i==0 and self.direccion=="izquierda":
                surface.blit(self.image5, (b[0], b[1]))
            elif i==0 and self.direccion=="arriba":
                surface.blit(self.image4, (b[0], b[1]))
            elif i==0 and self.direccion=="abajo":
                surface.blit(self.image6, (b[0], b[1]))
         
#cola
            elif i==len(self.body)-1 and self.bodyDireccion[i]=="derecha":
                surface.blit(self.image9, (b[0], b[1]))
            elif i==len(self.body)-1 and self.bodyDireccion[i]=="izquierda":
                surface.blit(self.image10, (b[0], b[1]))
            elif i==len(self.body)-1  and self.bodyDireccion[i]=="arriba":
                surface.blit(self.image12, (b[0], b[1]))
            elif i==len(self.body)-1 and self.bodyDireccion[i]=="abajo":
                surface.blit(self.image11, (b[0], b[1]))
#Cuerpo
            elif i!=0 and i<len(self.body)-1:
                surface.blit(self.chooseSpriteForBody(i,self.bodyDireccion[i]), (b[0], b[1]))

            elif i==0: #Cabeza
                surface.blit(self.image, (b[0], b[1]))
            elif i==len(self.body)-1:#cola
                surface.blit(self.image9, (b[0], b[1]))      
            elif i!=0:#cuerpo
                surface.blit(self.image2, (b[0], b[1]))
           
            i+=1

    def chooseSpriteForBody(self,i,bDireccion):
    
            if self.body[i][1] == self.body[i+1][1]:
                    if self.body[i][1]<self.body[i-1][1]:
                            if bDireccion=="izquierda":
                                    return self.image13

                            elif bDireccion=="derecha":  
                                    return self.image14
                                
                    elif self.body[i][1]>self.body[i-1][1]:
                            if bDireccion=="izquierda":
                                    return self.image15

                            elif bDireccion=="derecha":  
                                    return self.image16
                                
                    elif self.body[i][1]==self.body[i-1][1]:
                            return self.image2
                        
            elif self.body[i][0] == self.body[i+1][0]:
                    
                    if self.body[i][0]<self.body[i-1][0]:
                            if bDireccion=="izquierda":
                                    return self.image13

                            elif bDireccion=="derecha":  
                                   return self.image14
                                
                    elif self.body[i][0]>self.body[i-1][0]:
                            if bDireccion=="izquierda":
                                    return self.image15

                            elif bDireccion=="derecha":  
                                    return self.image16    
                    elif self.body[i][0]==self.body[i-1][0]:
                            return self.image7
                

            if self.body[i][1] == self.body[i+1][1]:
                    
                    if self.body[i][1]<self.body[i-1][1]:
                            if bDireccion=="arriba":
                                    return self.image14

                            elif bDireccion=="abajo":  
                                    return self.image13
                                
                    elif self.body[i][1]>self.body[i-1][1]:
                            if bDireccion=="arriba":
                                    return self.image16

                            elif bDireccion=="abajo":  
                                    return self.image15   
                    elif self.body[i][1]==self.body[i-1][1]:
                            return self.image7

                        
            elif self.body[i][0] == self.body[i+1][0]:
                    
                    if self.body[i][0]<self.body[i-1][0]:
                            if bDireccion=="arriba":
                                    return self.image13

                            elif bDireccion=="abajo":  
                                    return self.image15
                    elif self.body[i][0]>self.body[i-1][0]:
                            if bDireccion=="arriba":
                                    return self.image14

                            elif bDireccion=="abajo":  
                                    return self.image16    
                    elif self.body[i][0]==self.body[i-1][0]:
                            return self.image7
                            
            return self.image2
            

class Obstaculo(object):
    def __init__(self):

        self.image = pygame.image.load('images/puas.png')
        self.rect = self.image.get_rect()

       # self.body=[1020,540]
        

        self.rect.x=round(random.randrange(0,ANCHO-178)/30.0)*30.0
        self.rect.y=round(random.randrange(0,ALTO-178)/30.0)*30.0
        
        #self.rect.x = self.body[0]
        #self.rect.y = self.body[1]
  
    def draw(self, surface):
   
        surface.blit(self.image,(self.rect.x, self.rect.y))
      
 
                
     #   surface.blit(self.image,(self.x,self.y))


class Bordes(object):
    def __init__(self):


        self.image = pygame.image.load('images/bordesH.png')
        self.image2 = pygame.image.load('images/bordesV.png')


        self.rect = self.image.get_rect()
            
        self.body=[[0,0],[0,ALTO-60],[0,0],[ANCHO-60,0]]

      # self.rect.x=random.randrange(0,ANCHO-62)
        #self.rect.y=random.randrange(0,ALTO-62)
        
        
    
    def draw(self, surface):
      
        #surface.blit(self.image, (self.rect.x, self.rect.y))
        surface.blit(self.image, (self.body[0][0], self.body[0][1]))
        surface.blit(self.image, (self.body[1][0], self.body[1][1]))
        surface.blit(self.image2, (self.body[2][0],self.body[2][1]))
        surface.blit(self.image2, (self.body[3][0], self.body[3][1]))
##
                
     #   surface.blit(self.image,(self.x,self.y))
class Manzana(object):
        
    def __init__(self):

        self.image = pygame.image.load('images/manzana.png')
        self.rect = self.image.get_rect()
        self.cambio()

    def draw(self,surface):
        surface.blit(self.image,(self.x,self.y))

    def cambio(self):

        self.x=round(random.randrange(0,ANCHO-30)/30.0)*30.0
        self.y=round(random.randrange(0,ALTO-30)/30.0)*30.0
        self.rect.x = self.x
        self.rect.y=self.y


        


    
#Main
# ---------------------------------------------------------------------

pygame.init()

screen = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Snake Cyberpunk")
snake = Snake()
obstaculo = Obstaculo()
obstaculo2= Obstaculo()
bordes = Bordes()
fondo =  pygame.image.load('images/fondo.png')
manzana = Manzana() 
pygame.mixer.music.load('Musica/musiquita.mp3')
pygame.mixer.music.play(3)
running = True
pygame.mixer.music.load('Musica/musiquita.mp3')
sonidoManzana=pygame.mixer.Sound('Musica/comida.wav')
sonidoMuerte=pygame.mixer.Sound('Musica/muerte.wav')
pygame.mixer.music.play(3)
puntos = 0


while running:
    screen.blit(fondo, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    snake.handle_keys()
    snake.animate()
    tex_img, tex_rec = texto("Puntuacion: "+str(puntos), 120, 55, (255, 255, 255), 18)    
    screen.blit(tex_img, tex_rec)


    if snake.rect.colliderect(manzana.rect):
       manzana.cambio()
       if  manzana.rect.colliderect(obstaculo.rect):
               manzana.cambio()
       elif  manzana.rect.colliderect(obstaculo2.rect):
               manzana.cambio()
       elif  manzana.rect.colliderect(snake.rect):
               manzana.cambio()
       snake.add()       
       sonidoManzana.play()
       puntos+=1
       
    elif snake.rect.colliderect(obstaculo.rect):
        sonidoMuerte.play()
        running= False
        pygame.mixer.music.stop()

    elif snake.rect.colliderect(obstaculo2.rect):
        sonidoMuerte.play()
        running= False
        pygame.mixer.music.stop()
        
    elif snake.muerte():
        sonidoMuerte.play()
        running= False
        pygame.mixer.music.stop()
        
        
    #elif snake.rect.colliderect(bordes.rect):
        #sonidoMuerte.play()
        #running= False
        #pygame.mixer.music.stop()



        


    snake.draw(screen)
    manzana.draw(screen)
    obstaculo.draw(screen)
    obstaculo2.draw(screen)
    #bordes.draw(screen)
    screen.blit(tex_img, tex_rec)
    

       
    pygame.display.update()

    time.sleep(0.07)
pygame.display.quit()


