---
title: "1400_GAIA-1_A_Generative_World_Model_for_Autonomous_Driving"
authors:
  - "Anthony Hu"
  - "Lloyd Russell"
  - "Hudson Yeo"
  - "Zak Murez"
  - "George Fedoseev"
date: "2023.09"
doi: ""
arxiv: ""
score: 4.0
essence: "GAIA-1은 비디오, 텍스트, 액션 입력을 활용하여 현실적인 운전 시나리오를 생성하는 생성형 월드 모델로, 자율주행 시스템의 미래 예측 및 훈련을 향상시킨다."
tags:
  - "cat/Task-Oriented_Skill_Acquisition"
  - "sub/Language-Guided_Motion_Generation"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Hu et al._2023_GAIA-1 A Generative World Model for Autonomous Driving.pdf"
---

# GAIA-1: A Generative World Model for Autonomous Driving

> **저자**: Anthony Hu, Lloyd Russell, Hudson Yeo, Zak Murez, George Fedoseev, Alex Kendall, Jamie Shotton, Gianluca Corrado | **날짜**: 2023-09-29 | **URL**: [https://arxiv.org/abs/2309.17080](https://arxiv.org/abs/2309.17080)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: Architecture of GAIA-1. First, we encode information from all input modalities (video, text,*

GAIA-1은 비디오, 텍스트, 액션 입력을 활용하여 현실적인 운전 시나리오를 생성하는 생성형 월드 모델로, 자율주행 시스템의 미래 예측 및 훈련을 향상시킨다.

## Motivation

- **Known**: 기존 월드 모델은 레이블된 데이터에 의존하고 저차원 표현으로 인해 고충실도 샘플 생성에 어려움이 있으며, 생성형 비디오 모델은 시각적 리얼리즘은 뛰어나지만 미래 이벤트 표현 학습에 부족하다.
- **Gap**: 월드 모델의 의미 있는 미래 표현 학습 능력과 생성형 비디오 모델의 확장성 및 현실성을 동시에 달성하는 통합 접근법이 부재하다.
- **Why**: 자율주행의 안전성과 효율성은 미래 이벤트의 정확한 예측에 달려 있으며, 고충실도의 합성 시나리오 생성은 시스템 훈련 및 검증을 가속화할 수 있다.
- **Approach**: GAIA-1은 비디오 프레임을 벡터 양자화된 이산 토큰으로 변환하여 다음 토큰 예측 문제로 재구성하는 autoregressive transformer 기반 월드 모델과, 이를 고해상도 비디오로 렌더링하는 multi-task video diffusion decoder로 구성된다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: GAIA-1 multimodal video generation. GAIA-1 can generate videos by performing future*

- **다중모달 조건부 생성**: 비디오, 텍스트, 액션 입력을 통해 세밀하게 제어 가능한 운전 시나리오 생성
- **의미론적 표현 학습**: 정적·동적 요소(자동차, 보행자, 신호등 등)와 장면 역학에 대한 고수준 구조 이해
- **기하학적 이해**: 도로 요철에 의한 피치와 롤 변화 같은 3D 기하학적 현상의 자연스러운 캡처
- **인과관계 추론**: 다른 에이전트의 반응적 행동과 도로 이용자의 의사결정 인과성 이해
- **일반화 능력**: 훈련 데이터 범위를 벗어난 시나리오(예: 도로 경계 외 운전)로의 외삽 성능

## How

![Figure 2](figures/fig2.webp)

*Figure 2: Architecture of GAIA-1. First, we encode information from all input modalities (video, text,*

- 세 가지 입력 모달리티를 공통 d차원 공간으로 인코딩: 이미지는 pre-trained image tokenizer로 n=576 토큰으로, 텍스트는 T5-large로 m=32 토큰으로, 액션은 speed와 curvature를 l=2 스칼라로 표현
- 시간-공간 분해된 위치 임베딩 사용: T개의 학습 가능한 시간 임베딩과 m+n+l=610개의 공간 임베딩으로 토큰 위치 인코딩
- Autoregressive transformer를 통한 다음 토큰 예측: 입력 시퀀스 (c₁, z₁, a₁, ..., cₜ, zₜ, aₜ)에서 미래 토큰 예측
- Image tokenizer의 의미론적 향상: DINO 증류를 통해 토큰에 고수준의 의미론적 내용 부여
- Multi-task video diffusion decoder: 고해상도 비디오 렌더링과 시간적 업샘플링을 동시에 수행하여 부드러운 비디오 생성

## Originality

- 월드 모델과 생성형 비디오 모델을 명시적으로 분리하여 각각의 강점을 활용하는 이원 구조 설계
- 이산 토큰 기반 예측 문제로의 재구성으로 LLM의 성공 사례를 비디오 도메인에 적용
- DINO 증류를 통한 image tokenizer의 의미론적 강화로 고수준 구조 학습 촉진
- 비디오, 텍스트, 액션의 유연한 다중모달 조건부 생성으로 미세한 장면 제어 가능
- 실제 운전 데이터로부터 인과관계와 물리적 법칙을 자동으로 학습하는 unsupervised 접근

## Limitation & Further Study

- 평가 메트릭의 명시적 제시 부재: 정량적 성능 비교 기준이 논문에서 충분히 기술되지 않음
- 장기 예측의 안정성: 매우 긴 시간 지평에서의 누적 오차와 모드 붕괴(mode collapse) 경향에 대한 분석 필요
- 도메인 특수성: UK 도시 운전 데이터로만 학습하였으므로 다른 지역이나 운전 환경으로의 전이 학습 평가 필요
- 계산 비용: 두 개의 대규모 모델(transformer 월드 모델과 diffusion decoder)을 순차적으로 실행하므로 실시간 추론 가능성에 대한 논의 부족
- 후속 연구 방향: 모델 동작 해석성 분석, 실제 자율주행 시스템과의 통합 검증, 시뮬레이터-현실 간극 감소 전략

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: GAIA-1은 월드 모델과 생성형 비디오 모델의 상보적 강점을 창의적으로 결합하여 자율주행을 위한 고충실도 시뮬레이션과 미래 예측을 동시에 달성하는 혁신적 접근법으로, 자율주행 기술의 훈련 및 검증을 획기적으로 가속화할 가능성을 제시한다.

## Related Papers

- 🔄 다른 접근: [[papers/1359_Diffusion_for_World_Modeling_Visual_Details_Matter_in_Atari/review]] — GAIA-1과 DIAMOND 모두 생성형 world model을 활용하지만, 자율주행 시나리오 vs 게임 환경이라는 서로 다른 응용 도메인을 다룬다
- 🔗 후속 연구: [[papers/1472_Mastering_Diverse_Domains_through_World_Models/review]] — DreamerV3의 범용 world model 학습이 GAIA-1의 자율주행 특화 생성형 모델을 더 일반적인 도메인으로 확장한 접근법을 보여준다
- 🏛 기반 연구: [[papers/1604_Video_Language_Planning/review]] — Video Language Planning의 비디오-언어 통합 방법론이 GAIA-1의 멀티모달 생성형 world model 설계에 이론적 기반을 제공한다
- 🔗 후속 연구: [[papers/1472_Mastering_Diverse_Domains_through_World_Models/review]] — DreamerV3의 범용 world model이 GAIA-1의 자율주행 특화 생성형 모델을 더 다양한 도메인으로 확장할 수 있는 일반화된 접근법을 보여준다
- 🔄 다른 접근: [[papers/1455_Learning_Universal_Policies_via_Text-Guided_Video_Generation/review]] — 텍스트 가이드 비디오 생성과 GAIA-1 모두 언어-비디오 통합 생성을 다루지만, 범용 정책 vs 자율주행 특화라는 서로 다른 응용 범위를 가진다
- 🔄 다른 접근: [[papers/1359_Diffusion_for_World_Modeling_Visual_Details_Matter_in_Atari/review]] — GAIA-1과 DIAMOND 모두 생성형 world model을 다루지만, 자율주행 vs 게임 환경이라는 서로 다른 응용 도메인을 적용한다
