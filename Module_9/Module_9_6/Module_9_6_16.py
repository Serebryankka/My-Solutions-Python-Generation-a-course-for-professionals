def cyclic_shift(numbers: list[int | float], step: int) -> list[int]:
    if step < 0:
        for _ in range(abs(step)):
            numbers.append(numbers.pop(0))
    else:
        for _ in range(step):
            numbers.insert(0, numbers.pop())
