numbers = [
    243, -279, 395, 130, 89, 269, 861, 669, 939, 367, -46, 710,
    841, -280, -244, 274, -132, 273, 418, 432, -341, 437, 360,
    960, 195, 792, 106, 461, -35, 980, -80, 540, -358, 69, -26,
    -416, 597, 96, 533, 232, 755, 894, 331, 323, -383, -386, 231,
    436, 553, 967, 166, -151, 772, 434, 325, 301, 275, 431, 556,
    728, 558, 702, 463, 127, 984, 212, 876, -287, -16, -177, 577,
    604, 116, 500, 653, 669, 916, 802, 817, 762, -210, -353, 144,
    -351, 777, 805, 692, 22, -303, 249, 190, 411, 236, -274, 174,
    380, 71, 124, -85, 430
]


def func(lst, length):
    def rec(num):
        if num < length:
            print(f'Элемент {num}: {lst[num]}')
            rec(num + 1)

    rec(0)


func(numbers, len(numbers))
