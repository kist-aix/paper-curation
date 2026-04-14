---
title: "1618_PIMBS_Efficient_Body_Schema_Learning_for_Musculoskeletal_Hum"
authors:
  - "Kento Kawaharazuka"
  - "Takahiro Hattori"
  - "Keita Yoneda"
  - "Kei Okada"
date: "2025.06"
doi: ""
arxiv: ""
score: 4.0
essence: "Physics-Informed Neural Networks (PINNs) 개념을 적용하여 근골격 휴머노이드 로봇의 신체 스키마를 적은 데이터로 효율적으로 학습하는 PIMBS 방법을 제안한다."
tags:
  - "cat/Other"
  - "topic/humanoid"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kawaharazuka et al._2025_PIMBS Efficient Body Schema Learning for Musculoskeletal Humanoids with Physics-Informed Neural Net.pdf"
---

# PIMBS: Efficient Body Schema Learning for Musculoskeletal Humanoids with Physics-Informed Neural Networks

> **저자**: Kento Kawaharazuka, Takahiro Hattori, Keita Yoneda, Kei Okada | **날짜**: 2025-06-25 | **URL**: [https://arxiv.org/abs/2506.20343](https://arxiv.org/abs/2506.20343)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1.*

Physics-Informed Neural Networks (PINNs) 개념을 적용하여 근골격 휴머노이드 로봇의 신체 스키마를 적은 데이터로 효율적으로 학습하는 PIMBS 방법을 제안한다.

## Motivation

- **Known**: 근골격 휴머노이드는 인간의 근골격계를 모방하여 다양한 제어 이점을 제공하며, 기존 연구들은 실제 로봇 데이터만을 이용하여 관절각, 근육 긴장, 근육 길이 간의 관계를 학습해왔다.
- **Gap**: 실제 로봇에서 대량의 데이터 수집이 어렵고, 제한된 데이터로는 높은 정확도의 학습이 어려운 문제가 있다.
- **Why**: 근골격 휴머노이드는 복잡한 근육 경로를 가지고 있어 기하학적 모델과 실제 로봇 간 큰 차이가 발생하므로, 적은 데이터로도 효율적으로 신체 스키마를 학습할 수 있는 방법이 필요하다.
- **Approach**: 물리 법칙(토크와 근육 긴장의 관계: τ = −G^T(θ)f)을 손실 함수에 제약 조건으로 통합하여 neural network 기반 신체 스키마 학습을 강화한다.

## Achievement

![Figure 4](figures/fig4.webp)

*Fig. 4.*

- **PIMBS 방법 제안**: 물리 법칙 기반 제약을 neural network 학습에 통합하여 적은 데이터로도 높은 정확도 달성
- **이중 손실 함수**: 기본 MSE 손실(L_basic)과 물리 제약 손실(L_pinn)을 결합하여 차분 정보 활용
- **시뮬레이션 및 실제 로봇 검증**: 시뮬레이션된 근골격 구조와 실제 근골격 휴머노이드에서 모두 유효성 입증

## How

![Figure 4](figures/fig4.webp)

*Fig. 4.*

- 신체 스키마를 관절각 θ (또는 θ와 근육 긴장 f)를 입력으로 근육 길이 l을 출력하는 neural network h(θ) 또는 h(θ, f)로 모델링
- 기본 학습 손실 L_basic = MSE(l_pred, l_data)로 측정된 데이터의 재구성 오류 최소화
- 근육 Jacobian G = ∂h/∂θ를 계산하여 물리 제약 손실 L_pinn = (G^T f_data + τ_data)^2 추가
- 총 손실을 L_basic + λL_pinn 형태로 결합하여 neural network 가중치 W 최적화
- joint 구조가 정확하다는 가정 하에 중력 보상 토크 τ_data를 사전 계산하여 제약 조건으로 활용

## Originality

- PINNs 개념을 근골격 로봇의 신체 스키마 학습에 처음 적용하여 물리 제약 기반 학습 프레임워크 개발
- 토크-근육 긴장 관계식(τ = −G^T f)을 손실 함수에 직접 통합하여 differential information 활용
- 적은 데이터 환경에서의 효율적 학습을 통해 실제 로봇 데이터 수집 부담 감소

## Limitation & Further Study

- Joint 구조가 정확하다는 가정이 실제로 성립하지 않을 경우 성능 저하 가능
- 중력 보상 토크 τ_data 계산에 필요한 link 질량, 무게중심 등의 정확한 정보 요구
- wire 신장량 ΔN(θ, f)에 대한 근사(Eq. 5)가 성립하지 않는 극단적 상황에서의 적용 가능성 미검토
- 후속 연구: Joint 매개변수의 부정확성에 대한 강건성 개선, 복수 근육 간 상호작용 모델링, 동적 운동 중 신체 스키마 학습

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 Physics-Informed Neural Networks를 근골격 로봇의 신체 스키마 학습에 창의적으로 적용하여 적은 데이터로도 효율적인 학습을 가능하게 하는 실용적이고 혁신적인 방법을 제시한다. 시뮬레이션과 실제 로봇 실험을 통한 검증으로 제안 방법의 타당성을 충분히 입증했다.