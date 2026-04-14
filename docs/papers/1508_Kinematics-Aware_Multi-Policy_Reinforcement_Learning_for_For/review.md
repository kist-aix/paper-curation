---
title: "1508_Kinematics-Aware_Multi-Policy_Reinforcement_Learning_for_For"
authors:
  - "Kaiyan Xiao"
  - "Zihan Xu"
  - "Cheng Zhe"
  - "Chengju Liu"
  - "Qijun Chen"
date: "2025.11"
doi: "10.48550/arXiv.2511.21169"
arxiv: ""
score: 4.0
essence: "본 논문은 휴머노이드 로봇이 고하중 산업 작업에서 민첩한 조작과 능동적 힘 상호작용을 동시에 수행할 수 있도록 kinematics 사전 정보를 임베딩한 heuristic reward 함수와 force 기반 curriculum learning을 활용한 3단계 RL 프레임워크를 제안한다."
tags:
  - "cat/Humanoid_Locomotion_Control_Systems"
  - "sub/Full-Body_Reinforcement_Learning"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Xiao et al._2025_Kinematics-Aware Multi-Policy Reinforcement Learning for Force-Capable Humanoid Loco-Manipulation.pdf"
---

# Kinematics-Aware Multi-Policy Reinforcement Learning for Force-Capable Humanoid Loco-Manipulation

