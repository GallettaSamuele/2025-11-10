from database.DB_connect import DBConnect
from model.order import Order
from model.oridni2 import Ordini2
from model.store import Store


class DAO:
    @staticmethod
    def getAllStore():
        conn = DBConnect.get_connection()
        results = []
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * from stores"
        cursor.execute(query)
        for row in cursor:
            results.append(Store(**row))
        cursor.close()
        conn.close()
        return results


    @staticmethod
    def getAllOrders(store_id):
        conn = DBConnect.get_connection()
        results = []
        cursor = conn.cursor(dictionary=True)
        query = """
                select *
                from orders o
                where o.store_id = %s
                """
        cursor.execute(query, (store_id,))
        for row in cursor:
            results.append(Order(**row))
        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getArchiGrafo(store_id):
        conn = DBConnect.get_connection()
        results = []
        cursor = conn.cursor(dictionary=True)
        query = """
                select o.order_id , o.order_date , sum(oi.quantity) as quantity
                from orders o, order_items oi 
                where o.order_id = oi.order_id and o.store_id = %s
                group by o.order_id
                order by quantity desc
                """
        cursor.execute(query, (store_id,))
        for row in cursor:
            results.append(Ordini2(**row))
        cursor.close()
        conn.close()
        return results