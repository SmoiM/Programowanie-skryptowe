import sys

def addCanal(kanal, key):
    if key in kanal:
        print ("Kanal " + key + " juz istnieje")
    else:
        kanal[key] = []

def removeCanal(kanal, key):
    if key in kanal:
        del kanal[key]
    else:
        print("Kanal " + key + " nie istnieje")

def addArticle(kanal, key, article):
    if article in kanal[key]:
        print ("Artykul " + article + " juz istnieje")
    else:
        kanal[key].append(article)

def removeArticle(kanal, key, article):
    if article in kanal[key]:
        kanal[key].remove(article)
    else:
        print ("Artykul " + article + " nie istnieje")
        
def numberOfArticles(kanal, key):
    return len(kanal[key])

kanal = {}

try:
    sys.argv[1]
    istnieje = 1
    max = int(sys.argv[1])

except:
    istnieje = 0

try:
    while True:
        choice = (input("\n***\n1 - dodaj kanal \t2 - usun kanal\n3 - dodaj artykul\t4 - usun artykul\n***\nWybor: "))
        match choice:
            case '1':
                text = str(input("\nPodaj nazwe kanalu do dodania: "))
                pom = text.split(', ')
                for i in pom:
                    addCanal(kanal, i)

            case '2':
                text = str(input("\nPodaj nazwe kanalu do usuniecia: "))
                pom = text.split(', ')
                for i in pom:
                    removeCanal(kanal, i)

            case '3':
                kan = str(input("\nPodaj kanal do ktorego chcesz dodac artykul: "))   
                if kan not in kanal:
                    print("Nie ma takiego kanalu")
                else:             
                    text = str(input())
                    pom = text.split(', ')
                    for i in pom:
                        ilosc = numberOfArticles(kanal, kan)
                        match istnieje:
                            case 1:     # uzytkownik podal max liczbe artykulow w kanala
                                if ilosc < max:
                                    addArticle(kanal, kan, i)
                                else:
                                    print("Przekroczono dopuszczalna liczbe artykolow, czyli", max)
                            case 0:     # dowolna liczba artykulow dozwolona
                                addArticle(kanal, kan, i)

            case '4':
                kan = str(input("\nPodaj kanal z ktorego chcesz usunac artykul: "))
                if kan not in kanal:
                    print("Nie ma takiego kanalu")
                else:
                    text = str(input())
                    pom = text.split(', ')
                    for i in pom:
                        removeArticle(kanal, kan, i)
            case _:
                print ("Niepoprawny wybor :(")
except:
    print(kanal)

