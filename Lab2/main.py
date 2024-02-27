#-*-coding: utf-8-*-

# 1. Zdefiniuj dwie zmienne napisowe (lancuch1, lancuch2), a każda z nich ma zawierać wielolinijkowy tekst w języku polskim, kodowanie UTF-8


# Pierwszy sposób zapisywania wielolinijkowego tekstu
lancuch1 = '''Państwo Dursleyowie spod numeru czwartego przy Privet
Drive mogli z dumą twierdzić, że są całkowicie normalni,
chwała Bogu. Byli ostatnimi ludźmi, których można by
posądzić o udział w czymś dziwnym lub tajemniczym, bo po
prostu nie wierzyli w takie bzdury.'''

# Drugi sposób zapisywania wielolinijkowego tekstu
lancuch2 = "Pan Dursley był dyrektorem firmy Grunnings produkującej świdry.\nBył to rosły, otyły mężczyzna pozbawiony szyi, za to wyposażony w wielkie wąsy.\nNatomiast pani Dursley była drobną blondynką i miała szyję dwukrotnie dłuższą od\nnormalnej, co bardzo jej pomagało w życiu, ponieważ większość dnia spędzała na podglądaniu sąsiadów.\nSyn Dursleyów miał na imię Dudley, a rodzice uważali go za najwspanialszego chłopca na świecie."

# 2. Spowoduj aby połączona zawartość zmiennych lancuch1 oraz lancuch2 została trzykrotnie wypisana (powielona) na ekran — proszę nie używać pętli. Ponadto operacja łączenia i powielania ma być zapisana w jednej linii

print (3 * (lancuch1 + lancuch2))

# 3. Zdefiniuj zmienną lancuch zawierającą dowolny tekst

lancuch = 'Pan Dursley zatrzymał się, jakby mu nogi wrosły w chodnik.'

# 4. Za pomocą funkcji 'print', bez użycia pętli, wypisz:
#       pierwszy znak łańcucha
print(lancuch[0])
#       dwa pierwsze znaki
print(lancuch[:1])
#       wszystkie znaki, za wyjątkiem dwóch pierwszych znaków
print(lancuch[2:])
#       przedostatni znak łańcucha
print(lancuch[-2])
#       trzy ostatnie znaki
print(lancuch[-3:])
#       wszystkie znaki na pozycjach parzystych
print(lancuch[1::2]) # Pozycje parzyste w tekscie, czyli nieparzyste indeksy dla Pythona

# 5. Proszę sprawdzić czy łańcuchy znaków mogą być modyfikowane tzn. czy można przypisać nową wartość do zaindeksowanej pozycji łańcucha
try:
    lancuch[0] = 'D'
except:
    print('Nie da się modyfikować łancuchów znaków')