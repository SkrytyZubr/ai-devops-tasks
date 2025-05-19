### Jak działa to wyrażenie regularne

```regex
^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$
```

1. `^` i `$` - oznaczają początek i koniec ciągu, wymuszając dopasowanie całego tekstu
2. Główny wzorzec `(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)` dopasowuje liczby 0-255:
   - `25[0-5]` - dopasowuje 250-255
   - `2[0-4][0-9]` - dopasowuje 200-249
   - `[01]?[0-9][0-9]?` - dopasowuje 0-199
3. `\.` - dopasowuje kropkę (znak kropki musi być eskejpowany)
4. `{3}` - powtarza poprzedni wzorzec dokładnie 3 razy (pierwsze trzy oktety z kropkami)
5. Na końcu wzorzec jest powtórzony jeszcze raz bez kropki (czwarty oktet)

### Testy

**Poprawne adresy IPv4:**
- `192.168.1.1` - ✅ Standardowy adres lokalny
- `127.0.0.1` - ✅ Localhost
- `0.0.0.0` - ✅ Adres "każdy interfejs"
- `255.255.255.255` - ✅ Broadcast
- `10.0.0.1` - ✅ Prywatny adres klasy A

**Niepoprawne adresy:**
- `192.168.1` - ❌ Za mało oktetów
- `192.168.1.1.1` - ❌ Za dużo oktetów
- `192.168.1.256` - ❌ Wartość oktetu > 255
- `192.168.01.1` - ❌ Niepotrzebny wiodący zero
- `192.168.1.1a` - ❌ Zawiera niedozwolone znaki
- `192.168.1.` - ❌ Brakuje ostatniego oktetu
- `.192.168.1.1` - ❌ Rozpoczyna się od kropki

To wyrażenie regularne dokładnie sprawdza, czy adres IP jest w formacie IPv4 i czy każdy oktet jest w prawidłowym zakresie wartości.
