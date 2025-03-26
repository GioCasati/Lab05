from dataclasses import dataclass


@dataclass
class Studente:
    def __init__(self, matricola, cognome, nome, CDS):
        self._matricola : int = matricola
        self._cognome : str = cognome
        self._nome : str = nome
        self._CDS : str = CDS

    def __str__(self):
        return f"{self._cognome} {self._nome} ({self._matricola})"

    def __eq__(self, other):
        return self._matricola == other._matricola

    def __hash__(self):
        return hash(self._matricola)