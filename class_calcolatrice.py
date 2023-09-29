class Calcolatrice:
    def __init__(self):
        pass
    
    def addizione(self,a,b):
        """
        Restituisce la somma di due numeri.
        Args:
            a (int o float): Il primo numero.
            b (int o float): Il secondo numero.
        Returns:
            int o float: La somma di a e b.
        Raises:
            TypeError: Se uno dei due argomenti non è un numero.
        """
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            return a + b
        else:
            raise TypeError('Entrambi gli argomenti devono essere numeri')

    def sottrazione(self,a,b):
        """
        Restituisce la differenza tra due numeri.
        Args:
            a (int o float): Il primo numero.
            b (int o float): Il secondo numero.
        Returns:
            int o float: La differenza tra a e b.
        Raises:
            TypeError: Se uno dei due argomenti non è un numero.
        """
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            return a - b
        else:
            raise TypeError('Entrambi gli argomenti devono essere numeri')

    def moltiplicazione(self,a,b):
        """
        Restituisce il prodotto di due numeri.
        Args:
            a (int o float): Il primo numero.
            b (int o float): Il secondo numero.
        Returns:
            int o float: Il prodotto di a e b.
        Raises:
            TypeError: Se uno dei due argomenti non è un numero.
        """
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            return a * b
        else:
            raise TypeError('Entrambi gli argomenti devono essere numeri')

    def divisione(self,a,b):
        """
        Restituisce il risultato della divisione tra due numeri.
        Args:
            a (int o float): Il dividendo.
            b (int o float): Il divisore.
        Returns:
            int o float: Il risultato della divisione di a per b.
        Raises:
            TypeError: Se uno dei due argomenti non è un numero.
            ZeroDivisionError: Se il divisore (b) è zero.
        """
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            if b == 0:
                raise ZeroDivisionError('Impossibile dividere per zero')
            return a / b
        else:
            raise TypeError('Entrambi gli argomenti devono essere numeri')

    def elevazione_potenza(self,a,b):
        """
        Restituisce il risultato dell'elevazione di un numero alla potenza di un altro numero.
        Args:
            a (int o float): La base.
            b (int o float): L'esponente.
        Returns:
            int o float: Il risultato di a elevato alla potenza di b.
        Raises:
            TypeError: Se uno dei due argomenti non è un numero.
        """
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            return a ** b
        else:
            raise TypeError('Entrambi gli argomenti devono essere numeri')

calc = Calcolatrice()