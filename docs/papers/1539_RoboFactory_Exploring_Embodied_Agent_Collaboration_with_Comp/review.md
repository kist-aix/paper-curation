---
title: "1539_RoboFactory_Exploring_Embodied_Agent_Collaboration_with_Comp"
authors:
  - "Yiran Qin"
  - "Li Kang"
  - "Xiufeng Song"
  - "Zhenfei Yin"
  - "Xiaohong Liu"
date: "2025.03"
doi: ""
arxiv: ""
score: 4.0
essence: "본 논문은 다중 구체화 에이전트(embodied multi-agent) 시스템의 협력을 위해 논리적, 공간적, 시간적 제약을 조합한 compositional constraints 개념을 제시하고, 이를 기반으로 자동화된 데이터 수집 프레임워크 RoboFactory를 개발하여 다중 에이전트 조작 벤치마크를 제공한다."
tags:
  - "cat/Robotic_Foundation_Model_Development"
  - "sub/Robotic_Interaction_Datasets"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Qin et al._2025_RoboFactory Exploring Embodied Agent Collaboration with Compositional Constraints.pdf"
---

# RoboFactory: Exploring Embodied Agent Collaboration with Compositional Constraints

> **저자**: Yiran Qin, Li Kang, Xiufeng Song, Zhenfei Yin, Xiaohong Liu, Xihui Liu, Ruimao Zhang, Lei Bai | **날짜**: 2025-03-20 | **URL**: [https://arxiv.org/abs/2503.16408](https://arxiv.org/abs/2503.16408)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1. When performing the task “Grab the steak and use the camera to photograph it with 4 embodied agents”, collabor*

본 논문은 다중 구체화 에이전트(embodied multi-agent) 시스템의 협력을 위해 논리적, 공간적, 시간적 제약을 조합한 compositional constraints 개념을 제시하고, 이를 기반으로 자동화된 데이터 수집 프레임워크 RoboFactory를 개발하여 다중 에이전트 조작 벤치마크를 제공한다.

## Motivation

- **Known**: 단일 에이전트 로보틱 조작 시스템은 BC, diffusion policy 등 imitation learning 방법으로 발전했고, LLM 기반 데이터 생성도 시도되었다. 그러나 다중 에이전트 협력 시나리오에서의 자동화된 안전한 데이터 생성은 충분히 연구되지 않았다.
- **Gap**: 기존 단일 에이전트 방법을 다중 에이전트에 단순 적용할 수 없으며, 논리적 일관성, 공간 충돌 회피, 시간 효율성 등을 동시에 고려하는 체계적 프레임워크와 벤치마크가 부재하다.
- **Why**: 제조업, 의료 지원 등 현실 응용에서 다중 로봇 협력이 필수적이고, 안전하고 효율적인 다중 에이전트 시스템 설계는 확장 가능한 로보틱 자동화의 핵심이다.
- **Approach**: LLM 기반 RoboBrain이 global task를 compositional constraints(논리, 공간, 시간 제약)로 변환하고, RoboChecker가 이를 실행 가능한 제약 인터페이스로 구현하여 안전하고 효율적인 다중 에이전트 궤적을 생성한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2. Overview of RoboFactory. Given the global task description, prior information, and observations, RoboBrain gen*

- **Compositional Constraints 개념 도입**: 논리적(interaction rules), 공간적(collision avoidance), 시간적(scheduling efficiency) 제약을 체계화하여 다중 에이전트 협력 문제를 구조화
- **RoboFactory 벤치마크 구축**: 첫 번째 embodied multi-agent manipulation 벤치마크로, 자동화된 데이터 수집과 다양한 협력 시나리오 제공
- **다중 에이전트 Imitation Learning 평가**: diffusion policy 기반 다중 에이전트 시스템의 아키텍처 및 학습 전략 탐색으로 safe and efficient embodied multi-agent systems 구축 가능성 입증

## How

![Figure 2](figures/fig2.webp)

*Figure 2. Overview of RoboFactory. Given the global task description, prior information, and observations, RoboBrain gen*

- LLM(GPT)을 활용한 RoboBrain이 global task description, prior information, observations로부터 sub-goal 생성 및 textual compositional constraints 출력
- Motion primitives를 호출하여 unconstrained trajectory sequences 생성
- RoboChecker에서 constraint interfaces를 설계하여 logical, spatial, temporal constraints를 실행 가능한 형태로 변환
- Voxelization, spatial constraint enforcement, temporal scheduling 등 구체적 인터페이스 구현
- 생성된 궤적에 대해 imitation learning(BC, diffusion policy 등) 방법 적용 및 다중 에이전트 아키텍처 설계(centralized vs decentralized 등) 비교 평가

## Originality

- **Compositional constraints의 체계화**: 단순한 충돌 회피를 넘어 논리적 consistency, temporal efficiency를 형식화하여 다중 에이전트 협력의 본질을 포착
- **자동화된 안전 데이터 생성 파이프라인**: LLM과 constraint enforcement를 결합하여 원격 조작 없이 대규모 데이터 생성 자동화
- **첫 번째 embodied multi-agent manipulation 벤치마크**: 다중 에이전트 조작의 표준 평가 환경 제공으로 후속 연구 기반 마련

## Limitation & Further Study

- 제안된 compositional constraints가 세 가지 유형으로 제한되며, 더 복잡한 상호작용 시나리오(e.g., 확률적 협력, 적대적 에이전트)에 대한 확장성 미흡
- LLM 기반 RoboBrain의 generalization 성능 평가 부족 — 새로운 task type에 대한 성공률, failure case 분석 필요
- 실제 로봇 하드웨어에서의 검증 부재 — 시뮬레이션 기반 데이터 생성이 실제 환경에서의 domain gap 미해결
- 다중 에이전트 imitation learning의 확장성 분석 부족 — 에이전트 수 증가 시 성능 저하, 계산 복잡도 분석 필요
- 후속 연구: (1) 더 풍부한 constraint 타입 추가 (hierarchical, probabilistic constraints), (2) sim-to-real transfer learning 기법 적용, (3) reinforcement learning과의 결합으로 constraint violation 시 적응적 재계획

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 다중 에이전트 로보틱 협력의 핵심 도전 문제를 compositional constraints로 우아하게 해결하고, 첫 번째 벤치마크를 제공함으로써 다중 에이전트 embodied AI 연구의 중요한 기초를 마련했다. 다만 실제 로봇 검증과 확장성 분석이 추가되면 더욱 강력한 기여가 될 것이다.

## Related Papers

- 🏛 기반 연구: [[papers/1337_Compose_Your_Policies_Improving_Diffusion-based_or_Flow-base/review]] — diffusion/flow 기반 정책 구성 방법론을 바탕으로 농구와 같은 장기 과제에서의 정책 통합을 해결한다.
- 🔄 다른 접근: [[papers/1565_MaskedMimic_Unified_Physics-Based_Character_Control_Through/review]] — 복잡한 전신 제어를 위해 정책 구성과 마스킹 기반 모션 생성이라는 서로 다른 접근법을 사용한다.
- 🔗 후속 연구: [[papers/1439_Harmon_Whole-Body_Motion_Generation_of_Humanoid_Robots_from/review]] — 전신 동작 생성의 기본 원리를 농구라는 특정 스포츠 영역에서의 장기 과제 해결로 확장한다.
