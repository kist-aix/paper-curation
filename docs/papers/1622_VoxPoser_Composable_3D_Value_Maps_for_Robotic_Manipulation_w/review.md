---
title: "1622_VoxPoser_Composable_3D_Value_Maps_for_Robotic_Manipulation_w"
authors:
  - "Wenlong Huang"
  - "Chen Wang"
  - "Ruohan Zhang"
  - "Yunzhu Li"
  - "Jiajun Wu"
date: "2023.07"
doi: ""
arxiv: ""
score: 4.0
essence: "LLM의 affordance 추론 능력과 code-writing 능력을 활용하여 3D value map을 생성하고, 이를 model-based planning으로 로봇 trajectory 합성에 활용하는 zero-shot 로봇 조작 방법론."
tags:
  - "cat/Embodied_Navigation_and_Planning"
  - "sub/Spatial_Language_Understanding"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Huang et al._2023_VoxPoser Composable 3D Value Maps for Robotic Manipulation with Language Models.pdf"
---

# VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models

> **저자**: Wenlong Huang, Chen Wang, Ruohan Zhang, Yunzhu Li, Jiajun Wu, Li Fei-Fei | **날짜**: 2023-07-12 | **URL**: [https://arxiv.org/abs/2307.05973](https://arxiv.org/abs/2307.05973)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: VOXPOSER extracts language-conditioned affordances and constraints from LLMs and grounds*

LLM의 affordance 추론 능력과 code-writing 능력을 활용하여 3D value map을 생성하고, 이를 model-based planning으로 로봇 trajectory 합성에 활용하는 zero-shot 로봇 조작 방법론.

## Motivation

- **Known**: LLM은 강력한 추론과 계획 능력을 가지고 있으나, 기존 로봇 조작 방법은 사전정의된 motion primitive에 의존하여 확장성이 제한된다.
- **Gap**: LLM의 추상적 지식을 로봇의 고차원 제어 신호로 직접 변환하고, 추가 학습 없이 다양한 객체와 자유형식 명령에 대응하는 방법이 부재했다.
- **Why**: 로봇 조작의 일반화를 위해서는 대규모 로봇 데이터 수집 부담을 줄이면서도 LLM의 광범위한 세계 지식을 활용할 수 있는 방법이 필수적이다.
- **Approach**: LLM이 자유형식 명령에서 affordance와 constraint를 Python code로 추론하고, VLM을 호출하여 3D voxel space에 reward/cost map을 구성한 후, 이를 model-based planner의 목적함수로 사용하여 closed-loop trajectory를 합성한다.

## Achievement

![Figure 3](figures/fig3.webp)

*Figure 3: Visualization of composed 3D value maps and rollouts in real-world environments. The top row*

- **Zero-shot 일반화**: 추가 학습 없이 open-set 명령과 open-set 객체에 대한 다양한 조작 작업 수행
- **3D value map 구성**: LLM의 code-writing 능력으로 affordance와 constraint를 시각 공간에 grounding하는 새로운 방법 제시
- **Closed-loop robustness**: Model-based planning을 통해 동적 perturbation에 강건한 trajectory 합성
- **Online learning 통합**: Contact-rich interaction을 위한 dynamics model 효율적 학습 가능
- **대규모 실증**: 시뮬레이션과 실제 로봇에서 15+ 가지 일상 조작 작업 검증

## How

![Figure 2](figures/fig2.webp)

*Figure 2: Overview of VOXPOSER. Given the RGB-D observation of the environment and a language in-*

- LLM prompt engineering으로 affordance (grasp point, motion direction) 및 constraint (collision avoidance) 추론
- LLM이 생성한 Python code에서 CLIP, open-vocabulary detector 등 VLM API 호출하여 객체/부위 위치 감지
- NumPy 등 array operation으로 3D voxel grid에 affordance는 high value, constraint 영역은 low value 할당
- Composed value map을 trajectory optimization (예: iLQR, MPC) 문제의 cost function으로 설정
- Closed-loop MPC로 RGB-D observation 기반 real-time feedback 통합하여 robust trajectory 생성
- 선택적으로 online data로 환경 dynamics model 학습하여 contact-rich task 개선

## Originality

- LLM의 code generation 능력을 로봇 affordance 추론과 3D spatial grounding에 활용하는 새로운 paradigm
- VLM과의 조합을 통해 language-conditioned cost function을 직접 observation space에 구성하는 접근
- Pre-trained foundation model (LLM, VLM)을 task-specific fine-tuning 없이 활용하는 zero-shot 방법론
- Potential field 및 constrained optimization 기반 planning과 language understanding의 효과적 결합

## Limitation & Further Study

- LLM이 생성한 affordance가 부정확할 경우 robustness 저하 가능성 (LLM hallucination 미해결)
- Sub-task 분해(L → ℓ1, ℓ2, ...)는 별도 high-level planner 필요하며, long-horizon planning 성능 미평가
- Contact-rich task의 경우 online learning 필수이므로, 완전 zero-shot 성능 제한
- Computation cost (LLM inference, VLM perception, trajectory optimization) 분석 부재
- Real-world 실험이 제한적일 수 있으며, 더 다양한 환경과 극단적 상황에서의 평가 필요
- 후속 연구: LLM uncertainty quantification, end-to-end long-horizon task planning, 더 효율적인 dynamics learning

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: VoxPoser는 LLM의 높은 수준 추론과 code 생성 능력을 3D 로봇 조작에 처음으로 효과적으로 연결한 혁신적 방법으로, zero-shot 일반화와 실제 로봇 적용 가능성을 보여주는 의미 있는 기여이다. 다만 affordance 정확성, 장기 계획, 계산 효율성 측면의 개선이 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/1561_SayPlan_Grounding_Large_Language_Models_using_3D_Scene_Graph/review]] — VoxPoser의 3D value map 생성이 SayPlan의 3D scene graph grounding과 결합되어 더 정교한 언어 기반 로봇 조작 계획을 수립할 수 있음
- 🏛 기반 연구: [[papers/1369_Do_As_I_Can_Not_As_I_Say_Grounding_Language_in_Robotic_Affor/review]] — VoxPoser의 affordance reasoning과 code-writing이 Do As I Can, Not As I Say의 언어 기반 affordance grounding 원리를 3D 공간으로 확장한 형태
- 🔄 다른 접근: [[papers/1334_Code_as_Policies_Language_Model_Programs_for_Embodied_Contro/review]] — VoxPoser는 3D value map 기반으로, Code as Policies는 직접적인 코드 생성으로 LLM을 embodied control에 활용하는 서로 다른 접근법
- 🔄 다른 접근: [[papers/1529_ReKep_Spatio-Temporal_Reasoning_of_Relational_Keypoint_Const/review]] — VoxPoser의 3D value maps와 ReKep의 relational keypoint constraints는 모두 로봇 조작을 위한 3D 공간 표현의 서로 다른 접근법이다.
- 🔗 후속 연구: [[papers/1333_CLIPort_What_and_Where_Pathways_for_Robotic_Manipulation/review]] — VoxPoser는 CLIPort의 공간적 정밀성을 3D 값 맵을 통한 구성 가능한 조작으로 확장한다
