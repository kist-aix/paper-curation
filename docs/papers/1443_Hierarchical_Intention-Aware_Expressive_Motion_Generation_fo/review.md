---
title: "1443_Hierarchical_Intention-Aware_Expressive_Motion_Generation_fo"
authors:
  - "Lingfan Bao"
  - "Yan Pan"
  - "Tianhu Peng"
  - "Dimitrios Kanoulas"
  - "Chengxu Zhou"
date: "2025.06"
doi: ""
arxiv: ""
score: 4.0
essence: "본 논문은 비전-언어 모델(VLM)의 의도 추론과 diffusion 기반 동작 생성을 계층적으로 결합하여, 인간의 의도와 감정 맥락을 인식하고 실시간으로 표현력 있는 제스처를 생성하는 인간형 로봇 시스템 HIAER을 제안한다."
tags:
  - "cat/Humanoid_Teleoperation_and_Interaction"
  - "sub/Socially_Expressive_Robotics"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Bao et al._2025_Hierarchical Intention-Aware Expressive Motion Generation for Humanoid Robots.pdf"
---

# Hierarchical Intention-Aware Expressive Motion Generation for Humanoid Robots

> **저자**: Lingfan Bao, Yan Pan, Tianhu Peng, Dimitrios Kanoulas, Chengxu Zhou | **날짜**: 2025-06-02 | **URL**: [https://arxiv.org/abs/2506.01563](https://arxiv.org/abs/2506.01563)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1: Overall framework of the proposed work. (a) The high-level system architecture. Multimodal inputs XI = (Vin, Lin*

본 논문은 비전-언어 모델(VLM)의 의도 추론과 diffusion 기반 동작 생성을 계층적으로 결합하여, 인간의 의도와 감정 맥락을 인식하고 실시간으로 표현력 있는 제스처를 생성하는 인간형 로봇 시스템 HIAER을 제안한다.

## Motivation

- **Known**: 최근 VLM은 고수준 인간 의도 해석에 뛰어났으며, diffusion 모델은 텍스트 조건부로 표현력 있는 동작을 생성할 수 있다. 또한 AMASS, HumanML3D 같은 대규모 모션 데이터셋이 일반화된 생성 모델 학습을 가능하게 했다.
- **Gap**: 기존 접근법들은 명시적 기능 목표 분해에 집중하며, 암묵적인 감정 의도와 사회적 맥락을 통합적으로 처리하지 못하고, 동적 상황에서의 적응적 제스처 생성이 부족하다.
- **Why**: 인간-로봇 상호작용에서 의도 이해와 감정 인식을 바탕으로 한 표현력 있는 비언어적 반응은 신뢰 구축, 협력 촉진, 사용자 참여 증대에 필수적이다.
- **Approach**: 계층적 프레임워크로 VLM의 in-context learning을 통해 사회적 의도와 valence-arousal 감정 매개변수를 추론한 후, 이를 조건으로 text-to-motion diffusion 모델(DART)이 제스처를 생성하고, RL 기반 whole-body controller로 실제 로봇에서 실행한다.

## Achievement

![Figure 4](figures/fig4.webp)

*Fig. 4: Qualitative results across the six representative interaction scenarios. Each subfigure from (a) to (f) displays*

- **계층적 의도-감정 통합 프레임워크**: VLM의 ICL과 Chain-of-Thought 프롬팅으로 사회적 의도 추론과 V-A 공간 감정 맥락 추정을 동시에 수행하는 통합 모듈 개발
- **V-A 매개변수화**: 복잡한 사회적 의도를 valence-arousal 차원으로 매개변수화하여 상황 맞춤형 표현력 있는 동작 선택 가능
- **실시간 다양한 동작 생성**: DART diffusion 모델과 대규모 모션 데이터셋을 결합하여 템플릿 의존 없이 고품질의 물리적으로 타당한 제스처 실시간 합성
- **물리 로봇 구현 및 검증**: 실제 인간형 로봇에서 완전한 시스템 구현 및 현실적 HRI 시나리오에서 사회적 지능과 맥락 적절성이 향상되었음을 실증

## How

![Figure 1](figures/fig1.webp)

*Fig. 1: Overall framework of the proposed work. (a) The high-level system architecture. Multimodal inputs XI = (Vin, Lin*

- VLM (πi) 모듈: 사전-프롬프트(Lpre), few-shot 예제, 대화 이력(HI/O)을 활용하여 다중모드 입력(시각 Vin, 언어 Lin)에서 장면 설명(d), 의도(i), 신뢰도(c), V-A 추정, 동작 원시형(⟨m⟩) 추출
- Motion Planner (πp): 의도 모듈 출력을 조건으로 DART text-to-motion diffusion 모델이 시간적으로 일관성 있는 인간 동작 궤적(ŷt:t+n) 합성
- Retargeting: 합성된 궤적을 로봇의 운동학(kinematics)에 맞게 변환하여 목표 궤적(yt:t+n) 생성
- Whole-body Controller (πw): RL 기반 제어기가 최종 궤적을 로봇 액션(at)으로 변환하여 물리 로봇에서 안정적으로 실행

## Originality

- VLM의 의도 추론과 V-A 감정 공간을 통합하여 사회적 맥락 인식 동작 생성의 완전한 폐루프 구현
- Confidence scoring과 fallback 동작을 포함한 구조화된 프롬팅 전략으로 의도 추론의 신뢰성 향상
- DART diffusion 모델과 RL 기반 whole-body controller를 대규모 인간 모션 데이터셋 위에 통합하여 템플릿 기반 방식의 제약 극복
- 실제 인간형 로봇 플랫폼에서 완전한 파이프라인 검증으로 이론에서 실무까지의 간격 축소

## Limitation & Further Study

- V-A 공간의 이산화로 인한 복잡한 감정 상태의 표현 한계 및 연속적 감정 변화 추적의 정확도 향상 필요
- VLM의 의도 추론이 입력된 few-shot 예제의 품질과 대화 이력에 크게 의존하는 잠재적 편향 문제
- 실시간 성능과 계산 비용 간 트레이드오프로 인한 확장성 제약 및 더 저지연 추론 방법 개발 필요
- 현재 실험이 제한된 HRI 시나리오에 중점을 두고 있으므로, 더 다양한 문화적·사회적 맥락에서의 일반화 검증 필요
- **후속 연구**: 더 표현력 있는 감정 모델(예: 고차원 감정 공간), 온라인 프롬프트 학습, 장기간 상호작용에서의 누적 맥락 관리 등

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 VLM 기반 의도 추론과 diffusion 동작 생성을 계층적으로 결합하고 감정 컨텍스트를 통합하여 사회적으로 지능형인 로봇 제스처를 실현한 의미 있는 연구이며, 실제 로봇 플랫폼에서의 완전한 구현과 검증으로 높은 실용적 가치를 보유하고 있다.

## Related Papers

- 🔄 다른 접근: [[papers/1381_EMOTION_Expressive_Motion_Sequence_Generation_for_Humanoid_R/review]] — 둘 다 휴머노이드의 표현적 동작 생성을 다루지만 HIAER은 의도인식에, EMOTION은 감정표현에 중점을 둔다
- 🏛 기반 연구: [[papers/1387_ExBody2_Advanced_Expressive_Humanoid_Whole-Body_Control/review]] — ExBody2의 전신 표현적 제어 기술이 HIAER의 감정적 제스처 생성의 기반이 된다
- 🔗 후속 연구: [[papers/1268_An_Empirical_Evaluation_of_Four_Off-the-Shelf_Proprietary_Vi/review]] — VLM의 멀티모달 이해 능력을 휴머노이드의 실시간 표현적 동작 생성에 확장 적용했다
- 🔄 다른 접근: [[papers/1289_Bi-Level_Motion_Imitation_for_Humanoid_Robots/review]] — 휴머노이드 표현적 동작에서 의도-감정 기반과 계층적 의도 인식의 다른 접근이다
