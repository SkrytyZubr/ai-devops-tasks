function findPairsOptimized(arr, targetSum) {
  const pairs = [];
  const seen = new Set();
  
  for (let num of arr) {
    const complement = targetSum - num;
    
    if (seen.has(complement)) {
      pairs.push([complement, num]);
    }
    
    seen.add(num);
  }
  
  return pairs;
}
