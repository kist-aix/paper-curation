---
title: "1389_ExploRLLM_Guiding_Exploration_in_Reinforcement_Learning_with"
authors:
  - "Runyu Ma"
  - "Jelle Luijkx"
  - "Zlatan Ajanovic"
  - "Jens Kober"
date: "2024.03"
doi: ""
arxiv: ""
score: 4.0
essence: "ExploRLLM은 대규모 언어 모델(LLM)이 생성한 정책 코드로 RL 에이전트의 탐색을 유도하면서, 잔차 RL 에이전트가 FM의 물리적 이해 부족을 보완하는 방식으로 로봇 조작 작업의 샘플 효율성과 수렴성을 개선한다."
tags:
  - "cat/Task-Oriented_Skill_Acquisition"
  - "sub/Foundation_Model_Agents"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ma et al._2024_ExploRLLM Guiding Exploration in Reinforcement Learning with Large Language Models.pdf"
---

# ExploRLLM: Guiding Exploration in Reinforcement Learning with Large Language Models

> **저자**: Runyu Ma, Jelle Luijkx, Zlatan Ajanovic, Jens Kober | **날짜**: 2024-03-14 | **URL**: [https://arxiv.org/abs/2403.09583](https://arxiv.org/abs/2403.09583)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1: Graphical overview of ExploRLLM.*

ExploRLLM은 대규모 언어 모델(LLM)이 생성한 정책 코드로 RL 에이전트의 탐색을 유도하면서, 잔차 RL 에이전트가 FM의 물리적 이해 부족을 보완하는 방식으로 로봇 조작 작업의 샘플 효율성과 수렴성을 개선한다.

## Motivation

- **Known**: Foundation Model(FM)은 zero-shot 및 few-shot 설정에서 우수한 성능을 보이지만 물리적, 공간적 이해가 제한적이며, RL은 큰 관측 및 행동 공간에서 샘플 효율성과 수렴이 어렵다는 문제가 알려져 있다.
- **Gap**: FM과 RL의 장점을 효과적으로 결합하되, FM의 불완전한 예측을 RL의 학습 메커니즘으로 보완하면서 동시에 RL의 탐색을 효율화할 수 있는 통합 방법이 부족하다.
- **Why**: 로봇 조작 작업에서 샘플 효율성과 수렴 안정성 향상은 실제 로봇 학습의 실용성과 비용 효율성에 직결되며, FM과 RL의 결합은 이를 달성할 수 있는 유망한 접근법이다.
- **Approach**: ExploRLLM은 LLM/VLM을 통해 관측 공간(object-centric 표현)과 행동 공간(residual action)을 축소하고, LLM 기반 탐색 전략으로 RL 에이전트가 의미 있는 행동 영역을 탐색하도록 유도하며, 잔차 RL 에이전트가 실제 환경에서의 미세한 조정을 학습한다.

## Achievement

![Figure 4](figures/fig4.webp)

*Fig. 4: Training curves for varying exploration rates in SH and LH tasks. ExploRLLM outperforms the exploration policies*

- **LLM 기반 탐색 전략**: 계층적 언어 모델 프로그램(high-level과 low-level 정책)을 생성하여 ϵ-greedy 기반 탐색을 확장하고 의미 있는 상태-행동 쌍 수집을 가속화
- **관측/행동 공간 축소**: VLM의 affordance 인식을 통해 object-centric observation과 residual action space로 변환하여 RL의 탐색 공간 차원 축소
- **성능 개선**: 테이블탑 조작 작업에서 FM 단독 정책 및 RL 베이스라인 모두를 초과하는 성능 달성
- **Zero-shot Sim-to-Real 전이**: 추가 학습 없이 시뮬레이션에서 학습한 정책이 실제 로봇에 성공적으로 전이

## How

![Figure 2](figures/fig2.webp)

*Fig. 2: Implementation structure of ExploRLLM for tabletop manipulation, combining the strengths of RL and FMs.*

- LLM을 사용하여 자연언어 명령을 미리 정의된 템플릿으로 해석하고 객체 카테고리 강조
- VLM을 통해 이미지에서 관련 객체의 bounding box 추출 및 위치 정보 Xt와 image patches Mt 획득
- 관측 공간을 {interpreted command, object positions, image crops, gripper state}로 구성
- 행동 공간을 {primitive index k, object index i, residual position xr}로 정의하여 residual action ã_t = (k_t, i_t, x_t^r) 형성
- Algorithm 1의 LLM 기반 탐색 정책 πEXP 적용: ϵ 확률로 LLM이 생성한 high-level 및 low-level 정책을 순차 실행, 1-ϵ 확률로 RL 정책 πRL 선택
- Off-policy RL 알고리즘(예: SAC)을 사용하여 잔차 행동 공간에서 정책 학습

## Originality

- FM 기반 행동을 단순한 보상 신호 또는 정규화 대상이 아닌 **탐색 단계**로 활용하는 새로운 관점
- 계층적 언어 모델 프로그램을 통한 **구조화된 LLM 기반 탐색** 도입으로 ϵ-greedy 전략의 한계 극복
- Object-centric 및 residual action space로의 **자동화된 공간 축소** 메커니즘 제안
- FM의 affordance 인식과 RL의 적응적 학습을 통한 **상보적 강화** 접근법

## Limitation & Further Study

- 테이블탑 조작 작업으로 평가 범위가 제한적이며, 더 복잡한 고차원 작업에 대한 확장성 검증 필요
- LLM의 정확성 및 신뢰성이 탐색 효율성에 미치는 영향에 대한 상세 분석 부재
- ϵ(탐색률) 파라미터의 최적화 방법과 작업별 민감도에 대한 심화 연구 필요
- 실제 로봇 실험이 제한적이므로 다양한 로봇 플랫폼 및 환경에서의 일반화 가능성 검증 필요
- VLM의 object detection 오류에 대한 robustness 및 완화 전략 추가 개발 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: ExploRLLM은 FM과 RL의 장점을 효과적으로 결합하여 로봇 조작의 샘플 효율성을 크게 개선하는 실용적인 방법을 제시하며, 특히 LLM 기반 탐색 전략의 혁신성과 실제 로봇에서의 zero-shot 전이 성공은 높은 가치를 가진다. 다만 평가 범위 확대와 일반화 가능성 검증이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/1418_Guiding_Pretraining_in_Reinforcement_Learning_with_Large_Lan/review]] — ExploRLLM과 ELLM 모두 LLM을 RL 탐색에 활용하지만, 정책 코드 생성 vs 목표 기반 안내라는 서로 다른 접근 방식을 사용한다
- 🔗 후속 연구: [[papers/1416_Grounding_Large_Language_Models_in_Interactive_Environments/review]] — GLAM의 LLM 기반 interactive learning이 ExploRLLM의 LLM 가이드 탐색을 온라인 학습 환경으로 확장한 구현체로 볼 수 있다
- 🏛 기반 연구: [[papers/1410_GR-3_Technical_Report/review]] — GR-3의 대규모 VLA 모델이 ExploRLLM의 LLM-RL 통합 방법론을 foundation model 수준에서 구현할 수 있는 기반을 제공한다
- 🏛 기반 연구: [[papers/1416_Grounding_Large_Language_Models_in_Interactive_Environments/review]] — GLAM의 LLM 기반 interactive environment 학습이 ExploRLLM의 LLM 가이드 탐색을 온라인 강화학습 환경으로 확장하는 기반 방법론을 제공한다
- 🔄 다른 접근: [[papers/1418_Guiding_Pretraining_in_Reinforcement_Learning_with_Large_Lan/review]] — ELLM과 ExploRLLM 모두 LLM을 RL 탐색에 활용하지만, 목표 기반 상식 안내 vs 정책 코드 생성이라는 서로 다른 메커니즘을 사용한다
