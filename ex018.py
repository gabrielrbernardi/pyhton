import math
ang_graus = int(input('Digite um angulo: '))
ang = math.radians(ang_graus)                                               #FUNCAO USADA PARA CONVERTER ANGULO DE GRAUS PARA RADIANOS
sen = math.sin(ang)
cos = math.cos(ang)
tan = math.tan(ang)
print(ang)
print('O valor do seno do angulo {:.1f} eh {:.2f}'.format(ang_graus,sen))
print('O valor do cosseno do angulo {:.1f} eh {:.2f}'.format(ang_graus,cos))
print('O valor da tangente do angulo {:.1f} eh {:.2f}'.format(ang_graus,tan))