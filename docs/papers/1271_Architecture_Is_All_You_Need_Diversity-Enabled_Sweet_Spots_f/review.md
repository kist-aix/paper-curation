---
title: "1271_Architecture_Is_All_You_Need_Diversity-Enabled_Sweet_Spots_f"
authors:
  - "Blake Werner"
  - "Lizhi Yang"
  - "Aaron D. Ames"
date: "2025.10"
doi: ""
arxiv: ""
score: 4.0
essence: "휴머노이드 로봇의 견고한 보행을 위해 고속의 proprioceptive stabilizer와 저속의 지각 기반 네비게이션 정책을 분리한 layered control architecture (LCA)를 제안하며, 이러한 구조적 분리가 복잡한 네트워크보다 견고성에 더 중요함을 보인다."
tags:
  - "cat/Humanoid_Locomotion_Control_Systems"
  - "sub/Multi-Modal_Humanoid_Control"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Werner et al._2025_Architecture Is All You Need Diversity-Enabled Sweet Spots for Robust Humanoid Locomotion.pdf"
---

# Architecture Is All You Need: Diversity-Enabled Sweet Spots for Robust Humanoid Locomotion

> **저자**: Blake Werner, Lizhi Yang, Aaron D. Ames | **날짜**: 2025-10-16 | **URL**: [https://arxiv.org/abs/2510.14947](https://arxiv.org/abs/2510.14947)

---

## Essence

![Figure 2](figures/fig2.webp)

*Fig. 2. Training and Deployment Overview: both actor and critic are two-stage architectures each with their own percepti*

휴머노이드 로봇의 견고한 보행을 위해 고속의 proprioceptive stabilizer와 저속의 지각 기반 네비게이션 정책을 분리한 layered control architecture (LCA)를 제안하며, 이러한 구조적 분리가 복잡한 네트워크보다 견고성에 더 중요함을 보인다.

## Motivation

- **Known**: end-to-end 학습 기반 휴머노이드 보행이 발전했지만, 불구조화된 환경에서의 견고성이 제한적이다. 항공우주 GNC 분야에서는 다층의 다속도 제어 구조가 오래전부터 표준으로 사용되어왔다.
- **Gap**: 현존하는 학습 기반 휴머노이드 제어는 단일 end-to-end 네트워크 설계에 치중하거나 복잡한 모델을 요구하는데, 구조적 분리의 중요성과 최소한의 LCA 설계에 대한 체계적 연구가 부족하다.
- **Why**: 휴머노이드 보행에서 fast low-level stabilization과 slow perceptual decision-making 사이의 timescale 불일치를 해결하는 것이 견고성의 핵심이며, 이는 실제 하드웨어 배포의 성공률을 크게 높일 수 있다.
- **Approach**: 두 단계 커리큘럼으로 학습하는 최소한의 LCA 설계: (1) 지각 제거 후 proprioceptive stabilizer를 먼저 학습하고, (2) compact local heightmap 인코더를 추가하여 저속 네비게이션 정책을 fine-tuning한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2. Training and Deployment Overview: both actor and critic are two-stage architectures each with their own percepti*

- **구조적 우월성**: layered 구조가 같은 복잡도의 monolithic end-to-end 설계를 크게 상회하며, 특히 ablation 분석에서 구조 제거 시 성능이 크게 저하됨을 보였다.
- **최소화된 설계**: 복잡한 환경 추정기, mixed-integer 최적화, world model, 정교한 네트워크 없이도 계단, 언덕길 등 복잡한 지형 과제에서 성공했다.
- **하드웨어 검증**: Unitree G1 휴머노이드에서 one-stage 지각 정책이 실패하는 stair 및 ledge 과제에 성공했다.
- **최적화 이론**: 두 단계 최적화가 one-stage 최적화보다 local maxima 수렴이 용이함을 수식으로 분석했다.

## How

![Figure 2](figures/fig2.webp)

*Fig. 2. Training and Deployment Overview: both actor and critic are two-stage architectures each with their own percepti*

- Fast stabilizer: proprioception만 입력받아 joint-space tracking을 수행하는 고속(200Hz) 정책으로 접촉 변동성 대응
- Navigation encoder: 압축된 local heightmap을 처리하는 저속(10Hz) 정책으로 장거리 지형 기하학 정보 제공
- Two-stage curriculum: 첫 단계에서 지각을 0으로 설정하여 stabilizer를 독립적으로 최적화, 두 번째 단계에서 navigation policy를 fine-tuning
- 표준 RL 보상: complex reward shaping 없이 기존 locomotion RL 보상으로 학습
- Narrow interfaces: 네비게이션에서 stabilizer로는 참조 신호 전달, 역방향으로는 추적 오차 및 상태 정보만 전달

## Originality

- GNC의 다층 구조 원칙을 명시적으로 휴머노이드 학습 제어에 적용하고 이를 'diversity-enabled sweet spots' 개념으로 일반화했다.", '두 단계 커리큘럼의 최적화 이론적 정당화를 제시하여 순차 최적화가 joint 최적화와 수렴 특성이 다름을 보였다.
- 최소화된 LCA 설계가 복잡한 설계와 동등 이상의 성능을 낼 수 있음을 체계적으로 입증했다.

## Limitation & Further Study

- 최적화 분석이 strictly concave 보상 함수 가정 기반인데, 실제 RL은 non-concave이므로 이론과 실제의 간격이 있다.
- Guidance layer(상위 계획)를 '주어진 것'으로 가정했으며, 전체 세 계층 통합에 대한 분석이 없다.", '현재 4개 과제(계단 오르내리기, 경사로)에 한정되며, 더 복잡한 동적 환경(장애물 회피, 동적 지형)에 대한 검증이 필요하다.
- Knowledge distillation 방법과의 아키텍처 동등성 비교가 미흡하며, 이를 깊이 있게 분석하는 것이 향후 과제다.
- Heightmap 기반 perception의 신뢰성이 depth 센서 노이즈에 얼마나 영향받는지에 대한 상세 분석이 부족하다.

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 휴머노이드 보행에서 네트워크 복잡도보다 아키텍처 분리가 중요함을 명확히 입증했으며, 최소한의 설계로 하드웨어에서 견고한 성능을 달성한 점이 실무적 가치가 높다. 다만 이론 분석과 실제 RL의 간격 및 과제의 제한성을 개선할 여지가 있다.

## Related Papers

- 🏛 기반 연구: [[papers/1309_CLOT_Closed-Loop_Global_Motion_Tracking_for_Whole-Body_Human/review]] — layered control architecture의 견고성이 RSR 루프의 sim-to-real 갭 해소에 기여한다
- 🔗 후속 연구: [[papers/1317_Contrastive_Representation_Learning_for_Robust_Sim-to-Real_T/review]] — 구조적 분리 원칙을 대조 학습 기반 견고한 제어로 확장한다
- 🔄 다른 접근: [[papers/1504_JAEGER_Dual-Level_Humanoid_Whole-Body_Controller/review]] — layered 제어 대신 dual-level 계층적 제어 접근 방식을 제시한다
- 🔗 후속 연구: [[papers/1309_CLOT_Closed-Loop_Global_Motion_Tracking_for_Whole-Body_Human/review]] — 견고한 제어 구조 설계에 RSR 루프의 시뮬레이션 개선 방법론을 추가한다
- 🏛 기반 연구: [[papers/1317_Contrastive_Representation_Learning_for_Robust_Sim-to-Real_T/review]] — proprioceptive 제어의 견고성에 구조적 분리 원칙을 활용한다
