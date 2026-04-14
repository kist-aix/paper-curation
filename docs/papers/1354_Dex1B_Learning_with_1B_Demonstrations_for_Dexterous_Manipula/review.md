---
title: "1354_Dex1B_Learning_with_1B_Demonstrations_for_Dexterous_Manipula"
authors:
  - "Jianglong Ye"
  - "Keyi Wang"
  - "Chengjing Yuan"
  - "Ruihan Yang"
  - "Yiquan Li"
date: "2025.06"
doi: ""
arxiv: ""
score: 4.0
essence: "생성 모델과 최적화 방법을 결합하여 10억 개의 고품질 손가락 조작 시연을 생성한 Dex1B 데이터셋과 이를 활용하는 DexSimple 방법을 제시하여 손가락 조작 작업의 성능을 22% 향상시켰다."
tags:
  - "cat/Embodied_Navigation_and_Planning"
  - "sub/Synthetic_Grasping_Datasets"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ye et al._2025_Dex1B Learning with 1B Demonstrations for Dexterous Manipulation.pdf"
---

# Dex1B: Learning with 1B Demonstrations for Dexterous Manipulation

> **저자**: Jianglong Ye, Keyi Wang, Chengjing Yuan, Ruihan Yang, Yiquan Li, Jiyue Zhu, Yuzhe Qin, Xueyan Zou, Xiaolong Wang | **날짜**: 2025-06-20 | **URL**: [https://arxiv.org/abs/2506.17198](https://arxiv.org/abs/2506.17198)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1: The Dex1B benchmark consists of 1B generated high-quality demonstrations for grasping (top) and articulation (mi*

생성 모델과 최적화 방법을 결합하여 10억 개의 고품질 손가락 조작 시연을 생성한 Dex1B 데이터셋과 이를 활용하는 DexSimple 방법을 제시하여 손가락 조작 작업의 성능을 22% 향상시켰다.

## Motivation

- **Known**: 손가락 조작은 로봇공학에서 오랫동안 연구된 분야이지만 고품질의 대규모 시연 데이터 수집이 어려웠으며, 최적화 기반 방법이나 강화학습을 통한 시연 생성이 시도되어 왔다.
- **Gap**: 기존 최적화 기반 방법은 느리고 초기화에 민감하며, RL 기반 방법은 다양성이 부족하고, 순수 생성 모델은 실현 가능성과 다양성 모두 제한적이다.
- **Why**: 대규모의 다양하고 물리적으로 타당한 시연 데이터는 학습 기반 손가락 조작 모델의 성능과 견고성을 크게 향상시킬 수 있기 때문이다.
- **Approach**: 최적화 기반으로 작은 규모의 seed 데이터셋을 구성한 후 generative model을 학습시키고, geometric constraints를 통합하여 실현 가능성을 개선하며, 조건부 생성과 debiasing 메커니즘으로 다양성을 확보한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Fig. 1: The Dex1B benchmark consists of 1B generated high-quality demonstrations for grasping (top) and articulation (mi*

- **Dex1B 데이터셋**: 6,000개 이상의 다양한 객체에 대해 grasping과 articulation 작업을 위한 10억 개의 시연으로 구성되며, DexGraspNet 대비 700배 이상의 시연 규모를 확보
- **DexSimple 베이스라인**: 조건부 생성과 강화된 손실 함수를 통합한 간단하면서도 효과적인 정책 학습 방법으로, Dex1B의 규모와 다양성을 활용하는 데 최적화
- **성능 향상**: 손가락 조합 작업에서 기존 최고 성능 대비 22% 향상을 달성하고 새로운 벤치마크 설정
- **sim-to-real 전이**: 시뮬레이션에서 학습한 정책이 실제 로봇 환경으로 효과적으로 전이되는 것을 실증

## How

![Figure 2](figures/fig2.webp)

*Fig. 2: Dex1B demonstration collection. The engine takes object assets and hand pose initialization as input, using a co*

- 최적화 기반 seed 데이터셋 구성: GraspIt 플래너와 유사한 접근을 통해 고품질 초기 시연 생성
- Geometric constraints 통합: 생성 모델에 기하학적 제약을 포함하여 물리적 실현 가능성 향상
- Debiasing 메커니즘: 덜 자주 관찰된 조건에 대한 hand pose 생성을 우선시하여 데이터 다양성 확장
- 조건부 생성: 객체 기하학 및 손 파라미터에 대한 조건부 생성으로 특정 조건에서의 다양한 행동 생성
- 반복적 파이프라인: seed 데이터셋으로부터 generative model 학습 → 데이터 생성 → 다시 학습 데이터에 포함하는 반복 과정
- Motion planning: 핵심 상호작용 지점의 hand pose를 합성하고 나머지 reaching, lifting 등의 동작은 motion planning으로 생성

## Originality

- 최적화와 생성 모델의 계층적 결합: 최적화로 seed 데이터를 확보하고 generative model로 대규모 확장하는 독창적 파이프라인
- 10억 규모의 시연 생성: 기존 연구 대비 획기적으로 확대된 데이터셋 규모와 이를 체계적으로 생성하는 방법론
- 다각도 debiasing 전략: 조건부 생성을 통한 다양성 확보로 순수 생성 모델의 보간 문제 해결
- 통합 벤치마크: grasping과 articulation을 통합한 포괄적 손가락 조작 벤치마크 제시

## Limitation & Further Study

- 생성 모델의 학습 초기 단계에서의 bias 영향: seed 데이터셋의 편향이 완전히 제거되지 않을 수 있음
- Shadow Hand, Inspire Hand, Ability Hand 등 특정 손 형태에만 최적화: 다른 손 구조로의 일반화 가능성 미검증
- 물리 시뮬레이션 기반 평가: 시뮬레이터의 정확도와 실제 환경의 차이로 인한 sim-to-real gap 가능성
- 후속 연구: 더 다양한 손 형태와 환경에 대한 확장, 온라인 학습을 통한 실시간 데이터 개선, diffusion model 등 다른 생성 모델 아키텍처 탐색

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 생성 모델과 최적화를 결합하여 10억 개의 대규모 손가락 조작 시연 데이터셋을 체계적으로 구성하고, 이를 활용한 간단하면서도 효과적한 학습 방법으로 최고 성능을 달성한 중요한 기여이다. 데이터셋의 규모, 다양성, 품질 측면에서 혁신적이며 실제 로봇 실험을 통한 검증도 충분하다.

## Related Papers

- 🔄 다른 접근: [[papers/1413_GraspVLA_a_Grasping_Foundation_Model_Pre-trained_on_Billion-/review]] — GraspVLA도 10억 규모 합성 데이터로 집기 학습하는 유사한 접근법을 사용한다.
- 🔗 후속 연구: [[papers/1356_DreamGen_Unlocking_Generalization_in_Robot_Learning_through/review]] — DreamGen의 합성 데이터 생성 파이프라인이 Dex1B의 대규모 시연 데이터 활용에 도움이 된다.
- 🏛 기반 연구: [[papers/1428_GraspDreamer_생성형_인간_시연_기반_기능적_파지_모방_학습/review]] — GraspDreamer의 생성형 시연 기반 학습이 Dex1B의 시연 데이터 생성 방법론과 연결된다.
- 🏛 기반 연구: [[papers/1353_DreamControl-v2_Simpler_and_Scalable_Autonomous_Humanoid_Ski/review]] — DreamControl의 whole-body humanoid control이 DreamControl-v2의 확장 가능한 기술 습득에 대한 기반 방법론을 제공한다.
- 🔗 후속 연구: [[papers/1405_Generative_Artificial_Intelligence_in_Robotic_Manipulation_A/review]] — Dex1B의 대규모 합성 데이터 생성이 로봇 조작의 데이터 부족 문제 해결에 기여한다.
- 🔄 다른 접근: [[papers/1413_GraspVLA_a_Grasping_Foundation_Model_Pre-trained_on_Billion-/review]] — Dex1B도 10억 규모 시연 데이터로 손가락 조작을 학습하는 유사한 접근법이다.
- 🏛 기반 연구: [[papers/1558_RVT-2_Learning_Precise_Manipulation_from_Few_Demonstrations/review]] — 대규모 demonstration 학습의 원리를 적은 수의 시연으로도 효과적인 학습이 가능한 방법론으로 발전시킨다.
- 🧪 응용 사례: [[papers/1442_Heracles_Bridging_Precise_Tracking_and_Generative_Synthesis/review]] — DreamControl의 전신 제어 기법이 정밀한 추적과 생성형 합성의 실제 적용 사례를 보여줌
- 🏛 기반 연구: [[papers/1575_Mobile-TeleVision_Predictive_Motion_Priors_for_Humanoid_Whol/review]] — 상체 조작을 위한 기반 기술로서 휴머노이드의 전신 제어에서 상체 정밀 조작 부분의 이론적 토대를 제공합니다.
- 🔗 후속 연구: [[papers/1428_GraspDreamer_생성형_인간_시연_기반_기능적_파지_모방_학습/review]] — Dex1B의 대규모 시연 데이터가 GraspDreamer의 합성 영상 생성을 보완한다.
