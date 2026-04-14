---
title: "1472_Mastering_Diverse_Domains_through_World_Models"
authors:
  - "Danijar Hafner"
  - "Jurgis Pasukonis"
  - "Jimmy Ba"
  - "Timothy Lillicrap"
date: "2023.01"
doi: ""
arxiv: ""
score: 4.0
essence: "DreamerV3는 world model을 학습하여 고정된 하이퍼파라미터로 150개 이상의 다양한 도메인에서 전문화된 알고리즘을 능가하는 범용 RL 알고리즘이다. normalization, balancing, transformation 기반의 robustness 기법으로 도메인 간 안정적 학습을 실현한다."
tags:
  - "cat/Task-Oriented_Skill_Acquisition"
  - "sub/Task_Learning_Benchmarks"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Hafner et al._2023_Mastering Diverse Domains through World Models.pdf"
---

# Mastering Diverse Domains through World Models

> **저자**: Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, Timothy Lillicrap | **날짜**: 2023-01-10 | **URL**: [https://arxiv.org/abs/2301.04104](https://arxiv.org/abs/2301.04104)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Benchmark summary. a, Using fixed hyperparameters across all domains, Dreamer*

DreamerV3는 world model을 학습하여 고정된 하이퍼파라미터로 150개 이상의 다양한 도메인에서 전문화된 알고리즘을 능가하는 범용 RL 알고리즘이다. normalization, balancing, transformation 기반의 robustness 기법으로 도메인 간 안정적 학습을 실현한다.

## Motivation

- **Known**: RL 알고리즘은 개발한 작업과 유사한 태스크에는 잘 작동하지만, 새로운 도메인으로 확장 시 상당한 인간의 전문성과 실험이 필요하다. 특히 Minecraft의 diamond 수집 같은 open world 문제는 sparse reward와 long horizon으로 인해 매우 어렵다.
- **Gap**: 기존 RL 알고리즘들은 도메인마다 다른 하이퍼파라미터 튜닝이 필요하고, world model 학습은 여전히 robustness 문제를 해결하지 못했다. 또한 인간 데이터나 curriculum 없이 Minecraft에서 diamond를 수집하는 것은 해결되지 않은 도전 문제였다.
- **Why**: RL을 실무에 광범위하게 적용하려면 새로운 도메인마다 재설정 없이 작동하는 범용 알고리즘이 필수적이다. 이는 RL의 실용성과 적용 범위를 크게 확장할 수 있다.
- **Approach**: world model 기반 actor-critic 구조에서 RSSM으로 환경 표현을 학습하고, symlog 변환, free bits, loss balancing 등의 robustness 기법을 도입하여 도메인 간 일관성을 확보했다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: Benchmark summary. a, Using fixed hyperparameters across all domains, Dreamer*

- **단일 설정으로 다중 도메인 우월성**: 고정된 하이퍼파라미터로 Atari, ProcGen, DMLab, Control Suite, Proprio Control, Visual Control, BSuite 등 150개 이상의 태스크에서 PPO, Rainbow, MuZero 등 전문화된 알고리즘을 능가
- **Minecraft diamond 달성**: 인간 데이터나 curriculum 없이 처음으로 Minecraft에서 diamond를 수집하는 데 성공
- **스케일 일관성**: 모델 크기와 학습 예산 변화에 따라 일관되고 예측 가능한 성능 개선
- **데이터 효율성**: 제한된 환경 상호작용 예산에서도 안정적인 학습 달성

## How

![Figure 3](figures/fig3.webp)

*Figure 3: Training process of Dreamer. The world model encodes sensory inputs into discrete*

- **Recurrent State-Space Model (RSSM)**: encoder로 입력을 discrete 표현으로 변환, sequence model이 representation 예측, dynamics/reward/continue predictor와 decoder로 미래 예측
- **Symlog 변환**: 서로 다른 크기의 신호(보상, 값)를 안정적으로 다루기 위해 동적 범위 압축
- **Free bits**: KL divergence 손실을 최소 1 nat로 제한하여 degenerate solution 방지
- **Loss balancing**: prediction, dynamics, representation 손실의 가중치(βpred=1, βdyn=1, βrep=0.1) 조정으로 도메인 간 일관성 확보
- **Actor-Critic 학습**: world model이 예측한 abstract representation 궤적에서 actor와 critic을 학습
- **멀티스텝 비디오 예측**: 5 프레임 context로 45 프레임을 중간 이미지 없이 예측하여 환경 이해도 검증

## Originality

- **Robustness 기법의 통합 설계**: normalization, balancing, transformation을 조합하여 단일 설정으로 다중 도메인을 처리하는 원칙적 접근
- **Free bits의 창의적 활용**: representation loss의 고정 가중치와 결합하여 환경 복잡도 자동 조절
- **Minecraft 정복**: 사전 데이터 없이 open world 문제를 world model 기반 방법으로 해결한 첫 성과
- **광범위한 실증적 검증**: 150개 이상의 다양한 도메인과 데이터 예산에 대한 체계적 평가

## Limitation & Further Study

- **계산 비용**: world model 학습의 메모리 및 계산 오버헤드가 간단한 알고리즘 대비 높을 수 있음
- **모델 예측 오류 누적**: 장기 imagination 시 model error가 누적될 수 있으며, 이를 완전히 극복했는지 불명확
- **도메인 다양성의 한계**: 아직 다루지 않은 도메인(예: 매우 고차원적 관측, 동적 환경)에서의 일반화 능력 미검증
- **후속 연구 방향**: world model의 uncertainty 추정 개선, 더 장기적 horizon에서의 안정성, 실제 로봇 작업에의 확장 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: DreamerV3는 world model 기반 RL의 robustness 문제를 해결하여 단일 설정으로 다중 도메인을 마스터하는 실질적 성과를 달성했다. 특히 Minecraft diamond 수집은 이 분야의 오랜 미해결 과제를 처음으로 정복한 것으로, RL의 실용적 적용 범위를 크게 확장한 중요한 기여다.

## Related Papers

- 🏛 기반 연구: [[papers/1359_Diffusion_for_World_Modeling_Visual_Details_Matter_in_Atari/review]] — DreamerV3의 world model 기반 범용 RL 알고리즘이 DIAMOND의 diffusion world model 설계에 도메인 간 일반화와 안정적 학습의 이론적 기반을 제공한다
- 🔗 후속 연구: [[papers/1400_GAIA-1_A_Generative_World_Model_for_Autonomous_Driving/review]] — DreamerV3의 범용 world model이 GAIA-1의 자율주행 특화 생성형 모델을 더 다양한 도메인으로 확장할 수 있는 일반화된 접근법을 보여준다
- 🏛 기반 연구: [[papers/1581_Multi-task_Deep_Reinforcement_Learning_with_PopArt/review]] — Multi-task Deep RL의 PopArt 정규화 기법이 DreamerV3의 도메인 간 안정적 학습을 위한 normalization과 balancing 기법에 이론적 기반을 제공한다
- 🔗 후속 연구: [[papers/1400_GAIA-1_A_Generative_World_Model_for_Autonomous_Driving/review]] — DreamerV3의 범용 world model 학습이 GAIA-1의 자율주행 특화 생성형 모델을 더 일반적인 도메인으로 확장한 접근법을 보여준다
- 🔗 후속 연구: [[papers/1359_Diffusion_for_World_Modeling_Visual_Details_Matter_in_Atari/review]] — DreamerV3의 world model 기반 범용 RL이 DIAMOND의 diffusion world model 아이디어를 더 일반적인 도메인으로 확장한 버전이다
- 🔗 후속 연구: [[papers/1581_Multi-task_Deep_Reinforcement_Learning_with_PopArt/review]] — PopArt를 활용한 다중 작업 학습 방법론을 world model 기반 다양한 도메인 마스터링에 적용하여 더 안정적인 학습을 가능하게 한다.
