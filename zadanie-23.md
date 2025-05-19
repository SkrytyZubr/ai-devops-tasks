## Analiza złożoności zoptymalizowanego algorytmu

### Złożoność czasowa: O(n)
- Algorytm wykonuje tylko jedną iterację przez tablicę wejściową
- Operacje `has()` i `add()` na obiekcie Set mają złożoność O(1) w średnim przypadku
- Dzięki temu cały algorytm ma liniową złożoność czasową

### Złożoność pamięciowa: O(n)
- W najgorszym przypadku do zbioru `seen` dodamy wszystkie elementy tablicy
- Dodatkowo tablica `pairs` może zawierać do O(n) par w najgorszym przypadku

## Opis optymalizacji

Algorytm został zoptymalizowany poprzez zastosowanie techniki "hash table lookup":

1. Zamiast zagnieżdżonych pętli, używamy pojedynczej pętli i struktury danych Set
2. Dla każdej liczby `num` obliczamy jej dopełnienie `complement = targetSum - num`
3. Sprawdzamy, czy dopełnienie już wystąpiło wcześniej (jest w zbiorze `seen`)
4. Jeśli tak, znaleźliśmy parę i dodajemy ją do wyników
5. Następnie dodajemy bieżącą liczbę do zbioru widzianych elementów

Ta technika zamienia problem wyszukiwania par na problem wyszukiwania pojedynczej wartości w zbiorze, co jest znacznie wydajniejsze. Zamiast sprawdzania każdej możliwej pary (n²), sprawdzamy tylko raz dla każdego elementu, czy jego dopełnienie istnieje (n).

Główną zaletą jest redukcja złożoności z kwadratowej O(n²) do liniowej O(n), co daje ogromną przewagę wydajnościową dla dużych zbiorów danych.
