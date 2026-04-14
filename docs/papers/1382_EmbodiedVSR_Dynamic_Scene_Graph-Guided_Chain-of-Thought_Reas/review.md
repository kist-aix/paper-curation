---
title: "1382_EmbodiedVSR_Dynamic_Scene_Graph-Guided_Chain-of-Thought_Reas"
authors:
  - "Yi Zhang"
  - "Qiang Zhang"
  - "Xiaozhu Ju"
  - "Zhaoyang Liu"
  - "Jilei Mao"
date: "2025.03"
doi: ""
arxiv: ""
score: 4.0
essence: "EmbodiedVSR는 동적 scene graph와 Chain-of-Thought 추론을 결합하여 embodied agent의 공간 추론 능력을 향상시키는 프레임워크이며, 이를 평가하기 위해 eSpatial-Benchmark 데이터셋을 제시한다."
tags:
  - "cat/Embodied_Navigation_and_Planning"
  - "sub/Embodied_Chain-of-Thought"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhang et al._2025_EmbodiedVSR Dynamic Scene Graph-Guided Chain-of-Thought Reasoning for Visual Spatial Tasks.pdf"
---

# EmbodiedVSR: Dynamic Scene Graph-Guided Chain-of-Thought Reasoning for Visual Spatial Tasks

