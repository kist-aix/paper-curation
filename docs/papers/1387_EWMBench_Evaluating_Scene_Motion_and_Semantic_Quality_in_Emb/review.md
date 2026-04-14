---
title: "1387_EWMBench_Evaluating_Scene_Motion_and_Semantic_Quality_in_Emb"
authors:
  - "Hu Yue"
  - "Siyuan Huang"
  - "Yue Liao"
  - "Shengcong Chen"
  - "Pengfei Zhou"
date: "2025.05"
doi: ""
arxiv: ""
score: 4.0
essence: "본 논문은 Embodied World Models (EWMs)의 성능을 평가하기 위한 전문 벤치마크인 EWMBench를 제안하며, 시각적 장면 일관성, 동작 정확성, 의미론적 정렬이라는 세 가지 핵심 측면을 기반으로 로보틱 조작 작업에서의 물리적 타당성과 행동 일관성을 평가한다."
tags:
  - "cat/Embodied_Navigation_and_Planning"
  - "sub/Embodied_Chain-of-Thought"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yue et al._2025_EWMBench Evaluating Scene, Motion, and Semantic Quality in Embodied World Models.pdf"
---

# EWMBench: Evaluating Scene, Motion, and Semantic Quality in Embodied World Models

> **저자**: Hu Yue, Siyuan Huang, Yue Liao, Shengcong Chen, Pengfei Zhou, Liliang Chen, Maoqing Yao, Guanghui Ren | **날짜**: 2025-05-14 | **URL**: [https://arxiv.org/abs/2505.09694](https://arxiv.org/abs/2505.09694)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: Overview of the EWMBENCH benchmark design. The framework begins with unified*

본 논문은 Embodied World Models (EWMs)의 성능을 평가하기 위한 전문 벤치마크인 EWMBench를 제안하며, 시각적 장면 일관성, 동작 정확성, 의미론적 정렬이라는 세 가지 핵심 측면을 기반으로 로보틱 조작 작업에서의 물리적 타당성과 행동 일관성을 평가한다.

## Motivation

- **Known**: 최근 text-to-video diffusion models이 언어 명령으로부터 고충실도 비디오를 생성할 수 있게 되었으며, 기존 비디오 생성 벤치마크들(VBench, T2V-CompBench 등)은 시각적 충실도와 언어 정렬에 중점을 두고 있다.
- **Gap**: 기존 평가 메트릭들은 EWMs의 고유한 요구사항인 물리적 타당성, 동작 일관성, 객체 상호작용 등을 충분히 평가하지 못하며, 로보틱 조작 작업의 특수성을 반영한 전문적 벤치마크가 부재하다.
- **Why**: 로보틱 조작 같은 embodied AI 응용에서는 배경과 객체 구성의 정적 일관성과 로봇의 동작이 지시사항과 물리 법칙을 만족해야 하므로, 일반 비디오 생성과는 다른 평가 기준이 필수적이다.
- **Approach**: Agibot-World 데이터셋을 기반으로 10개 작업의 30개 샘플로 구성된 curated 데이터셋을 구축하고, 장면 일관성, 동작 정확성, 의미론적 정렬을 평가하는 multi-dimensional evaluation toolkit을 개발하여 다양한 비디오 생성 모델을 체계적으로 평가한다.

## Achievement

![Figure 4](figures/fig4.webp)

*Figure 4: Evaluation Results of Video Generative Models.*

- **첫 번째 embodied task 전문 벤치마크**: embodied 작업에 특화된 체계적 평가 프레임워크 EWMBench 제안
- **다차원 평가 메트릭**: 기존 벤치마크가 미처 다루지 못한 trajectory dynamics, trajectory plausibility, interaction logic 등 8가지 평가 차원 포함
- **고품질 curated 데이터셋**: 논리적 의존성과 affordance를 반영한 다양한 로보틱 조작 작업 데이터셋 구축
- **기존 모델의 한계 파악**: 주요 text-to-video 생성 모델들의 embodied 작업에서의 성능 한계와 개선 방향 제시

## How

![Figure 2](figures/fig2.webp)

*Figure 2: Overview of the EWMBENCH benchmark design. The framework begins with unified*

- World initialization: 초기 장면 이미지, 언어 명령, 선택적 action trajectory를 입력으로 정의
- Dataset construction: Agibot-World에서 robotic manipulation 작업 선정, 정적 초기 프레임으로 클리핑하여 annotated instruction만 반영되도록 설계
- Multi-dimensional evaluation: (1) Scene Consistency - 배경/객체/embodiment 구조의 정적 요소 유지도, (2) Motion Correctness - trajectory 일관성과 task objective 정렬도, (3) Semantic Alignment - 언어 명령과의 정렬도 및 다양성 평가
- Metric design: video-based MLLMs를 활용한 prompt engineering, voxelized scoring으로 다중 해결책 인정, FID/FVD 같은 기존 메트릭과 새로운 embodied-specific 메트릭 조합

## Originality

- embodied AI 관점에서 비디오 생성 벤치마킹의 새로운 문제 정의: 일반 비디오 생성과의 구조적 차이를 명확히 함
- 로보틱 조작 데이터셋 기반 벤치마크: 실제 로봇 데이터(Agibot-World)를 활용한 최초의 embodied world model 평가 프레임워크
- 포괄적 평가 차원: 기존 벤치마크보다 8가지 평가 차원 모두를 포함하는 완전한 평가 체계 구축
- voxelized scoring과 affordance 기반 작업 설계로 embodied 도메인의 특수성 반영

## Limitation & Further Study

- 현재 로보틱 조작 작업에만 집중되어 있으며, 다른 embodied task(네비게이션, 그래스핑 등)로의 확장 필요
- 30개 샘플의 제한된 데이터셋 규모로 인한 통계적 신뢰성 문제, 더 큰 규모 데이터셋 구축 필요
- 시간적 일관성(temporal consistency)과 동작의 물리적 타당성 검증을 위한 추가 메트릭 개발 가능성
- 후속 연구에서 더 복잡한 멀티-에이전트 시나리오와 장기 수평선 생성(long-horizon generation) 평가 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 embodied AI 분야에서 그간 간과된 EWM 평가의 중요한 갭을 채우는 체계적이고 포괄적인 벤치마크를 제시하며, 실제 로봇 데이터 기반 데이터셋과 다차원 평가 메트릭을 통해 향후 embodied world model 개발에 실질적인 기여를 할 것으로 예상된다.

## Related Papers

- 🏛 기반 연구: [[papers/1356_DreamGen_Unlocking_Generalization_in_Robot_Learning_through/review]] — DreamGen의 video world model이 EWMBench의 Embodied World Models 평가 기준과 연결된다.
- 🔗 후속 연구: [[papers/1385_EO-1_An_Open_Unified_Embodied_Foundation_Model_for_General_R/review]] — EO-1의 unified embodied model이 EWMBench의 평가 대상이 될 수 있다.
- 🔄 다른 접근: [[papers/1452_Learning_Interactive_Real-World_Simulators/review]] — Learning Interactive Real-World Simulators도 embodied world modeling의 품질 평가를 다룬다.
