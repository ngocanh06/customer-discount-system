# Khách hàng thân thiết giảm 10% giá trị đơn hàng (khách hàng có tổng giá trị mua hàng từ 50 triệu/năm)
class Discount:
    def __init__(self, customer):
        self.customer = customer

    def apply_discount(self, order):
        if self.customer.total_spent >= 50000000:
            discount_amount = order.total_price * 0.10
            order.total_price -= discount_amount
            print(f"Áp dụng giảm giá 10% cho khách hàng thân thiết. Số tiền giảm: {discount_amount:.2f}")
        else:
            print("Khách hàng không đủ điều kiện để được giảm giá.")


def calculate_discount(total_spent):
    """Trả về tỷ lệ giảm giá theo tổng mức chi tiêu của khách hàng."""
    return 0.10 if total_spent >= 50000000 else 0.0
