const sum = require('./sum');

test('poprawnie dodaje 1 + 2 do wyniku 3', () => {
  expect(sum(1, 2)).toBe(3);
});

test('poprawnie dodaje liczby ujemne', () => {
  expect(sum(-1, -2)).toBe(-3);
});

test('poprawnie dodaje zero', () => {
  expect(sum(0, 5)).toBe(5);
});