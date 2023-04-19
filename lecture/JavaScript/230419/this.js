// - 일반적인 함수 내부에서의 this
const normalFunc = function() {
    console.log(this)       // this : 전역 객체
}
normalFunc()

// - 객체의 메서드 내부에서의 this
const obj = {
    name: 'test',
    myFunc: function() {
        console.log(this)   // this: 함수가 정의된 객체
    }
}
obj.myFunc()

// - 생성자 함수 내부에서의 this
function Person(name){
    this.name = name
    this.greeting = function() {
        console.log(this)       // this: 생성된 인스턴스
    } 
}

const me = new Person("상미")
me.greeting()

// - 화살표 함수 내부에서의 this
const person_obj = {
    name: "상미",
    greeting: () => {
        console.log(this)
    }
}
person_obj.greeting()

const person_obj2 = {
    name: "상미",
    greeting: function() {
        // 여기의 this를 참조
        // object 의 메서드가 가리키는 this: 메서드가 정의된 객체
        
        const arrowFunc = () => {
            // 화살표 함수는 한 단계 상위가 가지는 스코프의 this를 참조
            console.log(this)   // person_obj2를 가리킴
        }
        arrowFunc()
    }
}