---
title: "1395_FlowPolicy_Enabling_Fast_and_Robust_3D_Flow-based_Policy_via"
authors:
  - "Qinglun Zhang"
  - "Zhen Liu"
  - "Haoqiang Fan"
  - "Guanghui Liu"
  - "Bing Zeng"
date: "2024.12"
doi: ""
arxiv: ""
score: 4.0
essence: "FlowPolicy는 Consistency Flow Matching을 기반으로 3D point cloud 조건에서 로봇 조작 정책을 단일 추론 단계로 생성하는 프레임워크로, 속도를 7배 향상시키면서 경쟁력 있는 성능을 유지한다."
tags:
  - "cat/Robotic_Foundation_Model_Development"
  - "sub/VLA_Architecture_Surveys"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhang et al._2024_FlowPolicy Enabling Fast and Robust 3D Flow-based Policy via Consistency Flow Matching for Robot Ma.pdf"
---

# FlowPolicy: Enabling Fast and Robust 3D Flow-based Policy via Consistency Flow Matching for Robot Manipulation

> **저자**: Qinglun Zhang, Zhen Liu, Haoqiang Fan, Guanghui Liu, Bing Zeng, Shuaicheng Liu | **날짜**: 2024-12-06 | **URL**: [https://arxiv.org/abs/2412.04987](https://arxiv.org/abs/2412.04987)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: Overall pipeline. The top section visualizes FlowPolicy, where a straight-line flow enables the fastest data t*

FlowPolicy는 Consistency Flow Matching을 기반으로 3D point cloud 조건에서 로봇 조작 정책을 단일 추론 단계로 생성하는 프레임워크로, 속도를 7배 향상시키면서 경쟁력 있는 성능을 유지한다.

## Motivation

- **Known**: Diffusion Policy와 3D Diffusion Policy (DP3)는 시각 기반 모방 학습에서 효과적이지만, 다중 샘플링 단계로 인한 추론 비효율이 문제다. Flow Matching은 diffusion보다 수치적으로 안정적이며 Consistency Flow Matching은 일단계 생성을 가능하게 한다.
- **Gap**: 기존 Consistency Flow Matching은 복잡한 3D 시각 표현이 포함된 조건부 생성 능력이 미흡하며, 로봇 조작 작업에서 효율성과 정책 품질 간 균형을 달성하는 것이 미해결 과제다.
- **Why**: 로봇이 실시간으로 복잡한 조작 작업을 수행하려면 고속 정책 생성이 필수이고, 단일 단계 추론으로 고품질 행동을 생성할 수 있다면 실제 배포에서 실용성이 크게 향상된다.
- **Approach**: FlowPolicy는 velocity field의 자기 일관성을 정규화하여 flow dynamics를 개선하고, 3D point cloud 조건에서 noise에서 로봇 action으로의 직선 흐름을 정의하는 consistency flow matching을 적용한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: Comparison of FlowPolicy with the state-of-the-*

- **단일 단계 생성**: 완전한 3D 조건 정보를 활용하여 한 번의 forward pass로 고품질 로봇 행동 생성 가능
- **추론 속도 향상**: Adroit과 Metaworld에서 최대 7배의 추론 시간 단축 달성
- **경쟁력 있는 성능**: 속도 개선에도 불구하고 DP3 등 최신 방법과 비교하여 평균 성공률에서 우수한 수준 유지
- **조건부 consistency flow matching의 첫 적용**: 3D 로봇 조작 작업에서 처음으로 조건부 consistency flow matching 구현

## How

![Figure 2](figures/fig2.webp)

*Figure 2: Overall pipeline. The top section visualizes FlowPolicy, where a straight-line flow enables the fastest data t*

- 3D point cloud를 compact 3D representation으로 인코딩하고 로봇 상태를 임베딩하여 조건부 정보 구성
- Velocity field의 자기 일관성을 정규화하여 서로 다른 시간 상태에서 같은 action space로의 직선 흐름 정의
- Consistency flow matching을 통해 noise distribution에서 policy distribution으로의 매핑을 직선 경로로 학습
- 다중 세그먼트 훈련으로 action 생성의 품질과 효율성 사이의 균형 달성
- 37개의 Adroit과 Metaworld 작업에서 광범위한 실험 검증

## Originality

- 3D 시각 조건을 활용한 첫 번째 consistency flow matching 기반 로봇 정책 생성 프레임워크
- Velocity field의 자기 일관성 정규화를 통한 flow dynamics 개선이라는 새로운 기법 제안
- Diffusion model의 재귀적 특성을 피하고 direct ODE 정의를 통해 근본적인 효율성 향상
- Multi-segment training으로 accuracy-efficiency 트레이드오프를 체계적으로 해결

## Limitation & Further Study

- 시뮬레이션 환경(Adroit, Metaworld)에서만 평가되었으며, 실제 로봇에서의 성능 검증 부재
- 단일 단계 생성으로 인한 정책 성능이 완벽하지 않을 수 있으며, 극도로 정밀한 조작에서의 한계 미언급
- Consistency flow matching의 조건부 생성이 복잡한 multi-modal 시나리오에서 어떻게 작동하는지 상세히 분석 필요
- 후속 연구로 실제 로봇 플랫폼에서의 검증, 다양한 시각 인코더의 영향 분석, 동적 환경에서의 적응성 개선 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: FlowPolicy는 consistency flow matching을 로봇 조작에 처음 적용하여 단일 추론 단계로 7배 빠른 정책 생성을 달성하는 독창적인 접근법이며, 실시간 로봇 제어의 실용성 향상에 중요한 기여를 한다.

## Related Papers

- 🔄 다른 접근: [[papers/1391_Fast-in-Slow_A_Dual-System_Foundation_Model_Unifying_Fast_Ma/review]] — 단일 추론 단계 policy 생성과 dual-system 구조의 서로 다른 속도 최적화 접근법
- 🏛 기반 연구: [[papers/1403_Gemini_Robotics_15_Pushing_the_Frontier_of_Generalist_Robots/review]] — consistency flow matching 기반 빠른 정책 생성이 Gemini Robotics의 실시간 제어 기반
- 🔄 다른 접근: [[papers/1559_RVT_Robotic_View_Transformer_for_3D_Object_Manipulation/review]] — 3D 조작에서 multi-view transformer와 3D flow-based policy라는 서로 다른 3D 표현 학습 방법을 제시한다.
