
### npm fund

- 해당 패키지의 개발자에게 후원하는 방법을 알려줌
- `$ npm fund core-js` 을 해보면, core-js 개발자들에게 돈을 후원할 수 있는 사이트 열림

### npm audit

- 보안 및 의존성 취약점을 해결하기 위해 도와주는 도구

1. 보안 취약점
   
   - 다른 개발자들이 만들어놓은 패키지를 가져와서 사용
   - 개발자가 악성 코드를 넣어두면, 그대로 노출됨
   - 최소한의 보안 취약점을 검사해주기 위해 npm에서 제공하는 명령어

2. 의존성 문제 해결

    - 현재 프로젝트


## Vue 프로젝트 생성

`$ vue create vue-cli`

   - 패키지 설치 시 npm registry 에서 모듈을 받아온다
   - 매우 안정적으로 성장했지만, 항상 정상적이라고 보장할 수 없음
   - 평소에는 크게 문제가 없으나, 배포 등 중요한 작업 시 registry가 불안정하면 대처할 방법이 없음
   - 이 때를 대비해 npm이 미러사이트를 운영
     - 미러사이트: 네트워크 트래픽을 줄이기 위하여 서버를 복사해 놓은 웹사이트 혹은 컴퓨터 파일 서버
   - 에러가 아니라, `해당 미러사이트를 사용해서 설치할래?` 라고 물어보는 것


### ESLint

- JS 코드에서 문제시 되는 패턴들을 식별하기 위한 정적 코드 분석 도구
- 코드를 분석하여 문법적인 오류, 안티 패턴을 찾아주고 일관된 코드 스타일을 작성할 수 있도록 도와줌
  - 스타일 가이드를 적용하여 가이드를 따르지 않으면 잔소리를 하도록 설정할 수 있음
- 자바스크립트는 동적 분석
  - 프로그램을 직접 실행하면서 코드를 분석해야함
  - 코드 작업 중 에러를 찾도로 도와주는 도구 `Linter`라고 함
  - ESLint로 Linter 중 하나
- JSLint, JSHint 와 같이 다른 정적 분석 도구들도 있음
  - ESLint가 커스터마이징이 쉽고 확장성이 뛰어남
- 단점: ESLint의 규칙을 반드시 지켜야하기 때문에 공부할 때 힘듦


### npm run serve

- 개발 서버를 `$npm run serve`를 통해 실행했다
- 이게 가능한 이유가 뭘까?
  - 우리의 프로젝트는 어디에서 해당 명령어를 참고할까?

### package.json

- 프로젝트의 종속성 목록과 지원되는 브라우저 등 여러 구성 옵션이 작성되어 있음
- 어플리케이션이 실행되는 모드(개발, 배포 등) 및 실행 가능한 명령어에 대한 정보도 담고 있음
- 즉, 프로젝트 실행과 관련된 전반적인 관리를 해주는 파일
  - webpack과 같은 모듈 번들러와 함께 사용됨


### package.json vs package-lock.json

1. package.json
- 프로젝트에서 사용되는 npm 패키지들의 목록을 정의


2. package-lock.json
- `$npm install` 실행 시 자동으로 생성되는 파일
- __현재 프로젝트에서 사용 중인 패키지들과 버전 정보__ 를 포함
- 완벽한 패키지 설치를 보장하기 위해 사용됨
  - 패키지 간 의존성 관리를 자동으로 처리해줌
  - pip의 requirements.txt 역할

=> 다른 환경에서 동일한 환경을 구성하기 위해 사용
  - 공유 시 두 파일을 모두 주어야 함 
  - 공유 받은 파일들의 `name`, `version` 은 프로젝트에 맞게 수정
  
  - `package.json` 파일을 기반으로 패키지들을 설치
    - 명령어 : `$ npm install`


- npm install 동작 과정

  1. `package.json` 파일 검사
   - 설치가 필요한 패키지 목록 확인

  2. `package-lock.json` 파일 검사
   - 의존성 패키지 목록 확인

### package.json 심화

- `name` : 프로젝트의 이름
- `version` : 프로젝트의 버전
  - "0.1.0" = `[Major].[Minor].[Patch]`
  - `Major`: 기존 버전과 호환되지 않는 새로운 기능이 추가될 때 버전 업
      - 업데이트 안 하면 안 돌아간다 급의 수정
  - `Minor`: 기존 버전과 호환되는 새로운 기능이 추가될 때 버전 업
  - `Patch`: 기존 버전과 호환되는 버그 수정 및 기능 개선 시 버전 업
  
- `private`: true로 설정하면, npm 레지스트리에 해당 프로젝트를 배포할 수 없음
- `scripts`: 프로젝트에서 사용할 수 있는 실행 스크립트를 정의하는 객체
  - 각 속성은 해당 스크립트를 실행하기 위한 명령어를 정의
  - `$npm run` 과 함께 사용된다
  - Vue에서는 3개의 실행 모드가 존재한다
    - `serve`: "vue-cli-service serve" 명령어를 실행
      - Vue.js 개발 서버를 실행하여 애플리케이션을 브라우저에서 실행할 수 있도록 함
    - `build`: "vue-cli-service build" 명령어를 실행
      - Vue.js 애플리케이션을 빌드하여 배포할 수 있는 형태로 만들어 줌(dist 폴더가 생성됨)
      - 내부적으로 webpack을 이용하여 소스 코드 압축 등 번들링 작업(소스 코드 압축 및 최적화, 모듈화, 캐싱, 호환성 및 의존성 문제 해결 등)
    - `lint`: ESLint를 통해 문법 등 코드 오류 검사

- `dependencies`: 배포 환경에서 필요한 패키지를 정의
  - 버전 표기법
    - `틸드(~)`: 작성된 버전보다 높거나 같고, 다음 마이너 버전보다 낮은 버전 내에서 자동으로 업데이트
        - ex) `~1.2.3` => `>= 1.2.3` and `<1.3.0`
        - 전체적인 기능은 비슷하지만, 버그 수정 등이 끝난 최신 버전으로 업데이트
  
    - `캐럿(^)`: 작성된 버전보다 높거나 같고, 다음 메이저 버전보다 낮은 버전 내에서 자동으로 업데이트
        - ex) `^1.2.3` => `>= 1.2.3` and `<2.0.0`
        - 호환성을 유지하는 버전 중 가장 최신 버전으로 업데이트(많이 사용됨)

- `devDependencies`
- `eslintConfig`: ESLint 설정
- `browserslist`: 프로젝트가 지원하는 브라우저 리스트를 정의


### package-lock.json

- `resolved`: 해당 패키지의 다운로드 경로
- `integrity`: 다운로드 받은 패키지의 무결성을 체크하는 해시값
  - 정확한 패키지를 다운로드 받았는지 확인
  - 무결성 체크 실패 시 다운로드 중지
  - 보안, 일관성 등 관리하기 위해 매우 중요한 옵션
- `dev`: 개발 버전의 의존성으로 설치되었는지 여부 (true/false)
- `engines`: 해당 패키지를 사용하기 위해 필요한 Node.js 버전


