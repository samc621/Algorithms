function findMax(list) {
  let result = 0;
  for (i = 0; i < list.length; i++) {
    if (list[i] > result) {
      result = list[i];
    }
  }
  console.log(result);
}

findMax([1, 2, 18, 40, 6, 10]);
