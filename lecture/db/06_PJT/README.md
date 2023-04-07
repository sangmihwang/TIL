
## 목표

- 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web application 제작
- Django web framework 를 사용한 데이터 처리
- Django Model 과 ORM 
- Django Authentication System


## Model 클래스 정의

- User 모델 클래스에 AbstractUser 모델 클래스를 상속받는 custom 모델을 사용
- Django에는 권한 및 인증에 대한 기본적인 기능이 User Model로 구현되어있는데 필요한 데이터만 얻기 위해 custom 이 필요함
- 사용하려면 settings.py에 "AUTH_USER_MODEL = 'accounts.User'" 추가해주어야 함
- admin.py에 admin.site.register(Users, UserAdmin) 등록해주어야 함
- user model 에 대한 정의는 테이블을 만들기 전(migrate 전)에 작업해두는 것이 좋음
  
## render 와 redirect의 차이

- render는 템플릿을 불러오고 redirect는 URL로 이동
  
### redirect
  - 지금 내가 있는 페이지에서 다른 페이지를 지정, 아예 사용자를 그 페이지로 이동시킴. 
  - HttpResponseRedirect를 불러 페이지의 상단 url이 가고자하는 대상 template의 url로 바뀜
  - POST나 form을 통과시킨 뒤에 아예 새로운 페이지로 옮기려고 할 때 사용하는 방식

### render
  - 특정 template을 불러오기만 하는 것
  - redirect와는 다르게 페이지 상단 url이 가고자 하는 대상의 template로 바뀌지 않음
  - 예를 들어 index로 가는 return으로 render를 하면 화면은 이동하겠지만 url 주소엔 index로 적히지 않음. 그전 url그대로 남아있게 됨


## 로그인한 회원에게 한정된 기능 구현

- {% if user.is_authenticated %}{% endif %} 사욜
