                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                "w")

czas = []
temp = 0
k = 1

for i in f.readlines():
    znajdz = re.compile(args.pathname)
    dopasowania = znajdz.findall(i)

    if dopasowania != []:
        znajdz = re.compile(r"[\d]{2}\/[a-zA-Z]{3}\/[\d]{4}:\d{2}:\d{2}:\d{2}")
        dopasowania = znajdz.findall(i)
        czas.append(datetime.strptime(*dopasowania, '%d/%b/%Y:%H:%M:%S'))

    # if (znajdz.findall(i)):
        # g.write(i)
        
f.close()

for data in czas:
    for i in range (k, len(czas)):
        odejmowanie = czas[i] - data
        if odejmowanie.total_seconds() <= 60:
            temp += 1
            break
        else:
            break
    k += 1

print('Views of the given website for given host equals:', len(czas) - temp)    
        
# python3 .\przetwarzanieTekstow.py --host 73.44.199.53 --pathname https://www.techstuds.com/blog access.log
# python3 .\przetwarzanieTekstow.py --host 69.5.90.115 --pathname https://www.google.com/ access.log
# python3 .\przetwarzanieTekstow.py access.log 




