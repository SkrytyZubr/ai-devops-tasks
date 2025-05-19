function fetchUserData(userId) {
  return fetch(`https://api.example.com/users/${userId}`)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      return {
        name: data.name,
        email: data.email,
        lastLogin: new Date(data.lastLoginTimestamp)
      };
    })
    .catch(error => {
      console.error('Fetch error:', error);
      return null;
    });
}

/**
 * Pobiera dane użytkownika z API na podstawie jego identyfikatora
 * 
 * @param {string|number} userId - Identyfikator użytkownika
 * @returns {Promise<Object|null>} Promise rozwiązujący się do obiektu z danymi użytkownika lub null w przypadku błędu
 * @property {string} name - Imię i nazwisko użytkownika
 * @property {string} email - Adres email użytkownika
 * @property {Date} lastLogin - Data ostatniego logowania jako obiekt Date
 * @throws {Error} Błąd HTTP jeśli status odpowiedzi nie jest w zakresie 200-299
 * @example
 * // Pobierz dane użytkownika o id 123
 * fetchUserData(123)
 *   .then(user => {
 *     if (user) {
 *       console.log(`Użytkownik: ${user.name}, Email: ${user.email}`);
 *     } else {
 *       console.log('Nie udało się pobrać danych użytkownika');
 *     }
 *   });
 */
function fetchUserData(userId) {
  return fetch(`https://api.example.com/users/${userId}`)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      return {
        name: data.name,
        email: data.email,
        lastLogin: new Date(data.lastLoginTimestamp)
      };
    })
    .catch(error => {
      console.error('Fetch error:', error);
      return null;
    });
}