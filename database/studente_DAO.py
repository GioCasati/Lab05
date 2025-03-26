# Add whatever it is needed to interface with the DB Table studente
from model.corso import Corso
from model.studente import Studente
from database.DB_connect import get_connection


class Studente_DAO:

    def get_studenti_corso(self, codice_corso):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        lista_studenti = []
        query = ("""SELECT s.matricola, s.cognome, s.nome, s.CDS FROM iscrizione i, studente s WHERE i.matricola = s.matricola AND i.codins = %s""")
        cursor.execute(query,(codice_corso,))
        for studente in cursor:
            lista_studenti.append(Studente(**studente))
        cnx.close()
        print("Connection closed")
        return lista_studenti

    def get_studente_matricola(self, matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = ("""SELECT matricola, cognome, nome, CDS FROM  studente WHERE matricola = %s""")
        cursor.execute(query,(matricola,))
        stud = cursor.fetchall()
        if len(stud) == 0:
            cnx.close()
            print("Connection closed")
            return None
        elif len(stud) == 1:
            cnx.close()
            print("Connection closed")
            return Studente(**stud[0])

    def get_corsi_studente(self, matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = ("""SELECT c.codins, c.crediti, c.nome, c.pd 
                    FROM  corso c, iscrizione i, studente s
                    WHERE c.codins = i.codins AND i.matricola = s. matricola AND s.matricola = %s""")
        cursor.execute(query, (matricola,))
        res = cursor.fetchall()
        if len(res) == 0:
            cnx.close()
            print("Connection closed")
            return None
        else:
            cnx.close()
            print("Connection closed")
            lista_corsi = []
            for corso in res:
                lista_corsi.append(Corso(**corso))
            return lista_corsi