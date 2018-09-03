let min = 1;
let max = 1000000;
let lowerBound = min;
let higherBound = max;

let number = Math.floor(Math.random() * max) + min;

let count = 1;
function binarySearch(guess) {
  if (guess > number) {
    higherBound = guess;
    count++;
    binarySearch(Math.round((lowerBound + higherBound) / 2));
  } else if (guess < number) {
    lowerBound = guess;
    count++;
    binarySearch(Math.round((lowerBound + higherBound) / 2));
  } else if (guess == number) {
    console.log("The answer is " + guess + ".");
    console.log("This took " + count + " tries.");
  }
}

binarySearch(Math.round(max / 2));
