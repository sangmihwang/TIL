
// exports 객체에 add와 multiply 를 추가

exports.add = function(a, b) {
    return a + b;
}

exports.multiply = function(a, b) {
    return a * b;
}

// 외부로 보내기 싫으면 그냥 const
const mySub = function(a) {
    return a - 10
}
