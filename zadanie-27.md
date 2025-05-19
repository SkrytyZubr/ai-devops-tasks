# Wyjaśnienie zależności między etapami pipeline'u CI/CD

## Etapy początkowe
1. **Checkout kodu** → **Instalacja zależności**:
   - Najpierw pobieramy kod źródłowy, aby mieć dostęp do plików projektu
   - Następnie instalujemy zależności, które są niezbędne do budowania i testowania aplikacji

2. **Instalacja zależności** → **Budowanie aplikacji**:
   - Po zainstalowaniu wszystkich bibliotek i narzędzi, możemy przystąpić do kompilacji/budowania aplikacji
   - Ten etap tworzy artefakty potrzebne w kolejnych krokach (np. pliki JS, CSS, HTML)

## Równoległe etapy weryfikacji
Po zbudowaniu aplikacji, następujące etapy mogą być wykonywane równolegle, co przyspiesza pipeline:

3. **Budowanie** → **Testy jednostkowe / Analiza statyczna / Skanowanie bezpieczeństwa**:
   - **Testy jednostkowe**: Weryfikują poprawność poszczególnych komponentów
   - **Analiza statyczna**: Sprawdza jakość kodu (np. SonarQube)
   - **Skanowanie bezpieczeństwa**: Wykrywa podatności w kodzie i zależnościach

## Konteneryzacja i testy integracyjne
4. **Weryfikacja** → **Budowanie obrazu Docker**:
   - Dopiero po pozytywnej weryfikacji kodu budujemy obraz Docker
   - Zapobiega to tworzeniu wadliwych obrazów

5. **Obraz Docker** → **Publikacja w rejestrze** → **Testy integracyjne**:
   - Obraz musi być opublikowany w rejestrze, aby był dostępny dla środowisk testowych
   - Testy integracyjne używają opublikowanego obrazu do weryfikacji współpracy komponentów

## Wdrożenie i weryfikacja
6. **Testy integracyjne** → **Wdrożenie na Staging** → **Testy E2E**:
   - Po potwierdzeniu integracji komponentów, aplikacja jest wdrażana na środowisko staging
   - Testy end-to-end weryfikują działanie całej aplikacji w warunkach zbliżonych do produkcyjnych

7. **Testy E2E** → **Zatwierdzenie wdrożenia**:
   - Bramka zatwierdzenia wymaga ludzkiej decyzji przed wdrożeniem na produkcję
   - Zapewnia dodatkową warstwę kontroli dla krytycznych zmian

8. **Zatwierdzenie** → **Wdrożenie na Produkcję** → **Weryfikacja wdrożenia**:
   - Po zatwierdzeniu następuje wdrożenie na środowisko produkcyjne
   - Weryfikacja potwierdza poprawność działania aplikacji na produkcji

Ta struktura zapewnia stopniowe budowanie pewności co do jakości kodu i aplikacji przed jej wdrożeniem na produkcję, minimalizując ryzyko wprowadzenia błędów.
