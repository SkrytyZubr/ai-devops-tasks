### Opis rozwiązania

Funkcja `getCompletedTaskTitles` wykorzystuje łańcuch metod tablicowych JavaScript:

1. `filter()` - wybiera tylko zadania o statusie "completed"
2. `sort()` - sortuje przefiltrowane zadania według id w kolejności rosnącej
3. `map()` - transformuje każdy obiekt zadania, wybierając tylko pole `title`

Takie podejście jest zwięzłe, czytelne i funkcjonalne. Każda metoda zwraca nową tablicę, nie modyfikując oryginalnej.

### Przykład użycia

```javascript
const tasks = [
  { id: 3, title: "Zrobić zakupy", status: "completed" },
  { id: 1, title: "Napisać raport", status: "completed" },
  { id: 5, title: "Spotkanie z klientem", status: "pending" },
  { id: 2, title: "Opłacić rachunki", status: "completed" },
  { id: 4, title: "Przygotować prezentację", status: "in-progress" }
];

const completedTitles = getCompletedTaskTitles(tasks);
console.log(completedTitles);
// Wynik: ["Napisać raport", "Opłacić rachunki", "Zrobić zakupy"]
```
