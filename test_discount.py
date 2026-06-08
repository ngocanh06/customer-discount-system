from discount import calculate_discount, Discount


# class DummyCustomer:
#     def __init__(self, total_spent):
#         self.total_spent = total_spent


# class DummyOrder:
#     def __init__(self, total_price):
#         self.total_price = total_price


def test_tc01():
    # TC01: tổng giá trị mua hàng trước đơn hàng 60.000.000, giá trị đơn hàng hiện tại 2.000.000
    assert calculate_discount(60000000) == 0.1

    # customer = DummyCustomer(60000000)
    # order = DummyOrder(2000000)
    # Discount(customer).apply_discount(order)
    # assert order.total_price == 1800000.0


def test_tc02():
    # TC02: tổng giá trị mua hàng trước đơn hàng 30.000.000, giá trị đơn hàng hiện tại 2.000.000
    assert calculate_discount(30000000) == 0.0

    # customer = DummyCustomer(30000000)
    # order = DummyOrder(2000000)
    # Discount(customer).apply_discount(order)
    # assert order.total_price == 2000000


def test_tc03():
    # TC03: tổng giá trị mua hàng trước đơn hàng 49.000.000, giá trị đơn hàng hiện tại 2.000.000
    assert calculate_discount(49000000) == 0.0

    # customer = DummyCustomer(49000000)
    # order = DummyOrder(2000000)
    # Discount(customer).apply_discount(order)
    # assert order.total_price == 2000000