//문자열 처리 문제이기 때문에 Regular Expression을 통해 접근했습니다.
// 5단계 부터 조건은 if 조건문을 통해 구현.

function solution(new_id) {
  // answer 변수선언하여 new_id 배열 할당
  // 1단계: new_id의 모든 대문자를 대응되는 소문자로 치환
  let answer = new_id
    .toLowerCase()
    // 2단계: 알파벳 소문자, 숫자, '-', '_', '.'를 제외한 문자 제거(''로 치환)
    .replace(/[^a-z\d\-\_\.]/g, '')
    // 3단계: '.'가 2번 이상 연속된 부분 '.'으로 치환
    .replace(/[\.\.]+/g, '.')
    // 4단계: 문자열의 가장 앞이나 가장 뒤에 '.'이 있으면 제거
    .replace(/^\.|\.$/g, '');
  // 5단계: 빈문자열이라면 'a' 대입
  if (answer === '') {
    answer = 'a';
  }
  // 6단계: 문자열의 길이가 16이상이면, 첫 15개 문자를 제외한 나머지 문자 제거
  if (answer.length > 16) {
    answer = answer.slice(0, 15);
    // 제거 후, '.'가 문자열 끝에 위치하면
    if (answer[answer.length - 1] === '.') {
      // 제거
      answer = answer.replace(/\.$/g, '');
    }
  }
  // 7단계: 문자열의 길이가 2 이하일 경우,
  if (answer.length <= 2) {
    // 문자열의 길이가 3이 될 때까지
    while (answer.length < 3) {
      //반복하여 마지막문자를 끝에 붙인다.
      answer += answer[answer.length - 1];
    }
  }
  //완성.
  return answer;
}

const new_id = '...!@BaT#*..y.abcdefghijklm';
console.log(solution(new_id));
