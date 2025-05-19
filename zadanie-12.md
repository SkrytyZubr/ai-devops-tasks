def find_duplicates(list_of_items):
    duplicates = []
    for i in range(len(list_of_items)):
        for j in range(i+1, len(list_of_items)):
            if list_of_items[i] == list_of_items[j] and list_of_items[i] not in duplicates:
                duplicates.append(list_of_items[i])
    return duplicates

Tak, ten kod można znacznie zoptymalizować. Aktualna implementacja ma złożoność czasową O(n²), co jest nieefektywne dla dużych list.

Oto zoptymalizowana wersja z złożonością O(n):

```python
def find_duplicates(list_of_items):
    seen = set()
    duplicates = set()
    
    for item in list_of_items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
            
    return list(duplicates)
```

Optymalizacje:
1. Używam `set` zamiast listy do sprawdzania obecności elementów, co daje złożoność O(1) zamiast O(n)
2. Przechodzę przez listę tylko raz zamiast zagnieżdżonych pętli
3. Używam drugiego zbioru do przechowywania duplikatów, co eliminuje potrzebę sprawdzania `not in duplicates`
4. Na końcu konwertuję zbiór duplikatów z powrotem na listę

Ta implementacja jest znacznie wydajniejsza, szczególnie dla dużych zbiorów danych, i zachowuje tę samą funkcjonalność.
