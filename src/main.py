import Player
import os

player = Player.Player()


def grabsamples(directory):
    walker = os.walk(directory)
    dirs = []
    for i,v in enumerate(walker):
        for j,f in enumerate(v[2]):
            if f[0] == ".": continue
            player.read_and_parse_file("%s/%s" % (v[0],f))

grabsamples("../media")

#player.read_and_parse_file("../media/Binchois.xml")