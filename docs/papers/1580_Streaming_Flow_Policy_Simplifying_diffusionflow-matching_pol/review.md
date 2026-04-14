---
title: "1580_Streaming_Flow_Policy_Simplifying_diffusionflow-matching_pol"
authors:
  - "Sunshine Jiang"
  - "Xiaolin Fang"
  - "Nicholas Roy"
  - "Tomás Lozano-Pérez"
  - "Leslie Pack Kaelbling"
date: "2025.05"
doi: ""
arxiv: ""
score: 4.0
essence: "Action trajectory를 flow trajectory로 취급하여 diffusion/flow-matching 정책을 단순화하고, 흐름 샘플링 중 실시간으로 로봇에 action을 스트리밍할 수 있는 streaming flow policy를 제안한다."
tags:
  - "cat/Multimodal_Vision-Language_Policy_Learning"
  - "sub/Diffusion_Policy_Learning"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jiang et al._2025_Streaming Flow Policy Simplifying diffusionflow-matching policies by treating action trajectories.pdf"
---

# Streaming Flow Policy: Simplifying diffusion/flow-matching policies by treating action trajectories as flow trajectories

> **저자**: Sunshine Jiang, Xiaolin Fang, Nicholas Roy, Tomás Lozano-Pérez, Leslie Pack Kaelbling, Siddharth Ancha | **날짜**: 2025-05-28 | **URL**: [https://arxiv.org/abs/2505.21851](https://arxiv.org/abs/2505.21851)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: (a) Diffusion policy [1] and flow-matching policy [2] input a history of observations (not shown) to*

Action trajectory를 flow trajectory로 취급하여 diffusion/flow-matching 정책을 단순화하고, 흐름 샘플링 중 실시간으로 로봇에 action을 스트리밍할 수 있는 streaming flow policy를 제안한다.

## Motivation

- **Known**: Diffusion policy와 flow-matching policy는 action 수열을 학습할 수 있지만, 'trajectory of trajectories'를 샘플링하기 때문에 계산 비용이 높고 샘플링 완료까지 기다려야 action 실행이 가능하다.
- **Gap**: 기존 방법들은 중간 action trajectory를 버리고 전체 샘플링 과정이 끝날 때까지 robot 제어를 지연시켜야 하므로, 빠르고 반응성 있는 policy 실행이 어렵다.
- **Why**: Robot 제어에서 낮은 지연시간과 높은 반응성은 tight sensorimotor loop 구성에 필수적이며, 계산 효율성 개선은 실제 로봇 응용의 실시간성을 크게 향상시킨다.
- **Approach**: 마지막 action 주변의 narrow Gaussian에서 샘플링을 시작하고, flow matching으로 학습한 velocity field를 incrementally 통합하여 단일 trajectory를 구성한다. Demonstration trajectory 주변에 안정화되는 velocity field를 구성하여 distribution shift를 감소시킨다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: (a) To illustrate our method, we consider a toy example of 1-D robot actions with two demonstration*

- **On-the-fly streaming**: 흐름 샘플링 과정 중 action을 실시간으로 robot에 전달 가능하여 policy 실행 속도 대폭 개선
- **Multi-modal behavior 보존**: Flow matching의 특성을 활용하여 각 timestep의 marginal distribution이 training distribution과 일치하도록 함으로써 다중 모드 표현 능력 유지
- **Stabilizing flow**: Demonstration trajectory 주변에 안정화되는 velocity field 구성으로 distribution shift 감소 및 imitation learning 성능 향상
- **간단한 구조**: 기존 diffusion/flow policy 아키텍처 재사용 가능하며 입출력 차원만 AT에서 A로 변경

## How

![Figure 2](figures/fig2.webp)

*Figure 2: (a) To illustrate our method, we consider a toy example of 1-D robot actions with two demonstration*

- 각 demonstration trajectory에 대해 conditional flow(초기 action 분포 + velocity field)를 분석적으로 구성
- 구성된 velocity field를 목표로 하여 neural network vθ(a, t | h)를 flow matching으로 학습
- 추론 시 most recently executed action 주변의 narrow Gaussian에서 초기 action 샘플링
- 학습된 velocity field를 iteratively 적분하여 action trajectory 생성
- Stabilizing gain k를 활용하여 velocity field가 demonstration trajectory 근처에서 안정화되도록 유도

## Originality

- Action trajectory 자체를 flow trajectory로 취급하는 혁신적 관점 제시 - 기존의 'trajectory of trajectories' 패러다임과 근본적으로 다름", 'Flow time과 execution time을 일치시켜 streaming generation을 가능하게 한 구조적 통찰
- Demonstration trajectory 주변에 안정화되는 velocity field 구성 방법 - 제어 이론의 low-level stabilizing controller 개념을 flow matching에 적용
- Robot 센서 특성(proprioceptive feedback, forward kinematics)을 활용하여 state trajectory에서 직접 초기화할 수 있는 실용적 확장

## Limitation & Further Study

- **Joint distribution 미보장**: Marginal distribution만 일치하므로 training 데이터에 없던 trajectory 세그먼트의 조합이 생성될 수 있음
- **Global constraints 부재**: 전체 trajectory에 걸친 global constraint 표현 불가능하며, local constraint(joint constraints, convex velocity constraints)만 학습 가능
- **평가 범위**: 실험이 제한된 task(single 7-DOF robot arm)에서 수행되어 다양한 robot 형태에 대한 일반화 효과 불명확
- **Compositionality의 양면성**: Compositionality를 장점으로 제시하지만, 실제로 non-compositional 특성이 필요한 task에서의 성능 저하 가능성
- **후속 연구**: Global constraint 표현 방법 개발, 더 복잡한 task에서의 성능 평가, discrete action space로의 확장 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 action trajectory를 flow trajectory로 취급하는 근본적으로 새로운 관점을 제시하여 diffusion/flow policy의 계산 효율성과 반응성을 크게 개선한 논문이다. Streaming generation이라는 실용적 이점과 이론적 기반(flow matching)의 조화, 그리고 로봇 제어의 특성을 활용한 설계가 돋보이는 우수한 연구다.

## Related Papers

- 🏛 기반 연구: [[papers/1362_Diffusion_Policy_Visuomotor_Policy_Learning_via_Action_Diffu/review]] — 확산 정책의 기본 아이디어를 스트리밍 플로우로 단순화하여 실시간 액션 생성을 가능하게 한다.
- 🧪 응용 사례: [[papers/1525_Real-Time_Execution_of_Action_Chunking_Flow_Policies/review]] — 실시간 액션 청킹 플로우 정책 실행에서 스트리밍 플로우가 지연 시간을 크게 개선한다.
- 🔄 다른 접근: [[papers/1339_Consistency_Policy_Accelerated_Visuomotor_Policies_via_Consi/review]] — 일관성 정책과 스트리밍 플로우 정책이 각각 다른 방식으로 확산 모델의 추론 속도를 개선한다.
- 🔗 후속 연구: [[papers/1474_MEM_Multi-Scale_Embodied_Memory_for_Vision_Language_Action_M/review]] — 실시간 action chunking 실행 알고리즘을 MEM의 단기 메모리 기반 제어에 통합하여 지연 시간을 최소화할 수 있다
- 🔗 후속 연구: [[papers/1502_One-Step_Diffusion_Policy_Fast_Visuomotor_Policies_via_Diffu/review]] — streaming flow policy의 실시간 처리 프레임워크를 OneDP의 단일 단계 추론과 결합하여 지연 시간을 더욱 단축할 수 있다
- 🏛 기반 연구: [[papers/1613_VITA_Vision-to-Action_Flow_Matching_Policy/review]] — Streaming Flow Policy가 VITA의 vision-to-action flow matching 구조의 이론적 기반을 제공한다
- 🔗 후속 연구: [[papers/1618_VLA-Reasoner_Empowering_Vision-Language-Action_Models_with_R/review]] — Streaming Flow Policy의 온라인 계획을 MCTS 기반 추론으로 확장하여 장기 지평 문제 해결 능력을 강화했다
- 🔄 다른 접근: [[papers/1362_Diffusion_Policy_Visuomotor_Policy_Learning_via_Action_Diffu/review]] — Flow-matching policy가 diffusion policy와 다른 생성 모델 접근으로 visuomotor policy learning을 구현한다.
