---
title: "1328_Chain-of-Action_Trajectory_Autoregressive_Modeling_for_Robot"
authors:
  - "Wenbo Zhang"
  - "Tianrun Hu"
  - "Hanbo Zhang"
  - "Yanyuan Qiao"
  - "Yuchu Qin"
date: "2025.06"
doi: ""
arxiv: ""
score: 4.0
essence: "Chain-of-Action(CoA)은 역방향 궤적 자동회귀 모델링을 통해 로봇 조작 정책을 학습하는 새로운 시각-운동 정책 패러다임으로, 목표 상태부터 역순으로 행동 시퀀스를 생성하여 누적 오차를 완화한다."
tags:
  - "cat/Multimodal_Vision-Language_Policy_Learning"
  - "sub/Visual_Reasoning_Systems"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhang et al._2025_Chain-of-Action Trajectory Autoregressive Modeling for Robotic Manipulation.pdf"
---

# Chain-of-Action: Trajectory Autoregressive Modeling for Robotic Manipulation

> **저자**: Wenbo Zhang, Tianrun Hu, Hanbo Zhang, Yanyuan Qiao, Yuchu Qin, Yang Li, Jiajun Liu, Tao Kong, Lingqiao Liu, Xiao Ma | **날짜**: 2025-06-11 | **URL**: [https://arxiv.org/abs/2506.09990](https://arxiv.org/abs/2506.09990)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2 Chain-of-Action built on trajectory autoregressive modeling. The left part illustrates the network*

Chain-of-Action(CoA)은 역방향 궤적 자동회귀 모델링을 통해 로봇 조작 정책을 학습하는 새로운 시각-운동 정책 패러다임으로, 목표 상태부터 역순으로 행동 시퀀스를 생성하여 누적 오차를 완화한다.

## Motivation

- **Known**: 기존 시각-운동 정책은 순방향으로 다음 행동을 예측하는 방식으로 학습되어 누적 오차 문제를 겪으며, ACT와 Diffusion Policy 등이 이를 완화하기 위해 행동 청킹이나 노이징 과정을 도입했다.
- **Gap**: 순방향 예측 패러다임의 근본적인 한계는 현재 관측만을 기반으로 최적화되어 장기 목표 달성을 보장하지 못한다는 점이며, 기존 완화 기법들은 증상만 치료할 뿐 근본 원인을 해결하지 못한다.
- **Why**: 로봇 조작은 복잡한 다단계 작업을 요구하므로 목표 지향적 행동 생성이 필수적이며, 역순 생성을 통한 전역-국소 일관성 강화는 일반화 능력과 실행 신뢰성을 크게 향상시킬 수 있다.
- **Approach**: CoA는 keyframe 행동(목표 인코딩)부터 시작하여 역순으로 행동 토큰을 자동회귀적으로 생성하며, 이를 안정적으로 실현하기 위해 연속 행동 표현, 동적 정지, 역시간 앙상블, 다중 토큰 예측 등 4가지 핵심 설계를 통합한다.

## Achievement

![Figure 4](figures/fig4.webp)

*Figure 4 Success rate improvement on RLBench-60, sorted by improvement from high to low. The average success*

- **RLBench 벤치마크 성능**: 60개 작업에서 ACT 대비 16%, Diffusion Policy 대비 23% 성능 향상 달성
- **실제 로봇 조작**: 8가지 실제 조작 작업에서 ACT를 15% 초과 성능
- **공간 일반화**: keyframe-기반 역순 생성이 분포 외 조건에서 강한 일반화 능력 제시
- **구조적 단순성**: ACT와 유사한 아키텍처를 사용하면서도 패러다임 변화만으로 성능 향상을 달성하여 접근법의 우수성 입증

## How

![Figure 2](figures/fig2.webp)

*Figure 2 Chain-of-Action built on trajectory autoregressive modeling. The left part illustrates the network*

- Transformer 인코더-디코더 구조로 시각(CNN + patchify) 및 고유수용성 입력을 처리
- 학습 단계에서 행동 시퀀스를 역순으로 재배열하여 keyframe 행동 aT부터 a1까지 자동회귀적으로 생성
- **Continuous action representation**: 이산화로 인한 해상도 손실 제거 및 역순 누적 오차 방지
- **Multi-token prediction**: 하위 궤적(sub-trajectory)의 국소 의존성 모델링으로 학습 안정성 향상
- **Dynamic stop mechanism**: 목표까지의 거리 기반으로 생성 종료 판단, EOS 토큰 없이 폐루프 실행 실현
- **Reverse temporal ensemble**: 여러 역순 롤아웃을 앙상블하여 시간적 오정렬 완화 및 분산 감소

## Originality

- 로봇 조작에 역순 궤적 생성 패러다임을 최초 도입하여 순방향 예측의 근본적 한계 극복
- Action-level Chain-of-Thought 개념으로 행동 시퀀스에 직접 추론 구조 적용 (시각 이미지, 바운딩 박스 등 중간 표현 미사용)
- Keyframe을 자동회귀 구조의 초기 토큰으로 통합하여 계층적 모델링과 폐루프 실행을 단일 프레임워크 내에서 실현
- 역순 생성의 실제 구현을 위한 4가지 필수 설계(연속 표현, 다중 토큰, 동적 정지, 역시간 앙상블)의 체계적 제시

## Limitation & Further Study

- Keyframe 정의가 그리퍼 상태 변화나 관절 속도 근처 이상의 단순한 휴리스틱에 의존하여, 복잡한 작업에서 의미있는 목표 인코딩을 보장하지 못할 수 있음
- 역순 생성의 이론적 정당성(왜 역순이 순방향보다 나은가)에 대한 형식적 분석 부재
- 실제 환경에서의 평가가 8개 작업에 한정되어 있어 일반화 능력의 광범위한 검증 필요
- 동적 환경(움직이는 장애물, 다중 객체 상호작용)에서의 성능 미평가
- 계산 비용 분석 및 ACT, Diffusion Policy와의 속도 비교 부재
- 후속 연구로 더 정교한 목표 인코딩 방법, 수정 불가능한 오류에 대한 적응 메커니즘, 확장 가능성(VLA 모델)에 대한 검토 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: Chain-of-Action은 로봇 조작에서 누적 오차 문제를 근본적으로 해결하기 위해 역순 궤적 생성 패러다임을 도입하며, 필수 설계 요소들의 통합으로 순방향 방식을 명확히 상회하는 성능을 달성하여 시각-운동 정책 학습의 새로운 방향을 제시한다.

## Related Papers

- 🔄 다른 접근: [[papers/1342_CorrectNav_Self-Correction_Flywheel_Empowers_Vision-Language/review]] — 둘 다 시각-언어 모델의 오류 처리를 다루지만 Chain-of-Action은 역방향 궤적 모델링을, CorrectNav는 self-correction을 사용한다.
- 🔗 후속 연구: [[papers/1584_ThinkAct_Vision-Language-Action_Reasoning_via_Reinforced_Vis/review]] — ThinkAct의 vision-language-action reasoning이 CoA의 역방향 궤적 생성을 더 체계적인 추론 과정으로 발전시킬 수 있다.
- 🏛 기반 연구: [[papers/1528_Reflective_Planning_Vision-Language_Models_for_Multi-Stage_L/review]] — Reflective Planning의 multi-stage 계획 수립이 Chain-of-Action의 역방향 행동 시퀀스 생성에 대한 이론적 기반을 제공한다.
- 🏛 기반 연구: [[papers/1526_Real-World_Humanoid_Locomotion_with_Reinforcement_Learning/review]] — 이족 보행을 위한 심층 강화학습의 이론적 배경과 방법론적 토대를 제공함
- 🏛 기반 연구: [[papers/1467_Humanoid_Locomotion_as_Next_Token_Prediction/review]] — Chain-of-Action의 autoregressive 모델링이 Next Token Prediction 접근법의 기반이 된다
- 🔄 다른 접근: [[papers/1342_CorrectNav_Self-Correction_Flywheel_Empowers_Vision-Language/review]] — 둘 다 vision-language 모델의 오류 처리를 다루지만 CorrectNav는 self-correction flywheel을, Chain-of-Action은 역방향 궤적 모델링을 사용한다.
- 🏛 기반 연구: [[papers/1374_DynamicVLA_A_Vision-Language-Action_Model_for_Dynamic_Object/review]] — Chain-of-Action의 trajectory autoregressive modeling이 DynamicVLA의 dynamic object manipulation을 위한 기반 방법론이다.
