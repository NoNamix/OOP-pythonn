result = []

def divider(a, b):
    if a < b:
        raise ValueError("a")
    if b > 100:
        raise IndexError("b")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as e:
        print(f"Error: {e}")

print(result)