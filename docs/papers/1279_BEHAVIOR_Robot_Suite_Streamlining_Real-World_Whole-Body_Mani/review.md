---
title: "1279_BEHAVIOR_Robot_Suite_Streamlining_Real-World_Whole-Body_Mani"
authors:
  - "Yunfan Jiang"
  - "Ruohan Zhang"
  - "Josiah Wong"
  - "Chen Wang"
  - "Yanjie Ze"
date: "2025.03"
doi: ""
arxiv: ""
score: 4.0
essence: "BEHAVIOR Robot Suite (BRS)는 가정용 일상 작업을 수행하기 위한 양팔 협력, 안정적 네비게이션, 광범위한 말단 장치 도달성을 갖춘 전신 조작 로봇을 위한 통합 프레임워크를 제시한다. JoyLo 원격 조작 인터페이스와 WB-VIMA 시각운동 정책 학습 알고리즘을 통해 실세계 가정 작업 수행을 가능하게 한다."
tags:
  - "cat/Humanoid_Teleoperation_and_Interaction"
  - "sub/Humanoid_Teleoperation_Data"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jiang et al._2025_BEHAVIOR Robot Suite Streamlining Real-World Whole-Body Manipulation for Everyday Household Activit.pdf"
---

# BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities

> **저자**: Yunfan Jiang, Ruohan Zhang, Josiah Wong, Chen Wang, Yanjie Ze, Hang Yin, Cem Gokmen, Shuran Song, Jiajun Wu, Li Fei-Fei | **날짜**: 2025-03-07 | **URL**: [https://arxiv.org/abs/2503.05652](https://arxiv.org/abs/2503.05652)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Everyday household activities enabled by BEHAVIOR ROBOT SUITE (BRS), show-*

BEHAVIOR Robot Suite (BRS)는 가정용 일상 작업을 수행하기 위한 양팔 협력, 안정적 네비게이션, 광범위한 말단 장치 도달성을 갖춘 전신 조작 로봇을 위한 통합 프레임워크를 제시한다. JoyLo 원격 조작 인터페이스와 WB-VIMA 시각운동 정책 학습 알고리즘을 통해 실세계 가정 작업 수행을 가능하게 한다.

## Motivation

- **Known**: Mobile ALOHA, TidyBot++ 등의 기존 가정용 로봇 시스템들이 있으나, 대부분 양팔 협력, 네비게이션, 도달성, 원격 조작 인터페이스, 또는 학습 알고리즘의 각 측면에서 제약을 갖고 있다. BEHAVIOR-1K 벤치마크 분석을 통해 가정 작업의 성공에 필요한 핵심 역량들이 규명되어 있다.
- **Gap**: 기존 시스템들은 전신 조작(팔, 몸통, 모바일 베이스의 동시 제어)을 통합적으로 다루지 못하며, 비용 효율적이면서도 직관적인 원격 조작 인터페이스의 부족과 전신 동작을 효과적으로 모델링하는 학습 알고리즘의 부재가 있다.
- **Why**: 가정용 일상 작업은 다양한 높이(0.09m, 0.49m, 0.94m, 1.43m)의 물체 상호작용, 장거리 네비게이션, 협곡 공간 작업 등을 요구하므로 진정한 의미의 전신 조작 능력이 필수적이다. 이는 로봇이 실제 가정 환경에서 유용한 보조 역할을 수행하기 위해 중요하다.
- **Approach**: JoyLo는 Nintendo Joy-Con 컨트롤러를 장착한 저비용 운동학 쌍둥이 팔을 이용해 직관적이고 확장 가능한 원격 조작을 구현한다. WB-VIMA는 Point-Cloud, Proprioceptive, Action 토큰을 활용하여 Visuomotor Attention 메커니즘으로 다중 모달 관측을 동적으로 통합하고 양팔(14 DoF), 몸통(4 DoF), 모바일 베이스(3 DoF)를 자동회귀적으로 디코딩한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: Everyday household activities enabled by BEHAVIOR ROBOT SUITE (BRS), show-*

- **JoyLo 설계**: 컴팩트하고 저비용($500-$1000 미만)의 원격 조작 인터페이스로, 양팔, 몸통(요추/골반), 모바일 베이스를 단일 오퍼레이터가 동시 제어 가능하며 양방향 피드백을 통해 자연스러운 조작 경험 제공
- **WB-VIMA 알고리즘**: 계층적 신체 공간 상호 의존성을 활용한 자동회귀 전신 동작 예측으로 21 DoF 전체 신체 제어 모델링
- **실세계 성능**: 5가지 가정용 작업에서 단기 부분 작업 88% 성공률, 장기 전체 작업 최대 93% 성공률 달성
- **포괄적 하드웨어-소프트웨어 통합**: 이전 시스템들과 달리 하드웨어(dual-arm, 4-DoF torso, omnidirectional base), 원격 조작, 학습 알고리즘을 완전히 오픈소스화

## How


- BEHAVIOR-1K 벤치마크로부터 1,000개 가정 작업 분석하여 물체 높이 분포의 다중 모드 특성 파악 (Fig. 2)
- JoyLo의 Puppeteering 접근법: Joy-Con 좌측 스틱(모바일 베이스 속도), 우측 스틱(허리/골반), 방향키(몸통 높이), 트리거(그리퍼) 제어
- JoyLo 팔의 운동학 제약으로 불가능한 또는 배포 불가능한 동작 자동 차단
- 양방향 피드백: 토크 τ = Kp(qrobot - qJoyLo) + Kd(q̇robot - q̇JoyLo) - K 식으로 로봇 상태를 JoyLo 팔에 반영
- WB-VIMA 아키텍처: Point-Cloud, Proprioceptive 토큰의 자기-주의(self-attention) 기반 통합 후, 세 개의 독립 디코더로 각 신체 부위의 동작 자동회귀 생성 (Fig. 4)
- 점군(colored point cloud) 기반 시각 관측과 양팔/몸통/베이스 상태의 자기 수용 정보 활용
- Transformer 백본 아키텍처 기반 정책 모델

## Originality

- **JoyLo의 설계 혁신**: Nintendo Joy-Con의 컴팩트함과 다중 기능성을 활용하여 진정한 단일 오퍼레이터 양방향 피드백 기반 전신 원격 조작을 저비용으로 달성
- **계층적 신체 공간 기반 자동회귀 디코딩**: 양팔→몸통→베이스 또는 다른 순서로의 동작 생성 시 신체 부위 간 계층적 의존성을 명시적으로 모델링
- **포괄적 벤치마킹 접근**: 기존 프레임워크 비교표에서 BRS가 처음으로 하드웨어, 원격 조작, 학습 알고리즘을 모두 오픈소스화하면서 전신 제어의 모든 측면을 다룸
- **정성적 데이터 분석**: BEHAVIOR-1K로부터 물체 높이 분포의 다중 모드 구조를 도출하여 로봇 도달성 설계의 정당성 제시

## Limitation & Further Study

- **일반화 한계**: 평가가 5가지 구체적 가정 작업에만 제한되어 다양한 환경/시나리오에서의 성능 보편성 미실증
- **하드웨어 특화성**: JoyLo 설계가 Galaxea R1 로봇에 맞춰져 있어 다른 모바일 조작 플랫폼으로의 직접 이전성 불명확
- **성공률 분석 부재**: 실패 사례의 정성적 분석이나 실패 패턴 분류 미제시로 한계 이해 부족
- **비교 실험 제한**: 기존 원격 조작 방식(motion retargeting, kinesthetic teaching 등)과의 정량적 비교 실험 부재
- **후속 연구 방향**: (1) 다양한 로봇 플랫폼으로의 JoyLo 원칙 적용 및 적응성 검증, (2) 더 복잡한 장기 시퀀스 작업에 대한 WB-VIMA의 확장성 평가, (3) 시뮬레이션-현실 전이(sim-to-real) 학습과의 통합 탐색

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: BEHAVIOR Robot Suite는 가정용 일상 작업을 위한 전신 조작 로봇의 완전한 생태계를 제시하는 포괄적 연구로, JoyLo의 창의적인 저비용 설계와 WB-VIMA의 계층적 자동회귀 정책 학습이 결합되어 실세계 가정 로봇의 실질적 진전을 이룬다. 특히 하드웨어, 데이터 수집, 알고리즘을 완전히 오픈소스화함으로써 커뮤니티 확산 가능성이 높으며, 다중 도메인의 체계적 통합을 통해 로봇 학습 연구에 의미 있는 기여를 한다.

## Related Papers

- 🔄 다른 접근: [[papers/1272_ARMADA_Augmented_Reality_for_Robot_Manipulation_and_Robot-Fr/review]] — 실세계 전신 조작에서 물리적 로봇과 증강현실 기반 데이터 수집의 다른 방식이다
- 🔗 후속 연구: [[papers/1291_BiGym_A_Demo-Driven_Mobile_Bi-Manual_Manipulation_Benchmark/review]] — 가정용 일상 작업에서 BRS의 전신 조작이 BiGym의 양팔 조작을 확장한다
- 🏛 기반 연구: [[papers/1320_Coordinated_Humanoid_Manipulation_with_Choice_Policies/review]] — Choice Policy의 모듈식 접근에서 WB-VIMA 시각운동 정책이 기초가 된다
- 🧪 응용 사례: [[papers/1562_ManiSkill-HAB_A_Benchmark_for_Low-Level_Manipulation_in_Home/review]] — 가정 환경 저수준 조작 벤치마크에서 BRS의 일상 작업 수행 능력이 적용된다
- 🏛 기반 연구: [[papers/1291_BiGym_A_Demo-Driven_Mobile_Bi-Manual_Manipulation_Benchmark/review]] — 가정용 양팔 조작 벤치마크가 실세계 전신 조작 프레임워크의 기초가 된다
- 🔄 다른 접근: [[papers/1272_ARMADA_Augmented_Reality_for_Robot_Manipulation_and_Robot-Fr/review]] — 로봇 조작 데이터 수집에서 증강현실과 물리적 로봇 텔레오퍼레이션의 다른 접근이다
- 🔗 후속 연구: [[papers/1320_Coordinated_Humanoid_Manipulation_with_Choice_Policies/review]] — 통합 휴머노이드 조작에서 Choice Policy가 WB-VIMA 시각운동 정책을 확장한다
