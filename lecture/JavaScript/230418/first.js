let a = 10
let b = '글자'
// let c = False


console.log(a)
console.log(typeof(a))
console.log(b)
console.log(typeof(b))
// console.log(c)
// console.log(typeof(c))


const fruits = {
    a: 'apple',
    b: 'banana',
}
console.log(fruits)
console.log(fruits['a'])

const vegies = ['cucumber', 'cabbage', 'apple']
console.log(vegies)
console.log(vegies[0])
for (let i = 0; i < 3; i++) {
    console.log(vegies[i])
}
for (f in fruits) {
    console.log(f)
}
for (const key in fruits) {
    console.log(key)
    console.log(fruits[key])
}
