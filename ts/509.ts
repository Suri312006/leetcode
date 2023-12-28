function fib(n: number): number {
  let memo = {};

  return recur_fib(n, memo);
}

function recur_fib(n: number, memo: object) {
  //base case
  if (n <=1){
    return n
  }
  else if (memo[n]) {
    console.log(memo[n])
    return memo[n];
  } else {
    const val:number = recur_fib(n - 2, memo) + recur_fib(n - 1, memo);
    memo[n] = val;
    return val;
  }
}

fib(10)