![[1.png]]

**도메인**을 생성한다는 것은 하나의 프로젝트를 생성하는 것과 같은 의미입니다.

![[2.png]]

**도메인의 이름과 코드**를 정해주고 

어떤 **자연어(언어)처리**를 할 것인지 정해줍니다.

서비스 타입이 있는데

Trial 타입은 최대 5개 무료이며 6개월이 지나는 시점에서 자동 삭제 되니 주의해야합니다.

Standard부터는 직접적인 요금부과가 있으며 모델 생성시마다 해당 요금이 부과 됩니다.

CLOVA AiCall 서비스 타입은 CLOVA AiCall 서비스(AI 컨택센터)를 지원하기위한 기능으로, 챗봇 서비스에서는 과금되지 않으며 CLOVA AiCall 서비스에 통합과금됩니다.

![[3.png]]

![[4.png]]

처음에 해당 챗봇을 테스트하기 위해서는 대화를 생성해보면 됩니다.

![[Pasted image 20220927131741.png]]

#### 대화정보

대화 이름: 대화 이름은 고유하게 영어나 한글로 작성해주시면됩니다.

#### 질문 등록
정규식 가이드:  https://guide.ncloud-docs.com/docs/ko/chatbot-chatbot-3-7

![[Pasted image 20220927163636.png]]

![[Pasted image 20220927163650.png]]

```
<?>*? @{지역} @{공공센서}(값|데이터|결과)::(이|가) (뭐야|무엇(이야|입니까)|어(때|때요|떱니까|떤지)|궁금(해|합니다)|보여(줘|주세요)|알려(줘|주세요)|띄워(줘|주세요))("?")
```
라고 쓴 후에 |+추가|를 눌러 줍니다.

![[Pasted image 20220927163821.png]]

그렇게 되면 `@{지역}` 과 `@{공공센서}`가 색이 있는 것을 확인 할 수 있는데 해당 내용은 

![[Pasted image 20220927164933.png]]

에서 확인 할 수 있다,

## 엔티티

![[Pasted image 20220927165010.png]]


![[Pasted image 20220927165026.png]]

저장을 하게 되면 해당 엔티티를 등록하고 앞서 본것 처럼 질문에서 해당 내용을 사용할 수 있다.

엔티티 = 정해놓은 단어들의 집합이다.

