---
title: "1567_Mechanical_Intelligence-Aware_Curriculum_Reinforcement_Learn"
authors:
  - "Yusuke Tanaka"
  - "Alvin Zhu"
  - "Quanyou Wang"
  - "Yeting Liu"
  - "Dennis Hong"
date: "2025.06"
doi: ""
arxiv: ""
score: 4.0
essence: "병렬 구동 메커니즘을 가진 휴머노이드 로봇의 폐곡선 운동학을 GPU 가속 MuJoCo (MJX)에서 네이티브로 시뮬레이션하고, curriculum RL을 통해 기계적 지능을 활용한 보행 정책을 학습한다."
tags:
  - "cat/Humanoid_Locomotion_Control_Systems"
  - "sub/Multi-Modal_Humanoid_Control"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Tanaka et al._2025_Mechanical Intelligence-Aware Curriculum Reinforcement Learning for Humanoids with Parallel Actuatio.pdf"
---

# Mechanical Intelligence-Aware Curriculum Reinforcement Learning for Humanoids with Parallel Actuation

> **저자**: Yusuke Tanaka, Alvin Zhu, Quanyou Wang, Yeting Liu, Dennis Hong | **날짜**: 2025-06-30 | **URL**: [https://arxiv.org/abs/2507.00273](https://arxiv.org/abs/2507.00273)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1: BRUCE [2] hardware with three distinct parallel mechanisms, which*

병렬 구동 메커니즘을 가진 휴머노이드 로봇의 폐곡선 운동학을 GPU 가속 MuJoCo (MJX)에서 네이티브로 시뮬레이션하고, curriculum RL을 통해 기계적 지능을 활용한 보행 정책을 학습한다.

## Motivation

- **Known**: RL은 휴머노이드 로봇 보행에서 성과를 보였으나, 대부분의 프레임워크는 폐곡선 운동학 지원 부족으로 병렬 메커니즘의 기계적 이점을 활용하지 못한다. 기존 접근은 병렬 링크를 직렬 근사로 단순화하여 부최적 정책과 부정확한 모션 모델링을 초래한다.
- **Gap**: 시뮬레이터의 폐곡선 운동학 지원 제한으로 인해 differential pulley, four-bar linkage, five-bar linkage 등 병렬 메커니즘의 비선형 특성이 훈련 중 보존되지 않고 있다. 이는 복잡한 구동 시스템을 가진 로봇에서 특히 심각하다.
- **Why**: 병렬 메커니즘은 높은 복합 모터 출력, 감소된 관성, 높은 전달 비율의 이점을 제공하며, 상용 휴머노이드(Unitree H1, Fourier GR1, Optimus)에서 널리 사용되고 있다. 시뮬레이션에서 이 이점을 충분히 활용하면 정책 성능과 실세계 일반화를 향상시킬 수 있다.
- **Approach**: 세 가지 병렬 메커니즘(differential pulley, five-bar linkage, four-bar linkage)의 폐곡선 제약을 soft equality constraints로 formulate하고, GPU 가속 MJX에서 네이티브 시뮬레이션을 수행한다. Curriculum RL을 통해 BRUCE 휴머노이드 로봇에 end-to-end 보행 정책을 학습하고 MPC와 비교한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2: Generic topology definitions of the BRUCE’s parallel mechanisms.*

- **폐곡선 운동학 시뮬레이션**: Differential pulley, five-bar linkage, four-bar linkage의 정확한 수학적 formulation을 제시하고 MJX에서 구현하여 구동기-출력 매핑과 특이점을 명시적으로 표현
- **end-to-end 정책 학습**: Curriculum RL을 통해 폐곡선 메커니즘이 완전히 시뮬레이션된 상태에서 직접 학습하여 forward/inverse kinematics 필요성 제거
- **하드웨어 검증**: 학습된 정책을 BRUCE 하드웨어에 zero-shot 배포하여 기계적 지능 활용의 실질적 이점 입증
- **MPC 대비 성능**: 학습된 정책이 표면 일반화 및 실세계 zero-shot 배포 성능에서 MPC를 상회함을 실증

## How

![Figure 3](figures/fig3.webp)

*Fig. 3: Close-up of BRUCE’s cable-driven differential pulley.*

- **Differential pulley formulation**: 케이블 구동 differential pulley의 roll/pitch 관절 속도와 구동기 속도 간의 비선형 관계를 식 (1)로 표현 (ρL, ρR 기어 비 기반)
- **Five-bar linkage constraint**: 두 직렬 체인의 끝점 C, D가 일치하도록 제약하는 폐곡선 형성 (식 2-4), 5개의 가능한 운동학적 해 중 타당하고 원하는 configuration 선택
- **Four-bar linkage modeling**: 단일 구동기, 단일 출력 DoF로 비선형 전달 비율을 다항식으로 근사
- **GPU 가속 MJX 시뮬레이션**: Soft equality constraints를 사용하여 폐곡선 제약을 MJX에 구현하고 병렬 처리로 가속
- **Curriculum learning framework**: 간단한 부작업에서 복잡한 보행 작업으로 점진적으로 구조화된 훈련
- **Sim-to-real transfer**: Domain randomization, dynamics perturbation 적용하여 zero-shot 배포 가능성 확보
- **정책 평가**: MPC 컨트롤러와 성능 및 표면 일반화 비교

## Originality

- 폐곡선 운동학을 네이티브로 지원하지 않는 기존 시뮬레이터 한계를 극복하기 위해 MJX에서 soft equality constraints 기반 구현 제시
- Differential pulley, four-bar, five-bar linkage 세 가지 서로 다른 병렬 메커니즘을 통합적으로 formulate하고 단일 플랫폼에서 시뮬레이션한 최초 사례
- 병렬 메커니즘의 특이점(singularity)을 명시적으로 표현하여 실제 하드웨어의 비선형 특성을 훈련 단계부터 반영
- 구동기 공간에서 직접 end-to-end 정책 학습으로 forward/inverse kinematics 제거 및 기계적 이점의 직접 활용

## Limitation & Further Study

- **다중 해 처리**: Five-bar linkage의 5개 운동학적 해 중 선택 문제는 simulation sanity check에만 의존하며, 자동 선택 메커니즘이 부족
- **확장성**: 현재 formulation은 BRUCE의 특정 병렬 메커니즘에 최적화되어 있어 다른 로봇 플랫폼으로의 일반화 가능성이 제한적
- **실시간 계산**: Soft equality constraints 사용으로 수렴 속도와 정밀도 간의 trade-off 존재, 매개변수 튜닝 필요성
- **후속 연구**: (1) 자동 configuration selection 알고리즘 개발, (2) 다양한 병렬 메커니즘 형태에 대한 일반화된 제약 공식화, (3) 실시간 임베디드 배포를 위한 경량화 방법 탐색

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 병렬 메커니즘의 폐곡선 운동학을 GPU 가속 시뮬레이션에서 정확히 모델링하고 RL을 통해 학습한 정책을 실제 하드웨어에 성공적으로 배포한 우수한 연구이다. 상용 휴머노이드 로봇의 병렬 구동 메커니즘을 완전히 활용하는 새로운 방법론을 제시하며, sim-to-real 전이와 기계적 지능의 실질적 이점을 입증했다는 점에서 로봇 제어 분야에 상당한 기여를 한다.

## Related Papers

- 🏛 기반 연구: [[papers/1318_Being-H05_Scaling_Human-Centric_Robot_Learning_for_Cross-Emb/review]] — 병렬 구동 메커니즘의 제어를 위한 미분 기하학적 접근법이 폐곡선 운동학 시뮬레이션의 이론적 배경을 제공함
- 🔗 후속 연구: [[papers/1414_General_Humanoid_Whole-Body_Control_via_Pretraining_and_Fast/review]] — 일반적인 전신 제어 사전학습 개념을 병렬 구동 메커니즘이라는 특수한 하드웨어 구조에 맞춰 curriculum RL로 발전시킨 형태임
- 🏛 기반 연구: [[papers/1484_HumanPlus_Humanoid_Shadowing_and_Imitation_from_Humans/review]] — MuJoCo Playground의 GPU 가속 시뮬레이션 환경이 MJX 기반 폐곡선 운동학 시뮬레이션의 기술적 토대를 제공함
- 🔗 후속 연구: [[papers/1363_ECO_Energy-Constrained_Optimization_with_Reinforcement_Learn/review]] — Mechanical Intelligence-Aware Curriculum과 ECO의 에너지 제약을 결합하면 하드웨어 특성을 고려한 효율적 학습이 가능하다.
- 🏛 기반 연구: [[papers/1385_Evolutionary_Continuous_Adaptive_RL-Powered_Co-Design_for_Hu/review]] — Mechanical Intelligence-Aware Curriculum의 하드웨어 특성 고려 학습이 EA-CoRL의 공동 설계 최적화에 필수적인 이론적 기반을 제공한다.
