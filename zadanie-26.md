## Błędy w Jenkinsfile

1. Literówka `stesp` zamiast `steps` w etapie Build
2. Niepoprawne polecenie `npm build` - powinno być `npm run build`
3. Blok `when` jest umieszczony po bloku `steps`, podczas gdy powinien być przed nim
4. Brak poświadczeń/konfiguracji dla polecenia `docker push`
5. Brak pełnej nazwy obrazu z rejestrem dla `docker push`

## Poprawiona wersja

```groovy
pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'npm install'
                sh 'npm run build'
            }
        }
        
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
        
        stage('Deploy') {
            when {
                branch 'master'
            }
            steps {
                withCredentials([string(credentialsId: 'docker-registry-credentials', variable: 'DOCKER_CREDENTIALS')]) {
                    sh 'echo $DOCKER_CREDENTIALS | docker login -u username --password-stdin'
                    sh 'docker build -t registry.example.com/myapp:latest .'
                    sh 'docker push registry.example.com/myapp:latest'
                }
            }
        }
    }
    
    post {
        always {
            sh 'docker logout'
        }
    }
}
```

## Wyjaśnienie poprawek

1. **Poprawka literówki** - Zmieniono `stesp` na `steps` w etapie Build.

2. **Poprawne polecenie npm** - Zmieniono `npm build` na `npm run build`, co jest standardowym sposobem uruchamiania skryptów z package.json.

3. **Prawidłowa kolejność bloków** - Przeniesiono blok `when` przed blok `steps` zgodnie z wymaganą składnią Jenkins Pipeline.

4. **Dodano uwierzytelnianie Docker** - Użyto `withCredentials` do bezpiecznego uwierzytelniania w rejestrze Docker.

5. **Pełna nazwa obrazu** - Dodano nazwę rejestru do obrazu Docker, aby `push` działał poprawnie.

6. **Dodano sekcję post** - Dodano wylogowanie z rejestru Docker po zakończeniu, co jest dobrą praktyką bezpieczeństwa.

Dodatkowo poprawiłem formatowanie dla lepszej czytelności, dodając odstępy między etapami.
