---
title: "1324_Bridging_Language_and_Action_A_Survey_of_Language-Conditione"
authors:
  - "Xiangtong Yao"
  - "Hongkuan Zhou"
  - "Oier Mees"
  - "Yuan Meng"
  - "Ted Xiao"
date: "2023.12"
doi: ""
arxiv: ""
score: 4.0
essence: "자연언어 지시를 로봇의 물리적 행동으로 변환하는 language-conditioned robot manipulation 분야를 체계적으로 조사한 종합 서베이 논문으로, 언어가 로봇 시스템에 통합되는 4가지 주요 방식을 분류하고 최신 기술을 분석한다."
tags:
  - "cat/Robotic_Foundation_Model_Development"
  - "sub/Language_Model_Vulnerabilities"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yao et al._2023_Bridging Language and Action A Survey of Language-Conditioned Robot Manipulation.pdf"
---

# Bridging Language and Action: A Survey of Language-Conditioned Robot Manipulation

> **저자**: Xiangtong Yao, Hongkuan Zhou, Oier Mees, Yuan Meng, Ted Xiao, Yonatan Bisk, Jean Oh, Edward Johns, Mohit Shridhar, Dhruv Shah, Jesse Thomason, Kai Huang, Joyce Chai, Zhenshan Bing, Alois Knoll | **날짜**: 2023-12-17 | **URL**: [https://arxiv.org/abs/2312.10807](https://arxiv.org/abs/2312.10807)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2. This architectural framework provides a high-level overview of language-conditioned robot manipulation. The ag*

자연언어 지시를 로봇의 물리적 행동으로 변환하는 language-conditioned robot manipulation 분야를 체계적으로 조사한 종합 서베이 논문으로, 언어가 로봇 시스템에 통합되는 4가지 주요 방식을 분류하고 최신 기술을 분석한다.

## Motivation

- **Known**: 로봇 조작(robot manipulation)은 산업 환경에서 반복적 작업에 성공했지만, 비전문가가 비구조화 환경(homes, hospitals, warehouses)에서 로봇을 제어하기 위해서는 자연언어 인터페이스가 필요하다는 것이 인식되어 있다.
- **Gap**: 기존 로봇 제어 방식(프로그래밍, teleoperation, 보상함수 엔지니어링)은 전문가 지식을 요구하여 일반대중 접근성이 낮고, language-conditioned manipulation의 다양한 최신 기술 진전을 체계적으로 정리한 종합 분류 체계가 부족하다.
- **Why**: 자연언어 기반 로봇 제어는 비전문가 접근성을 높이고, 양방향 통신을 통해 인간-로봇 신뢰를 구축하며, 언어적 상식 지식을 로봇 제어에 활용함으로써 일반목적 로봇의 대중화를 가능하게 한다.
- **Approach**: Language, Perception, Control 3개 모듈로 구성된 아키텍처 프레임워크를 제시하고, language의 역할 방식에 따라 (1) 상태 평가용, (2) 정책 조건용, (3) 인지 계획 추론용, (4) 통합 vision-language-action 모델로 분류하여 분석한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1. Language-conditioned manipulation sits at the inter-*

- **종합적 분류 체계**: language-conditioned robot manipulation의 4가지 통합 방식(state evaluation, policy condition, cognitive planning, unified models) 제시
- **다축 분석 프레임워크**: 행동 단위성(action granularity), 데이터/감독 체계, 시스템 비용/지연시간, 환경/평가, 크로스모달 작업 명세 5가지 축에서 기술 분석
- **최신 기술 통합**: Large Language Models(LLMs), Vision-Language Models(VLMs), Vision-Language-Action Models, diffusion models, neuro-symbolic models 등 최신 기초 모델 활용 방식 체계화
- **개방형 과제 제시**: 일반화 능력 향상과 안전성 문제 해결에 대한 미래 연구 방향 제시

## How

![Figure 2](figures/fig2.webp)

*Figure 2. This architectural framework provides a high-level overview of language-conditioned robot manipulation. The ag*

- 자연언어 처리를 위해 BERT, RoBERTa, GloVe 등 텍스트 임베딩 모델과 LLMs의 의미 추출 및 고수준 계획 능력 활용
- 환경 인식을 위해 ResNet, Vision Transformers(ViT), Faster-RCNN, YOLO 등 CNNs 및 transformer 기반 아키텍처 사용
- 언어-비전 연결을 위해 CLIP, Flamingo 등 VLMs의 joint embeddings 활용으로 언어-조건 객체 감지 및 분할 수행
- 행동 생성을 위해 policy learning(강화학습, 모방학습) 또는 classical planners/controllers 적용
- representative methods를 Figure 3에서 시간 순서대로 제시하고 다양한 보상 체계(Figure 4)를 분석

## Originality

- Language, Perception, Control의 3모듈 분해 아키텍처는 관례적 로봇학 분류와 달리 언어 통합 방식에 최적화된 새로운 체계
- 4가지 언어 통합 방식(state evaluation, policy condition, cognitive planning, unified vision-language-action)의 명확한 분류는 기존 문헌에 없는 체계적 분류체계
- 5가지 분석 축(행동 단위성, 데이터 체계, 비용/지연, 환경/평가, 크로스모달 명세)을 통한 다차원적 기술 비교 프레임워크
- LLMs의 semantic reasoning과 zero/few-shot generalization 활용을 통한 텍스트 기반 상식 지식의 로봇 제어 시스템 이전 메커니즘 분석

## Limitation & Further Study

- 서베이 논문의 본질적 한계로 제시된 추출 본문이 주로 서론과 기본 프레임워크에 국한되어 있으며, 각 기술별 상세 분석 내용 부족
- 비구조화 환경에서의 실제 배포 사례와 성능 메트릭에 대한 정량적 비교가 본 발췌에서는 제시되지 않음
- cross-embodiment learning이나 로봇 네비게이션 등 다양한 태스크에서의 일반화 성능 분석 내용 미흡
- 후속 연구로는 safety verification, 분포외(out-of-distribution) 상황 대응, human-in-the-loop 학습 개선이 필요하며, formal specification languages와 LLMs의 융합 방향 탐구 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 자연언어 기반 로봇 조작이라는 중요한 응용 분야를 최신 foundation models와 연계하여 종합적으로 정리한 높은 수준의 서베이로, 체계적인 분류와 명확한 아키텍처 프레임워크를 제시하여 향후 연구 방향을 제시한다.

## Related Papers

- 🔗 후속 연구: [[papers/1303_Advances_in_Embodied_Navigation_Using_Large_Language_Models/review]] — language-conditioned manipulation의 기초 이론을 LLM 기반 embodied navigation으로 확장 적용한다
- 🔄 다른 접근: [[papers/1334_Code_as_Policies_Language_Model_Programs_for_Embodied_Contro/review]] — 언어와 로봇 행동의 연결을 각각 종합적 조사와 코드 생성이라는 다른 방식으로 접근한다
- 🏛 기반 연구: [[papers/1435_Instruct2Act_Mapping_Multi-modality_Instructions_to_Robotic/review]] — multi-modal instruction mapping의 구체적 구현이 language-conditioned manipulation의 실제 적용을 보여준다
- 🔗 후속 연구: [[papers/1493_Neural_Scaling_Laws_in_Robotics/review]] — BridgeData V2의 대규모 로봇 학습과 신경망 스케일링 법칙이 데이터 규모의 중요성에서 상호 보완적이다.
- 🏛 기반 연구: [[papers/1511_LangWBC_Language-directed_Humanoid_Whole-Body_Control_via_En/review]] — 언어 조건부 정책 학습 분야의 전반적인 이론적 배경과 방법론적 토대를 제공함
- 🔗 후속 연구: [[papers/1605_PACE_Physics_Augmentation_for_Coordinated_End-to-end_Reinfor/review]] — 단안 비디오에서 접촉 가이드된 실제-시뮬레이션 변환이 PACE의 물리 가이드된 보상 설계를 위한 현실적인 데이터 확장 방법을 제공합니다.
- 🔗 후속 연구: [[papers/1297_A_Real-to-Sim-to-Real_Approach_to_Robotic_Manipulation_with/review]] — CRISP는 단안 비디오에서 접촉 기반 Real2Sim을 통해 VLM 생성 보상의 물리적 검증을 확장한다
- 🏛 기반 연구: [[papers/1303_Advances_in_Embodied_Navigation_Using_Large_Language_Models/review]] — language-conditioned robot manipulation의 기초 이론이 LLM 기반 navigation의 언어 이해에 토대를 제공한다
- 🔄 다른 접근: [[papers/1334_Code_as_Policies_Language_Model_Programs_for_Embodied_Contro/review]] — 언어 명령을 로봇 행동으로 변환하는 방식을 각각 직접 코드 생성과 language-conditioned learning으로 다르게 접근한다
