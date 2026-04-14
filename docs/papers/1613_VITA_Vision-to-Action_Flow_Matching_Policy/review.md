---
title: "1613_VITA_Vision-to-Action_Flow_Matching_Policy"
authors:
  - "Dechen Gao"
  - "Boqi Zhao"
  - "Andrew Lee"
  - "Ian Chuang"
  - "Hanchu Zhou"
date: "2025.07"
doi: ""
arxiv: ""
score: 4.0
essence: "VITA는 시각 표현에서 잠재 행동으로 직접 흐르는 noise-free flow matching 정책으로, 기존의 반복적인 시각 조건화 모듈을 제거하여 추론 속도와 메모리 효율성을 획기적으로 향상시킨다."
tags:
  - "cat/Multimodal_Vision-Language_Policy_Learning"
  - "sub/Video_Action_Generation"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Gao et al._2025_VITA Vision-to-Action Flow Matching Policy.pdf"
---

# VITA: Vision-to-Action Flow Matching Policy

> **저자**: Dechen Gao, Boqi Zhao, Andrew Lee, Ian Chuang, Hanchu Zhou, Hang Wang, Zhe Zhao, Junshan Zhang, Iman Soltani | **날짜**: 2025-07-17 | **URL**: [https://arxiv.org/abs/2507.13231](https://arxiv.org/abs/2507.13231)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: A comparison between VITA and conventional flow matching and diffusion policies. Unlike*

VITA는 시각 표현에서 잠재 행동으로 직접 흐르는 noise-free flow matching 정책으로, 기존의 반복적인 시각 조건화 모듈을 제거하여 추론 속도와 메모리 효율성을 획기적으로 향상시킨다.

## Motivation

- **Known**: Flow matching과 diffusion 기반 정책들이 cross-modal 생성 작업에서 우수한 성능을 보이고 있으나, Gaussian 분포에서 샘플링하고 generative 과정의 각 단계에서 시각 정보를 반복적으로 주입하는 conditioning 모듈을 필요로 하여 시간과 메모리 오버헤드가 크다.
- **Gap**: 기존 flow matching 정책은 robotic control에서 필요한 실시간 처리(50-200Hz)를 위해 조건화 메커니즘의 비효율성을 극복해야 하며, 시각 표현과 행동 간의 차원 및 구조의 불일치 문제가 해결되지 않았다.
- **Why**: 로봇 제어의 실시간성 요구와 제한된 행동 데이터로부터 효율적으로 정책을 학습하는 것이 필수적이며, noise-free flow matching을 통해 아키텍처를 단순화하고 계산 효율성을 크게 개선할 수 있다.
- **Approach**: Action autoencoder를 통해 raw action을 시각 잠재 벡터와 정렬된 구조화된 잠재 공간으로 매핑하고, flow latent decoding을 제안하여 ODE 해결 단계를 통해 행동 재구성 손실을 역전파함으로써 end-to-end 학습을 가능하게 한다.

## Achievement

![Figure 4](figures/fig4.webp)

*Figure 4: Autonomous rollouts of VITA on five challenging real-world tasks, including two bimanual*

- **추론 속도 향상**: 기존 conditioning 모듈 방식 대비 1.5×-2× 빠른 추론 속도 달성
- **메모리 효율성**: 18.6%-28.7% 낮은 메모리 사용량으로 동일한 모델 크기에서 우수한 성능 구현
- **경쟁력 있는 성능**: ALOHA와 Robomimic의 9개 시뮬레이션 및 5개 실제 작업에서 최첨단 정책과 동등하거나 우수한 성공률 달성
- **아키텍처 단순화**: 첫 MLP-only flow matching 정책으로 ALOHA 이원 조작과 같이 도전적인 작업에 성공
- **학습 안정성**: 빠른 수렴과 높은 정밀도를 유지하면서 안정적인 학습 달성

## How

![Figure 2](figures/fig2.webp)

*Figure 2: An overview of the VITA architecture: The vision encoder maps observations into a source*

- 시각 인코더로 카메라 이미지를 latent image 분포로 변환
- Action autoencoder를 통해 raw action을 structured latent action space로 인코딩
- Flow matching을 사용하여 latent image distribution에서 latent action distribution으로의 직접 흐름 학습
- Flow latent decoding: ODE 해결 단계 동안 행동 재구성 손실을 역전파하여 latent action collapse 방지
- Action decoder를 통해 생성된 latent action을 실제 행동으로 디코딩
- Action autoencoder와 flow matching 모델을 joint training으로 함께 최적화

## Originality

- Flow matching의 이론적 유연성(source 분포 무제약)을 처음으로 visuomotor 정책에 실제로 적용하여 noise-free framework 개발
- Action autoencoder와 flow matching의 결합을 통해 차원 및 구조 불일치 문제 해결
- Flow latent decoding이라는 새로운 기법으로 sparse action 데이터 환경에서 latent space collapse를 방지하는 end-to-end 학습 전략 제시
- 기존의 사전 학습된 고정 latent space(image generation에서 사용) 방식과 달리, 제한된 action 데이터로부터 jointly 학습하는 새로운 패러다임 제안

## Limitation & Further Study

- 평가가 ALOHA와 Robomimic 벤치마크로 제한되어 있으며, 더 다양한 로봇 플랫폼과 작업에 대한 일반화 가능성이 미검증됨
- Grid-based visual representation 사용 시 transformer 같은 복잡한 아키텍처가 여전히 필요하므로, vector-based 표현 대비 효율성 이점이 제한됨
- Flow latent decoding의 추가 계산 비용(ODE 단계별 역전파)에 대한 상세 분석이 부족함
- 후속 연구로 multi-modal observation(예: 촉각, 음성)에 대한 확장과 더 복잡한 조작 작업에서의 적용 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: VITA는 flow matching의 이론적 자유도를 영리하게 활용하여 visuomotor 정책의 효율성과 성능을 동시에 달성한 의미 있는 기여이며, noise-free framework와 flow latent decoding은 독창적인 기술적 혁신으로서 로봇 제어 분야의 실용성을 크게 향상시킨다.

## Related Papers

- 🔄 다른 접근: [[papers/1502_One-Step_Diffusion_Policy_Fast_Visuomotor_Policies_via_Diffu/review]] — 둘 다 빠른 정책 추론을 목표하지만 VITA는 flow matching, One-Step Diffusion은 diffusion 기반의 다른 접근법이다
- 🔗 후속 연구: [[papers/1339_Consistency_Policy_Accelerated_Visuomotor_Policies_via_Consi/review]] — Consistency Policy의 일관성 보장 원리를 flow matching 정책에서 noise-free 방식으로 발전시켰다
- 🏛 기반 연구: [[papers/1580_Streaming_Flow_Policy_Simplifying_diffusionflow-matching_pol/review]] — Streaming Flow Policy가 VITA의 vision-to-action flow matching 구조의 이론적 기반을 제공한다
- 🧪 응용 사례: [[papers/1525_Real-Time_Execution_of_Action_Chunking_Flow_Policies/review]] — Real-Time Execution이 VITA의 빠른 추론 속도를 실제 로봇 환경에서 활용하는 방법을 구체적으로 보여준다
- 🔗 후속 연구: [[papers/1609_Vision-Language-Action_Models_for_Robotics_A_Review_Towards/review]] — VITA의 vision-to-action flow matching이 VLA 모델의 action generation 부분을 개선한 구체적 발전
- 🔗 후속 연구: [[papers/1362_Diffusion_Policy_Visuomotor_Policy_Learning_via_Action_Diffu/review]] — Vision-to-action flow matching이 diffusion policy의 action diffusion 개념을 flow matching으로 확장한다.
