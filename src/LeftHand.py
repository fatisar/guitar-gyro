# LeftHand models the dexterity of the fingers on the left hand and the combinations between fingers, which will represent
# the weight for the transition between the fingers
#
#   The dexterity of a finger is a subjective measure, so the user should be able to customize the values
#       for each finger, although the combination dexterities will be computed based on these values; it's too
#       troublesome for a user to specify the many combination dexterities
#
#   Lower dexterity values correspond to greater dexterity (since they're used to calculate the weight of a transition,
#       lower dexterity values yield smaller weights for a transition)
#
#   Weights differ for same-string and different-string transitions, the latter also assigning different weights for
#       up-string and down-string movements (i.e. w[(0,2) -> (1,1)] != w[(1,2) -> (0,1)], where (x,y) = (string,finger)
#
#   Default finger deterities are equal to their finger number (i.e. dex(index) = 1, dex(pinky) = 4)
#
#   Dexterities are stored as a 5 x 5 matrix of 4-tuples: (distance, same-string dex, up-string dex, down-string dex)
#       "up-string" is from a lower string to a higher (i.e. E -> A or 0 -> 1), "down-string" vice versa

class LeftHand:
    _combo_dexterities = [[(0.0,0.0,0.0,0.0)] * 5 for i in range(5)]
    
    def __init__(self, d0 = 0.0, d1 = 1.0, d2 = 2.0, d3 = 3.0, d4 = 4.0):
        d = (d0,d1,d2,d3,d4)
        self._dex = [(d[i]/float(i),) * 5 for i in range(1,5)]
        self.generate_combo_dexterities()

    def generate_combo_dexterities(self):
        cd = self._combo_dexterities        # cd[start-finger][end-finger]
        cd[1][1] = (0.0,0.0,1.0,2.0)
        cd[1][2] = (1.0,2.0,1.5,1.0)
        cd[1][3] = (2.0,1.0,1.0,1.5)
        cd[1][4] = (3.0,1.5,1.5,1.5)

        cd[2][1] = (-1.0,1.0,1.0,1.5)
        cd[2][2] = (0.0,0.0,1.5,2.5)
        cd[2][3] = (1.0,2.0,2.0,1.5)
        cd[2][4] = (2.0,1.5,1.5,1.5)

        cd[3][1] = (-2.0,2.0,1.0,1.0)
        cd[3][2] = (-1.0,2.5,2.0,1.5)
        cd[3][3] = (0.0,0.0,2.0,3.5)
        cd[3][4] = (1.0,1.5,2.0,1.5)

        cd[4][1] = (-3.0,1.5,1.0,1.0)
        cd[4][2] = (-2.0,2.0,1.5,1.0)
        cd[4][3] = (-1.0,1.5,1.5,2.0)
        cd[4][4] = (0.0,0.0,2.5,4.0)
        
        cd[1:] = [map(self.scale_by_dexterity,cd[i],self._dex[i-1]) for i in range(1,5)]
        self._combo_dexterities = cd

    def scale_by_dexterity(self,cw,d):
        return tuple(w * d for w in cw)

    def get_combo_by_distance(self, dist):
        d_str = dist[0]
        metric = 0 if d_str == 0 else (1 if d_str >= 1 else 2)
        cd = self._combo_dexterities
        combos = [(start,end,cd[start][end][metric]) for start in range(len(cd)) for end in range(len(cd[start])) if cd[start][end][0] == dist[1]]
        return combos


    def __str__(self):
        for i in range(5):
            print self._combo_dexterities[i]