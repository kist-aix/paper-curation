---
title: "1628_WholeBodyVLA_Towards_Unified_Latent_VLA_for_Whole-Body_Loco-"
authors:
  - "Haoran Jiang"
  - "Jin Chen"
  - "Qingwen Bu"
  - "Li Chen"
  - "Modi Shi"
date: "2025.12"
doi: ""
arxiv: ""
score: 4.0
essence: "WholeBodyVLA는 Vision-Language-Action 프레임워크로 humanoid 로봇의 대규모 공간에서 end-to-end 전신 조작-이동(loco-manipulation) 제어를 가능하게 한다. Unified latent learning으로 저비용 영상에서 학습하고 LMO RL policy로 정확한 이동 실행을 보장한다."
tags:
  - "cat/Multimodal_Vision-Language_Policy_Learning"
  - "sub/Humanoid_Egocentric_Learning"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jiang et al._2025_WholeBodyVLA Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control.pdf"
---

# WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control

> **저자**: Haoran Jiang, Jin Chen, Qingwen Bu, Li Chen, Modi Shi, Yanjie Zhang, Delong Li, Chuanzhe Suo, Chuang Wang, Zhihui Peng, Hongyang Li | **날짜**: 2025-12-11 | **URL**: [https://arxiv.org/abs/2512.11047](https://arxiv.org/abs/2512.11047)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Introducing WholeBodyVLA, a humanoid system that operates on Agibot X2 robot and*

WholeBodyVLA는 Vision-Language-Action 프레임워크로 humanoid 로봇의 대규모 공간에서 end-to-end 전신 조작-이동(loco-manipulation) 제어를 가능하게 한다. Unified latent learning으로 저비용 영상에서 학습하고 LMO RL policy로 정확한 이동 실행을 보장한다.

## Motivation

- **Known**: Humanoid 로봇은 dexterous manipulation과 agile locomotion이 필요하며, 기존 RL 기반 whole-body 방법과 VLA 시스템들이 발전해왔다. 그러나 manipulation-aware locomotion을 통합하는 대규모 공간 loco-manipulation은 미해결 상태이다.
- **Gap**: Humanoid teleoperation 데이터의 극심한 부족으로 loco-manipulation 지식 획득이 어렵고, 기존 RL controller의 낮은 정밀도와 안정성으로 인해 locomotion 명령 실행이 불안정하다.
- **Why**: Humanoid 로봇이 일반 목적의 embodied agent로 발전하려면 대규모 공간에서 정밀한 동시 조작과 이동이 필수적이며, 이는 복잡한 현실 작업 수행을 가능하게 한다.
- **Approach**: Action-free 인간 egocentric 영상에서 latent action model (LAM)로 이산 latent action을 학습하여 VLA 사전학습에 활용하고, discrete command interface를 사용하는 LMO RL policy로 정확한 저수준 제어를 실현한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: Introducing WholeBodyVLA, a humanoid system that operates on Agibot X2 robot and*

- **End-to-end loco-manipulation 통합**: 모듈화나 순차 처리 없이 단일 VLA 프레임워크에서 bimanual 조작과 locomotion(전진, 회전, squatting)을 동시에 수행
- **데이터 효율성**: Manipulation-aware locomotion용 저비용 egocentric 영상 수집 파이프라인 개발으로 대규모 데이터 확보
- **성능 향상**: AgiBot X2에서 이전 baseline 대비 21.3% 성능 향상 달성
- **강한 일반화 및 확장성**: 다양한 작업에서 일반화 능력 입증 및 높은 확장성 시연
- **신뢰성**: 50kg 이상의 무거운 하중 이동 등 현실 환경에서의 안정적 작동 검증

## How

![Figure 2](figures/fig2.webp)

*Figure 2: Pipeline of WholeBodyVLA. LAM is pretrained on manipulation and manipulation-*

- **Unified latent learning**: 분리된 locomotion LAM과 manipulation LAM을 각각 학습하여 서로 다른 시각 변화 패턴 캡처
- **이중 감독(dual supervision)**: Human video와 robot data를 혼합하여 두 LAM으로부터 일관된 의도 예측 학습
- **LMO RL policy**: 연속 속도 추적 대신 discrete command (advance, turn, squat 등)를 사용하여 정확한 위치 제어와 안정성 확보
- **두 단계 학습**: LAM 사전학습 후 경량 action decoder 추가 및 teleop 데이터로 미세조정
- **저수준 제어 분리**: High-level VLA는 locomotion command 생성, high-frequency RL controller가 실제 lower-body actions 실행

## Originality

- **Action-free 영상 활용의 혁신적 적용**: Tabletop manipulation에 제한된 기법을 humanoid loco-manipulation 영역으로 확장
- **Manipulation-aware locomotion 명시화**: 기존 velocity-tracking 목표의 한계를 인식하고 discrete command 인터페이스로 loco-manipulation 특화 설계
- **분리된 LAM 아키텍처**: Locomotion과 manipulation의 본질적 차이를 반영하여 독립적 latent space 구성
- **실제 teleoperation 데이터 수집 파이프라인**: 비용 효율적 단일 오퍼레이터 monocular 카메라 기반 수집 방식 제시
- **통합 프레임워크의 실현**: Table 1에서 보듯 기존 모든 접근의 부분적 한계를 극복하는 최초의 완전 통합 시스템

## Limitation & Further Study

- **데이터 규모 제한**: AgiBot World를 활용하더라도 manipulation LAM 학습 규모의 구체적 수치 미제시
- **단일 로봇 플랫폼**: AgiBot X2에서만 검증, 다른 humanoid 형태(Boston Dynamics Atlas 등)에 대한 generalization 미검증
- **Discrete command의 표현력**: Advance, turn, squat 등 정해진 명령만 가능하여 더 미세한 locomotion 제어 필요 작업에 제약 가능성
- **failure case 분석 부족**: Appendix C.3에 failure 통계만 언급되고 정성적 분석 미흡
- **후속연구 방향**: Quadruped 등 다른 embodiment으로 확장, vision-only 학습에서 proprioceptive feedback 통합, real-time dynamic obstacle 회피 능력 추가

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: WholeBodyVLA는 humanoid loco-manipulation의 오랜 과제를 action-free 영상 학습과 맞춤형 RL policy로 창의적으로 해결한 강력한 기여이다. 실제 로봇에서의 입증과 21.3% 성능 향상이 실질적 가치를 증명하나, 단일 플랫폼 검증과 이산 명령 제약은 향후 개선 대상이다.

## Related Papers

- 🔄 다른 접근: [[papers/1421_Helix_A_Vision-Language-Action_Model_for_Generalist_Humanoid/review]] — 둘 다 전신 제어이지만 Helix는 일반적 humanoid, WholeBodyVLA는 loco-manipulation 특화된 차이가 있다
- 🔗 후속 연구: [[papers/1628_WholeBodyVLA_Towards_Unified_Latent_VLA_for_Whole-Body_Loco-/review]] — unified latent learning을 통해 기존 분리된 locomotion과 manipulation을 통합한 전신 제어를 구현했다
- 🏛 기반 연구: [[papers/1249_A_Unified_and_General_Humanoid_Whole-Body_Controller_for_Ver/review]] — A Unified Humanoid Controller의 전신 제어 이론이 WholeBodyVLA의 loco-manipulation 통합 설계 기반이 된다
- 🧪 응용 사례: [[papers/1498_InterMimic_Towards_Universal_Whole-Body_Control_for_Physics-/review]] — InterMimic의 물리 기반 전신 제어와 WholeBodyVLA의 vision-language 기반 제어를 결합한 지능형 humanoid가 가능하다
