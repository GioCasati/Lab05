import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fill_interface(self):
        for corso in self._model.corsi():
            self._view._ddSelezioneCorso.options.append(ft.dropdown.Option(key=corso._codice_insegnamento, text=str(corso)))

    def handle_tentativo_inserimento_proibito(self, e):
        self._view.create_alert("Puoi solo specificare una matricola")
        self._view._txt_Nome.disabled = True
        self._view._txt_Cognome.disabled = True
        self._view._txt_CDS.disabled = True
        self._view._txtInMatricola.focus()
        self._view.update()

    def reset_student_fields(self):
        self._view._txt_Nome.disabled = True
        self._view._txt_Cognome.disabled = True
        self._view._txt_CDS.disabled = True
        self._view._txtInMatricola.value = ""
        self._view._txt_Nome.value = ""
        self._view._txt_Cognome.value = ""
        self._view._txt_CDS.value = ""
        self._view.update()

    def handle_cerca_iscritti_corso(self, e):
        self.reset_student_fields()
        codice_corso = self._view._ddSelezioneCorso.value
        if codice_corso is None:
            self._view.create_alert("Selezionare un corso")
            self._view._ddSelezioneCorso.focus()
        else:
            studenti = self._model.studenti_corso(codice_corso)
            self._view.txt_result.controls.append(ft.Text(f"\nRisultano {len(studenti)} iscritti al corso:", weight=ft.FontWeight.BOLD, size=20))
            for studente in studenti:
                self._view.txt_result.controls.append(ft.Text(studente))
        self._view.update()

    def handle_get_studente(self, e):
        self._view._txtInMatricola.disabled = True
        self._view._ddSelezioneCorso.value = None
        matricola = self._view._txtInMatricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola")
            self.reset_student_fields()
            self._view._txtInMatricola.disabled = False
            self._view._txtInMatricola.focus()
            self._view.update()
            return
        if not matricola.isdigit():
            self._view.create_alert("Inserire una matricola numerica")
            self.reset_student_fields()
            self._view._txtInMatricola.disabled = False
            self._view._txtInMatricola.focus()
            self._view.update()
            return

        studente = self._model.get_studente(matricola)
        if studente is None:
            self._view.create_alert("Matricola inesistente")
            self._view.txt_result.controls.append(ft.Text(f"La matricola {matricola} non appartiene a nessuno studente", color="red"))
            self.reset_student_fields()
        else:
            self._view._txt_Nome.disabled = False
            self._view._txt_Cognome.disabled = False
            self._view._txt_CDS.disabled = False
            self._view._txt_Nome.value = studente._nome
            self._view._txt_Cognome.value = studente._cognome
            self._view._txt_CDS.value = studente._CDS
        self._view._txtInMatricola.disabled = False
        self._view._txtInMatricola.focus()
        self._view.update()

    def handle_get_corsi_studente(self, e):
        self._view._txtInMatricola.disabled = True
        self._view._ddSelezioneCorso.value = None
        matricola = self._view._txtInMatricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola")
            self.reset_student_fields()
            self._view._txtInMatricola.disabled = False
            self._view._txtInMatricola.focus()
            self._view.update()
            return
        if not matricola.isdigit():
            self._view.create_alert("Inserire una matricola numerica")
            self.reset_student_fields()
            self._view._txtInMatricola.disabled = False
            self._view._txtInMatricola.focus()
            self._view.update()
            return

        studente = self._model.get_studente(matricola)
        if studente is None:
            self._view.create_alert("Matricola inesistente")
            self._view.txt_result.controls.append(
                ft.Text(f"La matricola {matricola} non appartiene a nessuno studente", color="red"))
            self.reset_student_fields()
        else:
            self._view._txt_Nome.disabled = False
            self._view._txt_Cognome.disabled = False
            self._view._txt_CDS.disabled = False
            self._view._txt_Nome.value = studente._nome
            self._view._txt_Cognome.value = studente._cognome
            self._view._txt_CDS.value = studente._CDS
            corsi = self._model.get_corsi_studente(matricola)
            if corsi is None:
                self._view.txt_result.controls.append(ft.Text(f"Lo studente {studente} non è iscritto ad alcun corso", color="red"))
            else:
                self._view.txt_result.controls.append(ft.Text(f"\nLo studente {studente} risulta iscritto a {len(corsi)} corsi:", weight=ft.FontWeight.BOLD, size=20))
                for corso in corsi:
                    self._view.txt_result.controls.append(ft.Text(corso))
        self._view._txtInMatricola.disabled = False
        self._view._txtInMatricola.focus()
        self._view.update()

    def handle_iscrizione(self, e):
        self._view._txtInMatricola.disabled = True
        self._view._ddSelezioneCorso.disabled = True
        matricola = self._view._txtInMatricola.value
        codice_corso = self._view._ddSelezioneCorso.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola")
            self.reset_student_fields()
            self._view._txtInMatricola.disabled = False
            self._view._ddSelezioneCorso.disabled = False
            self._view._txtInMatricola.focus()
            self._view.update()
            return
        if not matricola.isdigit():
            self._view.create_alert("Inserire una matricola numerica")
            self.reset_student_fields()
            self._view._txtInMatricola.disabled = False
            self._view._ddSelezioneCorso.disabled = False
            self._view._txtInMatricola.focus()
            self._view.update()
            return
        if codice_corso is None or codice_corso == "":
            self._view.create_alert("Scegliere un corso")
            self._view._txtInMatricola.disabled = False
            self._view._ddSelezioneCorso.disabled = False
            self._view._ddSelezioneCorso.focus()
            self._view.update()
            return

        studente = self._model.get_studente(matricola)
        if studente is None:
            self._view.create_alert("Matricola inesistente")
            self._view.txt_result.controls.append(
                ft.Text(f"La matricola {matricola} non appartiene a nessuno studente", color="red"))
            self.reset_student_fields()
            self._view._txtInMatricola.focus()
        else:
            self._view._txt_Nome.disabled = False
            self._view._txt_Cognome.disabled = False
            self._view._txt_CDS.disabled = False
            self._view._txt_Nome.value = studente._nome
            self._view._txt_Cognome.value = studente._cognome
            self._view._txt_CDS.value = studente._CDS
            iscrizione = self._model.iscrivi(studente, codice_corso)
            if not iscrizione:
                self._view.create_alert("Studente già iscritto al corso")
                self._view.txt_result.controls.append(
                    ft.Text(f"Lo studente {studente} è già iscritto al corso {codice_corso}", color="red"))
            else:
                self._view.txt_result.controls.append(
                    ft.Text(f"Studente - {studente} - iscritto con successo al corso {codice_corso}", color="green"))

        self._view._txtInMatricola.disabled = False
        self._view._ddSelezioneCorso.disabled = False
        self._view.update()