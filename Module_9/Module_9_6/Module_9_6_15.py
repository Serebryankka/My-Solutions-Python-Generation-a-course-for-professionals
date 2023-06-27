def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    return dict(name=grades['name'], top_grade=max(grades['grades']))
  
