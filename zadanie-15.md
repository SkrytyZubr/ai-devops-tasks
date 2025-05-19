function getEnvironmentConfig(env) {
  if (env === 'development') {
    return {
      apiUrl: 'http://localhost:3000/api',
      debug: true,
      timeout: 5000
    };
  } else if (env === 'testing') {
    return {
      apiUrl: 'http://test-server:3000/api',
      debug: true,
      timeout: 5000
    };
  } else if (env === 'staging') {
    return {
      apiUrl: 'https://staging.example.com/api',
      debug: false,
      timeout: 10000
    };
  } else if (env === 'production') {
    return {
      apiUrl: 'https://api.example.com',
      debug: false,
      timeout: 15000
    };
  } else {
    return {
      apiUrl: 'http://localhost:3000/api',
      debug: true,
      timeout: 5000
    };
  }
}

Ta funkcja getEnvironmentConfig zwraca różne konfiguracje w zależności od środowiska (env):
Dla development: lokalny URL API, włączone debugowanie, timeout 5s
Dla testing: URL API serwera testowego, włączone debugowanie, timeout 5s
Dla staging: URL API środowiska staging, wyłączone debugowanie, timeout 10s
Dla production: URL API produkcyjnego, wyłączone debugowanie, timeout 15s
Dla innych wartości: domyślnie konfiguracja development

```javascript
/**
 * Zwraca konfigurację dla określonego środowiska
 * @param {string} env - Nazwa środowiska
 * @returns {Object} Konfiguracja dla danego środowiska
 */
function getEnvironmentConfig(env) {
  const configs = {
    development: {
      apiUrl: 'http://localhost:3000/api',
      debug: true,
      timeout: 5000
    },
    testing: {
      apiUrl: 'http://test-server:3000/api',
      debug: true,
      timeout: 5000
    },
    staging: {
      apiUrl: 'https://staging.example.com/api',
      debug: false,
      timeout: 10000
    },
    production: {
      apiUrl: 'https://api.example.com',
      debug: false,
      timeout: 15000
    }
  };

  // Zwróć konfigurację dla danego środowiska lub konfigurację development jako domyślną
  return configs[env] || configs.development;
}
```
