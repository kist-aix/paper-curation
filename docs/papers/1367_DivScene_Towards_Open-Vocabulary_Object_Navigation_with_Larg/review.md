---
title: "1367_DivScene_Towards_Open-Vocabulary_Object_Navigation_with_Larg"
authors:
  - "Zhaowei Wang"
  - "Hongming Zhang"
  - "Tianqing Fang"
  - "Ye Tian"
  - "Yue Yang"
date: "2024.10"
doi: ""
arxiv: ""
score: 4.0
essence: "Large Vision-Language Models (LVLMs)의 embodied 환경 이해와 네비게이션 능력을 탐구하기 위해 81개 장면 유형과 5,707개 객체 범주를 포함하는 대규모 데이터셋 DivScene을 제시하고, CoT 설명을 통한 fine-tuning으로 GPT-4o를 20% 이상 상회하는 성능 달성."
tags:
  - "cat/Embodied_Navigation_and_Planning"
  - "sub/Open-Vocabulary_Scene_Navigation"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2024_DivScene Towards Open-Vocabulary Object Navigation with Large Vision Language Models in Diverse Sce.pdf"
---

# DivScene: Towards Open-Vocabulary Object Navigation with Large Vision Language Models in Diverse Scenes

> **저자**: Zhaowei Wang, Hongming Zhang, Tianqing Fang, Ye Tian, Yue Yang, Kaixin Ma, Xiaoman Pan, Yangqiu Song, Dong Yu | **날짜**: 2024-10-03 | **URL**: [https://arxiv.org/abs/2410.02730](https://arxiv.org/abs/2410.02730)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: Data collection process. On the left, we show the process of collecting scenes. We prompt GPT-4o to*

Large Vision-Language Models (LVLMs)의 embodied 환경 이해와 네비게이션 능력을 탐구하기 위해 81개 장면 유형과 5,707개 객체 범주를 포함하는 대규모 데이터셋 DivScene을 제시하고, CoT 설명을 통한 fine-tuning으로 GPT-4o를 20% 이상 상회하는 성능 달성.

## Motivation

- **Known**: LVLMs는 VQA와 문서 이해에서 우수한 성능을 보이고 있으나, 기존 object navigation 벤치마크(Matterport-3D의 21개 객체, ProcTHOR의 16개 객체)는 제한된 다양성을 가지고 있어 closed-vocab 작업에만 집중되어 있음.
- **Gap**: open-vocabulary object navigation 작업에서 LVLM의 성능이 미흡하며, 실제 환경의 다양성을 반영할 수 있는 충분히 큰 규모의 다양한 장면과 객체를 포함하는 벤치마크가 부재.
- **Why**: Open-vocabulary navigation은 현실적인 로봇 네비게이션 응용에 필수적이며, LVLM의 실제 embodied 환경 이해 능력을 종합적으로 평가할 수 있는 기초를 제공함.
- **Approach**: MIT Scenes Dataset의 81개 장면 유형을 기반으로 GPT-4를 활용해 자동 생성된 다양한 집 설명으로 Holodeck 프레임워크를 통해 4,614개 가상 주택을 구축하고, BFS를 이용한 최단 경로 에피소드 샘플링으로 학습 데이터 생성 후 Idefics 2 모델을 CoT 설명과 함께 fine-tuning.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: Data collection process. On the left, we show the process of collecting scenes. We prompt GPT-4o to*

- **DivScene 데이터셋 구축**: 4,614개 가상 주택, 81개 장면 유형, 5,707개 대상 객체 범주를 포함하는 기존 데이터셋보다 훨씬 더 다양한 open-vocabulary navigation 벤치마크 제시
- **NATVLM 모델 개발**: Idefics 2 기반 fine-tuned 모델이 GPT-4o 대비 약 20% 높은 성공률 달성
- **효율적 학습 방법**: 인간 주석 없이 BFS로 생성된 최단 경로만으로도 LVLM의 네비게이션 능력이 크게 향상될 수 있음을 입증
- **다중 데이터셋 일반화**: ProcTHOR, iTHOR, HM3D 등 3개 미공개 데이터셋에서 일반화 성능 검증

## How

![Figure 2](figures/fig2.webp)

*Figure 2: Data collection process. On the left, we show the process of collecting scenes. We prompt GPT-4o to*

- MIT Scenes Dataset의 81개 장면 유형을 기반으로 선택 및 분류
- GPT-4에 프롬프트를 통해 조명, 객체, 기타 속성을 포함한 다양한 집 설명 자동 생성
- Holodeck 프레임워크를 활용해 텍스트 설명으로부터 AI2THOR 플랫폼 상에서 가상 주택 자동 구축
- 각 주택에서 임의의 시작 위치와 대상 객체를 설정하고 0.25m 격자 맵으로 이산화한 후 BFS로 최단 경로 탐색
- MOVEAHEAD, ROTATERIGHT, ROTATELEFT, DONE 액션 공간 정의
- 총 약 23K개의 최단 경로 에피소드 샘플링
- Idefics 2 모델을 imitation learning으로 fine-tuning하되 각 액션 예측에 대한 CoT 설명 트레이스를 수동 수집하여 학습 데이터에 포함
- 다양한 LVLM 및 LLM 기반 베이스라인과 비교 평가

## Originality

- Open-vocabulary object navigation 작업을 공식적으로 정의하고 기존 dataset의 100배 이상 많은 객체 범주(5,707개)를 포함하는 새로운 대규모 벤치마크 제시
- 자동화된 집 생성 파이프라인(GPT-4 + Holodeck)을 통해 인간 주석의 부담을 크게 감소시키면서도 높은 다양성 달성
- CoT 설명을 navigation 작업에 통합하여 LVLM의 이해도를 향상시키는 novel 접근법
- BFS 최단 경로만으로 효과적인 학습이 가능함을 보여 강화학습 기반 접근법 대비 훨씬 경제적이고 효율적인 대안 제시

## Limitation & Further Study

- AI2THOR 플랫폼에만 국한되어 현실 세계 환경으로의 직접 적용 가능성 제한
- BFS 기반 최단 경로가 실제 navigation의 다양성을 완전히 대표하지 못할 수 있으며, 예외적 상황이나 비-최적 경로 처리 능력 미흡
- CoT 설명의 수동 수집으로 인한 확장성 한계 및 주관적 편향 가능성
- 현재 모델의 절대적 성공률이 여전히 50% 미만(NATVLM 약 50%)으로 실제 응용에 충분하지 않을 수 있음
- 후속 연구: (1) 현실 환경에서의 검증, (2) 자동 CoT 생성 기법 개발, (3) 더 큰 규모의 LVLM 활용 및 fine-tuning 전략 개선, (4) 복합 객체 관계나 공간 추론 능력 강화

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 open-vocabulary object navigation 작업을 처음 체계적으로 정의하고 기존의 100배 이상 다양한 객체를 포함하는 대규모 벤치마크를 제시하여 높은 학술적 기여도를 가짐. LVLM의 embodied AI 능력을 평가하기 위한 중요한 자산을 제공하며, BFS 기반 이모테이션 러닝과 CoT 설명의 조합으로 실용적이고 효율적인 학습 방법을 제시한 점이 탁월함.