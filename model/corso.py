from dataclasses import dataclass


@dataclass(order=True)
class Corso:
    def __init__(self, codins, crediti, nome, pd):
        self._codice_insegnamento : str = codins
        self._num_crediti : int = crediti
        self._nome : str = nome
        self._periodo_didattico : int = pd

    def __str__(self):
        return f"{self._nome} ({self._codice_insegnamento})"

    def __eq__(self, other):
        return self._codice_insegnamento == other._codice_insegnamento

    def __hash__(self):
        return hash(self._codice_insegnamento)