def remove_marks(text, marks):
    remove_marks.count += 1
    for mark in marks:
        text = text.replace(mark, '')
    return text

remove_marks.count = 0
