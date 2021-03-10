from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play(loops=5)
x = str(input('Agora está ouvindo?'))
