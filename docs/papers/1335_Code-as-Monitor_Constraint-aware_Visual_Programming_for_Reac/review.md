---
title: "1335_Code-as-Monitor_Constraint-aware_Visual_Programming_for_Reac"
authors:
  - "Enshen Zhou"
  - "Qi Su"
  - "Cheng Chi"
  - "Zhizheng Zhang"
  - "Zhongyuan Wang"
date: "2024.12"
doi: ""
arxiv: ""
score: 4.0
essence: "VLM을 활용하여 spatio-temporal constraint satisfaction 문제로 로봇 실패를 정식화하고, constraint elements를 추상화하여 VLM 생성 코드로 실시간 모니터링하는 Code-as-Monitor(CaM) 패러다임을 제안한다."
tags:
  - "cat/Robotic_Foundation_Model_Development"
  - "sub/Automated_Policy_Evaluation"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhou et al._2024_Code-as-Monitor Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Dete.pdf"
---

# Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection

> **저자**: Enshen Zhou, Qi Su, Cheng Chi, Zhizheng Zhang, Zhongyuan Wang, Tiejun Huang, Lu Sheng, He Wang | **날짜**: 2024-12-05 | **URL**: [https://arxiv.org/abs/2412.04455](https://arxiv.org/abs/2412.04455)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2. Overview of Code-as-Monitor. Given task instructions and prior information, the Constraint Generator derives t*

VLM을 활용하여 spatio-temporal constraint satisfaction 문제로 로봇 실패를 정식화하고, constraint elements를 추상화하여 VLM 생성 코드로 실시간 모니터링하는 Code-as-Monitor(CaM) 패러다임을 제안한다.

## Motivation

- **Known**: 최근 LLM/VLM 기반 연구들이 반응적 실패 감지(reactive failure detection)는 달성했으나, 계산 비용이 높고 3D spatio-temporal 인식 능력이 부족하며, 예방적 실패 감지(proactive failure detection)는 거의 탐구되지 않았다.
- **Gap**: 기존 방법들은 반응적 감지와 예방적 감지를 동시에 달성하지 못하며, 높은 정밀도와 실시간 효율성을 함께 만족하는 open-set 실패 감지 프레임워크가 부재하다.
- **Why**: 로봇이 복잡한 환경에서 장시간 작업을 수행할 때 예상치 못한 실패 방지와 예측 가능한 실패 예방이 모두 필수적이며, 이는 폐루프 로봇 시스템의 신뢰성을 크게 향상시킨다.
- **Approach**: Task instruction으로부터 constraint를 추출하고 constraint elements(점, 선, 면 등의 기하학적 추상화)를 시각적으로 표시한 후, VLM이 이를 기반으로 monitor code를 생성하여 추적된 constraint elements에 대해 실행하는 방식이다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1. For the task “Move the pan with lobster to the stove without losing the lobster”, (a) reactive failure detecti*

- **통합 프레임워크**: 반응적 감지와 예방적 감지를 spatio-temporal constraint satisfaction 문제로 통합하는 최초의 시도
- **Constraint Elements**: constraint 관련 entity/part를 콤팩트한 기하학적 요소로 추상화하여 추적 단순화 및 visual prompting 용이
- **성능 향상**: 심각한 외란 하에서 기저선 대비 28.7% 높은 성공률과 31.8% 단축된 실행 시간 달성
- **실시간 효율성**: VLM을 초기 호출 시점에만 사용하고 monitor code 실행으로 반복적 감지를 수행하여 실시간 모니터링 가능
- **다중 환경 검증**: CLIPort, Omnigibson, RL-Bench 시뮬레이터 및 실제 환경에서 일반화 성능 입증

## How

![Figure 2](figures/fig2.webp)

*Figure 2. Overview of Code-as-Monitor. Given task instructions and prior information, the Constraint Generator derives t*

- Constraint Generator: Task instruction과 multi-view RGB-D observations으로부터 textual constraints 도출
- Constraint Painter: 학습된 ConSeg 모델과 off-the-shelf tracker(Co-Tracker)를 이용하여 constraint elements를 RGB 이미지에 시각적으로 표시
- Code Generation: VLM(GPT-4o)이 시각적 constraint elements와 textual constraints를 입력받아 constraint satisfaction 평가 코드 생성
- Monitor Execution: 생성된 monitor code를 추적된 constraint element 위치에 대해 반복 실행하여 실패 감지 및 상세 피드백 제공
- Closed-loop Integration: 감지된 실패 피드백을 기반으로 re-planning 트리거하여 open-loop 제어 정책과 결합

## Originality

- **이중 감지 통합**: reactive와 proactive failure detection을 unified constraint framework으로 처음 통합
- **Constraint Elements 도입**: VLM의 일반화 능력을 유지하면서 기하학적 추상화로 정밀도와 효율성 동시 달성
- **Code-as-Monitor 패러다임**: LLM/VLM을 모니터링의 생성 단계에만 제한하고 실행 단계에서는 코드 평가로 실시간성 확보
- **Open-set 일반화**: 미리 정의되지 않은 실패와 새로운 entity/scene에 대한 적응 능력 제시

## Limitation & Further Study

- VLM이 초기 constraint 생성 시점에 필요하므로, 초기 호출 지연이 발생할 수 있음
- Constraint elements 검출을 위해 ConSeg 모델 학습이 필요하며, 매우 새로운 도메인에서는 추가 annotation이 필요할 수 있음
- 현재 실험은 manipulation 중심이므로 navigation 등 다른 로봇 작업 영역으로의 확장성 미검증
- **후속연구**: 다중모달 constraint 표현(시간, 힘 등), 더 복잡한 상호작용 시나리오, 제로샷 constraint element 검출 방법 개발이 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 open-set 반응적/예방적 실패 감지를 처음으로 통합하는 Code-as-Monitor 패러다임을 제안하며, constraint elements라는 창의적 추상화로 VLM의 일반화 능력과 실시간 효율성의 상충을 해결한 우수한 기여이다. 다양한 환경과 로봇 플랫폼에서의 광범위한 검증과 명확한 프레임워크 설계로 높은 가치를 지닌다.

## Related Papers

- 🔗 후속 연구: [[papers/1359_DualTHOR_A_Dual-Arm_Humanoid_Simulation_Platform_for_Conting/review]] — VLM 기반 constraint monitoring을 dual-arm humanoid 환경에서 contingency 메커니즘과 함께 확장 적용
- 🔄 다른 접근: [[papers/1386_Evaluating_Real-World_Robot_Manipulation_Policies_in_Simulat/review]] — 로봇 정책 평가를 constraint satisfaction으로 접근하는 것과 시뮬레이션 기반 평가의 상호보완적 방법론
- 🧪 응용 사례: [[papers/1238_A_21-DOF_Humanoid_Dexterous_Hand_with_Hybrid_SMA-Motor_Actua/review]] — 21-DOF 손재주 손의 정밀한 조작 능력을 GUI 기반 원격조작 시스템에 적용하여 비전문가도 사용할 수 있습니다.
- 🧪 응용 사례: [[papers/1359_DualTHOR_A_Dual-Arm_Humanoid_Simulation_Platform_for_Conting/review]] — dual-arm humanoid 시뮬레이션에서 constraint-aware monitoring을 contingency 상황에 적용
- 🔗 후속 연구: [[papers/1338_DexterCap_An_Affordable_and_Automated_System_for_Capturing_D/review]] — mocap 데이터 수집을 더 확장 가능하고 포터블한 시스템으로 발전시켰다
- 🧪 응용 사례: [[papers/1609_Vision-Language-Action_Models_for_Robotics_A_Review_Towards/review]] — DexCap의 data collection system이 VLA 모델의 real-world deployment에서 필수적인 데이터 수집 인프라를 제공
- 🔗 후속 연구: [[papers/1334_Code_as_Policies_Language_Model_Programs_for_Embodied_Contro/review]] — Code as Policies의 기본 개념을 constraint-aware programming으로 발전시켜 더 안전하고 제약을 고려한 정책 생성을 가능하게 한다
- 🔗 후속 연구: [[papers/1386_Evaluating_Real-World_Robot_Manipulation_Policies_in_Simulat/review]] — 시뮬레이션 기반 정책 평가가 constraint-aware monitoring과 결합하여 더 robust한 평가 체계 구축
- 🏛 기반 연구: [[papers/1587_Object-Centric_Dexterous_Manipulation_from_Human_Motion_Data/review]] — DexCap의 손 동작 캡처 시스템에서 수집한 데이터를 로봇 손의 실제 조작 정책 학습에 적용한다.
