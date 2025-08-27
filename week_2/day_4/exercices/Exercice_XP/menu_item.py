from psycopg2 import connect
from psycopg2.extras import RealDictCursor

class MenuItem:
    def __init__(self, item_name, item_price=None):
        self.item_name = item_name
        self.item_price = item_price

    def get_connection(self):
        try:
            conn = connect(
                database="python",
                user="postgres",
                password="123456",
                host="localhost",
                port="5432",
                cursor_factory=RealDictCursor
            )
            return conn
        except Exception as e:
            print("Database connection failed:", e)
            return None

    def save(self):
        conn = self.get_connection()
        if not conn:
            return {"message": "Database connection failed"}, 500
        try:
            with conn.cursor() as cursor:
                query = "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s) RETURNING *;"
                cursor.execute(query, (self.item_name, self.item_price))
                result = cursor.fetchone()
                conn.commit()
                return {"message": "Item created successfully", "item": result}, 201
        except Exception as e:
            return {"error": str(e)}, 500
        finally:
            conn.close()

    def delete(self):
        conn = self.get_connection()
        if not conn:
            return {"message": "Database connection failed"}, 500
        try:
            with conn.cursor() as cursor:
                query = "DELETE FROM Menu_Items WHERE item_name = %s AND item_price = %s RETURNING *;"
                cursor.execute(query, (self.item_name, self.item_price))
                result = cursor.fetchone()
                conn.commit()
                if result:
                    return {"message": f"Item '{self.item_name}' deleted successfully"}, 200
                else:
                    return {"message": "Item not found"}, 404
        except Exception as e:
            return {"error": str(e)}, 500
        finally:
            conn.close()

    def update(self, new_name, new_price):
        conn = self.get_connection()
        if not conn:
            return {"message": "Database connection failed"}, 500
        try:
            with conn.cursor() as cursor:
                query = "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s RETURNING *;"
                cursor.execute(query, (new_name, new_price, self.item_name))
                result = cursor.fetchone()
                conn.commit()
                if result:
                    self.item_name = new_name
                    self.item_price = new_price
                    return {"message": "Item updated successfully", "item": result}, 200
                else:
                    return {"message": "Item not found"}, 404
        except Exception as e:
            return {"error": str(e)}, 500
        finally:
            conn.close()
