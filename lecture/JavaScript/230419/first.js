const math = require('./math.js')

const sum = math.add(1, 5)
const mul = math.multiply(2, 5)
// const mysub = math.mySub(65)     // exports 안됐음

console.log(`두 수의 합: ${sum}`)
console.log(`두 수의 곱: ${mul}`)
// console.log(`?: ${mysub}`)