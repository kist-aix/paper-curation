---
title: "1459_LLM-State_Open_World_State_Representation_for_Long-horizon_T"
authors:
  - "Siwei Chen"
  - "Anxing Xiao"
  - "David Hsu"
date: "2023.11"
doi: ""
arxiv: ""
score: 4.0
essence: "개방형 환경에서 LLM의 장기 작업 계획을 위해 객체 속성을 동적으로 추적하고 업데이트하는 하이브리드 상태 표현 LLM-State를 제안한다. 이는 구조화된 객체 중심 표현과 비구조화된 행동 이력 요약을 결합하여 장기간 상태 추적 및 실패 복구를 개선한다."
tags:
  - "cat/Embodied_Navigation_and_Planning"
  - "sub/LLM_Task_Planning"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chen et al._2023_LLM-State Open World State Representation for Long-horizon Task Planning with Large Language Model.pdf"
---

# LLM-State: Open World State Representation for Long-horizon Task Planning with Large Language Model

> **저자**: Siwei Chen, Anxing Xiao, David Hsu | **날짜**: 2023-11-29 | **URL**: [https://arxiv.org/abs/2311.17406](https://arxiv.org/abs/2311.17406)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1: LLM-State Example. The proposed state representation is a mixture*

개방형 환경에서 LLM의 장기 작업 계획을 위해 객체 속성을 동적으로 추적하고 업데이트하는 하이브리드 상태 표현 LLM-State를 제안한다. 이는 구조화된 객체 중심 표현과 비구조화된 행동 이력 요약을 결합하여 장기간 상태 추적 및 실패 복구를 개선한다.

## Motivation

- **Known**: 기존 LLM 기반 작업 계획 방법들은 사전정의된 상태 표현이나 대규모 지상 진실 객체에 의존하거나 수동으로 설계된 피드백을 사용한다. 이는 개방형 환경의 복잡성을 충분히 포착하지 못하고 일반화 능력이 제한된다.
- **Gap**: 기존 방법들은 미관측 객체 속성을 명시적으로 추적하지 못하여 장기 작업에서 오류가 발생하며, 부분 관측 환경에서 대량의 텍스트 입력을 효과적으로 관리하지 못한다. 또한 실패 이유와 선행조건 분석이 부족하다.
- **Why**: 개방형 가정 환경에서의 로봇 자동화는 일상생활 품질 향상과 신체 제약이 있는 사람들의 접근성 증대에 중요하며, 이를 위해서는 복잡한 장기 작업을 신뢰성 있게 계획할 수 있는 시스템이 필수이다.
- **Approach**: LLM을 Attention, State Encoder, Policy의 세 역할로 활용하여 관련 객체를 선별하고 구조화된 객체-속성 표현을 자동으로 생성하며, 비구조화된 체인-오브-쏘트 기반 행동 이력 요약을 추가하여 속성 예측 정확도와 실패 복구 능력을 향상한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Fig. 1: LLM-State Example. The proposed state representation is a mixture*

- **하이브리드 상태 표현**: 구조화된 객체-속성 표현과 비구조화된 행동 요약을 결합하여 장기 작업의 정보 손실 문제를 완화한다.
- **동적 속성 확장**: LLM의 맥락 이해 능력을 활용해 예측되지 않은 객체 속성을 자동으로 추적하고 업데이트한다.
- **실패 분석 및 복구**: 실패한 행동과 그 원인을 추적하여 선행조건 미충족 등의 문제를 사전에 예방한다.
- **광범위한 실험 검증**: VirtualHome 시뮬레이션 및 실제 환경에서 기존 방법 대비 유의미한 성능 향상을 입증한다.

## How

![Figure 2](figures/fig2.webp)

*Fig. 2: Overview of the system framework. The task planner consists of three components: LLM as Encoder, LLM as State Es*

- LLM as Attention: 장시간 관측 텍스트에서 작업 목표와 관련된 객체를 식별하여 입력 복잡도를 감소시킨다.
- LLM as State Encoder: 식별된 객체와 실행된 행동을 입력받아 객체의 새로운 속성을 출력하는 상태 업데이트를 수행한다.
- 구조화된 표현 유지: 각 객체를 [객체명]: [속성1, 속성2, ...] 형식으로 표현하여 명시적 추적을 가능하게 한다.
- 비구조화된 요약 생성: 행동 이력을 단계별 chain-of-thought로 요약하고 최근 실패 행동의 원인을 분석한다.
- 반복적 세계 모델 업데이트: 시행착오를 통해 행동 선행조건 및 전이 효과를 지속적으로 개선한다.
- Closed-loop 실행: 행동 성공/실패 이진 결과를 피드백받아 다음 행동을 재계획한다.

## Originality

- LLM의 추론 능력을 상태 표현 구성에 직접 활용하는 새로운 패러다임: 기존 방법들과 달리 LLM 자체가 객체 속성 추적을 담당한다.
- 구조-비구조 하이브리드 접근: 명시성과 유연성의 균형을 위해 정형화된 객체 표현과 자유형식 행동 요약을 결합한 독창적 설계이다.
- 개방형 속성 공간: 미리 정의하지 않은 속성도 LLM이 자동으로 발견하고 추적할 수 있는 확장 가능한 표현이다.
- 실패 기반 학습: 행동 실패 원인 분석을 상태 표현에 통합하여 선행조건 추론 능력을 강화한다.

## Limitation & Further Study

- 완벽한 객체 탐지 및 견고한 저수준 행동 제어 가정: 실제 환경의 지각 오류나 제어 불안정성을 다루지 않는다.
- LLM 호출 비용 증가: 매 시간 단계에 Attention, State Encoder, Policy를 반복 실행하므로 계산 효율성이 제한된다.
- 정량적 비교 분석 부족: 초록에서 성능 향상을 언급하나 본문(발췌)에서 구체적 수치 결과가 제시되지 않는다.
- 속성 예측 오류 누적: 장기 작업에서 LLM의 속성 예측이 누적 오류를 야기할 가능성이 존재한다.
- 후속연구 제안: (1) 다중 모달리티 입력 통합, (2) 에너지 효율적 LLM 호출 스케줄링, (3) 지각 불확실성 처리 메커니즘, (4) 다양한 로봇 플랫폼으로의 일반화

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 개방형 환경의 장기 작업 계획을 위해 LLM의 추론 능력을 상태 표현 구성에 직접 활용하는 창의적 접근을 제시하며, 구조-비구조 하이브리드 설계를 통해 명시성과 유연성의 균형을 달성한다. 다만 실제 환경 적용, 계산 효율성, 정량적 검증에서 개선이 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/1434_Inner_Monologue_Embodied_Reasoning_through_Planning_with_Lan/review]] — LLM의 내적 독백을 통한 추론이 장기 작업에서 상태 표현과 결합될 때 더욱 효과적인 계획 수립이 가능합니다.
- 🔗 후속 연구: [[papers/1460_LLM3Large_Language_Model-based_Task_and_Motion_Planning_with/review]] — 객체 중심 상태 표현을 task and motion planning과 결합하여 더욱 체계적인 장기 작업 수행을 달성할 수 있습니다.
- 🔄 다른 접근: [[papers/1579_Statler_State-Maintaining_Language_Models_for_Embodied_Reaso/review]] — 두 논문 모두 상태 유지형 언어 모델을 다루지만, 하나는 객체 중심 표현에, 다른 하나는 체화된 추론에 집중합니다.
- 🧪 응용 사례: [[papers/1561_SayPlan_Grounding_Large_Language_Models_using_3D_Scene_Graph/review]] — 3D 장면 그래프를 이용한 언어 그라운딩이 객체 중심 상태 표현을 실제 환경에서 구현하는 데 활용됩니다.
- 🔗 후속 연구: [[papers/1434_Inner_Monologue_Embodied_Reasoning_through_Planning_with_Lan/review]] — LLM의 내적 독백을 통한 추론 방식을 장기 작업 계획에서 상태 표현과 결합하여 더욱 강화할 수 있습니다.
- 🔄 다른 접근: [[papers/1460_LLM3Large_Language_Model-based_Task_and_Motion_Planning_with/review]] — 두 논문 모두 LLM 기반 장기 계획을 다루지만, 하나는 모션 계획 실패 추론에, 다른 하나는 상태 표현에 집중합니다.
- 🔄 다른 접근: [[papers/1579_Statler_State-Maintaining_Language_Models_for_Embodied_Reaso/review]] — 로봇의 상태 관리를 위해 Statler는 명시적 상태 추적을, LLM-State는 개방형 세계 상태 표현을 사용하는 서로 다른 접근법
