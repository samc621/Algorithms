function Factorial(num) {
  let result = num;
  for (i = 1; i < num; i++) {
    result *= num - i;
  }
  console.log(result);
}

Factorial(5);
