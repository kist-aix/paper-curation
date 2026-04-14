---
title: "1454_Learning_Transferable_Visual_Models_From_Natural_Language_Su"
authors:
  - "Alec Radford"
  - "Jong Wook Kim"
  - "Chris Hallacy"
  - "Aditya Ramesh"
  - "Gabriel Goh"
date: "2021.02"
doi: ""
arxiv: ""
score: 4.0
essence: "400만 개의 (이미지, 텍스트) 쌍 데이터셋에서 이미지-텍스트 대조 학습(contrastive learning)을 통해 전이 가능한 시각 모델을 학습하고, 자연언어를 이용한 zero-shot 전이로 30개 이상의 다양한 컴퓨터 비전 작업에서 경쟁력 있는 성능을 달성한다."
tags:
  - "cat/Multimodal_Vision-Language_Policy_Learning"
  - "sub/Self-Supervised_Vision_Learning"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Radford et al._2021_Learning Transferable Visual Models From Natural Language Supervision.pdf"
---

# Learning Transferable Visual Models From Natural Language Supervision

> **저자**: Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, Ilya Sutskever | **날짜**: 2021-02-26 | **URL**: [https://arxiv.org/abs/2103.00020](https://arxiv.org/abs/2103.00020)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1. Summary of our approach. While standard image models jointly train an image feature extractor and a linear cla*

400만 개의 (이미지, 텍스트) 쌍 데이터셋에서 이미지-텍스트 대조 학습(contrastive learning)을 통해 전이 가능한 시각 모델을 학습하고, 자연언어를 이용한 zero-shot 전이로 30개 이상의 다양한 컴퓨터 비전 작업에서 경쟁력 있는 성능을 달성한다.

## Motivation

- **Known**: 기존 컴퓨터 비전 모델은 고정된 범주의 객체만 인식하도록 훈련되어 새로운 개념을 다루려면 추가 레이블 데이터가 필요하다. NLP에서는 웹 규모의 텍스트 사전학습이 GPT 계열 모델의 성능을 크게 향상시켰다.
- **Gap**: 이전의 이미지-캡션 학습 방법들은 작은 규모 데이터셋(100K-200K)에서만 훈련되어 성능이 낮았고, 약한 지도학습 접근법들은 감독 신호를 수동으로 제한(1000~18291개 클래스)해야 했다.
- **Why**: 자연언어는 무제한의 시각 개념을 표현할 수 있으므로 웹 규모의 데이터로부터 효율적인 사전학습이 가능하며, zero-shot 전이 능력은 다양한 다운스트림 작업에 대한 범용성을 제공한다.
- **Approach**: 400백만 개의 공개 인터넷 (이미지, 텍스트) 쌍에서 contrastive learning 목표로 이미지 인코더와 텍스트 인코더를 공동 훈련하고, 사전학습 후 자연언어 프롬프트로 zero-shot 분류기를 구성한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2. CLIP is much more efﬁcient at zero-shot transfer*

- **확장성과 효율성**: CLIP은 400M 이미지를 처리하며 이전 bag-of-words 방법 대비 4배 효율적이고, compute에 따른 성능이 매끄러운 확장 법칙을 따른다
- **Zero-shot 성능**: ImageNet에서 ResNet-50 수준의 정확도(약 50%)를 1.28M 훈련 예제 없이 달성하며, 30개 이상의 다양한 데이터셋(OCR, 행동 인식, 지리정보화, 미세한 객체 분류)에서 경쟁력 있는 성능을 보인다
- **강건성**: Zero-shot CLIP 모델이 동등한 정확도의 supervised ImageNet 모델보다 훨씬 강건하며, 분포 이동에 더 잘 대응한다
- **다중 작업 학습**: 단일 사전학습으로 OCR, 지리정보화, 행동 인식 등 다양한 작업을 자동으로 수행하는 능력을 습득한다

## How

![Figure 1](figures/fig1.webp)

*Figure 1. Summary of our approach. While standard image models jointly train an image feature extractor and a linear cla*

- 400백만 개의 (이미지, 텍스트) 쌍을 인터넷에서 수집하고 개방 데이터셋을 활용한다
- Contrastive pre-training: 배치 내 모든 (이미지, 텍스트) 쌍에 대해 유사도 행렬을 구성하고, 올바른 대응만을 최대화하는 대조 손실함수를 사용한다
- 이미지 인코더(CNN 또는 Vision Transformer 기반)와 텍스트 인코더(Transformer 기반) 아키텍처를 병렬로 훈련한다
- Zero-shot 추론: 클래스명 또는 설명(예: 'A photo of a dog')을 텍스트 인코더로 인코딩하여 선형 분류기를 동적으로 구성한다", '8개 모델 시리즈를 통해 계산량 범위에 걸친 확장성을 체계적으로 평가한다

## Originality

- 이전 이미지-캡션 학습과 달리 400M 규모의 대규모 데이터셋으로 확장하여 실질적인 성능 달성을 입증한다
- Contrastive objective를 bag-of-words 예측보다 4배 더 효율적임을 실증적으로 보이고, transformer 언어 모델 대비 3배 효율성을 달성한다
- Zero-shot 전이의 일반화 능력을 30개 이상의 다양한 데이터셋에서 체계적으로 평가한다
- 자연언어 지도 신호의 풍부성을 활용하여 동적 분류기 합성과 프롬프트 엔지니어링 가능성을 보여준다

## Limitation & Further Study

- ImageNet zero-shot 정확도(~50%)는 여전히 fully supervised ResNet-50(~76%)보다 상당히 낮으며, 데이터셋 특화 미세조정이 추가 성능 향상을 위해 필요할 수 있다
- 프롬프트 엔지니어링의 효과가 클래스마다 크게 다르며, 최적 프롬프트 설계 과정이 수동적이다
- 이미지-텍스트 쌍 데이터의 품질과 편향성이 학습된 표현의 공정성과 특정 개념의 강건성에 영향을 미칠 수 있다
- 텍스트 인코더에 대한 상세 분석이 부족하며, 언어 이해 능력의 한계가 zero-shot 성능을 제한할 수 있다
- **후속 연구**: 더 효율적인 프롬프트 자동화, 데이터 편향성 완화, 세밀한 시각적 개념에 대한 성능 향상, 멀티모달 표현의 해석가능성 연구

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: CLIP은 대규모 자연언어 지도학습을 통해 zero-shot 전이 성능의 새로운 기준을 제시하며, 간단한 contrastive 학습 목표의 확장성을 입증함으로써 다양한 비전 작업에 대한 범용 시각 모델의 가능성을 열었다.

## Related Papers

- 🔗 후속 연구: [[papers/1415_Grounding_DINO_Marrying_DINO_with_Grounded_Pre-Training_for/review]] — CLIP의 contrastive learning 방법론이 Grounding DINO의 vision-language grounding에 핵심적으로 적용됩니다.
- 🔄 다른 접근: [[papers/1571_Sigmoid_Loss_for_Language_Image_Pre-Training/review]] — 둘 다 vision-language pre-training이지만 CLIP는 contrastive에, Sigmoid Loss는 다른 loss function에 중점을 둡니다.
- 🔗 후속 연구: [[papers/1365_DINOv2_Learning_Robust_Visual_Features_without_Supervision/review]] — CLIP의 supervised contrastive learning을 unsupervised visual feature learning인 DINOv2로 확장한 발전된 형태입니다.
- 🏛 기반 연구: [[papers/1415_Grounding_DINO_Marrying_DINO_with_Grounded_Pre-Training_for/review]] — CLIP의 contrastive learning이 Grounding DINO의 vision-language grounding 메커니즘의 핵심 기반 기술입니다.
- 🔄 다른 접근: [[papers/1520_R3M_A_Universal_Visual_Representation_for_Robot_Manipulation/review]] — 자연어 감독을 통한 시각 모델 학습과 인간 비디오 기반 표현 학습은 서로 다른 접근이지만 상호 보완적이다
- 🏛 기반 연구: [[papers/1611_Visual_Instruction_Tuning/review]] — CLIP의 vision-language pre-training이 Visual Instruction Tuning의 multimodal 정렬 학습 기반이 된다
- 🔄 다른 접근: [[papers/1365_DINOv2_Learning_Robust_Visual_Features_without_Supervision/review]] — CLIP의 natural language supervision이 DINOv2의 unsupervised approach와 대조되는 vision feature learning 방법을 제시한다.
- 🏛 기반 연구: [[papers/1571_Sigmoid_Loss_for_Language_Image_Pre-Training/review]] — 자연어 감독을 통한 시각 모델 학습의 기반이 되는 언어-이미지 사전학습 손실 함수를 제공한다.
