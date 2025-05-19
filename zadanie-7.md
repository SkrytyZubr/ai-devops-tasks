
Read file: check_docker.sh
Wyjaśnienie skryptu check_docker.sh linia po linii:

`#!/bin/bash` - To jest tzw. "shebang", który informuje system, że skrypt powinien być wykonany przez interpreter bash.

`# Sprawdź, czy usługa Docker działa` - To jest komentarz, który opisuje, co robi następna część kodu.

`if systemctl is-active --quiet docker; then` - Ta linia sprawdza, czy usługa Docker jest aktywna (uruchomiona). Polecenie `systemctl is-active` sprawdza stan usługi, a flaga `--quiet` powoduje, że nie wyświetla żadnych komunikatów.

`echo "Docker jest już uruchomiony"` - Jeśli Docker jest uruchomiony, skrypt wyświetla ten komunikat.

`else` - Jeśli Docker nie jest uruchomiony, wykonywany jest kod po tej linii.

`echo "Docker nie jest uruchomiony. Próba uruchomienia..."` - Wyświetla komunikat informujący o próbie uruchomienia Dockera.

`sudo systemctl start docker` - Ta komenda próbuje uruchomić usługę Docker z uprawnieniami administratora (sudo).

`if systemctl is-active --quiet docker; then` - Ponownie sprawdza, czy Docker został pomyślnie uruchomiony.

`echo "Docker został pomyślnie uruchomiony"` - Jeśli Docker został uruchomiony, wyświetla komunikat o sukcesie.

`else` - Jeśli Docker nadal nie działa, wykonywany jest kod po tej linii.

`echo "Nie udało się uruchomić Dockera. Sprawdź logi: sudo journalctl -u docker"` - Wyświetla komunikat o błędzie i podpowiada, jak sprawdzić logi Dockera.

`exit 1` - Kończy działanie skryptu z kodem błędu 1, co oznacza, że wystąpił problem.

`fi` - Zamyka drugi blok warunkowy (if).

`fi` - Zamyka pierwszy blok warunkowy (if).

`exit 0` - Kończy działanie skryptu z kodem 0, co oznacza, że wszystko przebiegło pomyślnie.
