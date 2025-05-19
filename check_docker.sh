#!/bin/bash

# Sprawdź, czy usługa Docker działa
if systemctl is-active --quiet docker; then
    echo "Docker jest już uruchomiony"
else
    echo "Docker nie jest uruchomiony. Próba uruchomienia..."
    
    # Próba uruchomienia usługi Docker
    sudo systemctl start docker
    
    # Sprawdź, czy uruchomienie się powiodło
    if systemctl is-active --quiet docker; then
        echo "Docker został pomyślnie uruchomiony"
    else
        echo "Nie udało się uruchomić Dockera. Sprawdź logi: sudo journalctl -u docker"
        exit 1
    fi
fi

exit 0