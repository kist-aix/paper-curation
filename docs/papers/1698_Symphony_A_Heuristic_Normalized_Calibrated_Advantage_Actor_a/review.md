---
title: "1698_Symphony_A_Heuristic_Normalized_Calibrated_Advantage_Actor_a"
authors:
  - "Timur Ishuov"
  - "Michele Folgheraiter"
  - "Madi Nurmanov"
  - "Goncalo Gordo"
  - "Richárd Farkas"
date: "2025.12"
doi: ""
arxiv: ""
score: 3.0
essence: "Symphony는 휴머노이드 로봇을 안전하게 훈련하기 위해 Swaddling 정규화, Fading Replay Buffer, Temporal Advantage를 결합한 결정론적 Actor-Critic 알고리즘이다. 제한된 parametric noise와 action strength 조절을 통해 sample efficiency, safety, smooth motion을 동시에 달성한다."
tags:
  - "cat/Other"
  - "topic/humanoid"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ishuov et al._2025_Symphony A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for.pdf"
---

# Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots

> **저자**: Timur Ishuov, Michele Folgheraiter, Madi Nurmanov, Goncalo Gordo, Richárd Farkas, József Dombi | **날짜**: 2025-12-11 | **URL**: [https://arxiv.org/abs/2512.10477](https://arxiv.org/abs/2512.10477)

---

## Essence

![Figure 4](figures/fig4.webp)

*Fig. 4: Swaddling Regularization with β as temperature.*

Symphony는 휴머노이드 로봇을 안전하게 훈련하기 위해 Swaddling 정규화, Fading Replay Buffer, Temporal Advantage를 결합한 결정론적 Actor-Critic 알고리즘이다. 제한된 parametric noise와 action strength 조절을 통해 sample efficiency, safety, smooth motion을 동시에 달성한다.

## Motivation

- **Known**: SAC, PPO, RedQ 등 기존 off-policy/on-policy 알고리즘들은 sample efficiency 또는 안전성 중 하나에 최적화되어 있으며, 실제 휴머노이드 로봇 훈련에서는 motor/gearbox 손상 위험이 있다.
- **Gap**: 실제 로봇 훈련에서 높은 sample efficiency를 유지하면서도 jerky movement를 방지하고 mechanism safety를 보장하는 통합적인 알고리즘이 부족하다.
- **Why**: 휴머노이드 로봇은 실제 환경에서 수십만 스텝을 기다릴 수 없고, 부적절한 제어는 기계 장치에 직접적인 손상을 입힐 수 있어 안전성이 중요하다.
- **Approach**: 제한된 Gaussian noise (σ=1/e)와 action strength penalty를 통해 exploration을 제어하고, Fading Replay Buffer로 recent와 long-term memory를 균형있게 활용하며, Temporal Advantage를 통해 Actor-Critic 동시 업데이트를 수행한다.

## Achievement

![Figure 4](figures/fig4.webp)

*Fig. 4: Swaddling Regularization with β as temperature.*

- **Sample Efficiency**: Update-to-Data ratio 3으로 높은 sample efficiency 달성
- **Safety**: Continuous noise 대신 제한된 parametric noise와 action strength 조절로 mechanical safety 보장
- **Smooth Motion**: Temporal Advantage와 exponential weighted moving average로 jerky movement 제거
- **Computational Efficiency**: Actor와 Critic을 단일 Object로 통합하여 한 줄의 Loss로 구현
- **Hardware-Aware Design**: Motor/gearbox 손상을 고려한 heuristic 설계

## How

![Figure 1](figures/fig1.webp)

*Fig. 1: a) x*tanh(x/2) - Rectified Huber Symmetric Error, b)*

- 3개의 Critic network (각 128 nodes)를 연결하여 384-node distribution 생성
- Target Critic 출력에 hyperbolic tangent 기반 fixed weights 적용 (Table I)
- Fading Replay Buffer: tanh((πi)e) 함수로 recent experience에 높은 priority 할당 (Table II)
- Temporal Advantage QT = αQ̄T-1 + (1-α)Q*target로 정규화된 advantage 계산
- 정규화된 보상 r̂과 Rectified Huber Symmetric Error loss 함수 사용
- Swaddling 정규화: control cost penalty로 action strength 제약
- N_exp=10,240 exploration 스텝에서 수집한 보상으로 normalization factor 계산

## Originality

- Swaddling regularization: 인간 발달 metaphor를 기반으로 한 novel restraint mechanism
- Fading Replay Buffer: tanh 기반 smooth priority scheduling으로 기존 prioritized replay buffer와 차별화
- Temporal Advantage: exponential moving average를 활용한 새로운 advantage 정규화 방식
- Fixed weight distribution (Table I): sorted Q-distribution에 역함수 가중치 적용하는 heuristic 설계
- 통합 Actor-Critic Object: 두 네트워크의 동시 업데이트를 구조적으로 간소화

## Limitation & Further Study

- Heuristic 접근법으로 인한 이론적 정당성 부족 (α=0.5~0.7, β 선택 근거 불명확)
- 실제 휴머노이드 로봇(예: Boston Dynamics, Tesla)에 대한 실험 결과 미제시
- Simulation 환경에서의 성능 비교 실험 부재 (SAC, PPO, RedQ와의 정량적 비교 없음)
- 384-node distribution과 3-Critic 구조의 선택 이유가 경험적이고 일반화 가능성 미흡
- Update-to-Data ratio 3의 최적성 검증 부족
- 후속연구: 다양한 실제 로봇 플랫폼에서의 검증, 이론적 convergence 분석, hyperparameter 자동 조정 메커니즘

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 3/5
- Overall: 3/5

**총평**: Symphony는 실제 휴머노이드 로봇 훈련의 실질적 문제들(safety, efficiency, smoothness)을 종합적으로 해결하는 창의적인 heuristic 알고리즘이다. 그러나 이론적 기초와 실증적 검증이 부족하여 학술적 엄밀성과 재현성 면에서 개선이 필요하다.