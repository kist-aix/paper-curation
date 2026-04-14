---
title: "1373_DualVLA_Building_a_Generalizable_Embodied_Agent_via_Partial"
authors:
  - "Zhen Fang"
  - "Zhuoyang Liu"
  - "Jiaming Liu"
  - "Hao Chen"
  - "Yu Zeng"
date: "2025.11"
doi: ""
arxiv: ""
score: 4.0
essence: "DualVLA는 Vision-Language-Action 모델에서 추론 능력을 추가할 때 발생하는 행동 성능 저하(action degeneration)를 해결하기 위해, 이중층 데이터 프루닝과 이중 교사 적응형 증류 전략을 통해 추론과 행동을 부분적으로 분리하는 접근법을 제시한다."
tags:
  - "cat/Multimodal_Vision-Language_Policy_Learning"
  - "sub/VLA_Model_Optimization"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Fang et al._2025_DualVLA Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action.pdf"
---

# DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action

> **저자**: Zhen Fang, Zhuoyang Liu, Jiaming Liu, Hao Chen, Yu Zeng, Shiting Huang, Zehui Chen, Lin Chen, Shanghang Zhang, Feng Zhao | **날짜**: 2025-11-27 | **URL**: [https://arxiv.org/abs/2511.22134](https://arxiv.org/abs/2511.22134)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1. DUALVLA first constructs a sparse, information-dense embodied reasoning dataset by combining video event predi*

DualVLA는 Vision-Language-Action 모델에서 추론 능력을 추가할 때 발생하는 행동 성능 저하(action degeneration)를 해결하기 위해, 이중층 데이터 프루닝과 이중 교사 적응형 증류 전략을 통해 추론과 행동을 부분적으로 분리하는 접근법을 제시한다.

## Motivation

- **Known**: Vision-Language-Action(VLA) 모델은 로봇 조작 데이터셋에서 미세 조정을 통해 강한 조작 성능을 달성할 수 있으며, 최근 연구들은 로봇 궤적에 추론 주석을 추가하여 일반화된 VLA를 구축하려고 시도하고 있다.
- **Gap**: specialist VLA에 추론 능력을 추가하기 위해 multimodal 데이터를 혼합하여 미세 조정할 때, 조작 성능이 오히려 저하되는 현상이 발생하며, 이를 명확히 분석하고 해결하는 방법이 부족하다.
- **Why**: 진정한 embodied agent는 정확한 행동 실행 능력과 복잡한 상황을 이해하는 추론 능력을 동시에 가져야 하므로, 이 두 능력 간의 성능 트레이드오프 문제를 해결하는 것이 중요하다.
- **Approach**: DualVLA는 두 가지 주요 기법을 활용한다: (1) video event prediction과 kinematic cues를 결합하여 중복적인 embodied reasoning을 제거하는 이중층 데이터 프루닝, (2) specialist VLA를 action teacher로, 추론 능력 유지를 위한 reasoning teacher를 활용하는 이중 교사 적응형 증류 전략.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2. VLMs possess strong reasoning ability but lack action*

- **행동 성능 개선**: SimplerEnv에서 평균 61.0의 성공률 달성하여 specialist VLA 대비 행동 성능 저하 현상 완화
- **다중 모달 성능**: 8개의 경쟁 벤치마크에서 평균 65.4점 달성으로 추론 능력과 행동 능력의 균형 입증
- **평가 프레임워크 제시**: VLA Score를 통해 reasoning, intention, action, alignment 4개 차원으로 VLA 성능을 세밀하게 평가하는 최초의 평가 체계 제공
- **실제 로봇 실험**: 시뮬레이션과 실제 로봇 환경 모두에서 일관된 성능 개선 입증

## How

![Figure 1](figures/fig1.webp)

*Figure 1. DUALVLA first constructs a sparse, information-dense embodied reasoning dataset by combining video event predi*

- **이중층 데이터 프루닝**: embodiment 신호와 scene-level event 변화를 모두 활용하여 중복적인 embodied reasoning을 식별하고 제거하되, 행동-critical 콘텐츠는 유지
- **이중 교사 적응형 증류**: specialist VLA를 action teacher로 활용하여 로봇 데이터에 대한 fine-grained supervision 제공, 동시에 reasoning teacher를 통해 multimodal 추론 능력 보존
- **혼합 훈련**: 로봇 데이터와 multimodal reasoning 데이터에 서로 다른 soft-label supervision 할당하여 균형잡힌 학습 유도
- **VLA Score 평가**: MLLM-as-a-Judge 패러다임을 도입하여 action, reasoning, intention, 그리고 reasoning-action alignment를 독립적으로 평가

## Originality

- **Action degeneration 문제의 명시적 정의**: 기존 연구에서 간과했던 specialist VLA에서 reasoning VLA로의 전환 과정에서의 성능 저하 현상을 구체화하고 정식화
- **부분적 분리 전략**: reasoning과 action을 완전히 분리하지 않으면서도 데이터와 손실 함수 수준에서 부분적으로 분리하는 새로운 접근
- **이중층 프루닝 메커니즘**: embodied reasoning의 중복성을 탐지하기 위해 kinematic cues와 scene-level 변화를 동시에 활용하는 창의적인 전략
- **VLA 전용 평가 체계**: 기존의 task success rate 중심 평가를 넘어 MLLM을 평가자로 활용하는 다차원적 평가 프레임워크 최초 제시

## Limitation & Further Study

- **데이터 프루닝의 휴리스틱 의존성**: video event prediction과 kinematic cues 기반의 프루닝이 다양한 로봇 작업 유형에 일관성 있게 적용되는지에 대한 검증이 제한적
- **VLA Score의 평가자 신뢰성**: MLLM evaluator의 주관성과 일관성에 대한 상세한 분석 부족 및 인간 평가와의 상관성 검증 필요
- **확장성 검증**: 주로 manipulation 중심의 로봇 작업에서 평가되었으며, 다른 embodied agent 도메인(navigation, 사람-로봇 상호작용 등)으로의 일반화 가능성 미확인
- **후속 연구**: (1) 더 정교한 데이터 프루닝 메커니즘 개발, (2) VLA Score의 robustness 및 reliability 향상, (3) 다양한 embodied task에서의 검증

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 Vision-Language-Action 모델의 실질적인 문제인 action degeneration을 명확히 정의하고, 이를 해결하기 위한 이중층 프루닝과 이중 교사 증류 전략을 제시함으로써 추론 능력과 조작 능력의 균형을 효과적으로 달성하였다. 특히 VLA 평가를 위한 다차원적 프레임워크 제시는 향후 embodied AI 연구의 평가 표준으로서 중요한 기여를 한다.

## Related Papers

- 🔄 다른 접근: [[papers/1621_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Ro/review]] — VLABench의 language-conditioned robotics benchmark가 DualVLA의 action degeneration 문제를 평가하는 다른 접근을 제시한다.
- 🔗 후속 연구: [[papers/1618_VLA-Reasoner_Empowering_Vision-Language-Action_Models_with_R/review]] — VLA-Reasoner의 reasoning 능력 강화가 DualVLA의 추론과 행동 분리 접근을 더욱 발전시킨다.
- 🏛 기반 연구: [[papers/1584_ThinkAct_Vision-Language-Action_Reasoning_via_Reinforced_Vis/review]] — ThinkAct의 vision-language-action reasoning이 DualVLA의 추론 능력 보존을 위한 이론적 기반을 제공한다.
