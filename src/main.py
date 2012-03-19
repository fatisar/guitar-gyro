import Player
import os

player = Player.Player()
player.generate_tab_for_file("../media/Binchois.xml")

def grabsamples(directory):
    walker = os.walk(directory)
    dirs = []
    for i,v in enumerate(walker):
        for j,f in enumerate(v[2]):
            if f[0] == ".": continue
            player.generate_tab_for_file("%s/%s" % (v[0],f))

#grabsamples("../media")
