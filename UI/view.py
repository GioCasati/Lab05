import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("Gestione studenti e corsi", color="blue", size=24)

        self._ddSelezioneCorso = ft.Dropdown(label="Seleziona un corso", width=550, options=[])
        self._btnCercaIscrittiCorso = ft.ElevatedButton(text="Cerca iscritti al corso", on_click=self._controller.handle_cerca_iscritti_corso)

        self._txtInMatricola = ft.TextField(
            label="Inserisci una matricola",
            width=180)
        self._txt_Nome = ft.TextField(
            label="Nome",
            width=180,
            read_only=True,
            on_focus=self._controller.handle_tentativo_inserimento_proibito,
            disabled=True)
        self._txt_Cognome = ft.TextField(
            label="Cognome",
            width=180,
            read_only=True,
            on_focus=self._controller.handle_tentativo_inserimento_proibito,
            disabled=True)
        self._txt_CDS = ft.TextField(
            label="Corso di Studi",
            width=180,
            read_only=True,
            on_focus=self._controller.handle_tentativo_inserimento_proibito,
            disabled=True)

        self._btnCercaStudente = ft.ElevatedButton(text="Cerca studente", on_click=self._controller.handle_get_studente)
        self._btnCercaCorsiDiStudente = ft.ElevatedButton(text="Cerca corsi a cui lo studente è iscritto", on_click=self._controller.handle_get_corsi_studente)
        self._btnIscriviStudenteACorso = ft.ElevatedButton(text="Iscrivi studente", on_click=self._controller.handle_iscrizione)

        self._page.controls.append(self._title)

        row1 = ft.Row([self._ddSelezioneCorso, self._btnCercaIscrittiCorso])
        self._page.controls.append(row1)

        row2 = ft.Row([self._txtInMatricola, self._txt_Nome, self._txt_Cognome, self._txt_CDS], )
        self._page.controls.append(row2)

        row3 = ft.Row([self._btnCercaStudente, self._btnCercaCorsiDiStudente, self._btnIscriviStudenteACorso])
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)

        self._controller.fill_interface()
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update(self):
        self._page.update()
