# Add whatever it is needed to interface with the DB Table corso
from model.corso import Corso
from model.studente import Studente
from database.DB_connect import get_connection


class Corso_DAO:

    def get_all_corsi(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        lista_corsi = []
        query = "SELECT * FROM corso"
        cursor.execute(query)
        for corso in cursor:
            lista_corsi.append(Corso(**corso))
        cnx.close()
        print("Connection closed")
        return lista_corsi