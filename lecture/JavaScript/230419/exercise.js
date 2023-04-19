// const nums = [1,2,3,4,5,6,7,8]

// for (let i = 0; i < nums.length; i++) {
//   console.log('nums[' + i + ']: ' + nums[i])
// }


// for (num in nums) {
    
//     console.log(num, typeof Number(num))
// }

const nums = [1, 2, 3, 4]

const tripleFunc = function (number) {
    return number**3
}

const tripleNumbers = nums.map(tripleFunc)
console.log(tripleNumbers)