// answer를 전역변수로 해서 값을 0으로 초기화
var answer = 0;

function dfs(node, numbers, target, value) {
  answer;
  length = numbers.length;
  //노드(인덱스)값이 numbers의 길이와 같고 target의 값이 value와 같으면
  if (node === length && target === value) {
    //answer를 1 증가하고
    answer += 1;
    //함수를 종료
    return;
  }

  //노드 값이 numbers의 길이만 같으면
  if (node === length) {
    //함수 종료
    return;
  }
  // dfs 함수 재귀 (노드 값을 1 증가, value 인수자리를 numbers의 인덱스 더한 값으로)
  dfs(node + 1, numbers, target, value + numbers[node]);
  // dfs 함수 재귀 (노드 값을 1 증가, value 인수자리를 numbers의 인덱스 뺀 값으로)
  dfs(node + 1, numbers, target, value - numbers[node]);
}

// 솔루션 함수
function solution(numbers, target) {
  // 전역 변수
  answer;
  // dfs 함수를 호출 (node 0으로, value도 0)
  dfs(0, numbers, target, 0);
  // answer를 반환한다.
  return answer;
}

console.log(solution([1, 1, 1, 1, 1], 3));
