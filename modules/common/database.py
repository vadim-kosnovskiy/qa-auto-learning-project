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
            f"SELECT id, quantity "
            f"FROM products "
            f"WHERE id = {product_id};")

        return self.cursor.fetchall()

    def insert_product(self, id_, name, descript, qnt):
        self.cursor.execute(
            f"INSERT OR REPLACE INTO products(id, name, description, quantity) "
            f"VALUES ({id_}, '{name}', '{descript}', {qnt});"
        )
        self.connection.commit()

    def delete_product_by_id(self, id_):
        self.cursor.execute(
            f"DELETE FROM products "
            f"WHERE id = {id_};"
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

    def get_summary_product_qnt_by_name(self, prod_name):
        self.cursor.execute(
            f"SELECT SUM(quantity) "
            f"FROM products "
            f"WHERE '{prod_name}' LIKE name;"
        )

        return self.cursor.fetchone()

    def get_product_max_count_and_its_sum(self):
        self.cursor.execute(
            f"SELECT t.name, MAX(count_name), t.sum_qnt "
            f"FROM (SELECT name, COUNT(name) AS count_name, SUM(quantity) AS sum_qnt"
            f"      FROM products "
            f"      GROUP BY name) as t ;"
        )

        return self.cursor.fetchone()

    def insert_invalid_type_qnt(self, id_, name, descript, qnt):
        self.cursor.execute(
            f"INSERT OR REPLACE INTO products(id, name, description, quantity) "
            f"VALUES ({id_}, '{name}', '{descript}', '{qnt}');"
        )
        self.connection.commit()
