---
title: "1549_RoboTron-Nav_A_Unified_Framework_for_Embodied_Navigation_Int"
authors:
  - "Yufeng Zhong"
  - "Chengjian Feng"
  - "Feng Yan"
  - "Fanfan Liu"
  - "Liming Zheng"
date: "2025.03"
doi: ""
arxiv: ""
score: 4.0
essence: "RoboTron-Nav는 perception, planning, prediction을 통합하는 embodied navigation 프레임워크로, multitask collaboration (navigation + EQA)과 adaptive 3D-aware history sampling을 통해 언어 기반 시각 네비게이션 성능을 향상시킨다."
tags:
  - "cat/Embodied_Navigation_and_Planning"
  - "sub/Embodied_Chain-of-Thought"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhong et al._2025_RoboTron-Nav A Unified Framework for Embodied Navigation Integrating Perception, Planning, and Pred.pdf"
---

# RoboTron-Nav: A Unified Framework for Embodied Navigation Integrating Perception, Planning, and Prediction

> **저자**: Yufeng Zhong, Chengjian Feng, Feng Yan, Fanfan Liu, Liming Zheng, Lin Ma | **날짜**: 2025-03-24 | **URL**: [https://arxiv.org/abs/2503.18525](https://arxiv.org/abs/2503.18525)

---

## Essence

![Figure 3](figures/fig3.webp)

*Figure 3. Overview of RoboTron-Nav architecture. The current frame It is initially processed through 2D and 3D feature e*

RoboTron-Nav는 perception, planning, prediction을 통합하는 embodied navigation 프레임워크로, multitask collaboration (navigation + EQA)과 adaptive 3D-aware history sampling을 통해 언어 기반 시각 네비게이션 성능을 향상시킨다.

## Motivation

- **Known**: 기존 ObjectNav 모델들은 VLM을 활용하여 객체 위치 파악에는 우수하지만, 경로 계획 설명과 장기 네비게이션 효율성이 떨어지며, 재방문 영역에서 관찰 중복성이 발생한다.
- **Gap**: 현재 네비게이션 모델은 의사결정 과정을 명확히 하지 못하고, 장기 네비게이션 중 중복된 historical perception을 효과적으로 관리하지 못한다.
- **Why**: embodied AI의 신뢰성 있는 네비게이션을 위해서는 강력한 perception, planning, prediction 능력이 필수이며, 장기 네비게이션 효율성 향상이 실제 로봇 응용에 중요하다.
- **Approach**: Multitask collaboration을 통해 navigation과 EQA 과제를 공동 학습하여 perception과 planning을 강화하고, adaptive 3D-aware history sampling으로 spatial과 semantic 차원의 관찰 중복을 최소화한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2. Top: During long-term navigation, agents may revisit*

- **CHORES-S 벤치마크 SOTA**: ObjectNav에서 81.1% success rate 달성, 기존 방법 대비 9% 절대 개선
- **Multitask collaboration 전략**: Navigation과 EQA 과제의 공동 학습으로 의사결정 과정의 해석가능성 향상
- **Adaptive 3D-aware history sampling**: Spatial 및 semantic 차원에서 관찰 중복성을 제어하여 장기 네비게이션 효율성 극대화

## How

![Figure 3](figures/fig3.webp)

*Figure 3. Overview of RoboTron-Nav architecture. The current frame It is initially processed through 2D and 3D feature e*

- Visual encoder (UVFormer + ViT)를 통한 현재 프레임의 2D/3D 특성 추출
- Adaptive 3D-aware history sampling: RGB 프레임을 공간적으로 인접하지 않거나 다른 시점에서 캡처한 경우만 유효한 관찰로 선택
- Position-enhanced historical features: 에이전트 위치 정보로 historical semantic features를 강화하여 중복 탐색 방지
- EQA 데이터셋 확장: Navigation 데이터셋에 명시적 의사결정 과정을 모델링하는 QA 쌍 추가
- LLM 기반 multimodal fusion: 지시사항과 시각 특성을 LLM으로 처리하여 action과 answer 동시 생성

## Originality

- Navigation과 EQA의 multitask collaboration을 통해 perception과 planning을 명시적으로 통합하는 novel한 접근
- 3D 공간 정보를 활용한 adaptive history sampling으로 spatial-semantic 차원의 중복성을 동시에 처리
- Navigation 데이터셋으로부터 의사결정 과정을 모델링하는 EQA 데이터셋을 자동으로 구축하는 방법론
- Position-enhanced features를 통해 trajectory 정보를 historical perception에 직접 통합하는 설계

## Limitation & Further Study

- EQA 데이터셋 구축 방법의 자세한 검증이 부족하며, 생성된 QA 쌍의 품질 평가 지표 부재
- Adaptive sampling 전략이 모든 환경 특성에 최적일지 불명확하며, 서로 다른 벤치마크에 대한 일반화 성능 분석 필요
- LLM의 계산 비용 및 추론 시간에 대한 분석이 제시되지 않아 실시간 로봇 응용 가능성 평가 곤란
- 3D reconstruction 정확도 저하 상황에서의 시스템 강건성 테스트 필요
- 후속 연구: 다양한 환경 특성에 맞는 적응형 history sampling 파라미터 최적화, lightweight LLM 활용 방안 탐색, 실제 로봇 플랫폼에서의 검증

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: RoboTron-Nav는 multitask collaboration과 adaptive history sampling이라는 두 가지 혁신적 구성요소를 통해 embodied navigation의 해석가능성과 효율성을 동시에 개선하며, SOTA 성능 달성으로 실용적 가치가 높다. 다만 데이터셋 구축 방법론과 실시간 적용 가능성에 대한 추가 검증이 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/1382_EmbodiedVSR_Dynamic_Scene_Graph-Guided_Chain-of-Thought_Reas/review]] — EmbodiedVSR의 dynamic scene graph guided reasoning이 RoboTron-Nav의 perception, planning, prediction 통합을 더 동적인 추론으로 확장한다.
- 🏛 기반 연구: [[papers/1304_ALFRED_A_Benchmark_for_Interpreting_Grounded_Instructions_fo/review]] — ALFRED의 grounded instruction interpretation이 RoboTron-Nav의 언어 기반 시각 네비게이션의 기초 방법론을 제공한다.
- 🔄 다른 접근: [[papers/1630_WMNav_Integrating_Vision-Language_Models_into_World_Models_f/review]] — WMNav의 world models 통합과 RoboTron-Nav의 multitask collaboration은 모두 네비게이션 성능 향상을 위한 서로 다른 접근법이다.
- 🔗 후속 연구: [[papers/1378_Embodied_Navigation_Foundation_Model/review]] — RoboTron-Nav의 통합 네비게이션 프레임워크가 NavFoM의 범용성을 확장한다.
