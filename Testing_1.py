def s_shipping_cost(weight, distance):
    """
    Tính phí vận chuyển dựa trên:
      - weight: trọng lượng (kg), float
      - distance: quãng đường (km), float
    Trả về: shipping_cost (float)
    """
    # Kiểm tra dữ liệu hợp lệ
    if weight < 0 or distance < 0:
        raise ValueError("weight hoặc distance không được âm")
    
    # Xác định đơn giá cơ bản
    if weight <= 1:
        base_rate = 1.0
    elif weight <= 5:
        base_rate = 1.5
    else:
        base_rate = 2.0
    
    # Tính phí cơ bản
    cost = base_rate * distance
    
    # Nếu quãng đường > 500km, cộng thêm phụ phí 10%
    if distance > 500:
        cost *= 1.1
    
    return cost

