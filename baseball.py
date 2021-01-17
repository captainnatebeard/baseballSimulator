import random

class Team:
    def __init__(self, lineup, pitchers, name):
        self.lineup = lineup
        self.pitchers = pitchers
        self.name = name
        #assert type(lineup) == type([]), "lineup must be a list... you jive turkey"

    def __repr__(self):
        return "%s" % self.name


class Pitcher:
    def __init__(self, bAvgAgainst, name, handed):
        self.bAvgAgainst = bAvgAgainst
        self.name = name
        self.handed = handed


    def __repr__(self):
        return "%s" % self.name



class Player:
    def __init__(self, bavg, name, statusList, handed):
        self.bavg = bavg
        self.name = name
        self.statusList = statusList
        self.handed = handed


    def __repr__(self):
        return "%s" % self.name


    def status(self, pitcher):
        t = random.randrange(1, 1001)
        s = ((self.bavg * 1000) * (pitcher.bAvgAgainst * 1000)) / 324 # 324 represents known statistical advantage of pitcher in MLB
        print ("batting average:", self.bavg)
        print ("pitcher batting average against:", pitcher.bAvgAgainst)
        print ("randomly picked number", t)
        print ("combined average:", s)
        if t < s:
            #singles - 66%
            #doubles - 20%
            #triples - 11%
            #homeruns - 3%
            hitrand = random.randrange(1, 101)
            if hitrand > 97:
                playerStatus = 4
            elif (hitrand > 86) & (hitrand <= 97):
                playerStatus = 3
            elif (hitrand > 66) & (hitrand <= 77):
                playerStatus = 2
            else:
                playerStatus = 1
        else:
            playerStatus = 0
        return playerStatus


jMccann = Player(.318, "James McCann", [], "right")
mCabrera = Player(.329, "Miguel Cabrera", [], "right")
iKingsler = Player(.313, "Ian Kingsler", [], "right")
jIglesias = Player(.288, "Jose Iglesias", [], "right")
nCastellanos = Player(.320, "Nicholas Castellanos", [], "right")
jUpton = Player(.362, "Justin Upton", [], "right")
mMahtook = Player(.330, "Mikie Mahtook", [], "right")
jMartinez = Player(.388, "J.D. Martinez", [], "right")
vMartinez = Player (.324, "Victor Martinez", [], "right")

jVerlander = Pitcher(.306, "Justin Verlander", "right")
mFulmer = Pitcher(.293, "Michael Fulmer", "right")
jZimmerman = Pitcher(.358, "Jordan Zimmerman", "right")
mBoyd = Pitcher(.352, "Matt Boyd", "right")
aSanchez = Pitcher(.357, "Anibal Sanchez", "right")
dNorris = Pitcher(.363, "Daniel Norris", "right")
jWilson = Pitcher(.242, "Justin Wilson", "right")
sGreene = Pitcher(.311, "Shane Greene", "right")
wSaupold = Pitcher(.361, "Warwick Saupold", "right")
aWilson = Pitcher(.327, "Alex Wilson", "right")
dStumpf = Pitcher(.338, "Daniel Stumpf", "right")

tigers = Team([jMccann, mCabrera, iKingsler, jIglesias, nCastellanos, jUpton, mMahtook, jMartinez,
			vMartinez],[jVerlander, mFulmer, jZimmerman, mBoyd, aSanchez, dNorris, jWilson,
			sGreene, wSaupold, aWilson, dStumpf], "Detroit Tigers")


mZunino = Player(.331, "Mike Zunino", [], "right")
dValencia = Player(.314, "Danny Valencio", [], "right")
rCano = Player(.338, "Robinson Cano", [], "right")
jSegura = Player(.349, "Jean Segura", [], "right")
kSeager = Player(.323, "Kyle Seager", [], "right")
bGamel = Player(.322, "Ben Gamel", [], "right")
jDyson = Player(.324, "Jarrod Dyson", [], "right")
mHaniger = Player(.352, "Mitch Haniger", [], "right")
nCruz = Player(.375, "Nelson Cruz", [], "right")

aMiranda = Pitcher(.307, "Ariel Miranda", "right")
jPaxton = Pitcher(.277, "James Paxton", "right")
yGallardo = Pitcher(.346, "Yovani Gallardo", "right")
fHernandez = Pitcher(.321, "Felix Hernandez", "right")
sGaviglio = Pitcher(.332, "Sam Gaviglio", "right")
eRamirez = Pitcher(.284, "Erasmo Ramirez", "right")
eDiaz = Pitcher(.284, "Edwin Diaz", "right")
nVincent = Pitcher(.286, "Nick Vincent", "right")
jPazos = Pitcher(.333, "James Pazos", "right")
tZych = Pitcher(.323, "Tony Zych", "right")
mRzepczynski = Pitcher(.365, "Marc Rzepczynski", "right")

mariners = Team([mZunino, dValencia, rCano, jSegura, kSeager, bGamel, jDyson, mHaniger, nCruz],
            [aMiranda, jPaxton, yGallardo, fHernandez, sGaviglio, eRamirez, eDiaz, nVincent,
             jPazos, tZych, mRzepczynski],"Seattle Mariners")
