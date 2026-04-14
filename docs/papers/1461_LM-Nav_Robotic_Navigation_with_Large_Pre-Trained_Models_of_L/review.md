---
title: "1461_LM-Nav_Robotic_Navigation_with_Large_Pre-Trained_Models_of_L"
authors:
  - "Dhruv Shah"
  - "Blazej Osinski"
  - "Brian Ichter"
  - "Sergey Levine"
date: "2022.07"
doi: ""
arxiv: ""
score: 4.0
essence: "LM-Nav는 GPT-3, CLIP, ViNG 세 가지 사전학습된 모델을 조합하여 자연언어 명령으로 로봇이 실제 환경에서 네비게이션을 수행하는 시스템이다. 로봇 데이터에 대한 언어 주석 없이도 복잡한 실외 환경에서 장거리 네비게이션을 실현한다."
tags:
  - "cat/Embodied_Navigation_and_Planning"
  - "sub/Synthetic_Grasping_Datasets"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Shah et al._2022_LM-Nav Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action.pdf"
---

# LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action

> **저자**: Dhruv Shah, Blazej Osinski, Brian Ichter, Sergey Levine | **날짜**: 2022-07-10 | **URL**: [https://arxiv.org/abs/2207.04429](https://arxiv.org/abs/2207.04429)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Embodied instruction following with LM-Nav: Our system takes as input a set of raw observations*

LM-Nav는 GPT-3, CLIP, ViNG 세 가지 사전학습된 모델을 조합하여 자연언어 명령으로 로봇이 실제 환경에서 네비게이션을 수행하는 시스템이다. 로봇 데이터에 대한 언어 주석 없이도 복잡한 실외 환경에서 장거리 네비게이션을 실현한다.

## Motivation

- **Known**: 시각 기반 네비게이션은 대규모 미주석 궤적 데이터셋으로 학습 가능하며 우수한 일반화 성능을 제공한다. 그러나 기존 언어 명령 추종 방식은 비용이 많이 드는 언어 주석이 필요하다.
- **Gap**: 자체 감독 네비게이션의 확장성과 자연언어 인터페이스의 이점을 동시에 활용하면서도 로봇 데이터의 언어 주석을 요구하지 않는 방법이 부재하다.
- **Why**: 로봇과의 통신에 자연언어를 사용하는 것이 이미지 기반 목표 지정보다 훨씬 자연스럽고, 값비싼 주석 작업 없이 실제 환경에서 복잡한 고수준 지시를 따르는 로봇 시스템을 구축할 수 있다면 로봇 학습의 실용성이 크게 향상된다.
- **Approach**: 세 개의 독립적 사전학습 모델을 조합한다: GPT-3로 자연언어 지시를 텍스트 랜드마크 시퀀스로 디코딩하고, CLIP으로 랜드마크를 위상 지도에 그라운딩하며, ViNG으로 계획된 경로를 실행한다.

## Achievement

![Figure 4](figures/fig4.webp)

*Figure 4: Qualitative examples of LM-Nav in real-world environments executing textual instructions (left).*

- **파인튜닝 불필요한 통합 시스템**: 세 개의 대규모 사전학습 모델을 조합하여 목표 환경에서의 파인튜닝 없이 자연언어 명령 추종을 실현
- **언어 주석 제거**: 로봇 네비게이션 데이터의 언어 주석이 완전히 불필요하면서도 자유형식 텍스트 명령을 처리
- **실제 환경에서의 장거리 네비게이션**: 복잡한 외부 환경에서 수백 미터의 네비게이션을 성공적으로 시연
- **세밀한 명령 분화**: 경로 모호성을 해소하는 세밀한 고수준 명령 처리 능력 시연

## How

![Figure 2](figures/fig2.webp)

*Figure 2: LM-Nav uses VLM to infer a joint probability distribu-*

- GPT-3 LLM으로 자연언어 지시를 landmark 시퀀스로 파싱
- CLIP VLM을 사용하여 텍스트 landmark와 robot 관찰 이미지 사이의 결합 확률분포 추론
- ViNG VNM이 구축한 위상 그래프에서 확률적 목적을 최대화하는 그래프 탐색 알고리즘으로 계획 도출
- ViNG의 거리 예측으로 환경의 위상 지도('mental map') 구성", '계획된 경로를 따라 ViNG이 로봇 제어 실행

## Originality

- 대규모 사전학습 모델(언어, 시각, 내재화)을 최초로 결합하여 로봇 instruction following 달성
- VLN(Vision-Language Navigation)과 달리 시뮬레이터나 대규모 주석 궤적 데이터셋 없이 실제 복잡한 야외 환경에서 작동
- 자체 감독 정책(ViNG)과 사전학습 시각-언어 모델의 결합으로 새로운 환경 일반화 경로 제시
- 로봇 고유 언어 주석 대신 인터넷 규모의 언어-이미지 학습 활용이라는 혁신적 접근

## Limitation & Further Study

- GPT-3의 landmark 디코딩 정확도에 의존하며, 부정확한 landmark 분석이 성능 저하를 야기할 수 있음
- CLIP 기반 그라운딩의 robustness가 극한 날씨나 조명 변화에서 검증되지 않음
- ViNG 모델 자체의 내재적 한계(학습 환경과 큰 차이의 신규 환경에서의 성능 감소 가능성)
- 세 모델 간 오류 전파(error cascade)의 영향에 대한 심화 분석 부재
- **후속연구**: 각 모듈의 실패에 대한 오류 회복 메커니즘, 멀티모달 불일치 처리 개선, 더욱 안정적인 실외 환경 테스트

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: LM-Nav는 사전학습 대규모 모델의 획기적 조합을 통해 로봇 학습의 주요 병목(언어 주석)을 제거하면서도 실제 환경에서의 자연언어 네비게이션을 달성한 혁신적 연구다. 파인튜닝 없는 모듈식 설계와 실제 환경 검증이 학계와 산업 양쪽 모두에 높은 영향력을 제시한다.

## Related Papers

- 🔄 다른 접근: [[papers/1443_L3MVN_Leveraging_Large_Language_Models_for_Visual_Target_Nav/review]] — 두 논문 모두 사전훈련된 언어 모델을 네비게이션에 활용하지만, 접근 방식과 활용하는 모델 조합이 다릅니다.
- 🔗 후속 연구: [[papers/1487_Multimodal_Spatial_Language_Maps_for_Robot_Navigation_and_Ma/review]] — 사전훈련된 모델들의 조합을 멀티모달 공간 언어 맵과 결합하여 더욱 정교한 네비게이션을 구현할 수 있습니다.
- 🏛 기반 연구: [[papers/1612_Visual_Language_Maps_for_Robot_Navigation/review]] — 시각 언어 맵의 기본 개념이 사전훈련된 모델들을 활용한 네비게이션의 공간적 표현 기반을 제공합니다.
- 🏛 기반 연구: [[papers/1556_RT-H_Action_Hierarchies_Using_Language/review]] — 로보틱스 트랜스포머의 실세계 제어 방법론이 사전훈련된 모델들의 로봇 적용을 위한 기술적 토대가 됩니다.
- 🏛 기반 연구: [[papers/1396_ForesightNav_Learning_Scene_Imagination_for_Efficient_Explor/review]] — LM-Nav의 대규모 모델 기반 네비게이션이 ForesightNav의 장기 목표 선택에 기초가 된다.
- 🔄 다른 접근: [[papers/1443_L3MVN_Leveraging_Large_Language_Models_for_Visual_Target_Nav/review]] — 두 논문 모두 사전훈련된 언어 모델을 네비게이션에 활용하지만, 하나는 의미적 추론에, 다른 하나는 CLIP과의 조합에 집중합니다.
- 🏛 기반 연구: [[papers/1487_Multimodal_Spatial_Language_Maps_for_Robot_Navigation_and_Ma/review]] — 사전훈련된 멀티모달 모델의 특징을 공간적으로 융합하는 방법론이 로봇 네비게이션의 기반 기술을 제공합니다.
