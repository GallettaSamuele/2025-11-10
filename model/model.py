import itertools

import networkx as nx
from database.DAO import DAO


class Model:


    def __init__(self):
        self._grafo = nx.DiGraph()


    def getAllStore(self):
        return DAO.getAllStore()

    def fillMappaOrdini(self, store_id):
        self._mappaOrdini = {}
        ordini = DAO.getAllOrders(store_id)
        for ordine in ordini:
            self._mappaOrdini[ordine.order_id] = ordine

    def creaNodiGrafo(self, store_id):
        ordini = DAO.getAllOrders(store_id)
        for ordine in ordini:
            self._grafo.add_node(ordine)

    def creaArchiGrafo(self, store_id, K):
        ordini = DAO.getArchiGrafo(store_id)
        lista_combinazioni_ordini = itertools.combinations(ordini, 2)
        for ordine in lista_combinazioni_ordini:
            if ordine[0].order_date < ordine[1].order_date:
                diff = (ordine[1].order_date - ordine[0].order_date).days
                peso = (ordine[0].quantity + ordine[1].quantity)/diff
                if diff <= K:
                    self._grafo.add_edge(self._mappaOrdini[ordine[0].order_id], self._mappaOrdini[ordine[1].order_id], weight = peso)
            elif ordine[0].order_date > ordine[1].order_date:
                diff = (ordine[0].order_date - ordine[1].order_date).days
                peso = (ordine[1].quantity + ordine[0].quantity) / diff
                if diff <= K:
                    self._grafo.add_edge(self._mappaOrdini[ordine[0].order_id], self._mappaOrdini[ordine[1].order_id], weight = peso)

    def creaGrafo(self, store_id, K):
        self._grafo.clear()
        self.fillMappaOrdini(store_id)
        self.creaNodiGrafo(store_id)
        self.creaArchiGrafo(store_id, K)
