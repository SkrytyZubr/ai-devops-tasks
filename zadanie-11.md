Oto prosty test jednostkowy dla funkcji sum używający Jest:

```javascript
// sum.js
function sum(a, b) {
  return a + b;
}

module.exports = sum;
```

```javascript
// sum.test.js
const sum = require('./sum');

test('poprawnie dodaje 1 + 2 do wyniku 3', () => {
  expect(sum(1, 2)).toBe(3);
});

test('poprawnie dodaje liczby ujemne', () => {
  expect(sum(-1, -2)).toBe(-3);
});

test('poprawnie dodaje zero', () => {
  expect(sum(0, 5)).toBe(5);
});
```

Jest to popularny framework do testowania JavaScript, który zapewnia prostą składnię do pisania testów jednostkowych.

Instalacja Jest w projekcie:
1. Inicjalizacja projektu npm (jeśli jeszcze nie istnieje):
   ```
   npm init -y
   ```

2. Instalacja Jest jako zależność deweloperska:
   ```
   npm install --save-dev jest
   ```

3. Modyfikacja sekcji scripts w package.json:
   ```json
   "scripts": {
     "test": "jest"
   }
   ```

Uruchomienie testu:
```
npm test
```

Struktura plików projektu:
```
project/
├── node_modules/
├── sum.js           # Plik z funkcją
├── sum.test.js      # Plik z testami
├── package.json     # Konfiguracja npm
└── .gitignore       # Ignorowane pliki
```

Jest automatycznie wyszukuje pliki z rozszerzeniem .test.js lub znajdujące się w katalogu __tests__ i wykonuje zawarte w nich testy.
