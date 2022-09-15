class Graph(object):

    def __init__(self, knotenListe:list, kantenListe:list):
        self.knotenListe = knotenListe
        self.kantenListe = kantenListe
        
    def getAlleKnoten(self):
        print(self.knotenListe)

    def existiertKnoten(self, nameKnoten:str):
        return nameKnoten in self.knotenListe

    def addKnoten(self, nameKnoten:str):
        return self.knotenListe.append(nameKnoten)

    def delKnoten(self, nameKnoten:str):
        if nameKnoten in self.knotenListe:
            return self.knotenListe.remove(nameKnoten)

    def existiertKante(self, nameStartKnoten:str, nameZielKnoten:str):
        nameKanten = [nameStartKnoten,nameZielKnoten]
        return nameKanten in self.kantenListe

    def addKanten(self, nameStartKnoten:str, nameZielKnoten:str):
        if self.existiertKnoten(nameStartKnoten) and self.existiertKnoten(nameZielKnoten):
            kante = [nameStartKnoten, nameZielKnoten]
            return self.kantenListe.append(kante)

    def delKanten(self, nameStartKnoten:str, nameZielKnoten:str):
        if self.existiertKante(nameStartKnoten,nameZielKnoten): 
            kante = [nameStartKnoten, nameZielKnoten]
            return self.kantenListe.remove(kante)

    def getAlleNachbarn(self, nameKnoten:str):
        if self.existiertKnoten(nameKnoten):
            return

g = Graph(['A','B','C','D','E','F','G','H'],[['A','C'],['A','C'],['A','C'],['C','A'],['C','E'],['C','D'],['E','G'],['E','D'],['G','D'],['D','E'],['D','B'],['B','C'],['B','D'],['F','B'],['F','D'],['F','H'],['H','F'],['H','G']])

# g.addKanten('A','H')

g.getAlleKnoten()
