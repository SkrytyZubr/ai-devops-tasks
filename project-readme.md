# Simple Task API

REST API do zarządzania zadaniami, napisane w Node.js z Express i MongoDB.

## Opis

Simple Task API umożliwia zarządzanie zadaniami poprzez interfejs RESTful. Aplikacja pozwala na tworzenie, odczytywanie, aktualizację i usuwanie zadań, a także filtrowanie ich według statusu i priorytetów. System zawiera również prostą autoryzację użytkowników.

## Instalacja

1. Sklonuj repozytorium:
   ```
   git clone https://github.com/username/simple-task-api.git
   cd simple-task-api
   ```

2. Zainstaluj zależności:
   ```
   npm install
   ```

3. Skonfiguruj zmienne środowiskowe:
   ```
   cp .env.example .env
   ```
   Edytuj plik `.env` i ustaw odpowiednie wartości dla:
   - `MONGODB_URI` - adres bazy danych MongoDB
   - `PORT` - port serwera (domyślnie 3000)
   - `JWT_SECRET` - sekret do generowania tokenów JWT

4. Uruchom serwer:
   ```
   npm start
   ```

## Użycie

### Autoryzacja

API używa tokenów JWT do autoryzacji. Aby uzyskać token, należy wykonać żądanie POST na endpoint `/api/auth/login`.

Przykład:
```
POST /api/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}
```

Otrzymany token należy dołączać do nagłówka `Authorization` w formie `Bearer {token}` przy kolejnych żądaniach.

## Endpointy API

### Autoryzacja

- `POST /api/auth/register` - rejestracja nowego użytkownika
- `POST /api/auth/login` - logowanie i uzyskanie tokenu JWT

### Zadania

- `GET /api/tasks` - pobieranie listy zadań
  - Parametry: `status`, `priority`, `page`, `limit`
- `GET /api/tasks/:id` - pobieranie szczegółów zadania
- `POST /api/tasks` - tworzenie nowego zadania
- `PUT /api/tasks/:id` - aktualizacja zadania
- `DELETE /api/tasks/:id` - usuwanie zadania

### Przykład struktury zadania

```json
{
  "title": "Dokończyć raport",
  "description": "Przygotować miesięczny raport sprzedaży",
  "status": "in-progress",
  "priority": "high",
  "dueDate": "2023-12-31T23:59:59Z"
}
```

## Licencja

MIT
