function solution(new_id) {
  let answer = new_id.toLowerCase();
  answer = answer.replace(/[^a-z\d\-\_\.]/g, '');
  answer = answer.replace(/[\.\.]+/g, '.');
  answer = answer.replace(/^\.|\.$/g, '');
  if (answer === '') {
    answer += 'a';
  }
  if (answer.length >= 16) {
    answer = answer.slice(0, 15);
    if (answer[answer.length - 1] === '.') {
      answer = answer.replace(/\.$/g, '');
    }
  }
  if (answer.length <= 2) {
    while (answer.length < 3) {
      answer += answer[answer.length - 1];
    }
  }
  return answer;
}
