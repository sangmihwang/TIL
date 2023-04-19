const arrow1 = function (name) {
    return `hello, ${name}`
}
console.log(arrow1('a'))


// 1. function 키워드 삭제
const arrow2 = (name) => { 
    return `hello, ${name}`
}
console.log(arrow2('a'))


// 2. 인자가 1개일 경우에만 () 생략 가능
const arrow3 = name => {
    return `hello, ${name}`
}
console.log(arrow3('a'))


// 3. 함수 바디가 return 을 포함한 표현식 1개일 경우에 {} & return 삭제 가능
const arrow = name => `hello, ${name}`

console.log(arrow('a'))