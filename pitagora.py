
import math  # Importiamo il modulo math per utilizzare la funzione sqrt


class Quadrato:
    '''Classe per rappresentare un quadrato.

    Args:
        lato (float): Lunghezza del lato del quadrato.

    Attributes:
        lato (float): Lunghezza del lato del quadrato.

    Methods:
        perimetro(): Calcola il perimetro del quadrato.
        area(): Calcola l'area del quadrato.
        diagonale(): Calcola la lunghezza della diagonale del quadrato.'''
    
    def __init__(self,lato):
        self.lato = lato

    @property
    def perimetro(self):
        perimetro = self.lato * 4
        return perimetro

    @property
    def area(self):
        area = self.lato ** 2
        return area

    @property
    def diagonale(self):
        diagonale = self.lato * math.sqrt(2)
        return diagonale

class Rettangolo:
    '''Classe per rappresentare un rettangolo.

    Args:
        base (float): Base del rettangolo.
        altezza (float): Altezza del rettangolo.

    Attributes:
        base (float): Base del rettangolo.
        altezza (float): Altezza del rettangolo.

    Methods:
        perimetro(): Calcola il perimetro del rettangolo.
        area(): Calcola l'area del rettangolo.
        diagonale(): Calcola la diagonale del rettangolo.'''
    
    def __init__(self,base_rettangolo,altezza_rettangolo):
        self.base_rettangolo = base_rettangolo
        self.altezza_rettangolo = altezza_rettangolo
    
    @property
    def perimetro(self):
        perimetro = 2*(self.base_rettangolo) + 2*(self.altezza_rettangolo)
        return perimetro

    @property
    def area(self):
        area = self.base_rettangolo * self.altezza_rettangolo
        return area

    @property
    def diagonale(self):
        diagonale = math.sqrt((self.altezza_rettangolo**2) + (self.base_rettangolo**2))
        return diagonale 

class Rombo:
    '''Classe per rappresentare un rombo.

    Args:
        lato (float): Lunghezza del lato del rombo.
        diagonale_maggiore (float): lunghezza diagonale_maggiore.
        diagonale_minore (float): lunghezza diagonale_minore.

    Attributes:
        lato (float): Lunghezza del lato del rombo.
        diagonale_maggiore (float): lunghezza diagonale_maggiore.
        diagonale_minore (float): lunghezza diagonale_minore.

    Methods:
        perimetro(): Calcola il perimetro del rombo.
        area(): Calcola l'area del rombo.'''
    
    def __init__(self,lato_rombo,diagonale_maggiore,diagonale_minore):
        self.lato_rombo = lato_rombo
        self.diagonale_maggiore = diagonale_maggiore
        self.diagonale_minore = diagonale_minore

    @property
    def perimetro(self):
        perimetro = self.lato_rombo * 4
        return perimetro




