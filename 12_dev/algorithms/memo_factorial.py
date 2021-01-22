def memoize(fn):
    cache = {}
    def closure(*args):
        n = args[0]
        if n in cache:
            print("Fetching from cache", n)
            return cache[n]
        else:
            print("Calculating result", n)
            result = fn(n)
            cache[n] = result
            return result
    return closure

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

memoFactorial = memoize(factorial)
print(memoFactorial(5))
print(memoFactorial(6))
print(memoFactorial(6))

"""
const memoize = (fn) => {
  let cache = {};
  return (...args) => {
    let n = args[0];
    if (n in cache) {
      console.log('Fetching from cache', n);
      return cache[n];
    }
    else {
      console.log('Calculating result', n);
      let result = fn(n);
      cache[n] = result;
      return result;
    }
  }
}

const factorial = memoize(
  (x) => {
    if (x === 0) {
      return 1;
    }
    else {
      return x * factorial(x - 1);
    }
  }
);
console.log(factorial(5)); // calculated
console.log(factorial(5)); // calculated for 6 and cached for 5
"""
