---
title: "1368_DiWA_Diffusion_Policy_Adaptation_with_World_Models"
authors:
  - "Akshay L Chandra"
  - "Iman Nematollahi"
  - "Chenguang Huang"
  - "Tim Welschehold"
  - "Wolfram Burgard"
date: "2025.08"
doi: ""
arxiv: ""
score: 4.0
essence: "DiWA는 학습된 world model을 활용하여 diffusion 기반 로봇 정책을 오프라인으로 미세조정하는 프레임워크로, RL을 통해 상상 속 롤아웃에서 정책을 개선한다."
tags:
  - "cat/Multimodal_Vision-Language_Policy_Learning"
  - "sub/Diffusion_Policy_Learning"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chandra et al._2025_DiWA Diffusion Policy Adaptation with World Models.pdf"
---

# DiWA: Diffusion Policy Adaptation with World Models

> **저자**: Akshay L Chandra, Iman Nematollahi, Chenguang Huang, Tim Welschehold, Wolfram Burgard, Abhinav Valada | **날짜**: 2025-08-05 | **URL**: [https://arxiv.org/abs/2508.03645](https://arxiv.org/abs/2508.03645)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: (a) Standard diffusion policies trained via imitation learning are limited by offline data. (b) DPPO [17]*

DiWA는 학습된 world model을 활용하여 diffusion 기반 로봇 정책을 오프라인으로 미세조정하는 프레임워크로, RL을 통해 상상 속 롤아웃에서 정책을 개선한다.

## Motivation

- **Known**: Diffusion policy는 모방학습에서 안정성이 우수하지만 분포 이동에 취약하며, DPPO는 온라인 PPO를 통해 미세조정할 수 있지만 수백만 번의 환경 상호작용이 필요하다.
- **Gap**: 현재 diffusion policy의 미세조정 방법들은 온라인 환경 상호작용에 크게 의존하여 실제 로봇에서 비효율적이고 안전 문제가 있다.
- **Why**: 로봇 학습에서 실제 환경 상호작용은 비용이 크고 시간이 오래 걸리며 위험하므로, 오프라인에서 효율적으로 정책을 개선하는 방법이 실무적으로 중요하다.
- **Approach**: 데이터 효율성이 높은 world model을 오프라인 play 데이터로 학습한 후, 이를 안전한 시뮬레이터로 사용하여 diffusion policy를 오프라인 RL로 미세조정한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: (a) Standard diffusion policies trained via imitation learning are limited by offline data. (b) DPPO [17]*

- **오프라인 Diffusion Policy 미세조정**: Dream Diffusion MDP를 공식화하여 실제 또는 시뮬레이션 환경과의 상호작용 없이 diffusion policy를 완전히 오프라인으로 미세조정하는 최초의 프레임워크 제시
- **샘플 효율성 향상**: CALVIN 벤치마크에서 수십만 개의 오프라인 play 상호작용으로 학습한 world model만으로 모형 없는 기준선 대비 수 배 이상 적은 물리적 상호작용으로 성능 개선
- **제로샷 실제 환경 배포**: World model로 완전히 미세조정된 diffusion 정책이 추가 물리적 상호작용 없이 실제 로봇에 배포 가능함을 입증

## How

![Figure 2](figures/fig2.webp)

*Figure 2: DiWA framework: (1) A world model is trained on unstructured robot play data to learn latent dynamics.*

- Unstructured play 데이터로 task-agnostic world model을 학습하고 고정
- Expert demonstration으로 사전학습된 diffusion policy를 초기화
- World model에서 생성된 latent space 상상 롤아웃을 통해 on-policy RL(PPO) 적용
- Dream Diffusion MDP를 정의하여 denoising 과정의 각 단계를 환경 MDP의 일부로 모델링
- Reward signal을 통해 diffusion policy의 행동 분포를 개선하도록 학습

## Originality

- World model을 활용한 diffusion policy 미세조정이 처음 시도된 방법
- DPPO의 온라인 RL 의존성을 제거하고 완전 오프라인 학습으로 전환한 혁신적 접근
- World model을 frozen 시킨 task-agnostic 패러다임으로 다중 정책 미세조정에 재사용 가능
- 실제 로봇 play 데이터로 학습한 world model이 실제 환경 배포에 직접 적용 가능함을 최초 입증

## Limitation & Further Study

- World model의 누적 오차가 장기간 상상 롤아웃에서 문제가 될 수 있으며, 이에 대한 상세한 분석 부재
- CALVIN 벤치마크의 제한된 조작 작업 범위에서만 평가되어 더 복잡한 실제 환경에서의 일반화 가능성 미흡
- World model 학습을 위한 충분한 play 데이터 획득의 현실적 어려움에 대한 논의 부재
- Reward function 설계의 의존성과 reward 신호 오류가 정책 학습에 미치는 영향에 대한 연구 필요
- 다양한 로봇 플랫폼과 환경에서의 확장성 검증 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: DiWA는 world model을 활용한 offlineRL로 diffusion policy 미세조정의 샘플 효율성을 획기적으로 개선한 혁신적 연구로, 실제 로봇 학습의 실무적 도전 과제를 해결하는 의미 있는 기여이다.

## Related Papers

- 🔄 다른 접근: [[papers/1530_Learning_Humanoid_Navigation_from_Human_Data/review]] — 두 논문 모두 egocentric 시점에서의 시연 생성을 다루지만, 인간 보행 데이터 vs 조작 데이터라는 서로 다른 도메인에 집중함
