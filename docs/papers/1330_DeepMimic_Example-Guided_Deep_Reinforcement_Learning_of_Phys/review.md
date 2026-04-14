---
title: "1330_DeepMimic_Example-Guided_Deep_Reinforcement_Learning_of_Phys"
authors:
  - "Xue Bin Peng"
  - "Pieter Abbeel"
  - "Sergey Levine"
  - "Michiel van de Panne"
date: "2018.04"
doi: ""
arxiv: ""
score: 4.0
essence: "물리 기반 캐릭터 애니메이션을 위해 reinforcement learning과 모션 캡처 데이터를 결합하여, 참고 모션을 모방하면서도 물리적 현실성과 강건한 제어를 동시에 달성하는 방법을 제시한다."
tags:
  - "cat/Robotic_Foundation_Model_Development"
  - "sub/Character_Motion_Synthesis"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Peng et al._2018_DeepMimic Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills.pdf"
---

# DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills

> **저자**: Xue Bin Peng, Pieter Abbeel, Sergey Levine, Michiel van de Panne | **날짜**: 2018-04-08 | **URL**: [https://arxiv.org/abs/1804.02717](https://arxiv.org/abs/1804.02717)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1. Highly dynamic skills learned by imitating reference motion capture clips using our method, executed by physical*

물리 기반 캐릭터 애니메이션을 위해 reinforcement learning과 모션 캡처 데이터를 결합하여, 참고 모션을 모방하면서도 물리적 현실성과 강건한 제어를 동시에 달성하는 방법을 제시한다.

## Motivation

- **Known**: 물리 기반 캐릭터 제어는 오랫동안 연구되었으나, 수작업으로 설계된 컨트롤러는 일반화 능력이 제한적이고, 깊은 reinforcement learning 방법은 모션 품질이 낮고 부자연스러운 움직임을 생성하는 경향이 있다.
- **Gap**: 기존 deep RL 방법들은 고품질 모션을 생성하지 못하고 인공적 움직임을 보이며, 모션 캡처 데이터를 활용한 기존 접근법들은 복잡성이 높고 회복력 있는 움직임 생성에 제한이 있다.
- **Why**: physics-based character animation에서 모션 품질, 강건성, 상호작용성, 일반화 능력을 동시에 확보하는 것은 영화, 게임, 로봇 제어 등 실제 응용에 필수적이며, 데이터 기반과 학습 기반의 효과적인 결합은 산업적 가치가 크다.
- **Approach**: Motion imitation objective와 task objective를 결합한 reward 함수를 설계하고, 위상 정보(phase-aware policy)를 통합하여 reference motion을 강하게 모방하면서도 perturbation과 환경 변화에 대응할 수 있도록 RL 정책을 학습한다.

## Achievement


- **높은 모션 품질**: 참고 모션을 모방하면서도 Perturbation 없는 상황에서 기준 모션과 거의 구분 불가능한 품질을 달성
- **강건한 회복**: 모션 왜곡이나 외부 간섭에 대해 인공적 엔지니어링 없이 자연스러운 회복 전략을 학습
- **다양한 기술 습득**: Locomotion, acrobatics, martial arts 등 매우 다양한 스킬을 여러 캐릭터(humanoid, Atlas robot, 공룡, 드래곤)에서 학습
- **멀티-스킬 에이전트**: 여러 모션 클립을 통합하여 단일 정책이 다중 스킬을 수행하도록 학습
- **상호작용성**: Motion imitation과 task objective 결합으로 사용자 지정 목표(방향 이동, 공 던지기 등)를 달성하며 동시에 모션 스타일 유지

## How

![Figure 2](figures/fig2.webp)

*Fig. 2. Schematic illustration of the visuomotor policy network. The*

- Phase-aware policy network를 통해 참고 모션의 cyclic 구조를 명시적으로 모델링
- Motion imitation reward를 통해 현재 상태와 참고 모션의 현재 프레임 간 차이를 최소화
- Task reward (예: 목표 위치 도달, 물체 조작)와 imitation reward를 가중 결합
- Reference state initialization: 정책을 훈련할 때 참고 모션의 특정 상태에서 시작하여 highly dynamic 스킬 학습 가능성 증대
- Early termination: 정책이 참고 모션에서 벗어나면 에피소드를 중단하여 샘플 효율성과 학습 안정성 향상
- Multi-clip learning: Max operator 기반 reward, 다중 스킬 정책 학습, value function 기반 클립 시퀀싱의 세 가지 방법으로 다중 모션 클립 통합

## Originality

- Motion capture 데이터를 deep RL의 reward shaping으로 직접 활용하는 간단하면서도 효과적인 프레임워크
- Reference state initialization과 early termination이라는 두 가지 중요 기법이 highly dynamic 스킬 습득에 critical함을 체계적으로 입증
- Phase-aware policy를 통한 cyclic motion의 명시적 모델링으로 고품질 모션 학습 달성
- Multi-clip integration을 위한 세 가지 complementary 방법 제시 (max operator, multi-policy, value function sequencing)

## Limitation & Further Study

- 참고 모션이 제어 불가능한 동역학적 상황에 놓이면 정책 학습이 실패할 수 있으며, 참고 클립의 feasibility에 의존
- Highly dynamic 스킬에서 reference state initialization의 필요성이 높아 수동으로 효과적인 시작 상태를 선택해야 할 수 있음
- Multi-clip 학습에서 각 방법의 trade-off (정책 용량 vs 유연성)가 충분히 분석되지 않음
- 특정 캐릭터 형태(morphology)에 대한 적응 능력이 제한적일 수 있으며, 대규모 형태 변화에 대한 generalization 성능 미흡
- 후속 연구로 meta-learning을 통한 새로운 모션 클립 또는 캐릭터에 대한 빠른 적응, 자동화된 reference state selection, 더욱 정교한 multi-clip coordination 메커니즘 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: DeepMimic은 motion capture 데이터와 reinforcement learning을 효과적으로 결합하여 physics-based character animation의 오랫동안의 난제를 실질적으로 해결한 중요한 연구이다. Reference state initialization과 early termination이라는 간단하지만 효과적인 기법을 통해 높은 모션 품질, 강건성, 다양한 스킬 습득을 동시에 달성하며, 산업과 학계에 즉시 영향을 미칠 수 있는 실질적 가치를 보유하고 있다.

## Related Papers

- 🔗 후속 연구: [[papers/1266_AMOR_Adaptive_Character_Control_through_Multi-Objective_Rein/review]] — example-guided RL의 기초 방법을 adaptive multi-objective learning으로 확장하여 더 유연한 제어를 가능하게 한다
- 🔗 후속 연구: [[papers/1267_AMP_Adversarial_Motion_Priors_for_Stylized_Physics-Based_Cha/review]] — motion capture 기반의 physics-based control을 adversarial motion prior로 발전시켜 더 자연스러운 동작을 생성한다
- 🔄 다른 접근: [[papers/1275_ASE_Large-Scale_Reusable_Adversarial_Skill_Embeddings_for_Ph/review]] — physics-based character control에서 각각 example-guided learning과 adversarial skill embedding이라는 다른 접근법을 제시한다
- 🔄 다른 접근: [[papers/1266_AMOR_Adaptive_Character_Control_through_Multi-Objective_Rein/review]] — physics-based character control에서 모션 캡처 데이터 활용을 각각 다중 목표와 예시 기반 학습으로 접근한다
- 🏛 기반 연구: [[papers/1267_AMP_Adversarial_Motion_Priors_for_Stylized_Physics-Based_Cha/review]] — 모션 캡처 데이터로부터 자연스러운 동작을 생성하는 기초적인 adversarial learning 접근법을 제시한다
- 🔄 다른 접근: [[papers/1444_Hierarchical_Planning_and_Control_for_Box_Loco-Manipulation/review]] — 물리 기반 캐릭터 제어에서 강화학습과 diffusion 모델이라는 서로 다른 접근 방식을 보여준다.
- 🏛 기반 연구: [[papers/1538_Learning_Symmetric_and_Low-energy_Locomotion/review]] — DeepMimic의 physics-based 캐릭터 제어 방법론을 기반으로 동작 캡처 없이도 생물학적으로 타당한 보행을 학습한다.
- 🔗 후속 연구: [[papers/1565_MaskedMimic_Unified_Physics-Based_Character_Control_Through/review]] — DeepMimic의 physics-based character control을 motion inpainting 문제로 통합하여 더 유연한 제어 방법론을 개발한다.
