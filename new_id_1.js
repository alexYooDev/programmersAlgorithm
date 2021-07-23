// 다른 이의 풀이 해석.
//개선안 if문을 사용하지 않고, 정규식만을 사용하여 일관성있게 해결.

// 화살표 함수 사용
const solution = (new_id) => {
  // id 상수 선언하고 new_id 할당
  const id = new_id
    //체이닝 사용 => 변수를 재언급 할 필요X
    // 대문자를 소문자로 변환
    .toLowerCase()
    // /w === word를 의미, 알파벳, 숫자, _ 를 포함
    // /d === digit(숫자)을 의미
    // g === global 해당하는 모든 패턴을 문자열에서 검색
    .replace(/[^\w\d-_.]/g, '')
    // '.'가 {2,}번 연속되면 '.'로 치환
    .replace(/\.{2,}/g, '.')
    // '.'로 시작(\)하거나 끝($)나면 ''로 치환
    .replace(/^\.|\.$/g, '')
    // padEnd => 문자열 길이가 1에 이르기까지 'a'를 뒤에 pad함
    .padEnd(1, 'a')
    // 문자열의 인덱스 0 ~ 15까지만 남기고 나머지 잘라냄
    .slice(0, 15)
    // 자른 뒤 '.'로 시작하거나 끝나면 ''로 치환
    .replace(/^\.|\.$/g, '');
  // id 상수의 문자열 길이가 3에 이를 때까지 마지막 문자를 pad하여 반환.
  return id.padEnd(3, id[id.length - 1]);
};

const new_id = '...!@BaT#*..y.abcdefghijklm';
console.log(solution(new_id));
