Jakie są 5 kluczowych praktyk bezpieczeństwa dla aplikacji Dockerowych w środowisku produkcyjnym?

1. **Używaj obrazów z zaufanych źródeł** - korzystaj z oficjalnych obrazów lub twórz własne, unikaj nieznanych obrazów z publicznych repozytoriów, które mogą zawierać złośliwe oprogramowanie.

2. **Uruchamiaj kontenery jako użytkownik niepriwilegowany** - unikaj używania roota wewnątrz kontenera, dodając instrukcję `USER non-root-user` w Dockerfile i ustawiając `USER` na użytkownika bez uprawnień administratora.

3. **Implementuj zasadę najmniejszych uprawnień** - ograniczaj możliwości kontenera używając flag `--cap-drop=ALL` i dodając tylko niezbędne uprawnienia z `--cap-add`, oraz stosuj `read-only` dla systemów plików gdzie to możliwe.

4. **Skanuj obrazy pod kątem podatności** - używaj narzędzi jak Trivy, Clair lub Docker Scout do regularnego skanowania obrazów w poszukiwaniu znanych luk bezpieczeństwa.

5. **Izoluj sieci kontenerów** - twórz dedykowane sieci dla grup kontenerów, które muszą komunikować się ze sobą, ograniczając niepotrzebną komunikację między kontenerami i ekspozycję portów.

Jak mogę zaimplementować pierwszą z tych praktyk w moim Dockerfile i docker-compose.yml?

W Dockerfile:

```dockerfile
# Użyj oficjalnego obrazu z konkretnym tagiem (unikaj latest)
FROM node:18.16.1-alpine3.17

# Weryfikuj integralność pobranych pakietów
RUN apk add --no-cache --update \
    curl=8.0.1-r0 \
    && rm -rf /var/cache/apk/*

# Weryfikuj pobierane zewnętrzne zasoby za pomocą sum kontrolnych
ADD --checksum=sha256:a8ae0adbdef02b4d3cee84c7dd4019ac8cda5d711a2d10cffdfd401b4f0372ee https://example.com/app/package.tgz /app/

WORKDIR /app

# Kopiuj pliki z lokalnego kontekstu
COPY package*.json ./
RUN npm ci --only=production

# Kopiuj kod aplikacji
COPY . .

# Weryfikuj, że aplikacja działa poprawnie
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:3000/health || exit 1

# Uruchamiaj jako niepriwilegowany użytkownik
USER node

CMD ["node", "server.js"]
```

W docker-compose.yml:

```yaml
version: '3.8'

services:
  app:
    # Używaj własnych obrazów lub oficjalnych z konkretnym tagiem
    image: node:18.16.1-alpine3.17
    # Alternatywnie, buduj z lokalnego Dockerfile
    build:
      context: .
      dockerfile: Dockerfile
    # Dodaj etykiety dla lepszego zarządzania i audytu
    labels:
      org.opencontainers.image.source: "https://github.com/your-org/your-repo"
      org.opencontainers.image.vendor: "Your Company"
      org.opencontainers.image.revision: "${GIT_COMMIT}"
      org.opencontainers.image.created: "${BUILD_DATE}"
    # Unikaj używania woluminów zawierających wykonywalne pliki
    volumes:
      - ./data:/app/data:ro
  
  database:
    # Użyj oficjalnego obrazu z konkretnym tagiem
    image: postgres:15.3-alpine
    # Weryfikuj autentyczność obrazu (wymaga Docker Content Trust)
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 1G
```

Dodatkowe praktyki:
1. Włącz Docker Content Trust (`export DOCKER_CONTENT_TRUST=1`)
2. Regularnie aktualizuj obrazy bazowe
3. Dokumentuj źródło wszystkich obrazów w repozytorium
