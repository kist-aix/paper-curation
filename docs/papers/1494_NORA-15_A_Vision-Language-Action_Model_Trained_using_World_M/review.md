---
title: "1494_NORA-15_A_Vision-Language-Action_Model_Trained_using_World_M"
authors:
  - "Chia-Yu Hung"
  - "Navonil Majumder"
  - "Haoyuan Deng"
  - "Liu Renhang"
  - "Yankang Ang"
date: "2025.11"
doi: ""
arxiv: ""
score: 4.0
essence: "NORA-1.5는 flow-matching 기반 action expert를 추가하여 VLA 모델의 성능을 향상시키고, world model 및 action-based reward를 이용한 DPO 기반 post-training으로 실제 로봇 환경에서의 신뢰성과 일반화 능력을 개선한다."
tags:
  - "cat/Task-Oriented_Skill_Acquisition"
  - "sub/Foundation_Model_Agents"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Hung et al._2025_NORA-1.5 A Vision-Language-Action Model Trained using World Model- and Action-based Preference Rewa.pdf"
---

# NORA-1.5: A Vision-Language-Action Model Trained using World Model- and Action-based Preference Rewards

> **저자**: Chia-Yu Hung, Navonil Majumder, Haoyuan Deng, Liu Renhang, Yankang Ang, Amir Zadeh, Chuan Li, Dorien Herremans, Ziwei Wang, Soujanya Poria | **날짜**: 2025-11-18 | **URL**: [https://arxiv.org/abs/2511.14659](https://arxiv.org/abs/2511.14659)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1. Training pipeline of NORA-1.5 where firstly a VLA model is pre-trained through imitation learning and subseque*

NORA-1.5는 flow-matching 기반 action expert를 추가하여 VLA 모델의 성능을 향상시키고, world model 및 action-based reward를 이용한 DPO 기반 post-training으로 실제 로봇 환경에서의 신뢰성과 일반화 능력을 개선한다.

## Motivation

- **Known**: Vision-Language-Action 모델들이 embodied task에서 좋은 성능을 보이고 있으나, 서로 다른 embodiment나 실제 환경에 배포할 때 신뢰성과 일반화 능력이 부족하다는 것이 알려져 있다.
- **Gap**: 기존 VLA 모델들은 제한된 전문가 데이터에 의존하는 supervised fine-tuning에 기반하고 있어 일반화 능력이 제약되며, reward-driven post-training의 효과성과 확장성이 충분히 연구되지 않았다.
- **Why**: 더 신뢰할 수 있고 실세계에 배포 가능한 embodied agent를 개발하기 위해서는 효율적인 post-training 방법과 견고한 reward 메커니즘이 필수적이다.
- **Approach**: NORA backbone에 flow-matching 기반 action expert를 layer-wise self-attention으로 연결하고, action-conditioned world model (V-JEPA2-AC)과 deviation-from-ground-truth 휴리스틱을 결합한 reward 신호를 생성하여 DPO를 통해 post-training한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1. Training pipeline of NORA-1.5 where firstly a VLA model is pre-trained through imitation learning and subseque*

- **아키텍처 향상**: Flow-matching action expert 추가만으로도 NORA 대비 상당한 성능 향상을 달성하여, 기존 예상과 달리 flow-matching이 추론 속도뿐 아니라 정책 성능도 개선함을 입증
- **최고 성능 달성**: SimplerEnv, LIBERO 등 시뮬레이션 벤치마크와 Galaxea A1 등 실제 로봇 환경에서 state-of-the-art 결과 달성
- **효과적인 Reward 설계**: World model 기반 goal-reaching 평가와 거리 기반 휴리스틱을 결합한 경량 reward 메커니즘으로 일관된 성능 개선 달성
- **확장성 있는 Post-training 방법**: DPO 기반 preference 최적화가 추론-bound 대신 compute-bound 방식으로 대규모 데이터에 스케일하는 경로를 제시

## How

![Figure 1](figures/fig1.webp)

*Figure 1. Training pipeline of NORA-1.5 where firstly a VLA model is pre-trained through imitation learning and subseque*

- NORA 3B-parameter autoregressive VLA 모델을 기반으로 flow-matching 기반 action expert를 추가하여 layer-wise self-attention으로 결합
- V-JEPA2-AC action-conditioned world model을 이용하여 action 롤아웃의 goal 도달 가능성을 평가
- deviation-from-ground-truth 휴리스틱을 통해 world model의 예측 노이즈를 완화하고 안정적인 기준 제공
- 생성된 action 샘플들을 reward 신호로 순위 매겨 preference 데이터셋 구성
- Direct Preference Optimization (DPO)를 통해 target embodiment에 맞게 NORA-1.5 적응
- Open X-Embodiment 데이터셋에서 일반 로봇 데이터로 pre-training 후 시뮬레이션 및 실제 로봇 환경에서 평가

## Originality

- Flow-matching action expert와 autoregressive VLA의 결합을 통해 상호 이득을 입증 (VLA의 풍부한 표현을 활용하면서 동시에 trajectory-level planning 개선)
- World model과 기하학적 휴리스틱을 결합한 hybrid reward 설계로 noisy prediction 문제 해결
- Tractable likelihood가 없는 flow-matching/diffusion 기반 action head에도 적용 가능한 preference-based optimization 프레임워크 제시
- Open X-Embodiment의 다양한 embodiment 데이터를 하나의 보편적인 평가 함수로 순위 매겨 대규모 preference 데이터셋 구성 가능성 제시

## Limitation & Further Study

- Flow-matching expert가 저데이터 영역에서 VLA backbone과의 불충분한 joint training 때문에 성능 저하 가능성
- V-JEPA2-AC world model의 적응 데이터 부족으로 인한 예측 노이즈 문제 (deviation 휴리스틱으로만 부분적 완화)
- Reward 메커니즘의 정확성이 preference 데이터셋 품질에 크게 의존하여, 잘못된 순위 매김이 DPO 성능 저하 초래 가능
- 후속 연구: 더 정교한 world model 아키텍처나 ensemble 방법으로 reward 신호 정확성 개선, 저데이터 regime에서 flow-matching expert의 학습 메커니즘 강화, 다양한 embodiment에 대한 일반화 능력 분석 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: NORA-1.5는 flow-matching 기반 아키텍처 개선과 경량이면서도 효과적인 reward 기반 post-training을 결합하여 VLA 모델의 신뢰성과 실제 배포 가능성을 크게 향상시킨 의미 있는 연구이다. 광범위한 벤치마크에서의 성과와 확장 가능한 post-training 방법론은 embodied AI 분야에 실질적인 기여를 한다.

## Related Papers

- 🔄 다른 접근: [[papers/1615_VLA-0_Building_State-of-the-Art_VLAs_with_Zero_Modification/review]] — VLA 모델 구축에서 NORA-1.5의 복잡한 flow-matching 방식 대비 VLA-0의 단순한 텍스트 액션 표현 방식을 비교할 수 있다.
- 🏛 기반 연구: [[papers/1359_Diffusion_for_World_Modeling_Visual_Details_Matter_in_Atari/review]] — world model 기반 학습에서 시각적 세부사항의 중요성을 다룬 연구로 NORA-1.5의 world model 훈련 방법론에 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/1287_BeyondMimic_From_Motion_Tracking_to_Versatile_Humanoid_Contr/review]] — π_0의 vision-language-action flow model을 기반으로 NORA-1.5가 flow-matching 방식을 action expert에 적용하여 성능을 향상시켰다.
- ⚖️ 반론/비판: [[papers/1496_Octo_An_Open-Source_Generalist_Robot_Policy/review]] — NORA-1.5의 복잡한 아키텍처와 달리 Octo는 오픈소스 범용 로봇 정책으로 단순성과 접근성을 강조한다.
- 🔄 다른 접근: [[papers/1615_VLA-0_Building_State-of-the-Art_VLAs_with_Zero_Modification/review]] — VLA 모델 구축에서 VLA-0의 단순한 텍스트 액션 표현과 NORA-1.5의 복잡한 flow-matching 방식을 설계 철학과 성능 측면에서 비교할 수 있다.
