function increaseAndPrint(n, callback) {
    setTimeout(() => {
      const increased = n + 1;
      console.log(increased);
      if (callback) {
        callback(increased); // 콜백함수 호출
      }
    }, 1000);       // 1초마다
  }
  
  increaseAndPrint(0, n => {
    increaseAndPrint(n, n => {
      increaseAndPrint(n, n => {
        increaseAndPrint(n, n => {
          increaseAndPrint(n, n => {
            console.log('끝!');
          });
        });
      });
    });
  });

function increaseAndPrint2(n) {
return new Promise((resolve, reject)=>{
    setTimeout(() => {
    const increased = n + 1;
    console.log(increased);
    resolve(increased);
    }, 1000)
})
}

increaseAndPrint2(0)
.then((n) => increaseAndPrint2(n))
.then((n) => increaseAndPrint2(n))
.then((n) => increaseAndPrint2(n))
.then((n) => increaseAndPrint2(n)); // 체이닝 기법

function doSomething() {
    return new Promise((resolve, reject) => {
        resolve(100)
    });
  }
  
  doSomething()
      .then((value1) => {
          const data1 = value1 + 50;
          return data1
      })
      .then((value2) => {
          const data2 = value2 + 50;
          return data2
      })
      .then((value3) => {
          const data3 = value3 + 50;
          return data3
      })
      .then((value4) => {
          console.log(value4); // 250 출력
      })