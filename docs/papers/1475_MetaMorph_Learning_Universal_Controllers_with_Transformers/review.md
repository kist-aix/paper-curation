---
title: "1475_MetaMorph_Learning_Universal_Controllers_with_Transformers"
authors:
  - "Agrim Gupta"
  - "Linxi Fan"
  - "Surya Ganguli"
  - "Li Fei-Fei"
date: "2022.03"
doi: ""
arxiv: ""
score: 4.0
essence: "Transformer 기반의 MetaMorph을 제안하여 모듈식 로봇 설계 공간에서 다양한 로봇 형태에 대해 일반화 가능한 범용 제어기를 학습한다. 로봇의 형태정보를 Transformer의 조건화 모달리티로 취급하여 조합적 일반화와 제로샷 일반화를 달성한다."
tags:
  - "cat/Robotic_Foundation_Model_Development"
  - "sub/Robot_Foundation_Models"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Gupta et al._2022_MetaMorph Learning Universal Controllers with Transformers.pdf"
---

# MetaMorph: Learning Universal Controllers with Transformers

> **저자**: Agrim Gupta, Linxi Fan, Surya Ganguli, Li Fei-Fei | **날짜**: 2022-03-22 | **URL**: [https://arxiv.org/abs/2203.11931](https://arxiv.org/abs/2203.11931)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: MetaMorph. We ﬁrst process an arbitrary robot by creating a 1D sequence of tokens*

Transformer 기반의 MetaMorph을 제안하여 모듈식 로봇 설계 공간에서 다양한 로봇 형태에 대해 일반화 가능한 범용 제어기를 학습한다. 로봇의 형태정보를 Transformer의 조건화 모달리티로 취급하여 조합적 일반화와 제로샷 일반화를 달성한다.

## Motivation

- **Known**: Vision, NLP, Audio 분야에서는 대규모 사전학습 후 태스크 특화 미세조정으로 큰 성공을 거두었다. 로보틱스에서는 전통적으로 단일 로봇을 단일 태스크에 대해 학습하는 패러다임이 지배적이다.
- **Gap**: 모듈식 로봇 설계 공간에서 지수적으로 많은 형태의 로봇이 가능하지만, 각 새로운 설계에 대해 제어기를 훈련하는 것은 비현실적이다. 기존 연구는 단일 또는 적은 수(2-3개)의 로봇 변형만 다루었고, 높은 제어복잡도(15-20 DoFs)의 다양한 형태를 학습하는 범용 제어기에 대한 연구는 부족하다.
- **Why**: 모듈식 로봇 시스템이 실제 적용되려면 새로운 형태에 대한 빠른 배포와 하드웨어 고장 시 견고성이 필요하며, 범용 제어기는 로봇 공학의 '1 로봇 1 태스크' 패러다임을 타파할 수 있다.
- **Approach**: Transformer 아키텍처를 사용하여 로봇 모듈의 proprioceptive 정보와 형태정보를 결합한 토큰 시퀀스를 입력으로 받는다. 대규모 사전학습과 동적 재생 버퍼 균형화(dynamic replay buffer balancing)를 통해 다양한 로봇 형태에서의 학습을 최적화한다.

## Achievement

![Figure 4](figures/fig4.webp)

*Figure 4: Joint pre-training of modular robots. Mean reward progression of 100 robots from the*

- **범용 제어기 학습**: 고제어복잡도(15-20 DoFs)의 UNIMAL 설계 공간에서 수백 개의 다양한 로봇 형태를 단일 정책으로 제어 가능
- **제로샷 일반화**: 미학습 dynamics 변동(관절 감쇠, 질량), kinematics 변동(자유도, 형태 매개변수)에 대해 일반화 가능
- **표본 효율적 전이**: 사전학습된 정책이 새로운 로봇 형태와 태스크에 대해 빠른 적응 가능
- **Motor synergies 발견**: Attention mask 분석을 통해 신경생물학의 motor synergies 개념이 Transformer 제어기에서 자연스럽게 출현함을 확인

## How

![Figure 2](figures/fig2.webp)

*Figure 2: MetaMorph. We ﬁrst process an arbitrary robot by creating a 1D sequence of tokens*

- UNIMAL 설계 공간을 사용하여 구 및 원통 모듈의 조합으로 로봇 형태 표현
- 각 로봇의 kinematic tree를 1D 토큰 시퀀스로 변환하며, 각 토큰은 해당 모듈의 proprioceptive 정보(관절 각도, 속도)와 형태 매개변수(길이, 반지름, 밀도)를 포함
- Transformer 정책 네트워크에 모든 로봇 형태의 경험을 함께 학습(joint pre-training)
- Dynamic replay buffer balancing으로 학습이 느린 로봇 형태의 샘플 수집 비율을 동적으로 조정
- 다양한 로봇 형태에 대해 평면 이동, 불규칙 지형 이동, 모바일 조작 등 3D 로코모션 태스크에서 평가

## Originality

- 로봇 형태를 Transformer의 조건화 모달리티로 취급하는 새로운 관점 제시
- 기존 GNN 기반 방식과 달리, 명시적인 graph inductive bias 없이 순수 Transformer으로 형태 일반화 달성
- Dynamic replay buffer balancing 기법으로 다양한 학습 속도를 가진 로봇들의 공동 학습 문제 해결
- 높은 제어복잡도(15-20 DoFs)와 다양성을 가진 로봇 설계 공간에서의 범용 제어기 학습 시도
- 학습된 정책의 attention mechanism 분석을 통해 생물학적 motor synergies와의 연결고리 발견

## Limitation & Further Study

- UNIMAL 설계 공간에만 국한된 평가이며, 다른 모듈식 로봇 설계 공간(예: 자가 재구성 로봇)으로의 일반화 가능성 미검증
- 시뮬레이션 기반 실험만 수행되었으며, 실제 로봇 하드웨어에 대한 sim-to-real 전이 검증 부재
- 제로샷 일반화는 UNIMAL 공간 내의 형태 변동에만 한정되며, 완전히 새로운 로봇 구조(예: 비-tree 형태)로의 확장성 불명확
- 사전학습 규모와 계산비용에 대한 상세 분석 부족
- **후속 연구**: 실제 로봇 시스템에서의 검증, 더 복잡한 모듈식 설계 공간으로의 확장, 강화학습의 표본 비효율성 측면에서의 개선

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 로봇 공학에서 Transformer 기반 범용 제어기 학습의 새로운 패러다임을 제시하며, 높은 제어복잡도의 다양한 로봇 형태에 대한 제로샷 일반화를 달성했다. 모듈식 로봇 시스템의 실용화를 위한 중요한 기여이나, 실제 하드웨어 검증과 다른 설계 공간으로의 일반화가 후속과제이다.

## Related Papers

- 🏛 기반 연구: [[papers/1267_AMP_Adversarial_Motion_Priors_for_Stylized_Physics-Based_Cha/review]] — Adversarial Motion Prior의 물리 기반 캐릭터 제어가 Transformer 기반 범용 제어기의 기반 기술을 제공한다.
- 🔄 다른 접근: [[papers/1562_Scaling_Cross-Embodied_Learning_One_Policy_for_Manipulation/review]] — 다양한 로봇 형태에 대한 범용 정책 학습에서 Transformer와 cross-embodied learning의 서로 다른 접근법을 보여준다.
- 🔗 후속 연구: [[papers/1296_Bridging_the_Sim-to-Real_Gap_for_Athletic_Loco-Manipulation/review]] — 모듈식 로봇에서 다양한 형태로의 일반화와 로봇 간 통합 표준의 확장된 개념이 연결된다.
