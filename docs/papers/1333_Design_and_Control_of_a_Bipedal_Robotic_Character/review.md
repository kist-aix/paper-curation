---
title: "1333_Design_and_Control_of_a_Bipedal_Robotic_Character"
authors:
  - "Ruben Grandia"
  - "Espen Knoop"
  - "Michael A. Hopkins"
  - "Georg Wiedebach"
  - "Jared Bishop"
date: "2025.01"
doi: ""
arxiv: ""
score: 4.0
essence: "엔터테인먼트 로봇을 위해 예술적 표현성과 동적 이동성을 통합하는 이족 로봇의 설계 및 제어 시스템을 제시하며, reinforcement learning 기반 제어 구조와 실시간 puppeteering 인터페이스를 통해 믿을 수 있는 로봇 캐릭터를 구현한다."
tags:
  - "cat/Humanoid_Teleoperation_and_Interaction"
  - "sub/Socially_Expressive_Robotics"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Grandia et al._2025_Design and Control of a Bipedal Robotic Character.pdf"
---

# Design and Control of a Bipedal Robotic Character

> **저자**: Ruben Grandia, Espen Knoop, Michael A. Hopkins, Georg Wiedebach, Jared Bishop, Steven Pickles, David Müller, Moritz Bächer | **날짜**: 2025-01-09 | **URL**: [https://arxiv.org/abs/2501.05204](https://arxiv.org/abs/2501.05204)

---

## Essence

![Figure 2](figures/fig2.webp)

*Fig. 2.*

엔터테인먼트 로봇을 위해 예술적 표현성과 동적 이동성을 통합하는 이족 로봇의 설계 및 제어 시스템을 제시하며, reinforcement learning 기반 제어 구조와 실시간 puppeteering 인터페이스를 통해 믿을 수 있는 로봇 캐릭터를 구현한다.

## Motivation

- **Known**: 이족 로봇은 동적 이동성에서 인상적인 성과를 이루었으며, 인간-로봇 상호작용 연구에는 NAO, Pepper 등의 휴머노이드 로봇이 사용되어 왔다. Animation 원리를 로봇에 적용하여 표현력을 높이려는 시도들이 존재해왔다.
- **Gap**: 기존 로봇들은 일반용 플랫폼으로 설계되었고 기계적 설계와 모션이 독립적으로 개발되었으며, 이족 로봇에서 예술적 표현성과 동적 안정성을 동시에 만족하면서 실시간 제어가 가능한 통합 시스템이 부족하다.
- **Why**: 엔터테인먼트 및 인간-로봇 상호작용 애플리케이션에서 로봇의 성공은 인간의 주관적 지각에 크게 의존하며, 표현력 있는 움직임과 역학적 안정성을 함께 달성하는 것이 중요하다.
- **Approach**: Animation 제작과 기계 설계의 반복적 협력을 통해 창의적 의도 중심의 이족 로봇을 설계하고, PPO 기반 reinforcement learning으로 artistic motion을 모방하는 control policy를 학습한 후, animation engine과 puppeteering interface를 통해 실시간 제어를 가능하게 한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2.*

- **통합 개발 파이프라인**: animation, mechanical design, reinforcement learning, real-time puppeteering을 통합한 신속한 로봇 캐릭터 개발 워크플로우 제시
- **창의적 의도 중심 로봇 설계**: 기능 요구사항이 아닌 창의적 의도에 의해 주도된 기구학적 구조의 새로운 이족 로봇 개발
- **다중 motion 제어 전략**: 주기적 motion(걷기), episodic motion(춤), 정적 자세 등을 분류하여 별도의 control policy로 학습 및 전환 가능하도록 구현
- **실시간 puppeteering 인터페이스**: 두 개의 조이스틱으로 motion compositing, blending, switching을 직관적으로 제어하면서 believable character 표현 가능
- **강건한 motion 실행**: domain randomization과 conditional policy input을 통해 불확실성과 외부 교란에 강건하게 artistic motion을 실행

## How

![Figure 2](figures/fig2.webp)

*Fig. 2.*

- Classical animation 도구(rig, spherical joint)와 procedural gait generation tool을 사용하여 character proportions, motion range, walking cycle 설계
- Rigid body dynamics 기반 motion generation으로 physical plausibility 확보하며, 결과를 mechanical design에 피드백하여 geometry, actuator selection, structural analysis 수행
- Simulation model에 actuator models과 domain randomization을 포함하여 robust RL 학습 환경 구성
- Animation tools에서 kinematic motion references를 export하여 imitation rewards 정의 (simulated motion과 reference motion 유사성 최대화)
- High-level control commands를 정의하여 여러 개의 motion/motion type별 policy 학습 (PPO 사용)
- Runtime에서 animation engine이 user input과 animation content를 조합하여 command signal 생성 및 control policies와 interfacing
- Audio engine과의 동기화를 통해 show functions를 motion과 함께 실행

## Originality

- 기능 중심이 아닌 창의적 의도 중심으로 이족 로봇의 기구학적 구조를 설계한 점 (기존 휴머노이드는 인간 참조 사용)
- 여러 motion을 분류하여 별도의 control policy로 학습하고 runtime에 seamlessly 전환하는 divide-and-conquer 전략
- Direct motion control과 expressive animation을 결합한 puppeteering interface 제시 (기존 연구는 주로 완전 자율시스템 또는 완전 scripted animation)
- Animation authoring과 robot control의 통합 파이프라인으로 신속한 prototype 개발 가능 (1년 내 개발 완성)

## Limitation & Further Study

- Unique character에 특화된 설계로, 다른 형태의 캐릭터에 대한 generalization 가능성이 불명확함
- Puppeteering interface가 실시간 제어에 의존하므로 완전 자율적 장기 행동 계획 및 실행 불가
- System의 실외 환경 또는 극도로 불안정한 조건에서의 robustness 검증 부재
- Large-scale human motion dataset가 아닌 artist-authored animation에만 의존하므로, 확장성 있는 motion 라이브러리 구축 가능성 제한
- **후속연구**: (1) 다양한 캐릭터 디자인에 대한 파이프라인 적응 방법, (2) 자율적 high-level behavior planning 통합, (3) 복잡한 실외 환경에서의 안정성 강화, (4) 대규모 motion dataset 활용 가능성 탐색

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 animation 원리를 기반으로 한 창의적 로봇 캐릭터 설계와 reinforcement learning 제어의 통합으로 엔터테인먼트 로봇 개발에 새로운 접근 방식을 제시하며, 실제 구현 사례와 직관적 인터페이스를 통해 높은 실용적 가치를 입증한다.

## Related Papers

- 🔄 다른 접근: [[papers/1285_Berkeley_Humanoid_A_Research_Platform_for_Learning-based_Con/review]] — 이족 로봇에서 엔터테인먼트와 연구 플랫폼의 다른 설계 목적과 접근 방식이다
- 🏛 기반 연구: [[papers/1289_Bi-Level_Motion_Imitation_for_Humanoid_Robots/review]] — 엔터테인먼트 로봇에서 사회적 의도-감정 추론이 표현적 동작의 기초가 된다
- 🏛 기반 연구: [[papers/1301_Chasing_Stability_Humanoid_Running_via_Control_Lyapunov_Func/review]] — 엔터테인먼트 로봇의 동적 이동에서 CLF 기반 안정성 제어가 기초가 된다
- 🧪 응용 사례: [[papers/1381_EMOTION_Expressive_Motion_Sequence_Generation_for_Humanoid_R/review]] — 표현적 휴머노이드 동작 생성에서 엔터테인먼트 로봇의 예술적 표현성이 적용된다
- 🔗 후속 연구: [[papers/1301_Chasing_Stability_Humanoid_Running_via_Control_Lyapunov_Func/review]] — 이족 로봇 제어에서 CLF 기반 안정성이 엔터테인먼트 로봇의 동적 이동에 확장된다
- 🔄 다른 접근: [[papers/1285_Berkeley_Humanoid_A_Research_Platform_for_Learning-based_Con/review]] — 이족 로봇 설계에서 연구용과 엔터테인먼트용의 다른 목적과 접근 방식이다
- 🧪 응용 사례: [[papers/1289_Bi-Level_Motion_Imitation_for_Humanoid_Robots/review]] — 엔터테인먼트 로봇의 표현적 동작에서 사회적 의도와 감정 맥락 추론이 적용된다
