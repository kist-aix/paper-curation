---
title: "1560_SARA-RT_Scaling_up_Robotics_Transformers_with_Self-Adaptive"
authors:
  - "Isabel Leal"
  - "Krzysztof Choromanski"
  - "Deepali Jain"
  - "Avinava Dubey"
  - "Jake Varley"
date: "2023.12"
doi: ""
arxiv: ""
score: 4.0
essence: "SARA-RT는 Robotics Transformer를 on-robot 배포에 적합하도록 선형 주의(linear attention)로 변환하는 up-training 방법을 제시하여, quadratic 복잡도의 모델을 high quality 유지하면서 효율화한다."
tags:
  - "cat/Multimodal_Vision-Language_Policy_Learning"
  - "sub/Compact_VLA_Models"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Leal et al._2023_SARA-RT Scaling up Robotics Transformers with Self-Adaptive Robust Attention.pdf"
---

# SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention

> **저자**: Isabel Leal, Krzysztof Choromanski, Deepali Jain, Avinava Dubey, Jake Varley, Michael Ryoo, Yao Lu, Frederick Liu, Vikas Sindhwani, Quan Vuong, Tamas Sarlos, Ken Oslund, Karol Hausman, Kanishka Rao | **날짜**: 2023-12-04 | **URL**: [https://arxiv.org/abs/2312.01990](https://arxiv.org/abs/2312.01990)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1: Robotics Transformer policies obtained via Self-Adaptive Robust Attention (SARA) in action for three different m*

SARA-RT는 Robotics Transformer를 on-robot 배포에 적합하도록 선형 주의(linear attention)로 변환하는 up-training 방법을 제시하여, quadratic 복잡도의 모델을 high quality 유지하면서 효율화한다.

## Motivation

- **Known**: Transformer 기반 robotic policies는 우수한 semantic reasoning 능력을 제공하지만, 실제 로봇 배포에 있어 quadratic 시간 및 공간 복잡도로 인한 계산 비용이 매우 높다. 예를 들어 35M 파라미터 RT-1도 최대 3Hz 주파수로만 동작한다.
- **Gap**: 기존 linear attention 방법들은 random Gaussian projection을 사용하여 높은 정확도를 유지하지만 계산 오버헤드가 크고(보통 4K+ 이상에서만 실용적), 간단한 함수(ReLU, exp)를 사용하는 방식은 빠르지만 정확도가 낮다는 trade-off가 존재한다.
- **Why**: on-robot deployment에서 실시간성은 필수적이며, billion-parameter vision-language-action 모델들을 로봇에 배포하려면 계산 효율성을 확보하면서도 성능을 유지해야 한다.
- **Approach**: SARA(Self-Adaptive Robust Attention)는 선형 주의 함수 ϕ_f를 Gaussian 행렬 G로 전처리하여 개선하고, up-training이라는 새로운 fine-tuning 방법을 통해 사전학습된 모델을 선형 주의 버전으로 변환한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2: VR navigation via VL attention models on Matterport environments ([21]). The top-down view of the scene is in th*

- **RT-2 가속화**: 5B 파라미터 vision-language-action 모델(sequence length ~200)을 선형 주의로 변환하면서 high quality 유지
- **Point Cloud Transformer 최적화**: 대규모 point cloud(L ∈ [800, 4000])를 처리하는 PCT 정책 가속화
- **O(M+N) 복잡도 달성**: quadratic O(MN) 복잡도를 선형으로 감소
- **Zero-shot navigation 개선**: VR navigation 환경에서 Gaussian 전처리를 통해 ReLU 및 exp variant의 성능 향상

## How

![Figure 2](figures/fig2.webp)

*Fig. 2: VR navigation via VL attention models on Matterport environments ([21]). The top-down view of the scene is in th*

- 커널화(kernelization) 관점에서 kernel function K(x, y) = exp(x^⊤y)를 bi-linearization 가능한 형태로 표현
- ϕ_rand_f(z) = f(Gz) 형식으로 Gaussian 행렬 G를 사용한 randomized feature map 적용
- Up-training 프로세스를 통해 matrix G를 훈련하여 원본 softmax-attention을 모방하도록 학습
- 사전학습된 또는 이미 fine-tuned된 Transformer 기반 정책을 선형 주의 counterpart로 변환
- 시각-언어(VL) 모델의 CLIP 임베딩을 활용한 zero-shot 제어 메커니즘 제안

## Originality

- Up-training이라는 새로운 fine-tuning 패러다임 제시 — 기존 모델을 재훈련 없이 효율적인 버전으로 변환
- Gaussian 전처리를 통해 simple linear attention 함수의 정확도를 dramatic하게 개선하는 간단하면서도 효과적인 트릭 제시
- Robotics Transformer 배포의 실질적 문제(시간/공간 복잡도)에 대한 직접적 해결책 제공
- Vision-language 모델을 zero-shot navigation agent로 활용하는 창의적 접근법

## Limitation & Further Study

- 논문 발췌본에서 실제 on-robot deployment의 성능 메트릭(latency, throughput 등)이 구체적으로 제시되지 않음
- Gaussian 행렬 G의 차원 m 선택에 대한 명확한 가이드라인 부재 (m = d vs m = 2048 선택 기준 불명확)
- RT-2 및 PCT 외 다른 로보틱 모델에 대한 일반화 가능성 검증 필요
- Up-training 프로세스의 수렴성 및 최적화 이론에 대한 상세 분석 필요
- 다양한 로봇 플랫폼과 실제 물리적 작업(manipulation, grasping)에서의 성공률 비교 실험 확대 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: SARA-RT는 Robotics Transformer의 on-robot 배포라는 중요한 실제 문제를 우아하고 효과적으로 해결하며, up-training과 Gaussian 전처리라는 간단하지만 혁신적인 방법을 제시한다. 다만, 구체적인 성능 벤치마크와 광범위한 평가가 보강되면 더욱 강력한 contribution이 될 것이다.

## Related Papers

- 🔄 다른 접근: [[papers/1273_ARMOR_Egocentric_Perception_for_Humanoid_Robot_Collision_Avo/review]] — 휴머노이드 로봇의 충돌 회피를 위한 지각 시스템으로 이고센트릭 네비게이션의 실용적 응용 분야를 제시한다.
- 🏛 기반 연구: [[papers/1372_EgoMimic_Scaling_Imitation_Learning_via_Egocentric_Video/review]] — 대규모 이고센트릭 조작 데이터셋으로 AND 데이터셋과 유사한 실제 환경 데이터 수집 방법론을 제공한다.
- 🔗 후속 연구: [[papers/1409_GR-2_A_Generative_Video-Language-Action_Model_with_Web-Scale/review]] — 이고센트릭 비전을 활용한 휴머노이드 보행 제어에서 실시간 적응형 지각 시스템을 발전시킨다.
- 🧪 응용 사례: [[papers/1268_An_Empirical_Evaluation_of_Four_Off-the-Shelf_Proprietary_Vi/review]] — LookOut의 egocentric 네비게이션 시스템이 평가된 VIO 시스템들을 실제 humanoid 환경에서 활용하는 사례를 보여준다.
- 🧪 응용 사례: [[papers/1323_CReF_Cross-modal_and_Recurrent_Fusion_for_Depth-conditioned/review]] — LookOut의 real-world humanoid navigation이 CReF의 depth-conditioned locomotion을 실제 환경에서 검증하는 구체적 사례를 제공한다.
- 🔗 후속 연구: [[papers/1577_SpecPrune-VLA_Accelerating_Vision-Language-Action_Models_via/review]] — Robotics Transformer의 효율적 배포에서 선형 주의 변환과 액션-인식 프루닝의 상호 보완적 최적화를 제공한다.
