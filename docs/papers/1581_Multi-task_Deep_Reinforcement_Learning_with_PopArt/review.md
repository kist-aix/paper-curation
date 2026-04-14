---
title: "1581_Multi-task_Deep_Reinforcement_Learning_with_PopArt"
authors:
  - "Matteo Hessel"
  - "Hubert Soyer"
  - "Lasse Espeholt"
  - "Wojciech Czarnecki"
  - "Simon Schmitt"
date: "2018.09"
doi: ""
arxiv: ""
score: 4.0
essence: "Multi-task 심화강화학습에서 PopArt 정규화를 통해 서로 다른 보상 규모를 가진 작업들의 학습 영향도를 균등하게 조정하여, 단일 에이전트가 57개 Atari 게임에서 인간 성능을 초과하도록 달성한 연구이다."
tags:
  - "cat/Task-Oriented_Skill_Acquisition"
  - "sub/Task_Learning_Benchmarks"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Hessel et al._2018_Multi-task Deep Reinforcement Learning with PopArt.pdf"
---

# Multi-task Deep Reinforcement Learning with PopArt

> **저자**: Matteo Hessel, Hubert Soyer, Lasse Espeholt, Wojciech Czarnecki, Simon Schmitt, Hado van Hasselt | **날짜**: 2018-09-12 | **URL**: [https://arxiv.org/abs/1809.04474](https://arxiv.org/abs/1809.04474)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: Atari-57 (unclipped): Median human normalised*

Multi-task 심화강화학습에서 PopArt 정규화를 통해 서로 다른 보상 규모를 가진 작업들의 학습 영향도를 균등하게 조정하여, 단일 에이전트가 57개 Atari 게임에서 인간 성능을 초과하도록 달성한 연구이다.

## Motivation

- **Known**: 심화강화학습은 단일 작업에서 인간 성능을 초과하는 성과를 거두었으나, 대부분 각 작업마다 독립적으로 학습된 에이전트를 요구한다. IMPALA 같은 병렬 multi-task 학습 알고리즘이 존재하지만 여전히 인간 수준의 성능에 미치지 못한다.
- **Gap**: Multi-task 학습에서 보상 규모와 희소성의 차이로 인해 특정 작업이 과도하게 학습 동역학에 영향을 미쳐 일반화 성능이 저하되는 문제가 존재한다. 보상 클리핑도 이 문제를 완전히 해결하지 못한다.
- **Why**: 단일 정책이 다양한 작업을 동시에 해결할 수 있는 일반화 에이전트는 transfer learning과 실제 응용에서 매우 중요하며, 이는 강화학습의 장기적 실용성을 결정하는 핵심 문제이다.
- **Approach**: PopArt 정규화를 actor-critic 업데이트에 적용하여 보상 규모, 희소성, 에이전트 역량에 무관한 scale-invariant 업데이트를 도출한다. 이를 통해 모든 작업이 학습 동역학에 균등한 영향을 미치도록 한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: Atari-57 (unclipped): Median human normalised*

- **Atari-57 벤치마크**: 단일 에이전트가 110% 중앙값 정규화 점수 달성, 최초로 multi-task 도메인에서 인간 중앙값 성능 초과
- **DeepMind Lab-30 벤치마크**: 72.8% 평균 상한선 인간 정규화 점수 달성, 이전 SOTA(59.7%)를 크게 상향
- **단일 정책**: 57개 게임 모두에서 작동하는 하나의 가중치 세트로 통합된 정책 학습 성공

## How


- PopArt 정규화를 적용하여 value function 업데이트를 출력 보정(output adaptation)하게 설계
- IMPALA 아키텍처의 분산 actor-learner 구조를 유지하면서 정규화 통계를 동적으로 학습
- 중요도 표본추출(importance sampling) 보정을 활용한 off-policy 조정으로 delayed policy 문제 해결
- Actor-critic 프레임워크에서 REINFORCE 스타일의 정책 그래디언트와 bootstrapped multi-step 리턴 사용
- 테스트 시간에는 작업 인덱스를 조건으로 사용하지 않아 task-agnostic 정책 평가

## Originality

- PopArt을 multi-task RL에 처음 적용하여 작업 간 보상 규모 차이 문제에 대한 원칙적 해결책 제시
- 보상 클리핑의 한계를 명확히 분석하고, 비정상성 보상 동역학에 동적으로 대응하는 정규화 기법 도입
- Parallel multi-task 학습에서 단순한 휴리스틱이 아닌 수학적으로 정당화된 scale-invariant 업데이트 메커니즘 개발

## Limitation & Further Study

- PopArt이 정규화 통계 학습에 필요한 초기 데이터 수집 기간에 대한 분석 미흡
- 다양한 작업 유형(sparse reward, dense reward 등)에 대한 세부 ablation study 부족
- 테스트 시간에 task-agnostic 정책을 사용하는 것이 성능 상한을 제한할 가능성에 대한 검토 필요
- 후속 연구로 다른 정규화 기법(예: layer normalization, group normalization)과의 비교 분석 필요
- 더 복잡한 환경(robotic control, 실제 3D 시뮬레이션)에서의 일반화 가능성 검증 요구

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 PopArt 정규화를 활용하여 multi-task 심화강화학습의 오래되고 실질적인 문제를 우아하게 해결하였으며, 최초로 단일 정책이 다양한 작업에서 인간 수준 성능을 달성하도록 함으로써 강화학습의 일반화 능력 발전에 중요한 기여를 했다.

## Related Papers

- 🏛 기반 연구: [[papers/1621_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Ro/review]] — 다중 작업 학습에서 PopArt 정규화의 보상 규모 조정 방법론이 VLABench의 100개 과제 평가에서 성능 표준화의 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/1472_Mastering_Diverse_Domains_through_World_Models/review]] — PopArt를 활용한 다중 작업 학습 방법론을 world model 기반 다양한 도메인 마스터링에 적용하여 더 안정적인 학습을 가능하게 한다.
- 🔄 다른 접근: [[papers/1564_MaskedManipulator_Versatile_Whole-Body_Manipulation/review]] — 다중 작업 학습에서 PopArt의 보상 정규화 방식과 MaskedManipulator의 whole-body 조작 방식을 범용성 확보 측면에서 비교할 수 있다.
- 🧪 응용 사례: [[papers/1563_MASH_Cooperative-Heterogeneous_Multi-Agent_Reinforcement_Lea/review]] — 다중 에이전트 강화학습에서 PopArt 정규화를 적용하여 이종 에이전트 간의 학습 성능 차이를 조정하고 협력 효율성을 향상시킬 수 있다.
- 🏛 기반 연구: [[papers/1472_Mastering_Diverse_Domains_through_World_Models/review]] — Multi-task Deep RL의 PopArt 정규화 기법이 DreamerV3의 도메인 간 안정적 학습을 위한 normalization과 balancing 기법에 이론적 기반을 제공한다
- 🧪 응용 사례: [[papers/1621_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Ro/review]] — PopArt의 다중 작업 학습 정규화 방법론을 VLABench의 100개 과제 평가에서 성능 표준화와 공정한 비교를 위해 활용할 수 있다.
- 🔗 후속 연구: [[papers/1629_Whom_to_Trust_Elective_Learning_for_Distributed_Gaussian_Pro/review]] — 다중 작업 심층 강화학습이 Pri-GP의 분산 학습을 여러 작업으로 확장할 수 있는 방법론적 확장을 제공합니다.
