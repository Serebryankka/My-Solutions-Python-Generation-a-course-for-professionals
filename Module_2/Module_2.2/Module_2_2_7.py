def task():
    word = input()
    words = (input() for _ in range(int(input())))
    vowels = 'ауоыиэяюёе'
    indexes = [i for i in range(len(word)) if word[i] in vowels]
    count_indexes = len(indexes)
    result = []
    for w in words:
        count = 0
        for i in range(len(w)):
            if w[i] in vowels:
                if i not in indexes:
                    break
                else:
                    count += 1
        if count == count_indexes:
            result.append(w)

    return result


if __name__ == '__main__':
    print(*task(), sep='\n')
    
