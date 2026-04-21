class Voiture:

    def __init__(self, marque: str, vitesse_max: int):
        self.marque = marque
        self._vitesse_max = vitesse_max

    @property
    def marque(self):
        return self._marque

    @marque.setter
    def marque(self, value):
        self._marque = value

    @property
    def vitesse_max(self):
        return self._vitesse_max
    @vitesse_max.setter
    def vitesse_max(self, value):
        if value < 0:
            raise ValueError('vitesse_max must be > 0')
        self._vitesse_max = value

    def __str__(self):
        return f"Voiture(marque={self.marque}, vitesse_max={self.vitesse_max})"



voiture = Voiture("BMX", 5)
print(voiture)
