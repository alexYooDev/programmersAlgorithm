function solution(answers) {
  let answer = [];

  const first = [1, 2, 3, 4, 5];
  const second = [2, 1, 2, 3, 2, 4, 2, 5];
  const third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  const cnt = [0, 0, 0];

  cnt[0] = answers.filter((n, i) => n === first[i % first.length]).length;
  cnt[1] = answers.filter((n, i) => n === second[i % second.length]).length;
  cnt[2] = answers.filter((n, i) => n === third[i % third.length]).length;
  const max = Math.max(cnt[0], cnt[1], cnt[2]);

  if (max === cnt[0]) answer.push(1);
  if (max === cnt[1]) answer.push(2);
  if (max == cnt[2]) answer.push(3);

  return answer;
}
