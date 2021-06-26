function counter(arr, value) {
  var count = 0;
  arr.forEach(element => {
    if(element == value) count++;
  });
  return count;
}

function solution(arr) {
  var answer = [];
  var set = new Set([]);
  arr.forEach(element =>{
    if(set.has(element)) return;
    set.add(element);
    count = counter(arr, element);
    if (count > 1) answer.push(count);
  });
  if (answer.length == 0) answer.push(-1)
  return answer
}