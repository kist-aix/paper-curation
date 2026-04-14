---
title: "1401_Flow_Matching_Imitation_Learning_for_Multi-Support_Manipulat"
authors:
  - "Quentin Rouxel"
  - "Andrea Ferrari"
  - "Serena Ivaldi"
  - "Jean-Baptiste Mouret"
date: "2024.07"
doi: ""
arxiv: ""
score: 4.0
essence: "본 논문은 Flow Matching을 활용한 모방 학습으로 휴머노이드 로봇의 다중 접촉(multi-support) 조작 작업을 수행하는 통합 접근법을 제시하며, 실제 Talos 로봇에서 상자 밀기 및 식기세척기 닫기 작업을 시연한다."
tags:
  - "cat/Humanoid_Teleoperation_and_Interaction"
  - "sub/Force-Feedback_Teleoperation"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Rouxel et al._2024_Flow Matching Imitation Learning for Multi-Support Manipulation.pdf"
---

# Flow Matching Imitation Learning for Multi-Support Manipulation

> **저자**: Quentin Rouxel, Andrea Ferrari, Serena Ivaldi, Jean-Baptiste Mouret | **날짜**: 2024-07-17 | **URL**: [https://arxiv.org/abs/2407.12381](https://arxiv.org/abs/2407.12381)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1.*

본 논문은 Flow Matching을 활용한 모방 학습으로 휴머노이드 로봇의 다중 접촉(multi-support) 조작 작업을 수행하는 통합 접근법을 제시하며, 실제 Talos 로봇에서 상자 밀기 및 식기세척기 닫기 작업을 시연한다.

## Motivation

- **Known**: 휴머노이드 로봇의 전신 제어와 다중 접촉 작업에 대한 모델 기반 최적화 접근법이 존재하며, Diffusion 기반 모방 학습이 고차원 궤적 생성에 활용되고 있다.
- **Gap**: 다중 접촉 및 접촉 전환 시나리오에서의 전신 모방 학습이 미흡하며, Diffusion 대비 Flow Matching의 로봇 응용 우수성이 실제 휴머노이드에서 검증되지 않았다.
- **Why**: 휴머노이드 로봇이 팔을 추가 지지점으로 활용하면 작업 공간과 안정성이 향상되며, 접촉 선택의 다중양식성(multi-modality) 처리가 중요하다.
- **Approach**: 최적화 기반 다중접촉 전신 제어기와 Flow Matching을 결합하여 모방 학습 정책을 학습하고, 자율 실행 및 공유 자율성(shared autonomy) 모드를 지원한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1.*

- **Flow Matching의 로봇 우월성 증명**: 시뮬레이션에서 Flow Matching이 Diffusion과 전통적 행동 복제보다 로봇 응용에 적합함을 보여주었고, 더 빠른 추론 속도를 제공한다.
- **실제 휴머노이드 로봇 시연**: Talos 로봇에서 상자 밀기 및 식기세척기 닫기 작업을 학습 및 실행하여 다중 접촉 조작의 실용성을 입증했다.
- **공유 자율성 모드 개발**: 시연 범위 밖의 작업에서 자동 접촉 배치를 제공하여 인간 조작자를 지원하는 보조 원격 조종 기능을 구현했다.

## How

![Figure 2](figures/fig2.webp)

*Figure 2.*

- Flow Matching을 사용하여 시연으로부터 다중양식 궤적 분포를 학습하는 생성 모델 훈련
- 최적화 기반 다중접촉 전신 제어기(SEIKO)와 Flow Matching 정책을 통합하는 계층적 제어 구조 설계
- RGB-D 카메라와 마커 기반 자세 추정을 통한 고차원 상태 입력 처리
- 자율, 원격 조종, 공유 자율성 등 세 가지 운영 모드 지원
- 접촉 형성 시점과 위치를 학습된 정책으로 자동 결정

## Originality

- 다중 접촉 시나리오에서 Flow Matching을 적용한 첫 휴머노이드 로봇 연구
- Diffusion 대비 Flow Matching의 로봇 응용 우수성(빠른 추론, 수치 안정성)을 실제 하드웨어에서 검증
- 공유 자율성 모드에서 자동 접촉 배치를 제공하는 새로운 보조 방식 제안
- 전신 다중 접촉 제어와 생성 모델 기반 모방 학습의 통합

## Limitation & Further Study

- 시연 데이터 수집 및 레이블링 비용이 높으며, 환경 변화(예: 표면 재질, 마찰)에 대한 일반화 성능이 미검증
- Flow Matching의 초매개변수 선택과 학습 안정성에 대한 상세 분석 부재
- 실험이 Talos 단일 로봇에 국한되어 다른 휴머노이드 플랫폼으로의 전이 가능성 불명확
- 접촉 접촉 동역학(예: 미끄러짐, 마찰)을 명시적으로 모델링하지 않아 실패 사례의 분석이 제한적
- 후속 연구: 시뮬-투-실(sim-to-real) 전이 학습, 강화 학습 결합, 더 복잡한 비파지 조작 작업 확장

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 Flow Matching의 로봇 응용 우월성을 실제 휴머노이드에서 처음 입증하고, 다중 접촉 조작이라는 실용적 문제를 해결하는 통합 솔루션을 제시하여 로봇 모방 학습의 중요한 진전을 이룬다.

## Related Papers

- 🏛 기반 연구: [[papers/1354_DreamControl_Human-Inspired_Whole-Body_Humanoid_Control_for/review]] — Flow Matching을 활용한 multi-support manipulation 학습에서 자연스러운 동작 생성을 위해서는 DreamControl의 human motion prior가 중요한 기반 기술입니다.
- 🧪 응용 사례: [[papers/1436_HAIC_Humanoid_Agile_Object_Interaction_Control_via_Dynamics-/review]] — Flow Matching 기반 모방 학습 방법론은 HAIC의 동역학 인식 world model과 결합하여 미구동 물체와의 상호작용에서 더욱 안정적인 제어를 달성할 수 있습니다.
- 🔗 후속 연구: [[papers/1354_DreamControl_Human-Inspired_Whole-Body_Humanoid_Control_for/review]] — DreamControl의 human motion data 기반 diffusion prior는 Flow Matching 기반 multi-support manipulation의 자연스러운 동작 생성을 향상시킬 수 있습니다.
- 🔗 후속 연구: [[papers/1436_HAIC_Humanoid_Agile_Object_Interaction_Control_via_Dynamics-/review]] — HAIC의 동역학 인식 world model과 고차 동역학 예측 기술은 Flow Matching 기반 multi-support manipulation에서 물체 상호작용의 정확성을 크게 향상시킬 수 있습니다.
