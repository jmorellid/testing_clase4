import numpy as np

class ClaseLista():

    def __init__(self):
        self.claves = np.array([])
        self.elementos = np.array([])
        return None

    def __call__(self):
        return self.claves
    
    def count_elementos(self):
        """Cuenta la cantidad de elementos en la lista """
        n = len(self.elementos)
        return n

    def count_claves(self):
        """ Cuetna la cantidad de claves en la lista"""

        n = len(self.claves)
        return n

    def find(self, x):
        """ Encuentra el elemento para su clave x, de no encontrarlo devuelve False"""
        if self.claves.shape[0] > 0:
            try:
                idx = (self.claves == x).nonzero()
                return self.elementos[idx]
            except:
                return False
        else:
           return False

    def add(self, x, y):
        """ Agrega un par elemento clave a la lista"""
        if self.find(x):
            idx = (self.claves == x).nonzero()
            self.elementos[idx] = y
        
        else:
            self.claves = np.append(self.claves, x)
            self.elementos = np.append(self.elementos, y)

            idx_ordered = np.argsort(self.claves)
            self.claves = self.claves[idx_ordered]
            self.elementos = self.elementos

        return NotImplemented
    
    def delete(self, x):
        """ Borra un elemento clave de la lista a partir de su clave"""
        if self.find(x):
            idx = (~(self.claves == x)).nonzero()
            self.elementos = self.elementos[idx]
            self.claves = self.claves[idx]

        else: 
            raise ValueError('No encontró la clave!')

        return NotImplemented