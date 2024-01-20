import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(
            r"d:\Python\QA\qa-auto-learning-project\become_qa_auto.db"
        )
        self.cursor = self.connection.cursor()

    def test_connection(self):
        self.cursor.execute("SELECT sqlite_version();")
        record = self.cursor.fetchall()
        print(
            f"\nConnected successfully. SQLite Database Version is: {record}"
        )

    def get_all_users(self):
        self.cursor.execute("SELECT name, address, city FROM customers;")

        return self.cursor.fetchall()

    def get_user_address_by_name(self, name):
        self.cursor.execute(
            f"SELECT address, city, postalCode, country "
            f"FROM customers "
            f"WHERE name = '{name}';"
        )

        return self.cursor.fetchall()

    def update_product_qnt_by_id(self, product_id, qnt):
        self.cursor.execute(
            f"UPDATE products "
            f"SET quantity = {qnt} "
            f"WHERE id = {product_id};"
        )
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        self.cursor.execute(
            f"SELECT quantity "
            f"FROM products "
            f"WHERE id = {product_id};")

        return self.cursor.fetchall()

    def insert_product(self, id, name, descript, qnt):
        self.cursor.execute(
            f"INSERT OR REPLACE INTO products(id, name, description, quantity) "
            f"VALUES ({id}, '{name}', '{descript}', {qnt});"
        )
        self.connection.commit()

    def delete_product_by_id(self, id):
        self.cursor.execute(
            f"DELETE FROM products "
            f"WHERE id = {id};"
        )
        self.connection.commit()

    def get_detailed_orders(self):
        self.cursor.execute(
            "SELECT orders.id, customers.name, products.name, "
            "products.description, orders.order_date "
            "FROM orders "
            "JOIN customers ON orders.customer_id = customers.id "
            "JOIN products ON orders.product_id = products.id"
        )

        return self.cursor.fetchall()
