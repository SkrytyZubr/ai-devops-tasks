/**
 * Sprawdza, czy podany ciąg znaków jest poprawnym adresem IPv4
 * @param {string} ip - Ciąg znaków do sprawdzenia
 * @returns {boolean} - Zwraca true jeśli ciąg jest poprawnym adresem IPv4, w przeciwnym razie false
 */
function isValidIPv4(ip) {
  if (!ip || typeof ip !== 'string') {
    return false;
  }
  
  const ipv4Regex = /^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
  
  return ipv4Regex.test(ip);
}

// Przykłady użycia:
console.log('192.168.1.1:', isValidIPv4('192.168.1.1'));       // true
console.log('127.0.0.1:', isValidIPv4('127.0.0.1'));           // true
console.log('0.0.0.0:', isValidIPv4('0.0.0.0'));               // true
console.log('255.255.255.255:', isValidIPv4('255.255.255.255')); // true
console.log('192.168.1:', isValidIPv4('192.168.1'));           // false
console.log('192.168.1.256:', isValidIPv4('192.168.1.256'));   // false
console.log('192.168.01.1:', isValidIPv4('192.168.01.1'));     // true (JavaScript regex traktuje to jako poprawne)
console.log('a.b.c.d:', isValidIPv4('a.b.c.d'));               // false
console.log(':', isValidIPv4(''));                             // false
console.log(null, isValidIPv4(null));                          // false

