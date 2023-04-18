function myFunction(x) {
    // add 함수 내부의 x는 렉시컬 스코프에서 가져옴
    function add(y) {
        console.log(x + y)
    }
    return add
}

let func = myFunction(10)
func(2)         // 12


// 간단한 깊은 복사
{
    // 2차원 이상의 배열(객체)일 경우 얕은 복사가 발생하므로
    // 깊은 복사를 하여 사용을 잘 해야 함
    let numbers = [1,2,3]
    // ... = 스프레드 연산자 : 객체를 전개하여 각 요소를 개별적인 값으로 분이
    let newnumbers = [...numbers]   // depth 1 까지만 깊은 복사
    newnumbers
}

{
    let numbers = [
        [1,2,3],
        [4,5,6],
        7
    ]
    let newnumbers = [...numbers]
    newnumbers[0][1] = 10
    console.log(numbers)
    console.log(newnumbers)
    newnumberss[2] = 20
    console.log(numbers)
    console.log(newnumbers)
}