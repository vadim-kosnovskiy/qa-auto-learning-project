import pytest


@pytest.mark.database
def test_database_connection(database):
    database.test_connection()


@pytest.mark.database
def test_check_all_users(database):
    users = database.get_all_users()
    print("\n", users)


@pytest.mark.database
def test_check_user_sergii(database):
    [(address, city, postalCode, country)] = (
        database.get_user_address_by_name("Sergii"))

    assert address == "Maydan Nezalezhnosti 1", (
        "Address is not Maydan Nezalezhnosti 1"
    )
    assert city == "Kyiv", "City is not Kyiv"
    assert postalCode == "3127", "ZIP code is not equal 3127"
    assert country == "Ukraine", "Country is not Ukraine"


@pytest.mark.database
def test_product_qnt_update(database):
    database.update_product_qnt_by_id(1, 25)
    [(id_, quantity,)] = database.select_product_qnt_by_id(1)

    assert quantity == 25, "Quantity is not equal 25"


@pytest.mark.database
def test_product_insert(database):
    database.insert_product(4, "печиво", "солодке", 30)
    [(id_, quantity,)] = database.select_product_qnt_by_id(4)

    assert quantity == 30, "Quantity is not equal 30"


@pytest.mark.database
def test_product_delete(database):
    database.insert_product(99, "тестові", "дані", 999)
    database.delete_product_by_id(99)
    rec_list = database.select_product_qnt_by_id(99)

    assert len(rec_list) == 0, "Product delete unsuccessfully"


@pytest.mark.database
def test_detailed_orders(database):
    orders = database.get_detailed_orders()
    [(orders_id, customers_name, products_name, description, order_date)] = orders
    print("\n", orders)

    assert len(orders) == 1, "Amount orders is not equal 1"
    assert orders_id == 1, "ID is not equal 1"
    assert customers_name == "Sergii", "Customers name is not Sergii"
    assert products_name == "солодка вода", "Product name is not 'солодка вода'"
    assert description == "з цукром", "Description is not 'з цукром'"


@pytest.mark.database
def test_summary_product_qnt_by_name(database):
    (sum_qnt,) = database.get_summary_product_qnt_by_name("молоко")

    assert sum_qnt == 25


@pytest.mark.database
def test_product_max_count_and_its_sum(database):
    (name, count_product, sum_qnt) = database.get_product_max_count_and_its_sum()

    assert name == "солодка вода", "Name is not 'солодка вода'"
    assert count_product == 3, "Count product is not 3"
    assert sum_qnt == 43, "Sum is not 43"
