# Jak działa skrypt do komunikacji z Jenkins API

## Użyte biblioteki

1. **requests** - główna biblioteka do wykonywania żądań HTTP do Jenkins API
2. **sys** - obsługa wyjścia z programu i argumentów systemowych
3. **json** - parsowanie odpowiedzi JSON z API
4. **argparse** - parsowanie argumentów wiersza poleceń
5. **HTTPBasicAuth** (z requests.auth) - obsługa uwierzytelniania HTTP Basic
6. **urljoin** (z urllib.parse) - poprawne łączenie URL bazowego z endpointami

## Struktura i działanie

Skrypt jest zorganizowany w klasę `JenkinsAPI`, która enkapsuluje komunikację z API Jenkins:

1. **Inicjalizacja** - ustawia bazowy URL i dane uwierzytelniające
2. **_make_request** - metoda pomocnicza wykonująca żądania HTTP z obsługą błędów
3. **list_jobs** - pobiera listę wszystkich zadań
4. **get_job_info** - pobiera szczegółowe informacje o zadaniu
5. **get_build_status** - sprawdza status konkretnego buildu
6. **build_job** - uruchamia zadanie (z parametrami lub bez)
7. **_get_crumb** - obsługuje tokeny CSRF wymagane przez Jenkins

Funkcja `main()` obsługuje argumenty wiersza poleceń i wywołuje odpowiednie metody klasy.

## Obsługa błędów

Skrypt zawiera rozbudowaną obsługę błędów:
- Sprawdzanie kodów odpowiedzi HTTP
- Obsługa problemów z połączeniem
- Obsługa timeoutów
- Walidacja odpowiedzi JSON
- Informacyjne komunikaty błędów

## Przykładowe polecenia

### 1. Listowanie wszystkich zadań

```bash
python jenkins_api.py --url http://jenkins.example.com/ --username user --token abcd1234 list
```

### 2. Sprawdzanie statusu ostatniego buildu

```bash
python jenkins_api.py --url http://jenkins.example.com/ --username user --token abcd1234 status my-project
```

### 3. Sprawdzanie statusu konkretnego buildu

```bash
python jenkins_api.py --url http://jenkins.example.com/ --username user --token abcd1234 status my-project --build 42
```

### 4. Uruchamianie zadania bez parametrów

```bash
python jenkins_api.py --url http://jenkins.example.com/ --username user --token abcd1234 build my-project
```

### 5. Uruchamianie zadania z parametrami

```bash
python jenkins_api.py --url http://jenkins.example.com/ --username user --token abcd1234 build my-project --param BRANCH master --param ENVIRONMENT staging
```

Skrypt można łatwo rozszerzyć o dodatkowe funkcje, takie jak anulowanie buildów, pobieranie logów czy zarządzanie konfiguracją zadań.
