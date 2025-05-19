Proces konwersji JSON do CSV obejmuje następujące kroki i wyzwania:

1. **Identyfikacja struktury danych** - Analiza JSON do określenia struktury (zagnieżdżone obiekty, tablice) i mapowanie ich na płaską strukturę CSV.

2. **Definiowanie nagłówków** - Utworzenie pierwszego wiersza CSV z nazwami kolumn odpowiadającymi kluczom z JSON.

3. **Transformacja danych** - Konwersja każdego obiektu JSON na wiersz CSV.

4. **Obsługa wartości złożonych** - Największe wyzwanie, szczególnie przy tablicach jak `roles`:
   - Najprostsze rozwiązanie: łączenie wartości tablicy w jeden ciąg (np. `"admin,user"`)
   - Alternatywy: serializacja do JSON (`["admin","user"]`) lub tworzenie osobnych kolumn (`role_1`, `role_2`)

5. **Obsługa znaków specjalnych** - Wartości zawierające przecinki, cudzysłowy czy znaki nowej linii muszą być ujęte w cudzysłowy, a istniejące cudzysłowy podwojone.

6. **Obsługa wartości pustych** - Decyzja jak reprezentować wartości null/undefined (puste pole, "null", itp.).

7. **Spójność typów** - W przypadku różnych typów danych w tej samej kolumnie (np. liczba vs. string), konieczna jest standaryzacja.

W naszym przykładzie głównym wyzwaniem była reprezentacja tablicy `roles`, którą rozwiązano przez połączenie wartości przecinkami i ujęcie w cudzysłowy, co jest standardowym podejściem w CSV.
