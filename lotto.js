//두 배열 같의 중복을 카운트한 것을 활용하는 문제로 파악하여,
//기본적인 중첩반복문을 이용하여 완전탐색으로 접근했습니다.

// 중복 카운트 값을 조건문으로 조건을 체크하여 순위로 변환한 뒤,
// answer 배열에 최고순위, 최저순위 순으로 넣어서 해결했습니다.

function solution(lottos, win_nums) {
  const answer = [];
  // 최저순위를 저장할 변수 선언
  let min = 0;
  // 최고순위를 저장할 변수 선언
  let max = 0;

  // 중첩반복문을 통해 중복완전탐색
  for (let i = 0; i < lottos.length; i++) {
    for (let j = 0; j < lottos.length; j++) {
      // 중복이 있을 경우
      if (lottos[i] === win_nums[j]) {
        //최저순위를 증가한다
        min++;
      }
    }
    // lottos 배열에 0이 있으면
    if (lottos[i] === 0) {
      //최고순위를 증가한다.
      max++;
    }
  }
  //최고순위에 최저순위 카운트를 증감대입한다.
  max += min;
  // 최저순위 카운트가 2이상이면
  if (min >= 2) {
    // 최저순위 변수에 lottos 배열길이 - min +1 한 값을 재할당 => 중복카운트에서 순위로 변환작업.
    min = lottos.length - min + 1;
    // 2 이하일 경우: 낙첨
  } else {
    // lottos의 길이, 즉 6등 낙첨을 저장.
    min = lottos.length;
  }
  // max가 0이 아닐 경우 : 낙첨 외
  if (max !== 0) {
    //최고순위 변수에 lottos 배열길이 - max +1 한 값을 재할당 => 중복카운트에서 순위로 변환
    max = lottos.length - max + 1;
    // max가 0일 경우: 낙첨
  } else {
    // lottos의 길이인 낙첨 순위를 저장.
    max = lottos.length;
  }
  answer.push(max, min);
  return answer;
}

let lottos = [44, 1, 2, 5, 31, 25];
let win_nums = [20, 9, 3, 45, 4, 35];
console.log(solution(lottos, win_nums));
