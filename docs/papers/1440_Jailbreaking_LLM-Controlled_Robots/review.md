---
title: "1440_Jailbreaking_LLM-Controlled_Robots"
authors:
  - "Alexander Robey"
  - "Zachary Ravichandran"
  - "Vijay Kumar"
  - "Hamed Hassani"
  - "George J. Pappas"
date: "2024.10"
doi: ""
arxiv: ""
score: 5.0
essence: "LLM 기반 로봇 제어 시스템의 보안 취약점을 조사하기 위해 RoboPAIR 알고리즘을 제안하며, 이는 채팅봇 jailbreak와 달리 실제 물리적 해로운 행동을 유도하는 최초의 공격 방식이다."
tags:
  - "cat/Robotic_Foundation_Model_Development"
  - "sub/Language_Model_Vulnerabilities"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Robey et al._2024_Jailbreaking LLM-Controlled Robots.pdf"
---

# Jailbreaking LLM-Controlled Robots

> **저자**: Alexander Robey, Zachary Ravichandran, Vijay Kumar, Hamed Hassani, George J. Pappas | **날짜**: 2024-10-17 | **URL**: [https://arxiv.org/abs/2410.13691](https://arxiv.org/abs/2410.13691)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Jailbreaking LLM-controlled robots.*

LLM 기반 로봇 제어 시스템의 보안 취약점을 조사하기 위해 RoboPAIR 알고리즘을 제안하며, 이는 채팅봇 jailbreak와 달리 실제 물리적 해로운 행동을 유도하는 최초의 공격 방식이다.

## Motivation

- **Known**: LLM은 jailbreak 공격에 취약하며 악의적 프롬프트를 통해 해로운 텍스트를 생성할 수 있다는 것이 알려져 있다. 또한 로봇 제어를 위해 LLM이 고수준 플래너로 광범위하게 배포되고 있다.
- **Gap**: 기존 LLM jailbreak 연구는 텍스트 생성에만 초점을 맞추고 있으며, LLM 제어 로봇의 물리적 안전성과 jailbreak 취약성에 대한 체계적인 평가가 부재하다.
- **Why**: LLM 제어 로봇은 실제 물리적 피해를 초래할 수 있으므로, 배포 전 안전성 검증이 필수적이며 이를 통해 방어 알고리즘 개발의 기초를 마련할 수 있다.
- **Approach**: RoboPAIR 알고리즘을 설계하여 white-box, gray-box, black-box 세 가지 협박 모델에서 LLM 제어 로봇에 대한 jailbreak 공격을 수행하고, 새로운 유해 로봇 행동 벤치마크 데이터셋을 구성한다.

## Achievement

![Figure 3](figures/fig3.webp)

*Figure 3: Jailbreaking elicits harmful robotic actions. When directly prompted, LLM-controlled*

- **최초의 LLM 로봇 jailbreak 알고리즘**: RoboPAIR을 제시하여 실제 물리적 해로운 행동을 유도할 수 있음을 입증
- **다양한 협박 시나리오에서의 성공**: NVIDIA Dolphins, Clearpath Robotics Jackal UGV, Unitree Robotics Go2에서 100% 공격 성공률 달성
- **상용 로봇 시스템 최초 jailbreak**: 실제 배포된 상업용 Unitree Go2 로봇에 대한 최초의 성공적인 jailbreak 시연
- **포괄적인 벤치마크 구성**: 폭탄 해체, 비밀 감시, 무기 식별, 인간 충돌 등 세 개의 유해 로봇 행동 데이터셋 개발

## How

![Figure 4](figures/fig4.webp)

*Figure 4: Jailbreaking the Unitree Go2.*

- PAIR 챗봇 jailbreak 알고리즘을 기반으로 하여 로봇 제어 도메인으로 확장
- White-box 설정에서는 NVIDIA Dolphins LLM에 대한 전체 접근권을 활용
- Gray-box 설정에서는 Clearpath Jackal UGV의 GPT-4o 플래너에 대한 부분적 접근 활용
- Black-box 설정에서는 GPT-3.5 통합 Unitree Go2에 대한 쿼리만으로 공격 수행
- In-context learning, template-based, code injection 등 다양한 공격 방식 실험
- 유해 로봇 행동의 성공률을 측정하는 평가 메트릭 정의

## Originality

- 로봇 제어 시스템을 대상으로 하는 최초의 jailbreak 연구로, 기존 텍스트 기반 공격과 근본적으로 다른 물리적 피해 가능성 제시
- White-box, gray-box, black-box 협박 모델을 모두 포괄하는 포괄적인 위협 모델 분석
- 현실 배포 상용 로봇을 실제로 jailbreak한 최초의 사례로 보안 중요성 강조
- 로봇 특화 유해 행동 벤치마크의 최초 개발

## Limitation & Further Study

- 평가가 주로 시뮬레이션이나 제한된 실제 환경에서 수행될 가능성 있음
- 실제 배포 환경의 다양한 센서 설정, 네트워크 조건, 물리적 제약을 충분히 반영하지 못할 수 있음
- 방어 메커니즘에 대한 구체적인 제안이 부재하며 주로 문제 제시에 집중
- 로봇별 특화된 방어책 설계 필요성 제시 후속 연구 과제로 남음
- 상용 로봇 제조업체와의 책임 공개 과정에서 공개할 수 있는 기술적 상세 정보의 제약

## Evaluation

- Novelty: 5/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 5/5

**총평**: 본 연구는 LLM 제어 로봇의 물리적 안전성 위협을 최초로 체계적으로 입증한 중요한 보안 연구로, 실제 배포된 상용 로봇에 대한 jailbreak 성공은 AI 안전 분야에서 획기적인 발견이다. 다만 방어 메커니즘에 대한 구체적 제안은 후속 연구로 남겨져 있어 실제 배포 환경에서의 완전한 방어 책임은 산업체에 전가되는 측면이 있다.

## Related Papers

- 🏛 기반 연구: [[papers/1286_Beyond_Tools_and_Persons_Who_Are_They_Classifying_Robots_and/review]] — 로봇 AI 시스템의 분류와 거버넌스를 통해 jailbreak 공격의 사회적 위험성을 이해하는 기초를 제공한다
- 🔄 다른 접근: [[papers/1501_On_the_Vulnerability_of_LLMVLM-Controlled_Robotics/review]] — LLM/VLM 제어 로봇의 취약점을 다룬다는 동일한 문제의식을 다른 각도에서 접근한다
- 🔗 후속 연구: [[papers/1458_LLM-Driven_Robots_Risk_Enacting_Discrimination_Violence_and/review]] — LLM 기반 로봇의 차별과 폭력 위험을 구체적으로 분석하여 jailbreak의 실제 사회적 파급효과를 보여준다
- 🔗 후속 연구: [[papers/1458_LLM-Driven_Robots_Risk_Enacting_Discrimination_Violence_and/review]] — LLM 기반 로봇의 안전성 문제에 대한 상호 보완적인 분석으로, jailbreaking과 차별/폭력의 다른 측면을 다룬다.
- 🏛 기반 연구: [[papers/1501_On_the_Vulnerability_of_LLMVLM-Controlled_Robotics/review]] — LLM 제어 로봇의 jailbreaking 취약성이 일반적인 LLM/VLM 로봇 취약성 분석의 구체적 사례를 제공한다.
- 🧪 응용 사례: [[papers/1286_Beyond_Tools_and_Persons_Who_Are_They_Classifying_Robots_and/review]] — 로봇 AI 시스템의 분류 체계가 LLM 기반 로봇의 보안 취약점을 분석하는 구체적 틀을 제공한다
