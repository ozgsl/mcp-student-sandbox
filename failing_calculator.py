# ...existing code...
def safe_divide_list(data, numerator=100, handle_zero="skip"):
    """
    handle_zero: "skip" -> atla, "none" -> None koy, "raise" -> hata fırlat
    """
    results = []
    for d in data:
        if d == 0:
            if handle_zero == "raise":
                raise ZeroDivisionError("Division by zero for element in data")
            if handle_zero == "none":
                results.append(None)
            # "skip" -> hiç ekleme
            continue
        results.append(numerator / d)
    return results
# ...existing code...