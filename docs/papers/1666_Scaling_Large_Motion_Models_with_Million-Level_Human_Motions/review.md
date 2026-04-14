---
title: "1666_Scaling_Large_Motion_Models_with_Million-Level_Human_Motions"
authors:
  - "Ye Wang"
  - "Sipeng Zheng"
  - "Bin Cao"
  - "Qianshan Wei"
  - "Weishuai Zeng"
date: "2024.10"
doi: ""
arxiv: ""
score: 4.0
essence: "LLM의 성공에 영감을 받아 백만 단위 규모의 대규모 모션 데이터셋 MotionLib를 구축하고, 이를 기반으로 Being-M0 모델을 훈련하여 대규모 모션 생성 모델의 확장성을 입증하는 연구이다."
tags:
  - "cat/Other"
  - "topic/humanoid"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2024_Scaling Large Motion Models with Million-Level Human Motions.pdf"
---

# Scaling Large Motion Models with Million-Level Human Motions

> **저자**: Ye Wang, Sipeng Zheng, Bin Cao, Qianshan Wei, Weishuai Zeng, Qin Jin, Zongqing Lu | **날짜**: 2024-10-04 | **URL**: [https://arxiv.org/abs/2410.03311](https://arxiv.org/abs/2410.03311)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: TOP: While existing models perform well on*

LLM의 성공에 영감을 받아 백만 단위 규모의 대규모 모션 데이터셋 MotionLib를 구축하고, 이를 기반으로 Being-M0 모델을 훈련하여 대규모 모션 생성 모델의 확장성을 입증하는 연구이다.

## Motivation

- **Known**: Text-to-motion 생성 분야에서 VQ와 같은 벡터 양자화 기법과 CLIP, GPT-2 같은 인코더-디코더를 활용한 접근법이 존재한다. LLM의 성공은 대규모 데이터와 모델 크기 확장의 중요성을 보여준다.
- **Gap**: 현존하는 모션 생성 데이터셋(Motion-X, HumanML3D)은 크기가 매우 제한적이고, 모션 데이터의 비용 높음과 주석 작업의 복잡성으로 인해 대규모 모션 모델 개발이 어렵다. 또한 기존 VQ 기반 방식은 정보 손실과 제한된 코드북 크기로 인한 표현력 부족 문제가 있다.
- **Why**: 모션 생성은 게임, 영화, 로봇공학 등 다양한 실제 응용 분야를 가지고 있으며, 대규모 모션 모델의 개발은 다양한 모션에 대한 일반화 성능과 미지의 활동에 대한 생성 능력을 크게 향상시킬 수 있다.
- **Approach**: 체계적인 데이터 수집 파이프라인을 통해 120만 개 이상의 모션 시퀀스를 포함하는 MotionLib를 구축하고, 계층적 텍스트 설명을 추가하였다. MotionBook이라는 새로운 모션 인코딩 방식(2D-LFQ)을 제안하여 정보 손실을 최소화하고 코드북 용량을 확대한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: TOP: While existing models perform well on*

- **MotionLib 데이터셋**: 기존 데이터셋 대비 최소 15배 규모의 120만 개 이상 모션 시퀀스와 계층적 텍스트 주석을 포함하는 첫 번째 백만 규모 모션 생성 데이셋을 구축했다.
- **Being-M0 모델**: MotionLib를 활용하여 훈련된 대규모 모션 모델로서 미지의 활동을 포함한 광범위한 인간 활동에 대해 강건한 성능을 입증했다.
- **확장 법칙 규명**: 모션 생성에서 데이터 및 모델 크기 확장의 중요성을 처음으로 체계적으로 입증하고, 관절 예측 오류를 감소시키며 새로운 모션에 대한 일반화 성능을 개선했다.
- **MotionBook 인코딩**: 손실이 없는 컴팩트한 모션 특성 표현과 2D lookup-free 모션 tokenizer(2D-LFQ)를 제안하여 모션 코드북을 최소 100배 이상 확대하고 세부 모션 특성을 보존했다.

## How

![Figure 4](figures/fig4.webp)

*Figure 4: Comparison with different motion quantization on Motion-X (left) and MotionLib (right). We only show MPJPE*

- 대규모 모션 데이터셋 구축: Motion-X, HumanML3D 기존 데이터셋에 새로운 수집 데이터(93%)를 추가하여 MotionLib 구성
- 계층적 텍스트 주석: 단순 텍스트 설명 대신 상세한 계층적 텍스트 설명(상체, 하체 등) 추가로 표현 능력 강화
- 모션 인코딩 개선: 기존 H3D-format 특성의 정보 손실 문제를 해결하기 위해 더 효율적인 손실이 없는 특성 선택
- 2D-LFQ tokenizer 제안: 모션 시퀀스를 1D 임베딩 대신 2D 이미지(T×D×1)로 재구성하여 인코더 용량 확대
- Lookup-free 양자화: Mentzer et al. (2023)의 finite scalar quantization에 영감을 받아 코드북 붕괴를 방지하면서 대규모 모션 어휘 학습 가능하게 함
- 모델 스케일링 실험: 0.36B에서 13B까지 다양한 크기의 모델로 스케일링 법칙을 실증적으로 검증

## Originality

- 첫 번째 백만 규모 모션 생성 데이터셋인 MotionLib 구축으로 ImageNet 수준의 시각 벤치마크와 비교 가능한 규모 달성
- 2D-LFQ라는 lookup-free 모션 tokenizer 제안으로 기존 VQ 방식의 정보 손실과 코드북 크기 제한 문제를 혁신적으로 해결
- 모션 생성 분야에서 처음으로 데이터 및 모델 크기 확장의 효과를 체계적으로 규명하고 스케일링 법칙 제시
- 계층적 세부 텍스트 주석을 통해 기존의 단순 텍스트 설명보다 훨씬 풍부한 의미 정보 제공

## Limitation & Further Study

- 데이터셋 품질 검증: MotionLib의 구성 중 93%가 새로 수집된 데이터인데, 이들의 일관된 품질 관리 및 검증 방법에 대한 상세 설명이 부족하다.
- 모델 크기 최적점: 13B까지의 실험만 수행되었으며, 더 큰 규모 모델에서의 성능 수렴 특성이나 최적점 존재 여부는 미확인이다.
- 특정 활동 범주 성능: 미지의 활동에 대한 일반화는 보여주었으나, 특정 도전적인 모션(미세한 손가락 움직임, 복합 상호작용 등)에 대한 성능 한계는 명확하지 않다.
- 실시간 생성 평가: 애니메이션 등 실제 응용에서의 실시간 생성 성능과 지연 시간에 대한 평가가 제시되지 않았다.
- 후속 연구 방향: 더 큰 스케일의 모델 훈련, 다중 모달리티(음성, 이미지 등)와의 통합, 물리 기반 제약 조건 통합 등이 탐구될 필요가 있다.

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 모션 생성 분야에서 대규모 데이터와 모델 확장의 중요성을 처음으로 체계적으로 입증하며, MotionLib와 2D-LFQ 기술을 통해 실질적인 기여를 제공한다. 모션 생성 모델 개발의 새로운 기준을 제시하고 향후 연구의 견고한 기초를 마련한 중요한 연구이다.