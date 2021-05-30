import numpy as np

class ClaseLista():

    def __init__(self):
        self.claves = np.array([])
        self.elementos = np.array([])
        return None
    
    def count_elementos(self):
        n = len(self.elementos)
        return n

    def count_claves(self):
        n = len(self.claves)
        return n

    def find(self, x):
        if self.claves.shape[0] > 0:
            try:
                idx = (self.claves == x).nonzero()
                return self.elementos[idx]
            except:
                return False
        else:
           return False

    def add(self, x, y):
        if self.find(x):
            idx = (self.claves == x).nonzero()
            self.elementos[idx] = y

        else:
            self.claves = np.append(self.claves, x)
            self.elementos = np.append(self.elementos, y)

            idx_ordered = np.argsort(self.claves)
            self.claves = self.claves[idx_ordered]
            self.elementos = self.elementos[idx_ordered]
    
    def delete(self, x):
        if self.find(x):
            idx = (~(self.claves == x)).nonzero()
            self.elementos = self.elementos[idx]
            self.claves = self.claves[idx]

        else: 
            raise ValueError('No encontró la clave!')