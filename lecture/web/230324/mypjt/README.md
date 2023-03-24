
## forms.py

forms.py 작성 과정에서의 어려움 
- Movie 모델의 데이터 검증, 저장, 에러메시지, HTML을 관리하기 위해 ModelForm 사용 
  1. genre 필드에서 element를 select 할 수 있게 하는 과정에서 docs 참조
      - choices 목록을 처음에 단순 리스트로 나열하였더니 argument 개수 오류가 남. 튜플로 바꾸고 쌍으로 지어줌. 데이터베이스에 저장할 이름과 페이지에 표시될 이름 두가지를 쌍으로 묶어서 튜플로 작성
  2. score 필드에서 type 과 attribute를 지정해주기 위해 widget을 import 함
      - 범위를 지정해주기 위해선 models.py에 직접 validator 적용하였음. docs 참조함.

## detail.html

detail.html 작성 과정에서의 어려움
- 저장한 이미지가 표기되지 않는 상황

  1. media 파일의 경로를 settings.py에 지정해주지 않아서 이미지를 불러올 곳이 없었음. settings.py에 이미지 파일 경로를 지정해주었더니 media 폴더가 자동 생성되고 거기에 create에서 저장한 이미지 파일이 자동 업로드 됨.
  2. {{form.as_p}} 는 사용자의 입력을 받기 위한 목적으로 사용되기 때문에 detail.html이 아니라 create.html에 사용하는 것이 적합함! 
  3. 처음에 actor_image가 아니라 그냥 image로 받으려고 해서 계속 안됐음. 반드시 models.py에 작성한 이름 그대로 가져와야함

## update.html

update.html 작성 과정에서의 어려움
- reset 버튼은 사용해본적 없음

  1. sumbit 외의 버튼은 사용해본적이 없는데 reset 도 이미 <input> 태그 의 type 속성으로 저장되어 있어 사용할 수 있었음. 다만 완전히 모든 입력 데이터를 초기화하는 것이 아니고 update 화면에서의 reset 이기 때문에 처음 create 한 내용으로 초기화되는 것이 아쉬웠음.

