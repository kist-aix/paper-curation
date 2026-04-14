---
title: "1357_DreamZero_World_Action_Models_are_Zero-shot_Policies"
authors:
  - "| **날짜**:"
date: ""
doi: ""
arxiv: ""
score: 4.0
essence: "이 논문은 로봇 비전-언어-액션(VLA) 모델의 현황을 종합적으로 리뷰한 서베이로, 아키텍처, 학습 전략, 데이터 수집, 실제 배포까지 전체 스택을 다룬다."
tags:
  - "cat/Robotic_Foundation_Model_Development"
  - "sub/VLA_Architecture_Surveys"
  - "topic/physical-ai"
---

# DreamZero: World Action Models are Zero-shot Policies

> **저자**:  | **날짜**:  | **URL**: [https://dreamzero0.github.io/](https://dreamzero0.github.io/)

---

## Essence


이 논문은 로봇 비전-언어-액션(VLA) 모델의 현황을 종합적으로 리뷰한 서베이로, 아키텍처, 학습 전략, 데이터 수집, 실제 배포까지 전체 스택을 다룬다.

## Motivation

- **Known**: LLM과 VLM의 발전이 로봇공학에 영향을 미치고 있으며, 초기에는 vision-language 모델과 robot policy를 분리하여 사용했다. 최근 VLA 모델이 시각, 언어, 액션을 통합학습하여 일반화된 정책 개발을 목표로 하고 있다.
- **Gap**: 기존 서베이는 action tokenization이나 고수준 아키텍처에만 초점을 맞췄으나, 실제 로봇 배포를 위해서는 하드웨어, 데이터 수집, 증강, 평가 벤치마크까지 아우르는 종합적 가이드가 부족했다.
- **Why**: VLA 모델의 표준화된 아키텍처와 방법론이 부재하여 연구자들이 실제 로봇 시스템에 적용하기 어렵고, 데이터 부족, embodiment 전이, 계산 비용 등의 근본적 도전과제에 대한 체계적 이해가 필요하다.
- **Approach**: Vision-Language-Action 모델을 정의하고, 그 설계 전략의 진화, 아키텍처 컴포넌트, modality별 처리 기법, 학습 패러다임을 체계적으로 분류 및 분석하며, 실제 배포를 위한 로봇 플랫폼, 데이터셋, 평가 벤치마크를 종합적으로 리뷰한다.

## Achievement


- **종합적 전체 스택 리뷰**: 소프트웨어 아키텍처부터 하드웨어 플랫폼, 데이터 수집 전략, augmentation 기법, 평가 프로토콜까지 VLA의 모든 계층을 다룬 첫 번째 리뷰 논문
- **VLA 정의 및 분류**: Vision-Language-Action 모델을 명확히 정의하고, 다양한 설계 전략과 아키텍처의 진화 과정을 체계적으로 분류
- **실무자 가이드**: 실제 로봇 시스템 배포를 위한 구체적 권고사항과 최적 실행 방안 제시
- **핵심 도전과제 분석**: 데이터 부족, embodiment 전이, 계산 비용의 세 가지 근본적 제약조건을 상세히 분석

## How


- 로봇 플랫폼별 action space, proprioceptive observation space의 차이를 분석하여 embodiment 전이 문제 정의
- Vision-language datasets와 robot demonstration datasets의 불일치를 data availability 병목으로 식별
- Pre-trained VLM 백본을 활용한 다양한 architecture 방식들을 분류 및 비교
- Imitation learning, reinforcement learning, self-supervised learning 등 다양한 학습 패러다임 검토
- 공개 데이터셋, evaluation benchmarks, 실제 배포 사례들을 체계적으로 정리 및 카테고리화

## Originality

- 기존 좁은 범위의 서베이와 달리, 하드웨어 컴포넌트부터 소프트웨어 아키텍처, 데이터 파이프라인까지 VLA의 전체 스택을 아우르는 첫 종합 리뷰
- VLA를 명확하게 정의하여 스킬 선택 기반 시스템과 엔드-투-엔드 정책 학습을 구분
- Data scarcity, embodiment mismatch, computational cost라는 세 가지 근본적 도전과제를 체계적으로 분석 및 분류
- 실제 로봇 배포를 위한 실무자 지침을 제공하는 새로운 형태의 서베이 구조

## Limitation & Further Study

- 논문이 survey이므로 새로운 알고리즘이나 방법론을 제안하지 않으며, 기존 연구의 종합만 제시
- embodiment 전이 문제에 대한 근본적 해결책은 여전히 제시되지 않음 - 향후 연구에서 morphological 및 sensory 차이를 효과적으로 표현하는 방법 개발 필요
- 대규모 로봇 데이터 수집의 고비용 문제에 대해 human demonstration 활용 가능성만 언급하고, 구체적인 human-to-robot action mapping 방법의 개발이 필요
- 계산 비용 제약에 대해 문제만 식별하고 구체적 해결 방안은 미흡 - 경량화 모델, 효율적 학습 전략에 대한 더 깊이 있는 분석 필요
- VLA의 안전성, 강건성, 실시간 성능 등 실제 배포에 필수적인 속성들에 대한 논의 부족

## Evaluation

- Novelty: 3/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 종합 서베이는 VLA 분야의 현황을 체계적으로 정리하고 실무자를 위한 실질적 가이드를 제공하여 로봇공학 연구자들에게 높은 가치를 제공한다. 다만 향후 연구에서는 데이터 부족, embodiment 전이, 계산 효율성 등의 근본적 도전과제에 대한 구체적 해결책 개발이 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/1388_Exploring_Embodied_Multimodal_Large_Models_Development_Datas/review]] — VLA 모델 전체 스택 리뷰가 embodied multimodal 모델 발전의 포괄적 기초 자료 제공
- 🔗 후속 연구: [[papers/1397_Foundation_Model_Driven_Robotics_A_Comprehensive_Review/review]] — VLA 모델 서베이가 foundation model 기반 로봇공학의 구체적 구현 방향으로 확장
