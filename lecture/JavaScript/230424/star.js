// 별 찍기 함수
function drawStars(rows) {
  for (let i = 1; i <= rows; i++) {
    let stars = '*'
    for (let j = 2; j <= i; j++) {
      stars += '**'
    }
  console.log(stars)
  }
}

// 별 찍기 호출
const rows = 5 // 별을 몇 줄까지 찍을지 설정
drawStars(rows)