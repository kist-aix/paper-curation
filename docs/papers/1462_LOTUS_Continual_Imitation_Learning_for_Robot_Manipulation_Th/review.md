---
title: "1462_LOTUS_Continual_Imitation_Learning_for_Robot_Manipulation_Th"
authors:
  - "Weikang Wan"
  - "Yifeng Zhu"
  - "Rutav Shah"
  - "Yuke Zhu"
date: "2023.11"
doi: ""
arxiv: ""
score: 4.0
essence: "LOTUS는 물리 로봇이 인간 시연으로부터 계속 새로운 조작 과제를 학습하도록 하는 지속적 모방 학습 알고리즘으로, open-vocabulary vision model을 이용한 비지도 기술 발견과 메타-컨트롤러 기반의 기술 합성을 통해 시각 기반 조작을 수행한다."
tags:
  - "cat/Task-Oriented_Skill_Acquisition"
  - "sub/Continual_Skill_Learning"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wan et al._2023_LOTUS Continual Imitation Learning for Robot Manipulation Through Unsupervised Skill Discovery.pdf"
---

# LOTUS: Continual Imitation Learning for Robot Manipulation Through Unsupervised Skill Discovery

> **저자**: Weikang Wan, Yifeng Zhu, Rutav Shah, Yuke Zhu | **날짜**: 2023-11-03 | **URL**: [https://arxiv.org/abs/2311.02058](https://arxiv.org/abs/2311.02058)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1: Method Overview. LOTUS is a continual imitation learning*

LOTUS는 물리 로봇이 인간 시연으로부터 계속 새로운 조작 과제를 학습하도록 하는 지속적 모방 학습 알고리즘으로, open-vocabulary vision model을 이용한 비지도 기술 발견과 메타-컨트롤러 기반의 기술 합성을 통해 시각 기반 조작을 수행한다.

## Motivation

- **Known**: 계층적 강화학습 및 모방학습 기반의 기술 발견 방법들이 존재하며, 고정된 기술 집합이나 단일 과제에 초점을 맞춘 방법들이 주를 이룬다.
- **Gap**: 기존 기술 발견 방법들은 고정된 기술 집합을 가정하거나 높은 샘플 복잡도를 요구하며, 시간 경과에 따라 변화하는 데이터 분포를 다루지 못한다.
- **Why**: 로봇이 평생 동안 계속해서 새로운 과제를 효율적으로 학습하고 이전 과제의 성능을 유지하면서 새 과제로의 지식 전이를 달성해야 하는 실제 배포 환경에서 중요하다.
- **Approach**: Open-vocabulary vision model을 사용하여 비분할 시연에서 반복 패턴으로 기술을 추출하고, 증분 기술 클러스터링으로 기존 기술 업데이트와 새 기술 추가를 동적으로 관리하며, 메타-컨트롤러가 기술을 구성하여 새로운 과제를 해결한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Fig. 1: Method Overview. LOTUS is a continual imitation learning*

- **성공률 향상**: 상태 최고 기준 방법 대비 평균 11% 이상의 높은 성공률 달성
- **효과적인 지식 전이**: forward transfer와 backward transfer를 모두 달성하는 기술 기반 접근법 입증
- **실제 로봇 배포**: 시뮬레이션과 물리 로봇 하드웨어에서 체계적으로 검증
- **지속적 기술 발견**: 기술 라이브러리가 새로운 과제를 통해 지속적으로 성장하며 catastrophic forgetting 회피

## How

![Figure 2](figures/fig2.webp)

*Fig. 2: LOTUS consists of two processes: continual skill discovery with open-world perception and hierarchical policy le*

- Open-vocabulary vision model을 활용하여 시연 영상에서 반복되는 패턴을 기술로 추출
- 증분 기술 클러스터링 프로세스로 새 시연 세그먼트가 기존 기술과 유사한지 판단하여 기술 추가 또는 업데이트 결정
- Goal-conditioned visuomotor policy로 각 기술을 모델링하여 원본 이미지에서 동작
- 메타-컨트롤러가 각 시간 스텝에서 기술 인덱스를 선택하여 subgoal 생성
- Base task stage에서 초기 기술 라이브러리 구축 후 lifelong task stage에서 동적으로 기술 라이브러리 확장
- Experience replay를 통한 샘플 효율적 hierarchical behavior cloning 학습

## Originality

- 기존 기술 발견 방법과 달리 시간 변화하는 과제 스트림에서 동적으로 기술을 발견하는 새로운 문제 설정
- Open-vocabulary vision model을 활용한 비지도 기술 추출이 기존의 강화학습 기반 또는 수동 분할 방법과 구별됨
- 증분 기술 클러스터링을 통한 기술 라이브러리의 동적 성장 메커니즘의 혁신성
- 계층적 모방학습 프레임워크에 experience replay를 통합하여 실제 로봇에서의 샘플 효율성 개선

## Limitation & Further Study

- 초기 기술 라이브러리 구축을 위한 base task stage가 필요하며, 초기 설정이 이후 성능에 영향을 미칠 수 있음
- Open-vocabulary vision model의 성능에 의존적이며, 시각적으로 구별하기 어려운 기술들의 발견이 제한될 수 있음
- 메타-컨트롤러가 기술 라이브러리의 크기 증가에 따라 선택 공간이 커져 계산 비용 증가 가능성
- 후속 연구: 더 정교한 기술 유사도 측정 방법 개발, 메타-컨트롤러의 확장성 개선, 다양한 로봇 플랫폼에의 일반화

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: LOTUS는 지속적 모방학습에서 동적 기술 발견과 계층적 합성을 통해 실제 로봇이 효율적으로 평생 학습할 수 있도록 하는 혁신적 접근법으로, 견고한 실험 검증과 11% 이상의 성능 향상을 통해 그 효과성을 입증한다.

## Related Papers

- 🔗 후속 연구: [[papers/1457_LIBERO_Benchmarking_Knowledge_Transfer_for_Lifelong_Robot_Le/review]] — LOTUS의 지속적 모방 학습이 LIBERO의 생애주기 학습 벤치마크에서 제시한 지식 전이 문제를 실제 물리 로봇에서 해결하는 구체적 알고리즘을 제공한다
- 🔄 다른 접근: [[papers/1566_Scaling_Up_and_Distilling_Down_Language-Guided_Robot_Skill_A/review]] — LOTUS와 언어 가이드 스킬 증류 모두 지속적 스킬 학습을 다루지만, 비지도 기술 발견 vs 언어 기반 스킬 전이라는 서로 다른 접근법을 사용한다
- 🔗 후속 연구: [[papers/1321_Bootstrap_Your_Own_Skills_Learning_to_Solve_New_Tasks_with_L/review]] — LOTUS의 메타-컨트롤러 기반 기술 합성이 BOSS의 스킬 체이닝 방법론을 물리적 로봇 환경에서 지속적으로 학습하는 방향으로 확장한다
- 🏛 기반 연구: [[papers/1457_LIBERO_Benchmarking_Knowledge_Transfer_for_Lifelong_Robot_Le/review]] — LIBERO의 선언적/절차적 지식 전이 프레임워크가 LOTUS의 지속적 모방 학습에 필요한 지식 표현과 전이 방법론의 이론적 기반을 제공한다
- 🏛 기반 연구: [[papers/1534_RoboAgent_Generalization_and_Efficiency_in_Robot_Manipulatio/review]] — LOTUS의 연속 모방 학습 프레임워크가 RoboAgent의 12개 스킬 학습에서 지속적 학습 능력의 이론적 기반을 제공한다.
- 🧪 응용 사례: [[papers/1623_Voyager_An_Open-Ended_Embodied_Agent_with_Large_Language_Mod/review]] — LOTUS의 연속 모방 학습 방법론을 Voyager의 평생 학습 스킬 획득에 적용하여 실제 로봇 환경에서의 지속적 기술 발전을 가능하게 한다.
