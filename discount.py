def calculate_discount(total_before, order_value):
    """Tính số tiền giảm dựa trên tổng trước và giá trị đơn hàng hiện tại."""
    total_after = total_before + order_value
    if total_after >= 50000000:
        return order_value * 0.10
    return 0
