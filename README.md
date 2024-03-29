<div align='center'>
<image src="/final-pjt-front/src/assets/Logo_new.png" width="60%"><br>
</div>

<div align='center'>
<br>
<h1 style='text-decoration: none;'><b>필독(Flim Docs)</b></h1><br>
<div align='left'>
  <li>2023.05.15 - 2023.05.26 (2주) 진행</li>
  <li>삼성 청년 SW 아카데미</li>
  <li>영화와 관련된 모든 내용을 제공받을 수 있는 사이트</li>
</div>
<h3>프로젝트 구성원</h3>
  
|구분|노수혁|주영인|
|:---:|:---:|:---:|
|프론트엔드|메인, 전체 영화, 영화 정보, 영화 배우 정보, 댓글 및 대댓글, 영화 추천, 프로필 화면 디자인 및 기능 구현 <br> 회원 팔로우, 영화/댓글/대댓글 좋아요, 싫어요, 영화 추천 목록 기능 구현|영화 검색, 영화 월드컵, 로그인, 회원가입 화면 디자인 및 기능 구현 <br> 회원 팔로우, 댓글 좋아요, 싫어요, 영화 추천 목록 기능 구현|
|백엔드|api를 통한 영화 데이터 일정 주기 호출, cors 기능 구현|게시판, 사용자 계정 관리 기능 구현|
<br>
<br>
</div>

## 화면 구성 및 기능
<br>
<h3>1. 시작 화면</h3>

<div>
  <div align='center'>
    <image src="/내부 화면/시작 화면.JPG" width="80%">
  </div>
  <br>
  <div>
    <li>최신 영화 10개의 제목, 설명, 예고편이 화면에 출력(10초 후 다음 영화로 자동 슬라이드)</li>
    <li>테마 : 블랙 & 옐로우</li>
  </div>
</div>

### 2. 로그인 및 회원가입 화면
- CRUD 기능 구현
- 영화 평론(후기)를 영화 댓글란에 남길 수 있음
- 영화 detail page에서 보여주는 방식

### 3. 전체 영화 화면
- 로그인 / 로그아웃
- 회원가입 - 좋아하는 영화 장르 선택지 제공 / 회원탈퇴
- 아이디와 닉네임 중복 검사 버튼
- 비밀번호와 비밀번호 재 입력 시 일치 여부 확인
- 회원정보수정
- 게시글 작성 / 영화 좋아요 / 댓글 작성 시 로그인이 필요
- 자신이 작성한 글 / 자신 계정만 수정 or 삭제 가능
- (django 관리자로 계정마다 다른 권한 부여 기능 - 확인 필요)

### 4. 영화 정보 화면
- 자신 혹은 남이 남긴 후기에 남길 수 있는 글
- 댓글에 좋아요 버튼을 구현
- 댓글을 호감순 / 최신순으로 보여줄 수 있는 선택지 제공
- 대댓글까지만 구현 - 깊이 : 1차

### 5. 영화 댓글 정보 화면
- 영화 좋아요 기능 구현 / (별로에요 기능 구현)
- 좋아요 재 클릭 시 좋아요 취소 - 색을 통해 차이를 줌
- 리뷰 / 댓글에 좋아요 기능 구현

### 6. 영화배우 정보 화면
- 자신이 아닌 다른 사람의 계정을 팔로우하는 기능 구현
- (자신이 팔로우한 사람의 리뷰가 항상 영화 평론창의 최상단에 위치)

### 7. 영화 추천 화면
- 자신이 작성한 댓글, 좋아요한 목록 출력(영화 : 포스터 출력)
- 자신의 팔로우 / 팔로워 수 출력
- (개인별 프로필 사진 변경 기능)
- (자신이 좋아요 누른 영화의 장르 -> 선택된 장르의 횟수에 따라 추천 정도가 달라짐)

### 8. 영화 검색 화면

0. 평점 & 인기도 순으로 내림차순 정렬 후, 추천 (기본 구현 - 추후 다른 추천 서비스가 구현되면 고민)

1. 날씨 연관 - 근거에 대한 자료가 필요 (구현 까다로움)
- 날씨가 사람의 기분에 영향을 끼치는 정도에 대한 근거
- 영화가 사람의 기분에 영향을 끼치는 정도에 대한 근거

2. 다양한 주제의 추천 서비스
- 일주일동안 가장 많이 좋아요가 눌린 영화
- 영화 전체에서 가장 많은 좋아요를 가진 영화
- 사용자가 좋아하는 장르의 영화(좋아요가 높은 순)
- 로그인한 사용자에게 바로 추천영화를 보여줌
(로그인창 -> 영화 추천 페이지 -> 메인 페이지)

### 9. 영화 월드컵 화면
- 영화 배우에 대한 정보와 해당 배우가 출연한 작품을 표시


### 10. 프로필 화면
- 데이터에 있는 영화 중 무작위로 64개를 선택해 32강을 진행
- 보여주는 2개의 영화는 모두 영화의 예고편으로 만약 영화의 예고편이 없다면 해당 영화의 포스터를 출력
- 결과 창에서 영화 상세 페이지로 이동하는 버튼과 다시 시작 버튼 2가지를 보여준다.
- 다시 시작 버튼 클릭 시, 다시 이상형 월드컵 진행
- 영화 상세 페이지 버튼 클릭 시, 해당 영화의 상세 페이지로 이동


## ERD 구조

<div align='center'>
<image src="/image/ERD_first_1.png" width="80%"><br>
</div>


## 느낀점 및 소감

### 주영인
- 기존에 해왔던 작업이었지만 스켈레톤 코드를 제외하고 진행하려니 시간이 평소보다 더 소요 되었다.
- 거인의 어깨에서 시작을 해도 도중에 오타를 하나 잘못쳐서 발견하고 수정하는데 시간이 소요되어 완성하고 빌드테스트를 초반 부터 하는 것의 중요성을 느꼈다.
- 평소에 공부를 좀 더 하여 빠르게 개발하는데 노력할 필요를 느꼈다.
- 시간이 부족하여 조금만 더 주어졌으면 하는 아쉬움이 있다.
- 수업에 배우지 않은 내용도 찾아써야 되는점에 험난함을 느꼈다.

### 노수혁

- 초반 부분은 이미 다 배운 내용이였기에 금방 진행될 줄 알았으나 시간이 굉장히 많이 들었다.
- 처음 계획대로면 Vue와 DRF를 연결 후 다른 요구 사항을 구현해나가며 확인하려고 했으나, 연결하는데도 많은 시간이 들었고, 연결을 했지만 다른 것들을 구현해놓지를 않아서 제대로 되었는지 확인할 수가 없었다. → 계획에서의 실패가 조금 뼈 아팠다.
- 기획에 꽤나 많은 시간을 투자했음에도 여전히 정하지 못한 부분이 많아 하면서 계속 정하느라 굉장히 시간도 많이 들고, 체력적으로나 정신적으로 많이 지치게 되었다.
- 오류 수정에 조금 더 시간을 투자했어야 했는데 그러지 못해서 오류가 남아있다는 것이 굉장히 아쉽다.
- DRF와 Vue의 연결을 통해 출력하는 과정에서 굉장히 많이 오류와 문제 상황이 생겨서 너무 험난했다.
