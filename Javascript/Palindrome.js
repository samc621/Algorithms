let result = true;

function Palindrome(word) {
  let max = word.length;
  for (i = 1; i < max + 1; i++) {
    if (word[i - 1] != word[max - i]) {
      result = false;
    }
  }
  console.log(result);
}

Palindrome("ayya");
