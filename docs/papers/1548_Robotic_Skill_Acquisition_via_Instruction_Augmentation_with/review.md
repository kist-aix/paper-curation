---
title: "1548_Robotic_Skill_Acquisition_via_Instruction_Augmentation_with"
authors:
  - "Ted Xiao"
  - "Harris Chan"
  - "Pierre Sermanet"
  - "Ayzaan Wahid"
  - "Anthony Brohan"
date: "2022.11"
doi: ""
arxiv: ""
score: 4.0
essence: "Vision-Language Model (CLIP)을 미세조정하여 주석이 없는 대규모 로봇 조작 데이터셋에 자동으로 자연어 명령어를 생성하고, 이를 통해 언어 조건부 정책을 학습하는 DIAL 방법을 제안한다."
tags:
  - "cat/Robotic_Foundation_Model_Development"
  - "sub/VLA_Architecture_Surveys"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Xiao et al._2022_Robotic Skill Acquisition via Instruction Augmentation with Vision-Language Models.pdf"
---

# Robotic Skill Acquisition via Instruction Augmentation with Vision-Language Models

> **저자**: Ted Xiao, Harris Chan, Pierre Sermanet, Ayzaan Wahid, Anthony Brohan, Karol Hausman, Sergey Levine, Jonathan Tompson | **날짜**: 2022-11-21 | **URL**: [https://arxiv.org/abs/2211.11736](https://arxiv.org/abs/2211.11736)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1: DIAL consists of three steps: (1) Contrastive fine-tuning of a vision-language model (VLM) such as CLIP [39] on *

Vision-Language Model (CLIP)을 미세조정하여 주석이 없는 대규모 로봇 조작 데이터셋에 자동으로 자연어 명령어를 생성하고, 이를 통해 언어 조건부 정책을 학습하는 DIAL 방법을 제안한다.

## Motivation

- **Known**: 최근 VLM (CLIP, ViLD)이 로봇 작업에 적용되어 표현 학습과 장면 기술에 활용되고 있으며, 언어 조건부 로봇 정책은 보통 수작업으로 주석된 대규모 데이터셋에 의존한다.
- **Gap**: 기존 방법들은 모든 데이터에 대해 비용 많이 드는 인간 주석이 필요한데, 대부분의 실제 로봇 데이터는 언어 설명이 부족하다. 이를 자동으로 해결할 수 있는 확장 가능한 방법이 부재하다.
- **Why**: 자동 주석 방법은 대규모 로봇 데이터셋의 활용을 극대화하여 라벨링 비용을 절감하고, 미주석 데이터에서도 새로운 능력을 학습할 수 있도록 한다.
- **Approach**: CLIP을 소량의 크라우드소싱 주석 데이터로 미세조정한 후, 이를 대규모 미주석 데이터셋에 적용하여 약한 주석을 생성하고, 생성된 주석 데이터로 behavior cloning을 통해 언어 조건부 정책을 학습한다.

## Achievement

![Figure 5](figures/fig5.webp)

*Fig. 5: Given the same starting scene, DIAL follows the instructions of (a) pick can which is on the right of*

- **자동 주석 생성**: CLIP 기반 VLM을 미세조정하여 80,000개 시연 중 96.5%의 미주석 데이터에 자동으로 자연어 명령어 생성
- **새로운 능력 습득**: 원본 데이터셋에 없는 60개의 새로운 명령어에 대해 41% 이상의 성능 향상 달성
- **확장성**: 대규모 실제 로봇 평가 1,300회 이상을 통해 방법의 실용성 검증

## How

![Figure 1](figures/fig1.webp)

*Fig. 1: DIAL consists of three steps: (1) Contrastive fine-tuning of a vision-language model (VLM) such as CLIP [39] on *

- CLIP의 vision encoder와 text encoder를 작은 크라우드소싱 주석 데이터셋 (2,800개 시연)에 대해 contrastive loss로 미세조정
- 미세조정된 VLM을 이용하여 큰 미주석 데이터셋 (77,200개 시연)에 대해 다양한 자연어 명령어 생성
- 원본 및 재주석된 데이터를 결합하여 behavior cloning을 통해 언어 조건부 정책 학습
- 학습된 정책을 원본 데이터셋에 없는 새로운 명령어에 대해 평가

## Originality

- VLM을 보상 모델이나 에이전트 아키텍처 성분으로 사용하는 대신 데이터셋 주석 도구로 활용하는 새로운 관점 제시
- Hindsight relabeling 개념을 VLM 기반 자동 주석으로 확장하여 실제 로봇 환경에 적용
- 미세조정된 VLM을 통해 인터넷 규모의 사전 학습 지식을 로봇 데이터에 효과적으로 전이

## Limitation & Further Study

- 미세조정에 필요한 초기 크라우드소싱 주석 데이터 (2,800개)의 수집 비용 여전히 필요
- VLM의 오류가 누적될 수 있으며, 생성된 주석의 품질 검증 메커니즘 부족
- 특정 로봇 환경(테이블탑 조작)에서만 평가되었으므로 다른 도메인 적용성 미확인
- 후속 연구: (1) 더 적은 초기 주석으로 시작하는 방법, (2) 생성된 주석의 신뢰도 평가 기법, (3) 다양한 로봇 플랫폼과 작업에 대한 확장

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: VLM을 데이터 주석 도구로 활용하는 실용적이고 확장 가능한 방법을 제시하며, 1,300회 이상의 실제 로봇 평가를 통해 효과를 입증했다. 로봇 학습의 비용 효율성을 크게 향상시킬 수 있는 가치 있는 기여이다.

## Related Papers

- 🏛 기반 연구: [[papers/1315_AutoRT_Embodied_Foundation_Models_for_Large_Scale_Orchestrat/review]] — AutoRT의 대규모 로봇 데이터 수집 경험을 바탕으로 CLIP 기반 자동 언어 주석을 통한 instruction augmentation을 개발한다.
- 🏛 기반 연구: [[papers/1454_HOMIE_Humanoid_Loco-Manipulation_with_Isomorphic_Exoskeleton/review]] — 자연어 지도학습의 기본 원리를 로봇 조작 데이터에 자동으로 언어 명령을 생성하는 방법으로 확장한다.
- 🔗 후속 연구: [[papers/1555_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to/review]] — RT-2의 vision-language 통합 아이디어를 주석이 없는 데이터에서 자동으로 언어 조건부 정책을 학습하는 방향으로 발전시킨다.
- 🏛 기반 연구: [[papers/1555_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to/review]] — vision-language model의 로봇 적용 가능성을 보여주어 자동 instruction augmentation 연구의 이론적 기반을 제공한다.
