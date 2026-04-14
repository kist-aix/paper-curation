---
title: "1432_Improving_Vision-and-Language_Navigation_with_Image-Text_Pai"
authors:
  - "Arjun Majumdar"
  - "Ayush Shrivastava"
  - "Stefan Lee"
  - "Peter Anderson"
  - "Devi Parikh"
date: "2020.04"
doi: ""
arxiv: ""
score: 4.0
essence: "웹에서 수집한 대규모 이미지-텍스트 쌍으로 사전학습한 VLN-BERT 모델을 제안하여, 시각-언어 네비게이션 작업에서 객체 참조의 시각적 기초(grounding)를 개선한다."
tags:
  - "cat/Embodied_Navigation_and_Planning"
  - "sub/Language-Grounded_Action_Planning"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Majumdar et al._2020_Improving Vision-and-Language Navigation with Image-Text Pairs from the Web.pdf"
---

# Improving Vision-and-Language Navigation with Image-Text Pairs from the Web

> **저자**: Arjun Majumdar, Ayush Shrivastava, Stefan Lee, Peter Anderson, Devi Parikh, Dhruv Batra | **날짜**: 2020-04-30 | **URL**: [https://arxiv.org/abs/2004.14973](https://arxiv.org/abs/2004.14973)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1. We propose a compatibility model (right) for path selection in vision-and-*

웹에서 수집한 대규모 이미지-텍스트 쌍으로 사전학습한 VLN-BERT 모델을 제안하여, 시각-언어 네비게이션 작업에서 객체 참조의 시각적 기초(grounding)를 개선한다.

## Motivation

- **Known**: 기존 VLN 연구는 제한된 규모의 경로-지시 쌍(약 14k)으로만 학습해왔다. 웹 기반 시각-언어 사전학습(ViLBERT 등)은 단일 이미지 작업에서 성공했다.
- **Gap**: 웹 데이터의 정적이고 미학적인 이미지가 에이전트의 동적 관점과 다른 embodied VLN 작업으로 효과적으로 전이될 수 있는지 불명확하다.
- **Why**: VLN에서 'butterfly sculpture'나 'banister rail' 같은 장면 요소를 정확히 인식하려면 충분한 시각적 기초 학습이 필수적이며, 부족한 task-specific 데이터를 보충할 수 있다.
- **Approach**: BERT 기반 transformer 아키텍처를 경로-지시 쌍의 호환성 점수 모델로 개발하고, 언어 사전학습(Wikipedia/BooksCorpus) → 웹 이미지-텍스트 쌍(Conceptual Captions) → embodied 경로-지시 쌍의 3단계 학습 커리큘럼을 적용한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2. Images from the Conceptual Captions (CC) [24] (top) and Matterport3D*

- **경로 선택 성능 향상**: 단일 모델에서 success rate를 4.6 percentage point 증가, 앙상블 모델에서 3.0 percentage point 증가시켜 VLN 리더보드에서 73% 달성
- **웹 이미지-텍스트 사전학습의 효과**: Conceptual Captions 사전학습만으로 9.2 percentage point의 성능 향상 달성
- **학습 커리큘럼의 시너지 효과**: 각 단계가 유의미하며, 누적 효과가 개별 효과의 합보다 큼을 실증
- **시각적 기초 학습의 정성적 증거**: 그래디언트 기반 시각화로 모델이 합리적으로 객체 참조를 학습함을 입증

## How

![Figure 3](figures/fig3.webp)

*Fig. 3. We propose VLN-BERT (top), a visiolinguistic transformer-based model similar*

- VLN-BERT: 경로의 panoramic RGB 이미지 시퀀스와 네비게이션 지시를 입력받는 joint visiolinguistic transformer 모델
- 3단계 학습 커리큘럼: (1) BERT의 masked language modeling으로 언어 표현 학습, (2) ViLBERT 기반 웹 이미지-텍스트 쌍으로 시각-언어 기초 학습, (3) VLN 데이터셋의 경로-지시 쌍으로 fine-tuning
- 경로 선택: 기존 에이전트 모델로 beam search로 후보 경로 생성 후 VLN-BERT의 호환성 점수로 재순위화
- 공간 정보 인코딩: 각 이미지 영역에 대해 visual features뿐 아니라 공간 위치 정보 포함
- 그래디언트 기반 시각화: instruction 수정(예: 'fridge' 제거)에 따른 이미지 영역 중요도 변화 분석

## Originality

- Embodied AI 작업으로의 웹 기반 시각-언어 사전학습 전이 효과를 처음 체계적으로 조사
- 경로-지시 호환성을 판별 모델(discriminative model)로 명시적으로 학습 (기존의 follower/speaker 모델과 차별화)
- Domain shift 문제(curated 웹 이미지 vs. embodied 관점)를 인식하고 이를 해결하는 학습 커리큘럼 설계
- Panoramic 이미지 시퀀스 처리를 위한 VLN-BERT 아키텍처 확장

## Limitation & Further Study

- 웹 데이터와 embodied 데이터 간의 domain shift 문제를 완전히 해결하지 못함 (Fig. 2에서 보듯이 구성상 차이 존재)
- Unseen 환경에서의 성능 평가가 부분적이며, fully-observed 설정에서만 주요 결과 제시
- 학습 커리큘럼의 각 단계 기여도에 대한 더 깊은 분석 필요 (예: 웹 데이터의 특정 카테고리별 효과)
- 후속 연구: embodied 데이터와 웹 데이터 간의 적응(adaptation) 방법 개발, unseen 환경에서의 일반화 성능 개선, 다양한 embodied 작업으로의 확장

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 웹 규모의 비정체화된 시각-언어 데이터를 embodied 네비게이션에 효과적으로 활용하는 실질적인 방법을 제안하며, 명확한 성능 개선과 체계적인 ablation study를 통해 학습 커리큘럼의 가치를 입증한 견고한 연구이다.

## Related Papers

- 🔗 후속 연구: [[papers/1367_EgoActor_Grounding_Task_Planning_into_Spatial-aware_Egocentr/review]] — DivScene의 대규모 객체 범주가 VLN-BERT의 객체 참조 grounding을 확장한다.
- 🏛 기반 연구: [[papers/1378_Embodied_Navigation_Foundation_Model/review]] — NavFoM의 크로스-태스크 네비게이션이 VLN-BERT의 vision-language 사전학습에 기반한다.
- 🔄 다른 접근: [[papers/1607_Vision-Language_Navigation_A_Survey_and_Taxonomy/review]] — Vision-Language Navigation 서베이도 시각-언어 네비게이션의 전반적 발전을 다룬다.
- 🏛 기반 연구: [[papers/1367_EgoActor_Grounding_Task_Planning_into_Spatial-aware_Egocentr/review]] — VLN-BERT의 vision-language 사전학습이 DivScene의 LVLM 기반 네비게이션의 기초가 된다.
