def total(values):
    if not all(isinstance(value, (int, float)) for value in values):
        raise TypeError("values must be numeric")
    return sum(values)
