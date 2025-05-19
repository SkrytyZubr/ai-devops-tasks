# Jak używać Jenkins Configuration as Code (JCasC)

## Przygotowanie pliku konfiguracyjnego

1. Zapisz wygenerowany szablon YAML jako plik `jenkins.yaml`

2. Ustaw zmienne środowiskowe dla sekretów:
   ```bash
   export ADMIN_PASSWORD=bezpieczne_hasło
   export GITHUB_TOKEN=twój_token_github
   ```

## Instalacja i uruchomienie Jenkinsa z JCasC

### Metoda 1: Docker

1. **Utwórz plik Dockerfile**:
   ```dockerfile
   FROM jenkins/jenkins:lts
   
   # Zainstaluj sugerowane wtyczki
   RUN jenkins-plugin-cli --plugins \
       configuration-as-code \
       workflow-aggregator \
       git \
       pipeline-model-definition \
       docker-workflow \
       credentials \
       blueocean \
       role-strategy \
       timestamper \
       nodejs \
       docker-plugin
   
   # Skopiuj plik konfiguracyjny
   COPY jenkins.yaml /var/jenkins_home/jenkins.yaml
   
   # Ustaw zmienną środowiskową wskazującą na plik konfiguracyjny
   ENV CASC_JENKINS_CONFIG=/var/jenkins_home/jenkins.yaml
   
   # Ustaw uprawnienia
   USER root
   RUN chown jenkins:jenkins /var/jenkins_home/jenkins.yaml
   USER jenkins
   ```

2. **Zbuduj i uruchom kontener**:
   ```bash
   docker build -t jenkins-casc .
   
   docker run --name jenkins-casc \
     -p 8080:8080 -p 50000:50000 \
     -v jenkins_home:/var/jenkins_home \
     -v /var/run/docker.sock:/var/run/docker.sock \
     -e ADMIN_PASSWORD=bezpieczne_hasło \
     -e GITHUB_TOKEN=twój_token_github \
     jenkins-casc
   ```

### Metoda 2: Istniejąca instalacja Jenkinsa

1. **Zainstaluj wtyczkę Configuration as Code**:
   - Przejdź do "Manage Jenkins" > "Manage Plugins" > "Available"
   - Wyszukaj i zainstaluj "Configuration as Code"
   - Zrestartuj Jenkinsa

2. **Umieść plik konfiguracyjny**:
   - Skopiuj `jenkins.yaml` do katalogu `/var/lib/jenkins/` lub innego katalogu na serwerze

3. **Ustaw zmienną środowiskową**:
   - Edytuj plik konfiguracyjny Jenkinsa (np. `/etc/default/jenkins` na Ubuntu)
   - Dodaj: `CASC_JENKINS_CONFIG=/var/lib/jenkins/jenkins.yaml`
   - Alternatywnie, dodaj parametr JVM: `-Dcasc.jenkins.config=/var/lib/jenkins/jenkins.yaml`

4. **Zrestartuj Jenkinsa**:
   ```bash
   sudo systemctl restart jenkins
   ```

### Metoda 3: Docker Compose

1. **Utwórz plik docker-compose.yml**:
   ```yaml
   version: '3'
   services:
     jenkins:
       image: jenkins/jenkins:lts
       ports:
         - "8080:8080"
         - "50000:50000"
       volumes:
         - jenkins_home:/var/jenkins_home
         - ./jenkins.yaml:/var/jenkins_home/jenkins.yaml
         - /var/run/docker.sock:/var/run/docker.sock
       environment:
         - CASC_JENKINS_CONFIG=/var/jenkins_home/jenkins.yaml
         - ADMIN_PASSWORD=${ADMIN_PASSWORD}
         - GITHUB_TOKEN=${GITHUB_TOKEN}
       restart: always
   
   volumes:
     jenkins_home:
   ```

2. **Uruchom za pomocą Docker Compose**:
   ```bash
   docker-compose up -d
   ```

## Weryfikacja konfiguracji

1. Otwórz przeglądarkę i przejdź do `http://localhost:8080`

2. Zaloguj się jako `admin` z hasłem ustawionym w zmiennej `ADMIN_PASSWORD`

3. Sprawdź, czy konfiguracja została zastosowana:
   - Przejdź do "Manage Jenkins" > "Configuration as Code"
   - Kliknij "View Configuration" aby zobaczyć aktualną konfigurację

## Rozwiązywanie problemów

1. **Sprawdź logi Jenkinsa** w przypadku problemów:
   ```bash
   docker logs jenkins-casc
   ```

2. **Walidacja pliku YAML**:
   ```bash
   docker run -it --rm \
     -v $(pwd)/jenkins.yaml:/jenkins.yaml \
     jenkins/jenkins:lts \
     java -jar /usr/share/jenkins/jenkins.war \
     --plugin-dir=/usr/share/jenkins/ref/plugins/ \
     -Dcasc.jenkins.config=/jenkins.yaml \
     --check-configuration-as-code
   ```

3. **Eksport bieżącej konfiguracji** jako punkt odniesienia:
   - Przejdź do "Manage Jenkins" > "Configuration as Code" > "Download Configuration"

Jenkins Configuration as Code pozwala na wersjonowanie i automatyczne wdrażanie konfiguracji Jenkinsa, co jest kluczowym elementem podejścia "Infrastructure as Code".
