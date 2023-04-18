
// 1. null과 undefined

let a   // 서버로부터 데이터를 받아오는 코드
console.log(a)  // 결과가 undefined 라면
// 서버로부터 데이터를 못 받아온 것
// a라는 변수가 없는 게 아니라, 데이터가 없는 것

// 결과가 null이라면
// 서버가 데이터 없다고 명시한 것

// 2. 문자열 형변환

let str = "test"
let str2 = new String("test")

console.log(typeof(str))    // string
console.log(typeof(str2))    // object

console.log('5' - '2')      // 3
console.log(5 * '2')        // 10
console.log('10' / '2')     // 5

let str3 = 'hello'
let bool = true
console.log(str3 + bool)    // hellotrue : 문자열로 형변환 되어 계산
console.log(str3 - bool)    // NaN (Not-a-Number)
console.log(str3 * bool)    // NaN (Not-a-Number)

// true: 1, false: 0 으로 형변환
console.log(3 + true)
console.log(3 + false)
console.log(3 + Number(true))

