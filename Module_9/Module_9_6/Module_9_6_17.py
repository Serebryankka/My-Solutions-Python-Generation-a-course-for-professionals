def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return {k: v for k, v in enumerate(matrix, 1)}
  
