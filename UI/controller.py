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
        self._view._txtInMatricola.focus()

    def handle_cerca_iscritti_corso(self, e):
        codice_corso = self._view._ddSelezioneCorso.value
        if codice_corso is None:
            self._view.create_alert("Scegliere il corso")
            return
        for studente in self._model.studenti_corso(codice_corso):
            self._view.txt_result.controls.append(ft.Text(studente))
        self._view.update()

    def handle_get_studente(self, e):
        matricola = self._view._txtInMatricola.value
        if matricola == "":
            self._view.create_alert("Inserisci la matricola")
            self._view._txtInMatricola.focus()
            return
        if not matricola.isdigit():
            self._view.create_alert("Inserisci una matricola numerica")
            self._view._txtInMatricola.value = ""
            self._view._txtInMatricola.focus()
            return
        studente = self._model.get_studente(matricola)
        if studente is None:
            self._view.txt_result.controls.append(ft.Text(f"La matricola {matricola} non appartiene a nessuno studente", color="red"))
            self._view._txtInMatricola.value = ""
            self._view._txtInMatricola.focus()
            self._view.update()
            return
        self._view._txt_Nome.value = studente._nome
        self._view._txt_Cognome.value = studente._cognome
        self._view._txt_CDS.value = studente._CDS
        self._view.update()