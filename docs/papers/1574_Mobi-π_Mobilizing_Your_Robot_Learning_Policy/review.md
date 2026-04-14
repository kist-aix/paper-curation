---
title: "1574_Mobi-π_Mobilizing_Your_Robot_Learning_Policy"
authors:
  - "Jingyun Yang"
  - "Isabella Huang"
  - "Brandon Vu"
  - "Max Bajracharya"
  - "Rika Antonova"
date: "2025.05"
doi: ""
arxiv: ""
score: 4.0
essence: "학습된 조작 정책이 제한된 로봇 베이스 포즈에서만 훈련되어 모바일 플랫폼 배포 시 성능 저하 문제를 해결하기 위해, 정책 실행에 최적인 로봇 베이스 포즈를 찾는 '정책 모빌화(policy mobilization)' 문제를 정의하고 3D Gaussian Splatting과 샘플링 기반 최적화를 활용한 해결책을 제시한다."
tags:
  - "cat/Multimodal_Vision-Language_Policy_Learning"
  - "sub/Adversarial_Robot_Learning"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yang et al._2025_Mobi-$π$ Mobilizing Your Robot Learning Policy.pdf"
---

# Mobi-$π$: Mobilizing Your Robot Learning Policy

> **저자**: Jingyun Yang, Isabella Huang, Brandon Vu, Max Bajracharya, Rika Antonova, Jeannette Bohg | **날짜**: 2025-05-29 | **URL**: [https://arxiv.org/abs/2505.23692](https://arxiv.org/abs/2505.23692)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Introducing policy mobilization. (a) Assume a visuomotor policy π trained from one or a set of limited camera *

학습된 조작 정책이 제한된 로봇 베이스 포즈에서만 훈련되어 모바일 플랫폼 배포 시 성능 저하 문제를 해결하기 위해, 정책 실행에 최적인 로봇 베이스 포즈를 찾는 '정책 모빌화(policy mobilization)' 문제를 정의하고 3D Gaussian Splatting과 샘플링 기반 최적화를 활용한 해결책을 제시한다.

## Motivation

- **Known**: 학습된 비주얼모터 정책은 복잡한 조작 작업을 수행할 수 있지만, 대부분 제한된 로봇 위치와 카메라 시점에서 수집한 데이터로 훈련되어 새로운 로봇 베이스 포즈에 대한 일반화 성능이 낮다. 모바일 플랫폼에 배포할 때 정책이 훈련 분포 밖의 시점에서 실행되어 성능이 크게 저하된다.
- **Gap**: 기존 접근법은 정책 자체를 재훈련하거나 언어/객체 위치 기반의 비정책 인식 네비게이션을 사용하는데, 이는 추가 데이터 수집이 필요하거나 정책 호환성을 보장하지 못한다. 정책의 훈련 분포에 맞는 로봇 베이스 포즈를 능동적으로 찾는 방법이 부재하다.
- **Why**: 기존 고정 위치 로봇 데이터를 재사용하고 추가 훈련 데이터 없이 모바일 플랫폼에 조작 정책을 배포할 수 있게 되며, 네비게이션과 조작을 효과적으로 분리하여 각 모듈의 복잡도를 낮출 수 있다.
- **Approach**: 3D Gaussian Splatting을 이용한 scene 표현과 미분 가능 렌더링으로 후보 포즈의 적합성을 평가하고, 샘플링 기반 최적화를 통해 정책의 훈련 분포에 부합하는 최적 로봇 베이스 포즈를 탐색한다. 이와 함께 정책 모빌화의 난이도를 정량화하는 메트릭과 RoboCasa 기반 벤치마크 태스크 스위트를 제공한다.

## Achievement

![Figure 4](figures/fig4.webp)

*Figure 4: Spatial mobilization feasibility. We show the performance of running the given policy with Gaussian noise appl*

- **정책 모빌화 문제 정의**: 네비게이션과 조작을 분리하면서도 정책 호환성을 보장하는 새로운 문제 정식화로, 추가 데이터 수집 없이 기존 정책을 모바일 로봇에 배포 가능
- **종합적 평가 프레임워크**: 정책 모빌화 난이도를 정량화하는 메트릭, RoboCasa 기반 시뮬레이션 태스크 스위트, 분석용 시각화 도구로 구성된 Mobi-π 프레임워크 개발
- **실증적 성능 우수성**: 시뮬레이션 및 실제 모바일 조작 작업에서 비정책 인식 네비게이션과 학습 기반 정책 인식 기준선을 모두 초과하는 성능 달성

## How

![Figure 2](figures/fig2.webp)

*Figure 2: Overview of our proposed proof-of-concept method. The goal of our method is to find a proper robot pose p for *

- 3D Gaussian Splatting을 사용하여 novel view synthesis로 scene의 다양한 카메라 시점 표현
- 후보 로봇 베이스 포즈에서의 scene 렌더링을 통해 객체 가시성, 충돌 회피, 정책 in-distribution 정도 평가
- Score function을 정의하여 포즈의 적합성을 계산하고 sampling-based optimization으로 최적 포즈 탐색
- 기존 navigation 모듈과 조합하여 최적 포즈로 로봇 네비게이션한 후 조작 정책 실행
- 시뮬레이션과 실제 환경에서 다양한 baseline과 비교 평가

## Originality

- 정책의 훈련 분포에 맞는 로봇 베이스 포즈를 능동적으로 최적화하는 새로운 관점 제시
- 3D Gaussian Splatting과 미분 가능 렌더링을 활용한 novel view synthesis 기반 pose evaluation 방식의 창의적 적용
- 네비게이션-조작 분리와 정책 호환성을 동시에 달성하는 문제 정식화의 실용적 가치
- 정책 모빌화 난이도 메트릭과 벤치마크 스위트 제공으로 체계적 연구 기반 구축

## Limitation & Further Study

- 단일 작업 정책에 초점을 두었으며 다중 작업 정책 확장은 미래 과제
- 3D Gaussian Splatting이 단일 뷰 또는 제한된 뷰에서의 scene 표현 정확도에 의존
- scene 기하학이 크게 변하거나 동적 객체가 있는 복잡한 환경에서의 성능 미검증
- real-world 실험이 세 가지 작업으로 제한되어 있으며 더 다양한 환경과 객체 상호작용 연구 필요
- 계산 비용(3D GS reconstruction, optimization 시간) 분석과 최적화 방향 제시 부족

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 정책 모빌화라는 명확한 문제 정의와 실용적 해결책을 제시하여 기존 고정 위치 로봇 정책의 모바일 플랫폼 적용 가능성을 크게 높였다. 3D Gaussian Splatting 활용이 기술적으로 참신하고, 체계적 평가 프레임워크와 실증적 결과로 그 유효성을 잘 입증했으나, 현실 환경의 복잡성과 확장성 측면에서 추가 연구가 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/1286_Beyond_Tools_and_Persons_Who_Are_They_Classifying_Robots_and/review]] — 모바일 로봇 플랫폼에서 범용 정책 학습의 다른 접근법으로 베이스 포즈 최적화와 일반화를 비교할 수 있다.
- 🔗 후속 연구: [[papers/1575_Mobile-TeleVision_Predictive_Motion_Priors_for_Humanoid_Whol/review]] — 모바일 휴머노이드 전신 제어에서 예측적 모션 프라이어가 정책 모빌화의 성능을 보완한다.
- 🧪 응용 사례: [[papers/1488_NavDP_Learning_Sim-to-Real_Navigation_Diffusion_Policy_with/review]] — 네비게이션 확산 정책에서 정책 모빌화 기법이 실제 환경 배포 시 성능 향상에 기여한다.
- 🧪 응용 사례: [[papers/1495_NORA_A_Small_Open-Sourced_Generalist_Vision_Language_Action/review]] — 모바일 환경에서의 로봇 정책 실행과 소형 VLA 모델의 실시간 제어 능력이 직접적으로 연결된다.
