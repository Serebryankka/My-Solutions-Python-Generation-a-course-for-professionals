import sys
from decimal import Decimal, InvalidOperation

total_num = 0
total_no_num = 0
for line in sys.stdin:
    try:
        total_num += Decimal(line.rstrip())
    except InvalidOperation:
        total_no_num += 1

print(total_num)
print(total_no_num)
