from menu_item import MenuItem

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        conn = MenuItem(name).get_connection()
        if not conn:
            return None
        try:
            with conn.cursor() as cursor:
                query = "SELECT * FROM Menu_Items WHERE item_name = %s;"
                cursor.execute(query, (name,))
                result = cursor.fetchone()
                if result:
                    return MenuItem(result['item_name'], result['item_price'])
                return None
        finally:
            conn.close()

    @classmethod
    def all_items(cls):
        conn = MenuItem("dummy").get_connection()
        if not conn:
            return []
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM Menu_Items;")
                results = cursor.fetchall()
                return [MenuItem(r['item_name'], r['item_price']) for r in results]
        finally:
            conn.close()
