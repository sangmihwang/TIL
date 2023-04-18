// 전역 스코프
let a = 10
console.log(a)

// 블록 스코프 
// 스코프 내부에서 묶으면 변수에 값 재할당 가능
{
    let a = 20
    console.log(a)  // 20
}

if (true) {
    let a = 30
    console.log(a)  // 30
}

// 이런 식으로 스코프를 분리하여 사용 가능
const tmp = "test1"
{
    const tmp = "test2"
    console.log(tmp)    // test2
}
console.log(tmp)    // test1


// 블록 스코프 활용하기

let b = 10
if (true){
    const c = 20
    console.log(b)
} 

// if (true){
//     console.log(c)
// }

let x = 12
function myFunction() {
    // myFunction 의 함수 스코프
    // innerFunction 의 렉시컬 스코프
    let num = 19
    console.log(num)        // 19

    function innerFunction() {
        console.log(x)      // 12
    }
    innerFunction()
}
myFunction()
