---
title: "1626_WHALE_Towards_Generalizable_and_Scalable_World_Models_for_Em"
authors:
  - "Zhilong Zhang"
  - "Ruifeng Chen"
  - "Junyin Ye"
  - "Yihao Sun"
  - "Pengyuan Wang"
date: "2024.11"
doi: ""
arxiv: ""
score: 4.0
essence: "WHALE는 행동 조건화(behavior-conditioning)와 retracing-rollout 기법을 통해 embodied 환경에서 일반화 가능하고 확장 가능한 world model을 학습하는 프레임워크이며, 이를 기반으로 Whale-ST와 414M 파라미터의 Whale-X 모델을 제시한다."
tags:
  - "cat/Humanoid_Locomotion_Control_Systems"
  - "sub/Uncertainty-Aware_Model_Predictive_Control"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhang et al._2024_WHALE Towards Generalizable and Scalable World Models for Embodied Decision-making.pdf"
---

# WHALE: Towards Generalizable and Scalable World Models for Embodied Decision-making

> **저자**: Zhilong Zhang, Ruifeng Chen, Junyin Ye, Yihao Sun, Pengyuan Wang, Jingcheng Pang, Kaiyuan Li, Tianshuo Liu, Haoxin Lin, Yang Yu, Zhi-Hua Zhou | **날짜**: 2024-11-08 | **URL**: [https://arxiv.org/abs/2411.05619](https://arxiv.org/abs/2411.05619)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Qualitative evaluation on Meta-World, Open X-Embodiment, and our real-world tasks.*

WHALE는 행동 조건화(behavior-conditioning)와 retracing-rollout 기법을 통해 embodied 환경에서 일반화 가능하고 확장 가능한 world model을 학습하는 프레임워크이며, 이를 기반으로 Whale-ST와 414M 파라미터의 Whale-X 모델을 제시한다.

## Motivation

- **Known**: World model은 embodied agent의 의사결정을 위해 실제 환경 대신 시뮬레이션을 가능하게 하는 중요한 기술이다. 최근 연구들은 transformer, diffusion model 등 고급 아키텍처와 대규모 비디오 데이터를 활용하여 world model을 개선하고 있다.
- **Gap**: 기존 world model 연구는 분포 이동(distribution shift)으로 인한 일반화 오류와 신뢰할 수 있는 uncertainty estimation 문제를 충분히 해결하지 못했다. 특히 고차원 시각 데이터에서 대규모로 확장하면서 동시에 OOD 영역에서의 충실한 예측을 유지하는 것이 어렵다.
- **Why**: World model이 정책 최적화에 신뢰할 수 있는 예측을 제공해야 오프라인 강화학습 및 실제 로봇 제어와 같은 실제 응용이 가능하다. 정확한 불확실성 추정은 synthetic data 남용으로 인한 성능 저하를 방지할 수 있다.
- **Approach**: 정책 분포 편차를 직접 해결하는 behavior-conditioning 기법과 모델 앙상블 없이 효율적인 불확실성 추정을 제공하는 retracing-rollout 기법을 핵심으로 제시한다. 이 두 기법은 spatial-temporal transformer 기반 Whale-ST와 대규모 사전학습된 Whale-X에 적용된다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: Qualitative evaluation on Meta-World, Open X-Embodiment, and our real-world tasks.*

- **Behavior-conditioning 기법**: 정책 분포 편차를 직접 해결하여 world model의 일반화 오류를 감소시키고, policy-conditioned 학습에 기반한 보편적 기법
- **Retracing-rollout 기법**: 모델 앙상블 없이 효율적인 불확실성 추정을 실현하여 오프라인 정책 최적화 성능 향상
- **Whale-ST**: Spatial-temporal transformer 기반 확장 가능한 world model로 Meta-World 벤치마크에서 기존 방법 대비 우수한 가치 추정 정확도 및 비디오 생성 충실도 달성
- **Whale-X**: Open X-Embodiment 데이터셋의 970K 궤적으로 학습한 414M 파라미터 world model로 시각, 움직임, 작업 측면에서 강력한 OOD 일반화 능력 및 확장성 입증

## How

![Figure 3](figures/fig3.webp)

*Figure 3: Overall architecture of Whale-ST. The behavior-conditioning model encodes the observation and action*

- Behavior-conditioning: 입력 시퀀스에 행동(behavior) 토큰을 조건으로 포함하여 다양한 정책에 대한 모델 적응성 향상
- Retracing-rollout: 롤아웃 과정에서 모델의 예측 오류를 추적하여 불확실성을 추정하는 방식으로, end-effector 포즈 제어에 적용 가능
- Spatial-temporal transformer 아키텍처: 시각적 역학을 모델링하기 위해 spatial과 temporal 정보를 통합하는 transformer 기반 구조 활용
- Meta-World 벤치마크와 실제 로봇 플랫폼에서 광범위한 평가: 시뮬레이션과 실제 픽셀 기반 조작 작업 모두에서 검증
- Open X-Embodiment 대규모 사전학습: 다양한 로봇 시스템의 대규모 시연 데이터를 활용한 기초 world model 구축 및 최소 시연으로 미지 환경 적응

## Originality

- 행동 조건화(behavior-conditioning)는 기존 policy-conditioned 접근법을 확장한 것이나, 대규모 시각 기반 world model에 직접 적용하여 정책 분포 편차 문제를 체계적으로 해결하는 점이 새로움
- Retracing-rollout은 앙상블 없이 단일 모델에서 불확실성을 추정하는 간단하면서도 효과적인 기법으로, 기존 앙상블 기반 불확실성 추정과 차별화됨
- Whale-X는 Open X-Embodiment 데이터셋을 활용한 처음의 대규모 embodied world model 사전학습 시도로, 다중 로봇 시스템 간 전이 학습 가능성을 실증함
- Spatial-temporal transformer 기반 아키텍처와 behavior-conditioning, retracing-rollout의 결합은 확장성과 일반화성을 동시에 추구하는 통합적 접근

## Limitation & Further Study

- Behavior-conditioning의 이론적 근거가 제한적이며, 어떤 행동 표현이 최적인지에 대한 상세한 분석 부족
- Retracing-rollout 기법의 불확실성 추정이 실제 모델 오류를 완벽하게 포착하는지에 대한 한계 존재 가능성
- Whale-X의 실제 로봇 평가가 제한된 시나리오에서만 수행되었으며, 더욱 복잡한 조작 작업에 대한 성능 검증 필요
- 대규모 사전학습 데이터의 이질성(heterogeneity)이 모델 성능에 미치는 영향에 대한 심화 분석 부재
- 향후 연구: (1) 행동 조건화의 이론적 기초 강화, (2) 더 정교한 불확실성 추정 방법론 탐색, (3) 다양한 embodiment과 장기 지평 작업에 대한 확대 평가, (4) 모델의 실시간 적응 능력 개선

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: WHALE는 embodied AI의 핵심 과제인 일반화와 불확실성 추정을 직접 해결하는 실용적이면서도 이론적 기여도 큰 프레임워크이며, Whale-ST와 Whale-X를 통해 시뮬레이션과 실제 로봇 환경 모두에서 강력한 성과를 입증하여 world model 기반 의사결정의 실용화를 크게 전진시킨다.

## Related Papers

- 🏛 기반 연구: [[papers/1631_World_Models/review]] — 월드 모델의 기본 개념이 WHALE의 임바디드 환경을 위한 일반화 가능한 월드 모델 학습의 이론적 기초를 제공합니다.
- 🔄 다른 접근: [[papers/1407_FRoM-W1_Towards_General_Humanoid_Whole-Body_Control_with_Lan/review]] — 생성형 인터랙티브 환경과 행동 조건화 월드 모델이 환경 모델링에서 서로 다른 접근 방식을 제시합니다.
- 🔗 후속 연구: [[papers/1357_Dexterous_Manipulation_through_Imitation_Learning_A_Survey/review]] — 제로샷 월드 액션 모델이 WHALE의 retracing-rollout 기법을 정책 학습으로 확장할 수 있는 가능성을 보여줍니다.
- 🔗 후속 연구: [[papers/1569_MetaWorld-X_Hierarchical_World_Modeling_via_VLM-Orchestrated/review]] — 계층적 월드 모델링을 위한 VLM 기반 전문가 라우팅이 WHALE의 행동 조건화 월드 모델과 상호보완적으로 작용할 수 있습니다.
