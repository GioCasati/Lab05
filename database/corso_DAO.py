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

    def iscrivi(self, studente, codice_corso):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM iscrizione WHERE matricola = %s AND codins = %s"""
        cursor.execute(query, (studente._matricola, codice_corso))
        res = cursor.fetchall()
        if len(res) > 0:
            cnx.close()
            print("Connection closed")
            return False
        query = """INSERT INTO iscrizione VALUES (%s, %s)"""
        cursor.execute(query, (studente._matricola, codice_corso))
        cnx.commit()
        print("Connection committed")
        cnx.close()
        print("Connection closed")
        return True