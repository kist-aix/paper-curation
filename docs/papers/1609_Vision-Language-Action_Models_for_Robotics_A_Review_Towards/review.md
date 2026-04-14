---
title: "1609_Vision-Language-Action_Models_for_Robotics_A_Review_Towards"
authors:
  - "Kento Kawaharazuka"
  - "Jihoon Oh"
  - "Jun Yamada"
  - "Ingmar Posner"
  - "Yuke Zhu"
date: "2025.10"
doi: ""
arxiv: ""
score: 4.0
essence: "Vision-Language-Action (VLA) 모델이 로봇이 다양한 작업을 수행하도록 하는 통합 학습 방식에 대한 포괄적 리뷰로, 소프트웨어와 하드웨어 통합을 포함한 실제 배포 가이드를 제시한다."
tags:
  - "cat/Robotic_Foundation_Model_Development"
  - "sub/VLA_Architecture_Surveys"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kawaharazuka et al._2025_Vision-Language-Action Models for Robotics A Review Towards Real-World Applications.pdf"
---

# Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications

> **저자**: Kento Kawaharazuka, Jihoon Oh, Jun Yamada, Ingmar Posner, Yuke Zhu | **날짜**: 2025-10-08 | **URL**: [https://arxiv.org/abs/2510.07077](https://arxiv.org/abs/2510.07077)

---

## Essence


Vision-Language-Action (VLA) 모델이 로봇이 다양한 작업을 수행하도록 하는 통합 학습 방식에 대한 포괄적 리뷰로, 소프트웨어와 하드웨어 통합을 포함한 실제 배포 가이드를 제시한다.

## Motivation

- **Known**: LLM과 VLM이 자연어 처리와 컴퓨터 비전 분야에서 성공을 거두었으며, 일부 연구는 이들을 로봇에 적용하기 위해 고정된 모션 프리미티브나 모방 학습 기반 정책을 사용해왔다.
- **Gap**: 기존 조사는 행동 토큰화(action tokenization)나 고수준 아키텍처에만 초점을 맞췄지만, VLA의 표준화된 아키텍처와 훈련 방법론이 부재하며, 실제 로봇 시스템 배포를 위한 전체 스택(full-stack) 체계적 검토가 부족하다.
- **Why**: VLA는 최소한의 추가 데이터로 새로운 작업을 수행할 수 있는 범용 로봇 정책을 가능하게 하여, 실제 배포의 유연성과 확장성을 크게 높일 수 있기 때문이다.
- **Approach**: 이 논문은 VLA 모델의 진화 과정, 아키텍처, 모달리티별 처리 기법, 학습 패러다임을 체계적으로 검토하고, 로봇 플랫폼, 데이터 수집 전략, 공개 데이터셋, 데이터 증강, 평가 벤치마크를 포함한 실제 배포 고려사항을 제시한다.

## Achievement


- **포괄적 전체 스택 리뷰**: 기존 조사를 넘어 아키텍처뿐만 아니라 로봇 플랫폼, 데이터 수집, 데이터 증강, 평가 벤치마크를 통합하는 최초의 체계적 리뷰 제공
- **VLA 정의 및 분류**: Vision-Language-Action 모델의 명확한 정의(Definition I.1)와 기존 모델들의 분류 체계 확립
- **실무 가이드**: 실제 로봇 시스템에 VLA를 적용하려는 연구자들을 위한 실질적인 가이드 및 권장사항 제시
- **도전 과제 체계화**: 데이터 가용성, 체구화 전이(embodiment transfer), 계산 비용의 세 가지 핵심 도전 과제를 구조화하여 제시

## How


- VLA의 전략적 진화와 아키텍처 전환 경로를 역사적 관점에서 추적
- Vision encoder, Language model, Action decoder 등 핵심 구성 요소와 빌딩 블록 분석
- 멀티모달 입력(시각, 언어, 고유감각 등)의 modality-specific 처리 기법 검토
- Supervised learning, Reinforcement learning, Self-supervised learning 등 다양한 학습 패러다임 분류
- 로봇 시스템별 데이터 수집 전략(텔레오퍼레이션, 원격 조작 등) 분석
- 공개 데이터셋(RLDS, RoboNet, BridgeData 등) 조사 및 분류
- Sim-to-real transfer, Domain randomization 등 데이터 증강 기법 검토
- 로봇 플랫폼 유형(그리퍼 로봇, 휴머노이드, 모바일 로봇 등) 및 평가 벤치마크 분석

## Originality

- 기존 조사와 달리 소프트웨어와 하드웨어를 통합하는 최초의 전체 스택 리뷰 제공
- VLA 모델의 명확한 정의를 제시하여 범위를 명확히 하고 관련 접근법들과의 경계 구분
- 데이터 부족, 체구화 전이, 계산 비용이라는 근본적 도전 과제를 체계적으로 분석
- 이론적 논의와 실제 배포 고려사항을 연계하는 실무 중심의 관점 도입

## Limitation & Further Study

- 논문은 리뷰이므로 새로운 방법론이나 실험적 성과를 제시하지 않음
- VLA의 빠른 발전으로 인해 논문 작성 시점 이후의 최신 모델들(예: 2024년 이후)을 완전히 포함하지 못할 가능성
- 실제 로봇 배포에서의 실패 사례나 한계에 대한 상세한 논의가 제한적일 수 있음
- 다양한 로봇 플랫폼에서의 VLA 성능 비교를 위한 통일된 벤치마크 부재 문제 해결 방안이 불충분
- **후속 연구**: 크로스-도메인 학습, 저데이터 체제에서의 VLA 효율성, 실시간 계산 제약이 있는 엣지 로봇으로의 배포, 인간 피드백 기반 개선 방법론 개발 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 종합 리뷰는 VLA 연구 분야의 현황을 체계적으로 정리하고 실제 로봇 시스템 배포를 위한 실무 가이드를 제공하여, 로봇공학 커뮤니티가 VLA를 효과적으로 적용하는 데 큰 가치를 제공한다.

## Related Papers

- 🧪 응용 사례: [[papers/1335_Code-as-Monitor_Constraint-aware_Visual_Programming_for_Reac/review]] — DexCap의 data collection system이 VLA 모델의 real-world deployment에서 필수적인 데이터 수집 인프라를 제공
- 🏛 기반 연구: [[papers/1583_No_More_Marching_Learning_Humanoid_Locomotion_for_Short-Rang/review]] — Text2Reward의 language-driven reward shaping이 VLA 모델들의 language 이해 능력 향상에 필요한 기반 방법론
- 🔗 후속 연구: [[papers/1613_VITA_Vision-to-Action_Flow_Matching_Policy/review]] — VITA의 vision-to-action flow matching이 VLA 모델의 action generation 부분을 개선한 구체적 발전
- 🔄 다른 접근: [[papers/1591_Towards_Diverse_Behaviors_A_Benchmark_for_Imitation_Learning/review]] — OmniClone의 whole-body control이 VLA와 다른 접근으로 범용적 로봇 제어를 달성하는 대안적 솔루션
