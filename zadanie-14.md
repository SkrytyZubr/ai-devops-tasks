May 19 10:15:32 server dockerd[1234]: time="2025-05-19T10:15:32.123456789Z" level=info msg="Container 78a2b3c4 health status changed from starting to healthy"
May 19 10:16:45 server dockerd[1234]: time="2025-05-19T10:16:45.987654321Z" level=info msg="Container 78a2b3c4 failed to connect to 172.17.0.3:5432: connection refused"
May 19 10:16:47 server dockerd[1234]: time="2025-05-19T10:16:47.246813579Z" level=warning msg="Container 78a2b3c4 health status changed from healthy to unhealthy"

Te logi pokazują zmiany stanu zdrowia kontenera Docker o ID 78a2b3c4:

1. 10:15:32 - Kontener zmienił status ze "starting" na "healthy", co oznacza, że pomyślnie uruchomił się i przeszedł testy zdrowia.

2. 10:16:45 - Wystąpił problem z połączeniem do bazy danych PostgreSQL (port 5432) na adresie 172.17.0.3 - połączenie zostało odrzucone.

3. 10:16:47 - W konsekwencji problemu z połączeniem, status zdrowia kontenera zmienił się z "healthy" na "unhealthy".

Problem prawdopodobnie dotyczy niedostępności bazy danych PostgreSQL, do której kontener próbuje się połączyć.
