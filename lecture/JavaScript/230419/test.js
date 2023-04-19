const numbers = [1,2,3,4,5]

// 1. forEach : 원본 배열을 건들지 않고 내부 요소들에 접근해서 사용하고 싶을 떄
// element : 배열의 요소
// index : 배열 요소의 인덱스
// array : 원본 배열
numbers.forEach((element, index, array) => {
    console.log(element)
})

// 2. map : 원본 배열의 데이터를 기반으로 새로운 배열을 만들고 싶을 때 사용
const newNumbers = numbers.map((element, index, array) => {
    return element + 3
})

console.log(numbers)    // [ 1, 2, 3, 4, 5 ]
console.log(newNumbers) // [ 4, 5, 6, 7, 8 ]


// 3. filter : 원본 배열에서 필요한 데이터만 골라서 새로운 배열로 반환
// element : 배열의 요소
// index : 배열 요소의 인덱스
// array : 원본 배열
const filterNumbers = numbers.filter((element, index, array) => {
    // 조건이 true인 요소만 반환
    return element % 2 == 0
})

console.log(filterNumbers)  // [ 2, 4 ]


// 4. reduce: 원본 배열 데이터를 모두 사용하여 특정한 하나의 값을 얻고 싶을 때
    // 예시) 합계
let initialValue = 0
const sum = numbers.reduce((total, element, index, array) => {
    return total + element
}, initialValue)

console.log(sum) // 15

// 10부터 시작해서 numbers 중 짝수만 더해라
// 요소를 순회하며 return 되는 값이 total 변수에 할당
const result = numbers.reduce((total, element, index, array) => {
    if (element % 2 == 0) return total + element
    else return total
}, 10)

console.log(result) // 16 (= 10 + 2 + 4)

// 5. find : 배열에서 특정 값을 찾아서 반환, 못 찾으면 undefined 반환
const findNumber = numbers.find((element, index, array) => {
    return element == 3
})
console.log(findNumber)

// 6. some :  특덩 조건이 하나라도 맞으면 true, 모두 틀리면 false (one of)
const someNumber = numbers.some((element, index, array) => {
    return element < 4
})
console.log(someNumber) // true

// 7. every : 특정 조건이 모두 맞으면 true, 하나라도 틀리면 false (all of)
const everyFlag = numbers.every((element, index, array) => {
    return element < 6
})
console.log(everyFlag)  // true


