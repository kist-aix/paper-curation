---
title: "1467_Manipulate-Anything_Automating_Real-World_Robots_using_Visio"
authors:
  - "Jiafei Duan"
  - "Wentao Yuan"
  - "Wilbert Pumacay"
  - "Yi Ru Wang"
  - "Kiana Ehsani"
date: "2024.06"
doi: ""
arxiv: ""
score: 4.0
essence: "Vision-Language Model을 활용하여 실제 로봇 환경에서 특권 정보나 사전 설계된 스킬 없이 자동으로 로봇 조작 시연 데이터를 생성하는 Manipulate-Anything 프레임워크를 제안한다."
tags:
  - "cat/Embodied_Navigation_and_Planning"
  - "sub/Synthetic_Grasping_Datasets"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Duan et al._2024_Manipulate-Anything Automating Real-World Robots using Vision-Language Models.pdf"
---

# Manipulate-Anything: Automating Real-World Robots using Vision-Language Models

> **저자**: Jiafei Duan, Wentao Yuan, Wilbert Pumacay, Yi Ru Wang, Kiana Ehsani, Dieter Fox, Ranjay Krishna | **날짜**: 2024-06-27 | **URL**: [https://arxiv.org/abs/2406.18915](https://arxiv.org/abs/2406.18915)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: Manipulate Anything Framework. The process begins by inputting a scene representation*

Vision-Language Model을 활용하여 실제 로봇 환경에서 특권 정보나 사전 설계된 스킬 없이 자동으로 로봇 조작 시연 데이터를 생성하는 Manipulate-Anything 프레임워크를 제안한다.

## Motivation

- **Known**: RT-1과 Open-X-Embodiment 같은 대규모 로봇 시연 데이터 수집 프로젝트들이 진행되고 있으며, VLM을 활용한 로봇 제어 시스템들이 개발되고 있다.
- **Gap**: 기존 VLM 기반 로봇 제어 방법들은 특권 상태 정보가 필요하거나, 손으로 설계한 스킬에 의존하며, 제한된 객체 인스턴스만 조작할 수 있다는 한계가 있다.
- **Why**: 로봇 학습의 핵심 병목은 데이터의 양, 질, 다양성이며, VLM의 상식적 지식을 활용하면 현실 세계에서 확장 가능한 데이터 생성이 가능하다.
- **Approach**: Manipulate-Anything은 VLM으로 작업을 하위 작업으로 분해하고, 다중 관점 VLM으로 장면을 이해하며, 동작 생성 후 검증 모듈로 오류 복구를 수행하는 모듈식 파이프라인을 설계했다.

## Achievement

![Figure 5](figures/fig5.webp)

*Figure 5: Action Distribution for Generated Data: We compare the action distribution of data*

- **실제 환경 적응성**: 특권 상태 정보 없이 7개의 실제 세계 작업과 14개의 RLBench 시뮬레이션 작업에서 성공적으로 궤적을 생성
- **성능 우위**: VoxPoser, Scaling-up, Code-As-Policies 대비 현저히 우수한 성능을 보이며, 특히 시뮬레이션에서 10/14 작업에서 VoxPoser 초과
- **데이터 질 향상**: 생성된 시연으로 학습한 behavior cloning 정책이 인간 시연 데이터보다 5/12 작업에서 더 우수하고 4개 작업에서 동등한 성능 달성
- **Zero-shot 일반화**: 미처음 본 작업을 zero-shot으로 완수할 수 있으며, 실제 환경에서 38.57%의 작업 평균 성공률 달성

## How

![Figure 2](figures/fig2.webp)

*Figure 2: Manipulate Anything Framework. The process begins by inputting a scene representation*

- VLM을 사용하여 입력 장면 이미지와 작업 지시문으로부터 작업 관련 객체 식별 및 LLM으로 주 작업을 하위 작업으로 분해
- 각 하위 작업에 대해 다중 관점 이미지를 제공하여 VLM의 공간 추론 능력 강화
- Action generation 모듈에서 작업 특화 그래스 포즈 또는 코드 생성
- Sub-task verification 모듈로 각 하위 작업의 성공 여부 검증하고 실패 시 재계획 및 오류 복구 수행
- 성공한 궤적만 필터링하여 downstream policy 학습을 위한 시연 데이터로 사용

## Originality

- 기존 방법들과 달리 특권 정보나 사전 설계된 스킬 없이 임의의 정적 객체를 조작할 수 있는 완전히 자동화된 프레임워크 제시
- 다중 관점 VLM 활용으로 공간 추론 능력 향상 및 검증 기반 오류 복구 메커니즘 도입
- 생성된 데이터가 인간 시연보다 우수한 정책 학습을 가능하게 한다는 놀라운 발견

## Limitation & Further Study

- 실제 환경에서 38.57%의 성공률은 완전한 자동화에는 여전히 부족하며, 특정 유형의 복잡한 작업에서의 성능이 미실명
- VLM의 성능에 크게 의존하므로 VLM의 개선에 따라 성능이 변할 수 있음
- 동적 객체나 상호작용이 복잡한 시나리오에 대한 확장 가능성이 불명확함
- 후속 연구에서는 더 도전적인 다단계 작업, 동적 환경 처리, 현실의 노이즈와 불확실성에 대한 강건성 개선이 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: Manipulate-Anything은 VLM의 상식적 지식을 체계적으로 활용하여 실제 로봇 환경에서 확장 가능한 자동 데이터 생성을 달성한 혁신적인 프레임워크이며, 생성된 데이터가 인간 시연보다 우수한 정책을 학습시킬 수 있다는 놀라운 결과는 로봇 학습의 미래를 큰 변화시킬 수 있는 잠재력을 시사한다.

## Related Papers

- 🔄 다른 접근: [[papers/1452_Learning_Interactive_Real-World_Simulators/review]] — 두 논문 모두 로봇을 위한 시뮬레이션과 데이터 생성을 다루지만, 하나는 VLM 기반 자동화에, 다른 하나는 범용 시뮬레이터에 집중합니다.
- 🏛 기반 연구: [[papers/1315_AutoRT_Embodied_Foundation_Models_for_Large_Scale_Orchestrat/review]] — 대규모 로봇 orchestration 시스템이 VLM을 활용한 자동 조작 데이터 생성의 기반 인프라를 제공합니다.
- 🔗 후속 연구: [[papers/1372_DROID_A_Large-Scale_In-The-Wild_Robot_Manipulation_Dataset/review]] — 대규모 실세계 조작 데이터셋을 VLM 기반 자동 데이터 생성으로 확장하여 더욱 풍부한 학습 데이터를 구축할 수 있습니다.
- 🧪 응용 사례: [[papers/1540_Learning_to_Control_Physically-simulated_3D_Characters_via_G/review]] — 로봇 생성 방법론이 VLM 기반 조작 데이터 자동화에서 다양한 작업과 환경을 생성하는 데 활용됩니다.
- 🔄 다른 접근: [[papers/1399_From_Seeing_to_Doing_Bridging_Reasoning_and_Decision_for_Rob/review]] — Manipulate-Anything도 vision model을 통한 로봇 조작의 일반화를 다룬다.
- 🔄 다른 접근: [[papers/1452_Learning_Interactive_Real-World_Simulators/review]] — 두 논문 모두 로봇 조작을 위한 시뮬레이션과 데이터 생성을 다루지만, 하나는 범용 시뮬레이터에, 다른 하나는 VLM 기반 자동화에 집중합니다.
- 🔗 후속 연구: [[papers/1497_OctoNav_Towards_Generalist_Embodied_Navigation/review]] — INTENTION의 Intuitive Perceptor와 유사하게 Humanoid Locomotion as Next Token Prediction에서 언어 모델 기반 모션 생성 패러다임을 확장하여 구현한다.
