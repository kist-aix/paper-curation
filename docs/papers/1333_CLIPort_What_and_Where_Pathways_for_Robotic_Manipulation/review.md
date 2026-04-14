---
title: "1333_CLIPort_What_and_Where_Pathways_for_Robotic_Manipulation"
authors:
  - "Mohit Shridhar"
  - "Lucas Manuelli"
  - "Dieter Fox"
date: "2021.09"
doi: ""
arxiv: ""
score: 4.0
essence: "CLIPort는 CLIP의 의미론적 이해(what)와 Transporter의 공간적 정밀성(where)을 결합한 두 스트림 아키텍처를 통해, 자연어 명령으로 조건화된 로봇 조작 에이전트를 제시한다."
tags:
  - "cat/Embodied_Navigation_and_Planning"
  - "sub/Spatial_Language_Understanding"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Shridhar et al._2021_CLIPort What and Where Pathways for Robotic Manipulation.pdf"
---

# CLIPort: What and Where Pathways for Robotic Manipulation

> **저자**: Mohit Shridhar, Lucas Manuelli, Dieter Fox | **날짜**: 2021-09-24 | **URL**: [https://arxiv.org/abs/2109.12098](https://arxiv.org/abs/2109.12098)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2. CLIPORT Two-Stream Architecture. An overview of the semantic and spatial streams. The semantic stream uses a f*

CLIPort는 CLIP의 의미론적 이해(what)와 Transporter의 공간적 정밀성(where)을 결합한 두 스트림 아키텍처를 통해, 자연어 명령으로 조건화된 로봇 조작 에이전트를 제시한다.

## Motivation

- **Known**: End-to-end 신경망은 정밀한 공간 추론이 필요한 기술을 학습할 수 있으나 새로운 목표에 대한 일반화가 어렵고, 대규모 인터넷 데이터로 학습된 vision-language 모델은 뛰어난 의미론적 표현을 제공하나 미세한 조작에 필요한 공간 이해가 부족하다.
- **Gap**: End-to-end 조작 학습의 정밀성과 vision-language 모델의 의미론적 일반화 능력을 동시에 갖춘 프레임워크가 부재하며, 기존 언어-그라운딩 파이프라인은 객체 중심 표현으로 제한되어 변형 가능한 객체나 과립형 미디어를 처리하지 못한다.
- **Why**: 로봇이 인간과 같이 추상적 개념을 정확한 공간 행동으로 효율적으로 변환할 수 있다면, 현실적인 인간-로봇 상호작용에서 새로운 데모나 목표 이미지 수집의 필요성을 제거하여 실용성을 크게 향상시킬 수 있다.
- **Approach**: Pick-and-place 어포던스 예측으로 테이블탑 조작을 공식화하고, 사전학습된 CLIP 모델의 시각-언어 특성으로 의미론적 스트림을 조건화하면서 Transporter의 공간 정밀성을 유지하는 두 스트림 아키텍처를 제안한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1. Language-Conditioned Manipulation Tasks: CLIPORT is a broad framework applicable to a wide range of language-c*

- **멀티태스크 정책**: 10개의 시뮬레이션 태스크와 9개의 실제 로봇 태스크를 단일 모델로 학습하여 단일 태스크 정책과 동등하거나 우수한 성능 달성
- **데이터 효율성**: 실제 로봇 환경에서 단 179개의 이미지-액션 쌍으로 9개 태스크 학습 가능
- **의미론적 전이**: 학습 데이터에 없는 'pink block'과 같은 속성을 다른 태스크에서 효과적으로 전이", '**벤치마크 확대**: 1000개 이상의 고유 인스턴스를 가진 10개의 언어-조건화 조작 태스크 제시
- **명시적 표현 제거**: 객체 포즈, 인스턴스 분할, 메모리, 상징적 상태 등 명시적 표현 없이 end-to-end 학습

## How

![Figure 2](figures/fig2.webp)

*Figure 2. CLIPORT Two-Stream Architecture. An overview of the semantic and spatial streams. The semantic stream uses a f*

- CLIP의 사전학습된 비전-언어 임베딩을 의미론적 스트림의 조건화 신호로 활용
- Transporter의 equivariant spatial 표현을 공간적 스트림으로 유지하여 픽셀 단위 정밀성 확보
- Action-centric 인지를 통해 객체 감지 대신 어포던스 (pick/place 위치) 직접 예측
- Pick-and-place 프리미티브를 2-step 행동으로 정의하여 순차적 조작 구성
- 자연언어 명령어를 CLIP 인코더로 인코딩하여 시각 특성과 정렬
- Ravens 시뮬레이터에서 대규모 데이터셋으로 학습 후 실제 로봇으로 전이

## Originality

- Vision-language 모델(CLIP)을 미세한 공간 조작 작업에 직접 적용한 최초 사례
- Two-stream 아키텍처를 통한 의미론적-공간적 경로의 체계적 분리 및 통합
- Action-centric 인식을 기반으로 명시적 객체 표현 없이 언어-조건화 조작 구현
- 단일 멀티태스크 정책으로 10개 시뮬레이션 및 9개 실제 로봇 태스크 동시 수행
- 인지 심리학의 두 스트림 가설(dorsal/ventral stream)을 로봇 조작에 비유적으로 적용

## Limitation & Further Study

- 테이블탑 환경에 국한되어 3D 조작 공간이 제한적
- CLIP 모델의 사전학습 데이터에 포함되지 않은 개념에 대한 일반화 능력 미검증
- Suction gripper와 parallel-jaw gripper 같은 단순 그리퍼에 제한되며, 손가락이 많은 데스터러스 손에 대한 확장 가능성 미불명
- 실제 로봇 실험이 제한적(179 샘플)이므로 더 복잡한 현실 환경에서의 견건성 검증 필요
- 언어 표현의 복잡성(예: 공간 관계 표현) 및 모호성에 대한 체계적 분석 부족
- 후속 연구: 3D 다중 팔 조작, 강화학습과의 결합, 설명 가능성 향상, 장기 작업 계획 능력 확대

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: CLIPort는 대규모 사전학습 vision-language 모델을 정밀 로봇 조작과 효과적으로 결합하여 언어-조건화 멀티태스크 학습의 새로운 패러다임을 제시했으며, 실제 로봇에서의 데이터 효율성과 의미론적 일반화 능력은 로봇 조작 분야에 상당한 실질적 기여를 한다.

## Related Papers

- 🔗 후속 연구: [[papers/1622_VoxPoser_Composable_3D_Value_Maps_for_Robotic_Manipulation_w/review]] — VoxPoser는 CLIPort의 공간적 정밀성을 3D 값 맵을 통한 구성 가능한 조작으로 확장한다
- 🔄 다른 접근: [[papers/1574_SKT_Integrating_State-Aware_Keypoint_Trajectories_with_Visio/review]] — SKT는 CLIPort와 유사하게 공간적 정보와 의미론적 이해를 결합하지만 키포인트 궤적 기반 접근법을 사용한다
- 🏛 기반 연구: [[papers/1576_SpatialVLA_Exploring_Spatial_Representations_for_Visual-Lang/review]] — SpatialVLA는 CLIPort의 공간적 표현을 Vision-Language-Action 모델로 확장하는 기반을 제공한다