> **저자**: Kaiyan Xiao, Zihan Xu, Cheng Zhe, Chengju Liu, Qijun Chen | **날짜**: 2025-11-26 | **DOI**: [10.48550/arXiv.2511.21169](https://doi.org/10.48550/arXiv.2511.21169)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1. System architecture of the proposed training pipeline. The diagram illustrates the integration of the upper-body*

본 논문은 휴머노이드 로봇이 고하중 산업 작업에서 민첩한 조작과 능동적 힘 상호작용을 동시에 수행할 수 있도록 kinematics 사전 정보를 임베딩한 heuristic reward 함수와 force 기반 curriculum learning을 활용한 3단계 RL 프레임워크를 제안한다.

## Motivation

- **Known**: 휴머노이드 로봇은 산업 응용에 높은 잠재력을 가지고 있으며, RL 기반 locomotion 제어는 성숙한 기술이다. 기존 loco-manipulation 방법들은 저부하 dexterous 조작에 중점을 두고 있다.
- **Gap**: 고부하 산업 시나리오에서 dexterity와 능동적 힘 상호작용의 결합 요구사항을 충족하는 방법이 부재하며, decoupled 제어에서 상하체 조정 문제가 미해결 상태이다.
- **Why**: 휴머노이드 로봇이 무거운 부품 운반, 대형 도구 조작, 카트 운송 등 고하중 산업 작업을 수행하기 위해서는 locomotion과 manipulation 능력뿐 아니라 환경과의 상호작용력을 능동적으로 제어할 수 있어야 한다.
- **Approach**: 상체(upper-body), 하체(lower-body), delta-command 세 개의 modular policy를 순차적으로 학습하는 3단계 파이프라인을 구성하고, forward kinematics 사전 정보를 heuristic reward에 임베딩하며 force curriculum learning으로 능동적 힘 제어를 학습한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Fig. 1. System architecture of the proposed training pipeline. The diagram illustrates the integration of the upper-body*

- **Kinematics-aware heuristic reward function**: Forward kinematics 사전 정보를 암묵적으로 embedding하여 상체 정책의 수렴 속도를 가속화하고 성능을 향상
- **Force-based curriculum learning**: Locomotion 습득 후 target force와 반대 방향의 외부 간섭을 적용하여 robot이 능동적으로 힘을 발휘하고 조절하도록 학습
- **Delta-command policy**: Torso 동작으로 인한 수직 end-effector 변위를 보정하여 상하체 조정 문제 해결
- **Industrial-grade performance**: Unitree G1에서 4kg 물체 운반, 112.8kg 카트 밀기/당기기 등 고부하 작업 수행 검증

## How

![Figure 1](figures/fig1.webp)

*Fig. 1. System architecture of the proposed training pipeline. The diagram illustrates the integration of the upper-body*

- 3단계 training pipeline: (1) upper-body 정책 학습 - joint-space 및 task-space tracking 포함, (2) lower-body 정책 학습 - curriculum: locomotion → force-capable, (3) delta-command 정책으로 coordination
- Heuristic reward function 설계: Joint-angle 오차와 end-effector pose 오차를 결합하여 forward kinematics 매핑을 빠르게 학습
- Force curriculum: 기본 locomotion 습득 후 target exerted force를 도입하고 동일 크기의 반대 방향 외부 간섭 적용
- Delta-command module: Torso 동작으로 인한 vertical displacement를 계산하여 보정 offset 생성
- Command space 정의: End-effector pose, locomotion velocity, target exerted force로 구성
- Simulation 및 sim-to-real transfer: Domain randomization을 활용한 실제 로봇 배포

## Originality

- Forward kinematics 사전 정보를 reward 함수에 암묵적으로 embedding하는 novel한 접근 - 기존 inverse kinematics 기반 방법의 한계를 RL로 극복
- Force-based curriculum learning으로 수동적 적응을 넘어 능동적 힘 제어 학습 - 고부하 industrial task에 최적화
- Decoupled modular control에서 delta-command를 통한 upper-lower body 조정 - 3가지 policy의 효과적 통합 방식 제안
- 고부하(112.8kg) 실제 산업 작업 검증 - 기존 저부하 loco-manipulation 연구와 구별

## Limitation & Further Study

- Real-world 데이터는 단일 로봇(Unitree G1)에 국한되어 다른 humanoid 플랫폼 일반화 가능성 미검증
- Force curriculum에서 외부 간섭의 magnitude와 적용 방식이 고정적일 수 있으며, 더 복잡한 force profile에 대한 확장성 부족
- Delta-command policy가 특정 locomotion 동작에 최적화되어 있을 가능성 - 동적 환경 변화에 대한 adaptability 분석 필요
- Sim-to-real transfer의 domain randomization 상세 방법론과 현실 환경에서의 friction, contact dynamics 등 모델링 오차 영향 분석 미흡
- 후속 연구: (1) 다중 humanoid 플랫폼 검증, (2) Online adaptation mechanism 추가, (3) 복잡한 force trajectory 학습, (4) Partial observability 환경에서의 robust 성능

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 고부하 산업 loco-manipulation을 위한 체계적인 RL 프레임워크를 제시하며, kinematics 사전 정보와 force curriculum learning이라는 technical contribution을 통해 실제 고부하 작업(112.8kg 카트 조작)을 달성한 점에서 높은 가치를 지닌다. 다만 단일 로봇 플랫폼 검증과 force curriculum의 일반화 가능성 확보가 향후 과제이다.

## Related Papers

- 🔗 후속 연구: [[papers/1435_HAFO_A_Force-Adaptive_Control_Framework_for_Humanoid_Robots/review]] — 산업용 고하중 작업의 kinematics-aware RL은 HAFO의 강한 외력 상호작용 제어에서 발전한다.
- 🔄 다른 접근: [[papers/1558_Load-Aware_Locomotion_Control_for_Humanoid_Robots_in_Industr/review]] — 두 논문 모두 산업 환경에서의 load-aware control을 다루지만, 하나는 force-capable manipulation에, 다른 하나는 locomotion에 초점을 둔다.
- 🏛 기반 연구: [[papers/1392_FALCON_Learning_Force-Adaptive_Humanoid_Loco-Manipulation/review]] — Kinematics-aware multi-policy RL은 FALCON의 force-adaptive control 개념을 산업 환경으로 확장한다.
- 🏛 기반 연구: [[papers/1435_HAFO_A_Force-Adaptive_Control_Framework_for_Humanoid_Robots/review]] — HAFO의 force-capable manipulation은 산업용 고하중 작업을 위한 kinematics-aware 정책 학습의 기반이 된다.
- 🏛 기반 연구: [[papers/1329_CityNavAgent_Aerial_Vision-and-Language_Navigation_with_Hier/review]] — Openfly는 CityNavAgent의 aerial VLN을 위한 종합적인 공중 시각-언어 플랫폼 기반을 제공한다
