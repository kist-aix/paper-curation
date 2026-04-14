---
title: "1586_TidyBot_Personalized_Robot_Assistance_with_Large_Language_Mo"
authors:
  - "Jimmy Wu"
  - "Rika Antonova"
  - "Adam Kan"
  - "Marion Lepert"
  - "Andy Zeng"
date: "2023.05"
doi: ""
arxiv: ""
score: 4.0
essence: "이 논문은 대규모 언어모델(LLM)의 요약 능력을 활용하여 로봇이 적은 수의 예시로부터 사용자의 개인화된 물건 정리 선호도를 학습하고 일반화할 수 있음을 보여준다. TidyBot이라는 실제 모바일 매니퓨레이터에서 91.2% 벤치마크 정확도와 85.0% 실제 환경 성공률을 달성했다."
tags:
  - "cat/Embodied_Navigation_and_Planning"
  - "sub/Language-Grounded_Action_Planning"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wu et al._2023_TidyBot Personalized Robot Assistance with Large Language Models.pdf"
---

# TidyBot: Personalized Robot Assistance with Large Language Models

> **저자**: Jimmy Wu, Rika Antonova, Adam Kan, Marion Lepert, Andy Zeng, Shuran Song, Jeannette Bohg, Szymon Rusinkiewicz, Thomas Funkhouser | **날짜**: 2023-05-09 | **URL**: [https://arxiv.org/abs/2305.05658](https://arxiv.org/abs/2305.05658)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1 We study the task of household cleanup, where each*

이 논문은 대규모 언어모델(LLM)의 요약 능력을 활용하여 로봇이 적은 수의 예시로부터 사용자의 개인화된 물건 정리 선호도를 학습하고 일반화할 수 있음을 보여준다. TidyBot이라는 실제 모바일 매니퓨레이터에서 91.2% 벤치마크 정확도와 85.0% 실제 환경 성공률을 달성했다.

## Motivation

- **Known**: 로봇 가구정리는 오래된 연구 주제이며, 기존 접근법들은 사용자 선호도를 명시적으로 지정하거나 대규모 크라우드소싱 데이터를 요구했다. 최근 LLM의 상식 추론 능력이 로봇 시스템에 활용되고 있다.
- **Gap**: 기존 개인화된 물건 정리 방법들은 많은 사용자 데이터 수집이 필요하거나 새로운 사용자에게 적응하기 어려웠다. 적은 수의 예시로부터 일반화 가능한 개인화 선호도를 효율적으로 학습하는 방법이 부재했다.
- **Why**: 개인의 생활 방식과 문화적 배경에 따라 물건 정리 선호도가 크게 다르므로, 개인화된 로봇 어시스턴트는 일상적 가사업무 자동화에 필수적이다. 적응형 학습은 실제 배포 환경에서의 로봇 유용성을 크게 향상시킬 수 있다.
- **Approach**: 사용자가 제공한 적은 수의 물건 배치 예시를 LLM에 입력하여 일반화된 선호도 규칙으로 요약하게 하고, 오픈 어휘 이미지 분류기로 바닥의 물건을 인식하여 학습된 규칙에 따라 배치한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2 System overview. Once the user’s preferences have been summarized with an LLM, TidyBot will localize the closest*

- **벤치마크 성능**: 미공개 물건에 대해 91.2% 정확도 달성
- **실제 환경 성능**: TidyBot이 실제 테스트 시나리오에서 85.0%의 물건을 성공적으로 정리
- **데이터 효율성**: 추가 학습이나 대규모 데이터 수집 없이 기존 LLM 활용
- **확장성**: 물건 배치뿐만 아니라 조작 원시 작업(pick and place vs pick and toss) 선택까지 확장 가능
- **해석 가능성**: 텍스트 기반의 인간 이해 가능한 규칙 형태로 선호도 표현

## How

![Figure 2](figures/fig2.webp)

*Fig. 2 System overview. Once the user’s preferences have been summarized with an LLM, TidyBot will localize the closest*

- 사용자가 자연어로 물건 배치 예시 제공 (예: '노란 셔츠는 서랍에, 진한 보라색 셔츠는 옷장에')", "LLM에 few-shot 프롬프팅으로 예시들을 일반화된 규칙으로 요약 (예: '밝은색 옷은 서랍에, 어두운색 옷은 옷장에')", '요약된 규칙의 명사들을 CLIP 등 오픈 어휘 이미지 분류기로 그라운딩하여 이미지에서 탐지 가능하게 변환
- 로봇이 반복적으로 바닥의 물건을 감지, 분류, 목표 수용함에 배치하는 과정 수행
- 벤치마크 데이터셋과 실제 로봇 환경에서 정량적 평가 실시

## Originality

- LLM의 텍스트 요약 능력을 로봇 일반화 문제의 핵심으로 활용한 새로운 관점 제시
- 기존 협업 필터링, 공간 관계, 잠재 벡터 학습 기반 방법과 달리 추가 학습 없이 기존 LLM 직접 활용
- 개인화된 물건 정리 선호도 평가를 위한 벤치마크 데이터셋 공개
- 실제 모바일 매니퓨레이터 시스템 구현 및 평가로 실용성 입증
- 인간 선호도 평가 연구로 LLM 생성 규칙과 인간 평가 간 일관성 검증

## Limitation & Further Study

- LLM 성능은 모델 선택과 프롬프트 설계에 의존하며, 다양한 문화적 배경의 선호도 학습 능력에 대한 연구 부족
- 실제 환경에서 85% 성공률은 인식 오류(물건 감지 실패)와 조작 오류(픽 실패, 배치 실패) 누적의 영향
- 벤치마크는 텍스트 기반이고 실제 환경의 복잡성(가림, 불규칙한 배치, 다양한 표면)을 완전히 반영하지 못함
- 후속 연구: 시각적 특성이 아닌 의미적 속성 기반 분류 능력 강화, 로봇 조작 안정성 개선, 다문화 선호도 학습 메커니즘 개발

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 LLM의 요약 능력을 로봇 개인화 문제에 창의적으로 적용하여 데이터 효율적이고 해석 가능한 솔루션을 제시했다. 실제 로봇 시스템에서의 검증과 공개 데이셋 제공으로 실용성과 재현성을 담보하였으며, 서비스 로봇 개인화 분야에 중요한 기여를 한다.

## Related Papers

- 🔗 후속 연구: [[papers/1512_PaLM-E_An_Embodied_Multimodal_Language_Model/review]] — TidyBot의 개인화된 로봇 지원이 PaLM-E의 멀티모달 언어 모델 기반 embodied AI 능력을 특정 도메인(정리)에 특화시킨 확장
- 🏛 기반 연구: [[papers/1369_Do_As_I_Can_Not_As_I_Say_Grounding_Language_in_Robotic_Affor/review]] — TidyBot이 실제 환경에서 언어 기반 affordance grounding을 구현하는 방식이 Do As I Can, Not As I Say의 원리를 실용적으로 적용
- 🔄 다른 접근: [[papers/1341_CoPAL_Corrective_Planning_of_Robot_Actions_with_Large_Langua/review]] — TidyBot은 LLM을 통한 선호도 학습을, CoPAL은 대화형 계획 수정을 통해 로봇이 사용자 요구에 적응하는 다른 방식
