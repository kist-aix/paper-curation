---
title: "1416_Grounding_Large_Language_Models_in_Interactive_Environments"
authors:
  - "Thomas Carta"
  - "Clément Romac"
  - "Thomas Wolf"
  - "Sylvain Lamprier"
  - "Olivier Sigaud"
date: "2023.02"
doi: ""
arxiv: ""
score: 4.0
essence: "본 논문은 Large Language Model(LLM)을 대화형 환경에서 agent policy로 사용하며 online Reinforcement Learning으로 점진적으로 업데이트하여 functional grounding을 달성하는 GLAM 방법을 제안한다. 텍스트 기반 BabyAI 환경에서 LLM의 표본 효율성, 일반화 능력, online learning의 영향을 실증적으로 검증한다."
tags:
  - "cat/Task-Oriented_Skill_Acquisition"
  - "sub/Task_Learning_Benchmarks"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Carta et al._2023_Grounding Large Language Models in Interactive Environments with Online Reinforcement Learning.pdf"
---

# Grounding Large Language Models in Interactive Environments with Online Reinforcement Learning

> **저자**: Thomas Carta, Clément Romac, Thomas Wolf, Sylvain Lamprier, Olivier Sigaud, Pierre-Yves Oudeyer | **날짜**: 2023-02-06 | **URL**: [https://arxiv.org/abs/2302.02662](https://arxiv.org/abs/2302.02662)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: The GLAM method: we use an LLM as agent policy in an interactive textual RL*

본 논문은 Large Language Model(LLM)을 대화형 환경에서 agent policy로 사용하며 online Reinforcement Learning으로 점진적으로 업데이트하여 functional grounding을 달성하는 GLAM 방법을 제안한다. 텍스트 기반 BabyAI 환경에서 LLM의 표본 효율성, 일반화 능력, online learning의 영향을 실증적으로 검증한다.

## Motivation

- **Known**: 최근 LLM은 세계의 물리적 규칙에 대한 추상적 지식을 획득하여 의사결정 문제 해결에 활용되고 있다. 그러나 LLM의 내부 지식과 실제 환경 간의 정렬 부족으로 인해 functional competence가 제한된다.
- **Gap**: LLM이 대화형 환경과 상호작용하면서 점진적으로 지식을 grounding하고 업데이트할 수 있는지, 그리고 online RL을 통한 functional grounding의 실증적 효과가 규명되지 않았다.
- **Why**: LLM의 사전학습된 지식을 활용하여 sample efficient한 RL learning을 구현하고 동시에 환경과의 상호작용을 통해 실제 작동 능력(functional competence)을 확보할 수 있다면 embodied AI와 로봇제어 등 실제 응용에서 매우 중요하다.
- **Approach**: LLM을 agent policy로 사용하여 각 action의 조건부 확률을 계산하고 PPO(Proximal Policy Optimization)를 통해 환경의 reward signal로 LLM을 fine-tuning한다. 이를 위해 BabyAI를 텍스트 기반 환경으로 변환한 BabyAI-Text를 설계하여 실험한다.

## Achievement


- **표본 효율성 향상**: LLM 기반 policy가 작은 모델이나 scratch에서 학습하는 baseline에 비해 spatial/navigation 과제에서 월등히 빠른 학습 속도를 보임
- **객체 변화에 대한 일반화**: 학습된 LLM agent가 훈련 과정에서 보지 못한 새로운 객체에 대해 강한 일반화 성능을 달성
- **새로운 과제로의 제로샷 일반화**: 특정 조건에서 훈련되지 않은 새로운 spatial/navigation 과제로의 일반화 가능성을 실증
- **Online learning의 효과 입증**: 오프라인 Behavioral Cloning보다 online PPO 학습이 더 나은 functional grounding을 달성함을 확인
- **도구 공개**: RL 연구자들이 LLM을 대규모로 활용하도록 지원하는 Lamorel 라이브러리 개발 및 공개

## How

![Figure 1](figures/fig1.webp)

*Figure 1: The GLAM method: we use an LLM as agent policy in an interactive textual RL*

- BabyAI 플랫폼을 텍스트 기반 환경(BabyAI-Text)으로 변환하여 시각 인식의 복잡성을 배제하고 순수 텍스트 관찰/행동만으로 spatial reasoning 능력을 평가
- FLAN-T5의 encoder를 이용하여 goal description과 observation을 포함한 prompt에서 각 가능한 action 토큰의 조건부 확률을 계산
- 계산된 action 확률에 softmax를 적용하여 policy distribution을 생성하고 이로부터 action을 샘플링
- 환경으로부터 받은 reward signal을 이용하여 PPO 알고리즘으로 LLM과 value head를 동시에 fine-tuning
- 다양한 LLM 크기와 아키텍처(FLAN-T5 variants) 변형에 대한 ablation study를 수행하여 설계 선택 검증

## Originality

- LLM을 단순 planner가 아닌 **직접적인 agent policy**로 사용하면서 online RL로 functional grounding하는 첫 번째 체계적 연구
- 텍스트 기반 대화형 환경에서 LLM의 sample efficiency, 일반화, online learning 효과를 동시에 검증하는 포괄적 실험 설계
- 기존 BabyAI를 텍스트 기반으로 변환하여 spatial reasoning의 다양한 측면을 독립적으로 분석 가능하도록 한 환경 설계
- RL 커뮤니티를 위해 LLM 추론 최적화와 대규모 배치 처리를 지원하는 Lamorel 라이브러리 개발

## Limitation & Further Study

- 텍스트 기반 환경으로 제한되어 있으며, 로봇제어나 시각 기반 과제로의 확장 가능성이 명확하지 않음
- 제한된 action space(기본 navigation 명령)를 사용하여 더 복잡한 문제 영역으로의 확장성 검증 필요
- Online RL 학습 중 LLM 전체 parameter를 업데이트하는 계산 비용이 높으며, parameter-efficient fine-tuning(LoRA 등)과의 비교 부재
- 새로운 과제로의 일반화는 task 유사도가 높은 경우로 제한되어 있으며, 구조적으로 전혀 다른 과제로의 전이 능력 검증 필요
- 단일 LLM 계열(FLAN-T5)에 대해서만 실험하였으므로 다른 LLM 아키텍처(GPT-style 등)의 효과 비교 부재
- **후속 연구 방향**: (1) 시각 모달리티를 포함한 multimodal LLM의 functional grounding, (2) 더 복잡하고 대규모 action space 환경에서의 scalability 검증, (3) parameter-efficient adaptation 기법 적용, (4) 분포외(out-of-distribution) task에서의 일반화 능력 강화

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 LLM을 interactive environment에서 online RL로 grounding하는 중요한 첫 시도로서, 체계적인 실험과 명확한 분석을 통해 LLM 기반 policy의 sample efficiency 및 일반화 능력을 입증한다. 다만 텍스트 기반 제한 환경과 단일 모델 계열 평가라는 제약이 있으나, 공개 도구(Lamorel)와 함께 RL 커뮤니티에 기여할 가치 있는 연구이다.

## Related Papers

- 🏛 기반 연구: [[papers/1389_ExploRLLM_Guiding_Exploration_in_Reinforcement_Learning_with/review]] — GLAM의 LLM 기반 interactive environment 학습이 ExploRLLM의 LLM 가이드 탐색을 온라인 강화학습 환경으로 확장하는 기반 방법론을 제공한다
- 🔄 다른 접근: [[papers/1418_Guiding_Pretraining_in_Reinforcement_Learning_with_Large_Lan/review]] — GLAM과 ELLM 모두 LLM을 RL에 통합하지만, 온라인 점진적 업데이트 vs 사전 지식 기반 탐색 안내라는 서로 다른 접근법을 사용한다
- 🔗 후속 연구: [[papers/1477_MineDojo_Building_Open-Ended_Embodied_Agents_with_Internet-S/review]] — MineDojo의 대규모 멀티모달 환경이 GLAM의 LLM-RL 통합 방법론을 더 복잡하고 개방적인 환경에서 검증할 수 있는 확장된 플랫폼을 제공한다
- 🔗 후속 연구: [[papers/1418_Guiding_Pretraining_in_Reinforcement_Learning_with_Large_Lan/review]] — GLAM의 온라인 RL 업데이트가 ELLM의 LLM 가이드 사전훈련을 interactive environment에서 지속적으로 개선하는 방향으로 확장한다
- 🏛 기반 연구: [[papers/1477_MineDojo_Building_Open-Ended_Embodied_Agents_with_Internet-S/review]] — MineDojo의 대규모 개방형 환경이 GLAM의 LLM-RL 통합 방법론을 더 복잡하고 현실적인 환경에서 검증할 수 있는 플랫폼 기반을 제공한다
- 🧪 응용 사례: [[papers/1516_Plan-Seq-Learn_Language_Model_Guided_RL_for_Solving_Long_Hor/review]] — 대화형 환경에서 LLM을 grounding하는 연구로 PSL의 LLM 기반 고수준 계획을 실제 환경에서 적용하는 방법론을 제시한다.
- 🔗 후속 연구: [[papers/1389_ExploRLLM_Guiding_Exploration_in_Reinforcement_Learning_with/review]] — GLAM의 LLM 기반 interactive learning이 ExploRLLM의 LLM 가이드 탐색을 온라인 학습 환경으로 확장한 구현체로 볼 수 있다
