def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
# Example usage
result = magic_calculation(3, 4, 5)
print(result)
