def print_good_dates(data):
    print(*sorted([d.strftime('%B %d, %Y') for d in data if int(d.year) == 1992 and int(d.month) + int(d.day) == 29]), sep='\n')
    
