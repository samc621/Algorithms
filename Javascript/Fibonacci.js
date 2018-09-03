function fibonacci(depth) {
  let lastIndex = 0;
  let newIndex = 1;
  let phi = [];

  phi[0] = lastIndex;
  phi[1] = newIndex;
  for (i = 2; i < depth; i++) {
    let result = lastIndex + newIndex;
    phi[i] = result;
    lastIndex = newIndex;
    newIndex = result;
  }
  console.log(phi);
}

fibonacci(10);
