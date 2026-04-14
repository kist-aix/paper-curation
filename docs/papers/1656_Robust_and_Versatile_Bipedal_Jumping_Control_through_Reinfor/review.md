---
title: "1656_Robust_and_Versatile_Bipedal_Jumping_Control_through_Reinfor"
authors:
  - "Zhongyu Li"
  - "Xue Bin Peng"
  - "Pieter Abbeel"
  - "Sergey Levine"
  - "Glen Berseth"
date: "2023.02"
doi: ""
arxiv: ""
score: 4.0
essence: "Reinforcement learning과 새로운 정책 구조를 활용하여 이족 로봇 Cassie가 다양한 착지 위치와 방향으로 점프하는 강건하고 다목적인 동적 점프 제어를 실현했다."
tags:
  - "cat/Other"
  - "topic/humanoid"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Li et al._2023_Robust and Versatile Bipedal Jumping Control through Reinforcement Learning.pdf"
---

# Robust and Versatile Bipedal Jumping Control through Reinforcement Learning

> **저자**: Zhongyu Li, Xue Bin Peng, Pieter Abbeel, Sergey Levine, Glen Berseth, Koushil Sreenath | **날짜**: 2023-02-19 | **URL**: [https://arxiv.org/abs/2302.09450](https://arxiv.org/abs/2302.09450)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1: Representative dynamic jumping maneuvers performed by a bipedal robot Cassie using the proposed goal-conditioned*

Reinforcement learning과 새로운 정책 구조를 활용하여 이족 로봇 Cassie가 다양한 착지 위치와 방향으로 점프하는 강건하고 다목적인 동적 점프 제어를 실현했다.

## Motivation

- **Known**: 모델 기반 최적 제어는 접촉 수열이 사전에 정의되어야 하며 단일 고정 홉만 가능하고, 최근 RL 기반 방법은 사족 로봇에서는 성공했으나 이족 로봇의 동적 점프에서는 주기적 호핑 수준에 그쳤다.
- **Gap**: 이족 로봇이 다양한 목표 위치와 방향으로 강건하게 점프하고 착지하는 능력을 갖추기 위한 실제 세계 검증된 방법이 부재했다.
- **Why**: 이족 로봇의 민첩성 향상은 비정형 환경에서의 이동성을 크게 높일 수 있으며, 복잡한 접촉 역학과 언더액추에이션을 극복하는 것은 로봇 제어 분야의 중요한 도전 과제이다.
- **Approach**: 다단계 훈련 스킴과 장기 I/O 이력을 인코딩하는 새로운 정책 구조를 가진 goal-conditioned RL 프레임워크를 개발하여 시뮬레이션에서 훈련하고 실제 하드웨어로 전달했다.

## Achievement

![Figure 1](figures/fig1.webp)

*Fig. 1: Representative dynamic jumping maneuvers performed by a bipedal robot Cassie using the proposed goal-conditioned*

- **다목적 점프 제어**: 1.4m의 수평 점프, 0.44m 높이의 플랫폼으로의 점프, ±55° 방향 회전 점프 등 다양한 점프 작업을 성공적으로 수행
- **강건성 입증**: 다양한 점프 작업으로부터 학습한 기동을 활용하여 외부 교란이나 착지 실패로부터 복구 가능
- **시뮬레이션-실제 이전**: 추가 튜닝 없이 시뮬레이션에서 학습한 정책이 실제 Cassie 로봇에 직접 전달 가능함을 입증
- **선행 연구 대비 우월성**: 기존 최적 제어 방법 대비 더 긴 점프 거리(1.4m vs ~0.5m), 더 긴 비행 시간(0.58s vs ~0.42s), 제어된 착지 높이 달성

## How

![Figure 2](figures/fig2.webp)

*Fig. 2: The schematic to train the robot to perform versatile jumping*

- **정책 구조 설계**: 장기 I/O 이력을 인코딩하는 RNN과 단기 I/O 이력에 직접 접근하는 구조를 결합하여 성능 개선
- **다단계 훈련**: 서로 다른 목표를 위한 여러 훈련 단계를 포함하는 다단계 훈련 스킴 적용
- **도메인 랜더마이제이션**: 시뮬레이션-실제 간극 극복을 위해 시뮬레이션 환경의 다양성 확대
- **Goal-conditioned 학습**: 목표 위치와 방향을 조건으로 하는 정책을 학습하여 다양한 점프 작업을 단일 정책으로 처리
- **접촉 수열 자동 생성**: 사전 정의 없이 점프 목표에 따라 자동으로 적절한 접촉 수열 생성

## Originality

- 첫 번째로 이족 로봇이 제어된 착지 위치를 가진 다목적 점프를 실제 세계에서 수행하도록 한 시스템 개발
- 장기와 단기 I/O 이력을 모두 인코딩하는 새로운 정책 구조 제안으로 기존 아키텍처 대비 성능 향상 입증
- 다양한 점프 작업으로부터의 학습이 로봇의 강건성을 향상시킨다는 가설 제시 및 검증
- RL을 통해 접촉 수열을 명시적으로 사전 정의하지 않고 자동으로 생성하는 접근법

## Limitation & Further Study

- 훈련 시간과 계산 비용에 대한 구체적인 정량화가 부재
- 다양한 로봇 플랫폼(Cassie 외 다른 이족 로봇)으로의 일반화 검증 미흡
- 실제 세계에서의 환경 변수(지표면 특성, 날씨 등)에 대한 강건성 평가 부족
- 향후 연구: 더 많은 이족 로봇 플랫폼에 대한 검증, 온라인 학습 능력 추가, 3차원 복잡한 환경에서의 적용

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이족 로봇의 동적 점프 제어에서 RL과 새로운 정책 구조를 결합하여 기존 방법을 크게 뛰어넘는 실제 세계 성과를 달성한 우수한 연구이며, 다목적 강건한 로봇 제어의 새로운 가능성을 보여준다.