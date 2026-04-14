---
title: "1581_Structured_World_Models_from_Human_Videos"
authors:
  - "Russell Mendonca"
  - "Shikhar Bahl"
  - "Deepak Pathak"
date: "2023.08"
doi: ""
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 인간 비디오 데이터로 사전학습한 구조화된 world model을 로봇의 조작 작업에 미세조정하여, 30분 이내의 실제 상호작용으로 복잡한 조작 기술을 학습할 수 있는 SWIM 프레임워크를 제안한다."
tags:
  - "cat/Multimodal_Vision-Language_Policy_Learning"
  - "sub/Large-scale_Egocentric_Datasets"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Mendonca et al._2023_Structured World Models from Human Videos.pdf"
---

# Structured World Models from Human Videos

> **저자**: Russell Mendonca, Shikhar Bahl, Deepak Pathak | **날짜**: 2023-08-21 | **URL**: [https://arxiv.org/abs/2308.10901](https://arxiv.org/abs/2308.10901)

---

## Essence

![Figure 2](figures/fig2.webp)

*Fig. 2: Overview of SWIM. We first pre-train the world model on a large set of human videos. We finetune this on many ro*

본 논문은 대규모 인간 비디오 데이터로 사전학습한 구조화된 world model을 로봇의 조작 작업에 미세조정하여, 30분 이내의 실제 상호작용으로 복잡한 조작 기술을 학습할 수 있는 SWIM 프레임워크를 제안한다.

## Motivation

- **Known**: World model을 이용한 로봇 학습은 샘플 효율성을 높일 수 있으나, 실제 로봇 데이터 수집이 비용이 크고 시간이 많이 걸린다는 제약이 있다. 컴퓨터 비전과 NLP에서 대규모 데이터 활용의 성공 사례가 있다.
- **Gap**: 기존 world model은 저수준 조인트 공간에서 작동하여 로봇 형태학적 차이로 인해 인간 비디오에서 직접 학습하기 어렵다. 형태학적으로 불변인 고수준 행동 공간으로 대규모 인간 비디오 데이터를 활용하는 방법이 부족하다.
- **Why**: 일반적인 조작 로봇을 만들기 위해서는 다양한 작업에서 학습할 수 있는 효율적인 방법이 필요하며, 인터넷 규모의 인간 비디오를 활용하면 로봇 데이터 수집 비용을 크게 줄일 수 있다.
- **Approach**: 시각적 어포던스(grasp location, post-grasp waypoints)에 기반한 구조화된 고수준 행동 공간을 정의하여 인간과 로봇 모두에 적용 가능하게 한다. 대규모 인간 비디오로 world model을 사전학습한 후, 보상 감독 없이 소량의 로봇 상호작용 데이터로 미세조정하고 목표 이미지 기반 계획을 수행한다.

## Achievement

![Figure 4](figures/fig4.webp)

*Fig. 4: We evaluate SWIM on six different real-world manipulation tasks on two different robot systems (shown on the lef*

- **샘플 효율성**: 30분 이내의 실제 상호작용만으로 다양한 조작 작업을 학습 가능
- **일반화 성능**: 이전 방법 대비 약 2배 높은 성공률을 달성하면서 여러 환경과 로봇 시스템(Franka Arm, Hello Stretch)에서 검증
- **무감독 학습**: 작업 감독 없이 다양한 작업의 데이터를 단일 world model로 통합 학습 가능
- **확장성**: 인간 비디오 데이터가 증가함에 따라 성능이 지속적으로 향상

## How

![Figure 3](figures/fig3.webp)

*Fig. 3: World Model Training: Images and actions are encoded into*

- **사전학습 단계**: Epic-Kitchens 등 대규모 인간 비디오 데이터셋에서 visual affordance detector와 world model을 학습
- **행동 공간 설계**: 형태학적으로 불변인 구조화된 행동 공간(grasp location + post-grasp waypoints)으로 인간-로봇 간 행동 매핑
- **Dreamer 기반 구조**: Encoder, posterior, dynamics, decoder로 구성된 world model 아키텍처 사용
- **미세조정**: 보상 신호 없이 로봇이 수행한 어포던스 행동 데이터로 dynamics model만 적응
- **계획 및 배포**: 학습된 world model에서 목표 이미지 기반 계획을 수행하여 조작 태스크 실행

## Originality

- 형태학적으로 불변인 고수준 구조화 행동 공간을 정의하여 인간 비디오를 로봇 학습에 직접 활용하는 점이 참신함
- 사전학습 및 미세조정 모두에서 작업 감독을 제거하여 다양한 작업 데이터의 통합 학습을 가능하게 한 점
- 대규모 인터넷 비디오 데이터를 실제 로봇 조작 학습에 성공적으로 연결한 첫 실증 연구

## Limitation & Further Study

- 인간 손과 로봇 그리퍼의 상호작용이 충분히 유사하지 않을 수 있는 복잡한 조작 작업에서의 성능 제한
- 시각적 어포던스 기반 행동 공간이 비조작 기술(pushing, rotating 등)에 최적화되지 않을 가능성
- 다양한 카메라 각도와 조명 조건의 인간 비디오에서 학습한 모델의 도메인 적응 성능 평가 부족
- 후속 연구: 더 다양한 형태의 조작 작업과 로봇 형태학에 대한 적응, 언어 조건부 계획 통합, 실시간 재계획 메커니즘

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 형태학적으로 불변인 구조화 행동 공간이라는 창의적인 아이디어로 대규모 인간 비디오 데이터를 실제 로봇 학습에 성공적으로 연결하였으며, 광범위한 실험을 통해 샘플 효율성과 일반화 성능을 모두 입증하여 로봇 조작 학습 분야에 의미 있는 기여를 하였다.

## Related Papers

- 🔄 다른 접근: [[papers/1565_Scaling_Robot_Learning_with_Semantically_Imagined_Experience/review]] — 대규모 인간 비디오에서 로봇 학습의 다른 접근법으로 world model과 데이터 증강을 비교할 수 있다.
- 🏛 기반 연구: [[papers/1602_Unleashing_Large-Scale_Video_Generative_Pre-training_for_Vis/review]] — 비디오 생성 사전학습을 활용한 로봇 학습의 기반 아이디어를 구조화된 world model로 발전시킨다.
- 🔗 후속 연구: [[papers/1632_World_Simulation_with_Video_Foundation_Models_for_Physical_A/review]] — 비디오 기반 world model을 물리적 AI를 위한 세계 시뮬레이션으로 확장한다.
- 🔗 후속 연구: [[papers/1355_DreamDojo_A_Generalist_Robot_World_Model_from_Large-Scale_Hu/review]] — Human video로부터 structured world model을 학습하는 방법론을 robot manipulation에 특화된 world model로 확장한다.
- 🔄 다른 접근: [[papers/1565_Scaling_Robot_Learning_with_Semantically_Imagined_Experience/review]] — 대규모 인간 비디오 데이터를 로봇 학습에 활용하는 다른 접근법으로 데이터 증강과 사전학습을 비교할 수 있다.
- 🔗 후속 연구: [[papers/1602_Unleashing_Large-Scale_Video_Generative_Pre-training_for_Vis/review]] — 구조화된 world model을 대규모 비디오 생성 사전학습으로 발전시켜 멀티태스크 로봇 조작을 가능하게 한다.
- 🔗 후속 연구: [[papers/1291_3D-VLA_A_3D_Vision-Language-Action_Generative_World_Model/review]] — Structured World Models의 인간 비디오 기반 구조화된 월드 모델이 3D-VLA의 3D 월드 모델링을 더 체계적으로 발전시킬 수 있다.
- 🏛 기반 연구: [[papers/1316_Behavior_Transformers_Cloning_k_modes_with_one_stone/review]] — Multi-task Deep RL with PopArt의 multi-task 학습 방법론이 BeT의 k개 mode cloning에서 task 간 균형을 위한 기반을 제공한다.
