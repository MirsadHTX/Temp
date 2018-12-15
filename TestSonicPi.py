from psonic import *

#HUSK AT STARTE SONIC PI

#play(72)
#sleep(1)
#play(75)
#sleep(1)
#play(79)


#play(72,amp=2)
#sleep(0.5)
#play(74,pan=0.2) #left



#sleep(5)
synth(SINE, note=D4)
#synth(SQUARE, note=D4)
#synth(TRI, note=D4, amp=0.4)
#sleep(5)

'''
#Different synthesizer sounds
sleep(2)
use_synth(SAW)
play(38)
sleep(0.25)
play(50)
sleep(0.5)
use_synth(PROPHET)
play(57)
sleep(0.25)
'''


pause = 3
while True:
    if one_in(2):
        sample(LOOP_AMEN,rate=4)
        sleep(pause)
        pause = pause - 0.2

