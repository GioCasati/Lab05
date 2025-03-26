from database.DB_connect import DBConnect
from database.corso_DAO import Corso_DAO
from database.studente_DAO import Studente_DAO


class Model:
    def __init__(self):
        self._corso_dao = Corso_DAO()
        self._studente_dao = Studente_DAO()

    def corsi(self):
        return self._corso_dao.get_all_corsi()

    def studenti_corso(self, codice_corso):
        return self._studente_dao.get_studenti_corso(codice_corso)

    def get_studente(self, matricola):
        return self._studente_dao.get_studente_matricola(matricola)