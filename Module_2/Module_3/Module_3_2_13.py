from datetime import date
def main(data):
    data = sorted([date.fromisoformat(input()).strftime('%d/%m/%Y')  for _ in range(int(input()))])
    return "\n".join(data)
if __name__ == '__main__':
    print(main())
    