> **저자**: Yi Zhang, Qiang Zhang, Xiaozhu Ju, Zhaoyang Liu, Jilei Mao, Jingkai Sun, Jintao Wu, Shixiong Gao, Shihan Cai, Zhiyuan Qin, Linkai Liang, Jiaxu Wang, Yiqun Duan, Jiahang Cao, Renjing Xu, Jian Tang | **날짜**: 2025-03-14 | **URL**: [https://arxiv.org/abs/2503.11089](https://arxiv.org/abs/2503.11089)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1. Overview of EmbodiedVSR, a framework integrating multimodal interaction and dynamic task execution. EmbodiedVS*

EmbodiedVSR는 동적 scene graph와 Chain-of-Thought 추론을 결합하여 embodied agent의 공간 추론 능력을 향상시키는 프레임워크이며, 이를 평가하기 위해 eSpatial-Benchmark 데이터셋을 제시한다.

## Motivation

- **Known**: Multimodal Large Language Model (MLLM)과 Vision-Language Model (VLM)이 embodied intelligence에서 진전을 이루었으나, 현재의 모델들은 공간 추론에서 명시적 기하학적 근거 없이 물체 관계를 환상화하고 복잡한 다단계 작업에서 추론 과정이 단편화되는 문제를 가지고 있다.
- **Gap**: 기존 MLLM 기반 시스템은 동적 환경 이해를 요구하는 공간 추론 작업에서 암묵적 공간 지식에만 의존하며, task-specific fine-tuning을 통한 학습은 제한된 데이터 커버리지로 인해 실제 embodied 환경에 일반화되지 않는다.
- **Why**: 정확한 공간 추론 능력은 로봇이 현실 세계에서 조작 작업을 수행하기 위해 필수적이며, 구조화된 명시적 공간 표현을 갖춘 MLLM은 신뢰할 수 있는 embodied intelligence 시스템의 배포를 가능하게 한다.
- **Approach**: 동적 scene graph를 통해 물체 상태, 객체 간 관계, 행동 기반 환경 변화를 명시적으로 모델링하고, 이를 physics-constrained Chain-of-Thought 프로세스와 통합하여 zero-shot 공간 추론을 달성한다.

## Achievement

![Figure 4](figures/fig4.webp)

*Figure 4. eSpatial-RoboMIND Benchmark evaluation*

- **Zero-shot 공간 추론**: Task-specific fine-tuning 없이도 구조화된 scene graph 기반 추론으로 새로운 작업에 일반화
- **eSpatial-Benchmark 구축**: 실제 환경의 동적 상호작용을 포함한 세분화된 공간 주석과 적응형 어려움 수준을 갖춘 포괄적 데이터셋 개발
- **성능 향상**: 기존 MLLM 기반 방법 대비 정확도와 추론 일관성에서 우수한 성능, 특히 반복적 환경 상호작용이 필요한 장기 작업에서 검증
- **명시적 추론 메커니즘**: 물리적 일관성 규칙으로 검증되는 계층적 작업 분해를 통해 해석 가능성 및 신뢰성 향상

## How

![Figure 1](figures/fig1.webp)

*Figure 1. Overview of EmbodiedVSR, a framework integrating multimodal interaction and dynamic task execution. EmbodiedVS*

- Visual Aid Extractor를 통한 depth estimation과 object detection으로 시각 정보 추출
- Graph Vertex Extractor를 사용하여 객체와 속성을 노드로 추출
- Scene Graph Generator에서 객체 간 scaleless spatial relation ([+x, +y] 형식)을 명시적으로 생성
- Spatial CoT를 통해 subjects 식별 → scene graph 질의 → relation deduction → 답변 생성의 단계적 추론
- Short-term Visual-QA task loop와 long-term interactive task loop를 구분하여 dynamic replan 지원
- Interactor를 통한 voice/text I/O와 servo actuation으로 실제 robot control 통합

## Originality

- 동적 scene graph를 embodied AI 공간 추론에 처음 적용하여 명시적 기하학적 제약을 Chain-of-Thought와 통합
- Scaleless spatial relation 표현을 통해 scale invariant한 공간 관계 모델링
- Action-conditioned object state를 반영한 실제 manipulation 작업 기반 벤치마크 구축
- Zero-shot adaptability와 물리적 일관성을 동시에 확보하는 새로운 아키텍처 제안

## Limitation & Further Study

- Scene graph 구성이 depth estimation과 object detection의 품질에 의존하므로, 불완전한 시각 입력에서 오류 전파 가능성
- 복잡한 다중 agent 환경이나 동적으로 변화하는 대규모 장면에서의 확장성 검증 부재
- eSpatial-Benchmark가 주로 LEGO 및 tabletop 조작에 초점화되어 있어 다양한 embodied task로의 일반화 한계
- Scaleless spatial relation이 물리적 거리 정보를 버리므로, 정확한 metric scale이 필요한 정밀 조작에서 제한
- 후속 연구는 다중 modality sensor fusion, 실시간 scene graph update 최적화, 다양한 실제 로봇 플랫폼에서의 검증 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 MLLMs을 embodied intelligence에 적용하기 위해 동적 scene graph와 structured reasoning을 결합한 혁신적 접근법을 제시하며, 새로운 벤치마크와 함께 zero-shot 공간 추론에서 유의미한 성능 개선을 달성했다. 해석 가능성과 실용성 면에서 embodied AI 분야에 중요한 기여를 할 것으로 판단된다.

## Related Papers

- 🏛 기반 연구: [[papers/1381_Embodied-Reasoner_Synergizing_Visual_Search_Reasoning_and_Ac/review]] — Embodied-Reasoner의 Chain-of-Thought 추론이 EmbodiedVSR의 구조적 추론 프레임워크에 기반한다.
- 🔗 후속 연구: [[papers/1383_EmbSpatial-Bench_Benchmarking_Spatial_Understanding_for_Embo/review]] — EmbSpatial-Bench의 공간 이해 평가가 EmbodiedVSR의 spatial reasoning 성능 검증에 활용된다.
- 🔄 다른 접근: [[papers/1612_Visual_Language_Maps_for_Robot_Navigation/review]] — Visual Language Maps도 로봇의 공간 추론과 네비게이션을 위한 구조화된 표현을 제안한다.
- 🔗 후속 연구: [[papers/1381_Embodied-Reasoner_Synergizing_Visual_Search_Reasoning_and_Ac/review]] — EmbodiedVSR의 scene graph 구조가 Embodied-Reasoner의 시각 탐색과 추론을 체계화한다.
- 🔗 후속 연구: [[papers/1549_RoboTron-Nav_A_Unified_Framework_for_Embodied_Navigation_Int/review]] — EmbodiedVSR의 dynamic scene graph guided reasoning이 RoboTron-Nav의 perception, planning, prediction 통합을 더 동적인 추론으로 확장한다.
- 🔗 후속 연구: [[papers/1379_Embodied-R_Collaborative_Framework_for_Activating_Embodied_S/review]] — EmbodiedVSR의 dynamic scene graph가 Embodied-R의 spatial reasoning을 구조적으로 발전시킨다.
- 🏛 기반 연구: [[papers/1383_EmbSpatial-Bench_Benchmarking_Spatial_Understanding_for_Embo/review]] — EmbodiedVSR의 spatial reasoning 프레임워크가 EmbSpatial-Bench의 벤치마크 설계에 기여한다.
