import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._store = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDStore(self):
        stores = self._model.getAllStore()
        for store in stores:
            self._view._ddStore.options.append(ft.dropdown.Option(key = store.store_id, text = store.store_name, data=store, on_click=self.readStore))

    def readStore(self, e):
        self._store = e.control.data

    def handleCreaGrafo(self, e):
        self._view.txt_result.controls.clear()
        store_id = self._store.store_id
        K = self._view._txtIntK.value
        if K is None or K == "":
            self._view.txt_result.controls.append(ft.Text("Inserire un valore per K !!!!"))
            self._view.update_page()
            return
        try:
            intK = int(self._view._txtIntK.value)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text("Inserire un valore intero per K !!!!"))
            self._view.update_page()
            return
        self._model.creaGrafo(store_id, intK)
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato", color = "red"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi del grafo: {len(self._model._grafo.nodes())}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi del grafo: {len(self._model._grafo.edges())}"))
        archi = list(sorted(self._model._grafo.edges(data=True), key = lambda x : x[2]["weight"], reverse=True))
        for i in range(0, 5):
            self._view.txt_result.controls.append(ft.Text(f"Arco: {archi[i][0]} --> {archi[i][1]}  Peso: {archi[i][2]["weight"]}"))
        self._view.update_page()
        return


    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):
        pass