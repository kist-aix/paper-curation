---
title: "1345_DiffCoTune_Differentiable_Co-Tuning_for_Cross-domain_Robot_C"
authors:
  - "Lokesh Krishna"
  - "Sheng Cheng"
  - "Junheng Li"
  - "Naira Hovakimyan"
  - "Quan Nguyen"
date: "2025.05"
doi: ""
arxiv: ""
score: 4.0
essence: "DiffCoTune은 differentiable simulator를 활용하여 로봇 컨트롤러와 시뮬레이터 파라미터를 동시에 gradient 기반으로 튜닝하여 배포 도메인에서의 성능을 자동화된 방식으로 개선하는 프레임워크이다."
tags:
  - "cat/Robotic_Foundation_Model_Development"
  - "sub/Reinforcement_Learning_Training_Acceleration"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Krishna et al._2025_DiffCoTune Differentiable Co-Tuning for Cross-domain Robot Control.pdf"
---

# DiffCoTune: Differentiable Co-Tuning for Cross-domain Robot Control

> **저자**: Lokesh Krishna, Sheng Cheng, Junheng Li, Naira Hovakimyan, Quan Nguyen | **날짜**: 2025-05-29 | **URL**: [https://arxiv.org/abs/2505.24068](https://arxiv.org/abs/2505.24068)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1: Overview of the proposed automated co-tuning approach for*

DiffCoTune은 differentiable simulator를 활용하여 로봇 컨트롤러와 시뮬레이터 파라미터를 동시에 gradient 기반으로 튜닝하여 배포 도메인에서의 성능을 자동화된 방식으로 개선하는 프레임워크이다.

## Motivation

- **Known**: 로봇 컨트롤러의 sim-to-real 전이는 모델링 불일치로 인해 어려우며, 기존에는 robust control, domain randomization, system identification 등의 방법들이 각각 특정 한계를 가지고 있다.
- **Gap**: 기존 방법들은 시스템 식별과 컨트롤러 적응을 독립적으로 처리하거나 태스크별 수작업 설계가 필요하며, differentiable simulator를 활용한 통합적 co-tuning 접근은 부재했다.
- **Why**: 배포 도메인에서의 적절한 자동화된 튜닝은 로봇 시스템의 실제 활용을 위해 필수적이며, 소수의 시행(< 5회)으로 효과적인 전이를 달성하는 것이 산업적으로 중요하다.
- **Approach**: nominal controller와 differentiable simulator의 파라미터를 alternating optimization으로 동시에 튜닝하며, 배포 도메인에서 수집한 rollout을 활용하여 multi-step objective를 최적화한다.

## Achievement


- **자동화된 co-tuning 기법**: nominal controller와 differentiable simulator를 동시에 gradient 기반으로 튜닝하여 배포 도메인에서 체계적인 전이를 구현하며 소수의 시행으로 성능 개선 달성
- **광범위한 실험 검증**: cart-pole stabilization(저차원)부터 quadruped, biped tracking(고차원)까지 다양한 시스템에 적용 가능함을 입증
- **컨트롤러 범용성**: LQR, PD, MPC, DNN policy 등 서로 다른 특성의 model-based 및 learning-based controller에 모두 적용 가능
- **다중 도메인 전이**: 서로 다른 시뮬레이터 및 하드웨어 간 성공적인 전이 달성

## How

![Figure 2](figures/fig2.webp)

*Fig. 2: Phase portraits of progressive tuning iterates of DiffCoTune*

- Differentiable simulator f(x_t, u_t; β)와 controller π(x_t; θ)를 정의하고 closed-loop dynamics에 기반한 system identification objective J_sysId 수식화
- 배포 도메인에서 수집한 observable state x^sys_t를 이용하여 모델과 실제 시스템의 상태 차이를 최소화하는 목표 설정
- Task objective J_task를 정의하고 differentiable simulator를 거쳐 역전파 가능하도록 구조화
- Alternating optimization을 통해 (1) simulator parameter β를 고정하고 controller parameter θ를 업데이트, (2) controller를 고정하고 simulator parameter를 업데이트하는 과정을 반복
- 배포 도메인에서의 새로운 rollout을 활용하여 반복적으로 튜닝을 진행하며 수렴할 때까지 반복

## Originality

- System identification과 controller adaptation을 독립적이 아닌 coupled problem으로 통합하여 novel한 co-tuning formulation 제시
- 기존 multi-stage optimization(residual policy learning + simulator augmentation)과 달리 pure gradient-based co-tuning으로 hyperparameter 튜닝 필요성 제거
- Differentiable simulator의 활용을 system identification 목표가 아닌 controller deployment 성능 개선을 직접 목표로 전환
- Task-specific 설계 요구 없이 임의 복잡도의 controller에 적용 가능한 일반화된 프레임워크 개발

## Limitation & Further Study

- Differentiable simulator 구축의 초기 비용 및 복잡도: 모든 동역학을 differentiable하게 구현해야 하므로 기존 시뮬레이터 대비 개발 난이도가 높음
- 배포 도메인에서의 rollout 수집 필요: 방법의 실용성이 안전하고 빈번한 실시행이 가능한 시스템에 제한될 수 있음
- Local optimum에만 수렴 가능: Nominal controller 근처의 local solution을 찾으므로 초기 controller의 품질에 크게 의존
- High-dimensional uncertainty 모델링 부재: 매개변수로 표현되지 않는 비구조적 불확실성(friction 변화, 센서 노이즈 등)에 대한 robustness 분석 미흡
- **후속 연구 방향**: (1) uncertainty quantification을 통한 robustness 개선, (2) meta-learning으로 다중 도메인 일반화, (3) 적응 컨트롤러와의 결합

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 differentiable simulator를 활용한 controller co-tuning이라는 명확하고 혁신적인 아이디어를 제시하며, 다양한 시스템과 컨트롤러에 대한 광범위한 실험을 통해 그 유효성을 입증했다. 산업적 실용성이 높고 이론적 기여도 우수하나, differentiable simulator 구축의 초기 비용 및 배포 환경에서의 rollout 수집 요구 등이 광범위한 적용을 제한할 수 있다.

## Related Papers

- 🔗 후속 연구: [[papers/1351_DeeR-VLA_Dynamic_Inference_of_Multimodal_Large_Language_Mode/review]] — differentiable co-tuning에서도 상황별 계산 자원 할당을 위한 동적 추론 최적화 적용 가능
- 🔄 다른 접근: [[papers/1394_FLaRe_Achieving_Masterful_and_Adaptive_Robot_Policies_with_L/review]] — cross-domain 성능 향상을 위해 gradient 기반 자동 튜닝과 RL 미세조정의 상호보완적 접근
- 🔄 다른 접근: [[papers/1296_Bridging_the_Sim-to-Real_Gap_for_Athletic_Loco-Manipulation/review]] — cross-domain robot learning을 각각 VLA 기초 모델과 differentiable co-tuning으로 다르게 접근한다
- 🏛 기반 연구: [[papers/1394_FLaRe_Achieving_Masterful_and_Adaptive_Robot_Policies_with_L/review]] — 대규모 사전학습된 정책의 RL 미세조정이 differentiable co-tuning의 성능 안정화 기법 제공
