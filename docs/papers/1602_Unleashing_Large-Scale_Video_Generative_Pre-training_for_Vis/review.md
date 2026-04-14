---
title: "1602_Unleashing_Large-Scale_Video_Generative_Pre-training_for_Vis"
authors:
  - "Hongtao Wu"
  - "Ya Jing"
  - "Chilam Cheang"
  - "Guangzeng Chen"
  - "Jiafeng Xu"
date: "2023.12"
doi: ""
arxiv: ""
score: 4.0
essence: "GR-1은 대규모 비디오 생성 사전학습을 활용하여 멀티태스크 언어-조건부 시각 로봇 조작을 학습하는 GPT-스타일 transformer 모델이다. 로봇은 언어 지시, 관찰 이미지, 로봇 상태를 입력받아 로봇 액션과 미래 이미지를 end-to-end 방식으로 예측한다."
tags:
  - "cat/Multimodal_Vision-Language_Policy_Learning"
  - "sub/Visual_Representation_Learning"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wu et al._2023_Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation.pdf"
---

# Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation

> **저자**: Hongtao Wu, Ya Jing, Chilam Cheang, Guangzeng Chen, Jiafeng Xu, Xinghang Li, Minghuan Liu, Hang Li, Tao Kong | **날짜**: 2023-12-20 | **URL**: [https://arxiv.org/abs/2312.13139](https://arxiv.org/abs/2312.13139)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Overview of GR-1. GR-1 is first pre-trained on the task of video prediction with a large-*

GR-1은 대규모 비디오 생성 사전학습을 활용하여 멀티태스크 언어-조건부 시각 로봇 조작을 학습하는 GPT-스타일 transformer 모델이다. 로봇은 언어 지시, 관찰 이미지, 로봇 상태를 입력받아 로봇 액션과 미래 이미지를 end-to-end 방식으로 예측한다.

## Motivation

- **Known**: Generative pre-trained 모델은 NLP와 CV 분야에서 뛰어난 성능을 보였으며, Transformer 기반의 sequential decision making 모델들이 로봇 조작에 적용되고 있다. 또한 로봇 학습을 위한 다양한 사전학습 방법이 연구되고 있다.
- **Gap**: 기존 로봇 학습 방법은 로봇 데이터의 희소성과 멀티모달성을 충분히 해결하지 못했으며, 대규모 비디오 데이터를 활용한 생성 사전학습과 로봇 조작을 직접적으로 연결하는 연구가 부족했다.
- **Why**: 로봇 데이터 수집은 비용과 시간이 많이 들기 때문에 대규모 비디오 데이터셋을 활용한 사전학습을 통해 로봇 일반화 능력을 향상시킬 수 있다. 이는 로봇 조작의 실용성과 확장성을 크게 향상시킨다.
- **Approach**: GR-1은 먼저 대규모 비디오 데이터셋에서 video prediction 작업으로 사전학습한 후, 로봇 데이터로 fine-tuning된다. 모델은 unified GPT-스타일 transformer 아키텍처를 유지하여 두 단계가 seamless하게 연결된다.

## Achievement

![Figure 3](figures/fig3.webp)

*Figure 3: CALVIN Benchmark Results. We show examples of multi-task learning trained on*

- **CALVIN 벤치마크 성능**: 성공률을 88.9%에서 94.9%로 개선, 평균 길이(5개 연속 작업 중 완료된 작업 수)를 3.06에서 4.21로 향상
- **데이터 효율성**: 전체 데이터의 10% 사용 시 77.8% 성공률 달성 (최고 기준 모델 66.8%)
- **Zero-shot 일반화**: 보지 못한 장면에 대해 성공률을 53.3%에서 85.4%로 개선
- **실제 로봇 검증**: 객체 이동 및 관절 객체 조작 작업에서 기준 모델보다 우수한 성능을 보이며 분포 외(out-of-distribution) 일반화 능력 입증

## How

![Figure 1](figures/fig1.webp)

*Figure 1: Overview of GR-1. GR-1 is first pre-trained on the task of video prediction with a large-*

- Language encoder를 통해 자연언어 지시를 인코딩
- Robot state encoder로 로봇 상태를 처리
- Observation 이미지 시퀀스와 로봇 상태를 시간 순서대로 입력
- Causal transformer를 사용하여 미래 이미지와 로봇 액션을 auto-regressive하게 생성
- Large-scale 비디오 데이터셋(Ego4D 등)에서 video prediction으로 사전학습
- CALVIN 벤치마크 및 실제 로봇 데이터로 fine-tuning
- Action과 Image 토큰을 learnable tokens로 구분하여 처리

## Originality

- 비디오 생성 사전학습을 로봇 조작 학습과 직접적으로 연결한 최초의 시도
- Unified GPT-스타일 transformer 모델로 비디오 예측과 로봇 정책을 같은 아키텍처에서 학습
- 대규모 비디오 데이터에서의 사전학습이 로봇 조작의 일반화 능력을 크게 향상시킬 수 있음을 실증적으로 입증
- Language-conditioned 멀티태스크 로봇 조작에 end-to-end 생성 모델 적용

## Limitation & Further Study

- 사전학습에 사용되는 비디오 데이터셋(예: Ego4D)이 로봇 조작과 직접적인 연관이 없을 수 있으며, 이 domain gap의 영향에 대한 상세한 분석 부족
- 실제 로봇 실험이 제한적이며, 더 다양한 로봇 플랫폼과 작업에 대한 검증 필요
- Fine-tuning 데이터 크기, 비디오 사전학습 데이터 크기 등 각 요소의 상세한 ablation 부족
- 모델의 계산 복잡도와 실시간 추론 성능에 대한 분석이 제시되지 않음
- 후속 연구로 더 다양한 비디오 소스와 로봇 도메인 간 transfer learning에 대한 연구 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: GR-1은 대규모 비디오 생성 사전학습을 로봇 조작에 적용하여 뛰어난 성능과 일반화 능력을 보인 의미 있는 연구이다. Unified GPT-스타일 아키텍처의 단순성과 CALVIN 벤치마크에서의 우수한 성과, 그리고 실제 로봇에서의 검증이 강점이며, 로봇 학습에서 생성 모델의 가능성을 처음으로 체계적으로 입증했다는 점에서 가치 있다.

## Related Papers

- 🔄 다른 접근: [[papers/1565_Scaling_Robot_Learning_with_Semantically_Imagined_Experience/review]] — 대규모 데이터를 활용한 로봇 학습의 다른 접근법으로 비디오 생성 사전학습과 데이터 증강을 비교할 수 있다.
- 🔗 후속 연구: [[papers/1581_Structured_World_Models_from_Human_Videos/review]] — 구조화된 world model을 대규모 비디오 생성 사전학습으로 발전시켜 멀티태스크 로봇 조작을 가능하게 한다.
- 🏛 기반 연구: [[papers/1632_World_Simulation_with_Video_Foundation_Models_for_Physical_A/review]] — 물리적 AI를 위한 비디오 기반 world 시뮬레이션의 기반이 되는 비디오 생성 사전학습 방법론을 제공한다.
- 🏛 기반 연구: [[papers/1419_H3DP_Triply-Hierarchical_Diffusion_Policy_for_Visuomotor_Lea/review]] — large-scale video generative pre-training이 humanoid world model 구축의 핵심 기반 기술입니다.
- 🔗 후속 연구: [[papers/1437_InternVLA-A1_Unifying_Understanding_Generation_and_Action_fo/review]] — large-scale video generative pre-training을 robot action과 통합하여 visually-grounded action learning을 달성합니다.
- 🧪 응용 사례: [[papers/1493_Neural_Scaling_Laws_in_Robotics/review]] — 대규모 비디오 생성 사전훈련과 로봇공학의 스케일링 법칙이 visuomotor policy에서 공통적으로 적용된다.
- 🏛 기반 연구: [[papers/1565_Scaling_Robot_Learning_with_Semantically_Imagined_Experience/review]] — 비디오 생성 사전학습 모델을 로봇 조작에 활용하는 기본 아이디어의 이론적 기반을 제공한다.
- 🏛 기반 연구: [[papers/1581_Structured_World_Models_from_Human_Videos/review]] — 비디오 생성 사전학습을 활용한 로봇 학습의 기반 아이디어를 구조화된 world model로 발전시킨다.
- 🏛 기반 연구: [[papers/1598_Unified_Video_Action_Model/review]] — 대규모 비디오 생성 사전학습을 비디오-액션 통합 학습으로 발전시킨 기반 아이디어를 제공한다.
- 🔗 후속 연구: [[papers/1599_Unified_Vision-Language-Action_Model/review]] — 대규모 비디오 생성 사전학습을 discrete token 기반 통합 VLA로 발전시킨다.
- 🔗 후속 연구: [[papers/1310_Any-point_Trajectory_Modeling_for_Policy_Learning/review]] — Unleashing Large-Scale Video Generative Pre-training이 ATM의 비디오 기반 궤적 예측을 더 대규모로 확장하여 강화할 수 있다.
