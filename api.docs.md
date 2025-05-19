# Endpoint: GET /api/users

## Opis
Zwraca paginowaną listę użytkowników. Wyniki mogą być filtrowane według roli użytkownika.

## Parametry zapytania

| Parametr | Typ    | Wymagany | Opis                                            | Domyślna wartość |
|----------|--------|----------|------------------------------------------------|-----------------|
| page     | number | Nie      | Numer strony wyników                           | 1               |
| limit    | number | Nie      | Liczba wyników na stronę (maksymalnie 100)     | 10              |
| role     | string | Nie      | Filtrowanie użytkowników według roli           | -               |

## Przykładowe żądanie

```http
GET /api/users?page=2&limit=5&role=admin
```

## Przykładowa odpowiedź

```json
{
  "status": "success",
  "data": {
    "users": [
      {
        "id": "6",
        "username": "john.doe",
        "email": "john.doe@example.com",
        "role": "admin",
        "createdAt": "2023-03-15T14:30:45Z"
      },
      {
        "id": "7",
        "username": "jane.smith",
        "email": "jane.smith@example.com",
        "role": "admin",
        "createdAt": "2023-04-02T09:15:22Z"
      },
      {
        "id": "12",
        "username": "admin.user",
        "email": "admin.user@example.com",
        "role": "admin",
        "createdAt": "2023-05-18T11:42:10Z"
      }
    ]
  },
  "pagination": {
    "total": 8,
    "pages": 2,
    "currentPage": 2,
    "limit": 5,
    "hasNextPage": false,
    "hasPrevPage": true
  }
}
```

## Kody odpowiedzi

| Kod  | Opis                                                  |
|------|-------------------------------------------------------|
| 200  | Sukces - zwraca listę użytkowników                    |
| 400  | Błędne zapytanie - nieprawidłowe parametry            |
| 401  | Brak autoryzacji - wymagane uwierzytelnienie          |
| 403  | Zabronione - brak uprawnień do listy użytkowników     |
| 500  | Błąd serwera - problem z przetwarzaniem żądania       |
