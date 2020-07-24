import pygame
pygame.init()                   #Iniciar biblioteca pygame
song_name = str(input('Digite o nome da musica: '))         #the_sign-wherever_you_will_go.mp3
print('A musica {} sera tocada'.format(song_name))
pygame.mixer.music.load(song_name)
pygame.mixer.music.play()
pygame.event.wait()
