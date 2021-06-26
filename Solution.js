(function test() {
  var testArray = [1, 2, 3, 4, 5];
  function getLessThanThree(value) {
    return value <= 3;
  }
  var newArray = testArray.filter(getLessThanThree);
  console.log(newArray);
})();
