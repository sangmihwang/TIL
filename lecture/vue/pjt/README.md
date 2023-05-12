
## 09_PJT

## Vue를 활용한 SPA 구성


### 목표
- 영화 정보를 제공하는 SPA 제작
- AJAX 통신과 JSON 구조에 대한 이해
- VUE CLI, Vue Router 플러그인 활용



### 새롭게 학습한 부분

1. components와 views의 차이
   - 명시된 components 구조에 따라 app을 만들어야하는데 components와 views의 차이점에 대한 이해가 불분명해 어떤 vue 파일이 각각의 폴더에 속해야하는지 몰랐음.
   - 두 곳 모두 .vue 파일을 가진다.

   - `views` : router에서 호출할 경로가 설정된 vue 파일 (경로 역할)
   - `components`: view에서 import할 vue 파일 (method 등 실제 작동하는 코드 보유)

2. Bootstrap style 적용 어려움
   - bootstrap을 오랜만에 써서 헷갈렸음. vue에도 적용할 수 있는 것을 알게 되었음
   - 프로젝트 때 vue와 bootstrap을 함께 사용해 서비스를 구현하면 되겠음

3. vuex의 인스턴스 각각의 역할
   - `state` : vue에서의 data. store에 있는 모든 상태 정보. 개별 componenet들이 state에서 정보 가져와서 사용
   - `mutations` : state를 변경하는 유일한 방법이므로 모든 단계의 마지막에 mutations를 거쳐야함. 여기서 호출되는 함수는 반드시 동기적 함수. actions에서 commit()로 호출됨
   - `actions` : mutations과 비슷하지만 비동기 작업을 포함할 수 있음. store.js의 모든 요소와 메서드에 접근 할 수 있음. component에서 dispatch()로 호출됨
   - `getters` : vue의 computed. state를 활용하여 계산된 값을 얻고자 할 때 사용. 첫번째 인자로 state, 두번째 인자로 getter 맏음

4. 자주하는 실수
   - `img` 태그 안의 src로 이미지 url을 불러올 때 src의 경로는 큰따옴표로 묶어줘야 함. 그런데 여기서 movie마다 바뀌는 url값을 적용해주기 위해선 `백틱` 을 써야함. 때문에 "`{}`" 이런 꼴이 되어야하는데 이게 어색한 것 같아서 계속 하나만 쓰고 시도함. 