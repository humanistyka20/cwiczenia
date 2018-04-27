# program wyznaczający liczby pierwsze w zakresie od 0 do X
#(pobierane od użytkownika)

import math

liczba = int(input('Podaj liczbę: ')) # zmieniamy na integer 

for sprawdzanaLiczba in range(0, liczba):
    liczbaPierwsza = 1 # zakładamy,że obecna liczba jest pierwsza
    for sprawdzanyDzielnik in range(2, int(math.sqrt(sprawdzanaLiczba)) + 1):
        # sprawdzamy od 2 do pierwiastka z podanej liczby-(math.sqrt) musi być + 1 - 
        # - włączenie górnej granicy zakresu 
        if sprawdzanaLiczba % sprawdzanyDzielnik == 0: # dzielimy podaną liczbę
            # na sprawdzany dzielnik, jeżeli reszta jest równa zero, liczba nie jest pierwsza
            liczbaPierwsza = 0
            break
    if liczbaPierwsza == 1:
        print(sprawdzanaLiczba) # jeżeli wynik to 1, liczba jest pierwsza
