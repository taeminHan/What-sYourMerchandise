# WhatYourMerchandise

시각장애인을 위한 이미지 인식기반 음성 상품 정보출력  프로젝트


기존의 상품에는 아래와 같이 점자로 표시를 하지만 해당 내용은 음료의 종류만 제공할 뿐 무슨 음료인지는 알 수가 없다.
<div>
<img src="https://newsimg.hankookilbo.com/cms/articlerelease/2019/06/12/201906121483734269_34.jpg" width="50%"></img>
</div>


이 상황을 비 장애인에게 대입한다면
<div>
<img src="https://newsimg.hankookilbo.com/cms/articlerelease/2019/06/12/201906121483734269_33.jpg" width="30%"></img>
<img src="https://newsimg.hankookilbo.com/cms/articlerelease/2019/06/12/201906121483734269_32.jpg" width="30%"></img>
</div>


그러므로 시각장애인을 위한 인공지능을 활용한 상품인식 음성정보 출력 프로그램을 개발한다.

~킹카콜라를 구매해야하는데 혐시를 구매한다면 매우 큰 일이기 때문이다.~

그러므로 손쉽게 사용할 수 있는 스마트폰의 카메라를 이용하여 상품을 촬영하면

인식을 하여 음성으로 상품의 정보를 출력한다.

초도작업은 웹캠을 활용하지만 추후 개발을 통해 어플리케이션으로 도출해낸다.





많은 영감을 준 tvn드라마 스타트업이 도움이 되었습니다. ~수지 좋아요~

---
도커 공부가 필요함

스마트폰에 담겨져야 하기때문에 빠른속도와 경량화도 무시할 수 없다.

서버는 어떤것으로 해야하는지  촬영후 사진으로 판독할 것인지 아니면 실시간 영상인식으로 할것인지 정해야 한다.

---
2020-12-21

프로젝트 시작 

음료의 사진은 여러장이므로 다중클래스 분류를 사용 KNN 최근접 이웃 알고리즘을 이용하는것이 먼저 생각이 든다.

---
2020-12-30

시험용 데이터 수집

코카콜라, 스프라이트, 칠성사이다 jpg 형태로 수집

데이터 수집은 자주 해야 할 것!!

---
2021-01-01

일단은 클론코딩으로 시작. 데이터 수가 너무 부족하다 더 수집해야 한다.
멀티 라벨링작업은 완료했다.

---
2021-01-02

최초데이터 학습 결과

Training Data Set

코카콜라: 6장

칠성사이다: 9장

스프라이트: 8장
epochs = 50

![다운로드](https://user-images.githubusercontent.com/5088870/103459731-922dd180-4d54-11eb-837a-51e379168a00.png)

---
2021-01-06

2차 학습 결과

Training Data Set

코카콜라: 25장

칠성사이다: 25장

스프라이트: 25장

epochs = 50


![asd](https://user-images.githubusercontent.com/5088870/103679851-beea1f00-4fc8-11eb-8f56-808034b97931.png)



확실히 데이터셋을 늘리니 인식률이 좋다.

## 참고자료
opencv + Tensorflow를 활용한 이미지(손글씨) 예제  https://webnautes.tistory.com/1384

데이터셋 만들기 https://gusrb.tistory.com/12

케라스 활용 이미지 데이터셋 학습 https://lhh3520.tistory.com/376

## image

https://m.hankookilbo.com/News/Read/201906121483734269
