---
title: "1452_Learning_Interactive_Real-World_Simulators"
authors:
  - "Sherry Yang"
  - "Yilun Du"
  - "Kamyar Ghasemipour"
  - "Jonathan Tompson"
  - "Leslie Kaelbling"
date: "2023.10"
doi: ""
arxiv: ""
score: 4.0
essence: "인터넷 데이터로부터 학습된 generative model을 기반으로 인간, 로봇 등의 상호작용에 대한 시각적 결과를 시뮬레이션하는 universal simulator (UniSim)를 제안한다. 다양한 데이터셋을 통합하여 언어 지시, 로봇 제어, 인간 활동 등 다양한 모달리티의 행동을 입력받아 일관성 있는 비디오를 생성한다."
tags:
  - "cat/Embodied_Navigation_and_Planning"
  - "sub/Synthetic_Grasping_Datasets"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yang et al._2023_Learning Interactive Real-World Simulators.pdf"
---

# Learning Interactive Real-World Simulators

> **저자**: Sherry Yang, Yilun Du, Kamyar Ghasemipour, Jonathan Tompson, Leslie Kaelbling, Dale Schuurmans, Pieter Abbeel | **날짜**: 2023-10-09 | **URL**: [https://arxiv.org/abs/2310.06114](https://arxiv.org/abs/2310.06114)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: A universal simulator (UniSim). The simulator of the real-world learns from broad data with diverse*

인터넷 데이터로부터 학습된 generative model을 기반으로 인간, 로봇 등의 상호작용에 대한 시각적 결과를 시뮬레이션하는 universal simulator (UniSim)를 제안한다. 다양한 데이터셋을 통합하여 언어 지시, 로봇 제어, 인간 활동 등 다양한 모달리티의 행동을 입력받아 일관성 있는 비디오를 생성한다.

## Motivation

- **Known**: Generative model들이 텍스트, 이미지, 비디오 생성에 혁신을 가져왔으며, 시뮬레이션 기반 로봇 학습과 sim-to-real transfer는 활발히 연구되고 있다. 그러나 서로 다른 특성의 데이터셋(로봇 제어, 인간 활동, 이미지 등)을 통합하여 통일된 인터랙티브 시뮬레이터를 구축하는 것은 미해결 과제이다.
- **Gap**: 기존 시뮬레이터들은 특정 도메인에 제한되어 있으며, 다양한 모달리티의 행동과 이질적인 데이터셋을 통합하는 방법이 부족하다. 또한 현실과 거의 구별되지 않는 고품질의 비디오를 장기간 일관성 있게 생성하는 것이 어렵다.
- **Why**: 통합 시뮬레이터는 게임/영화 콘텐츠 생성, 순수 시뮬레이션 환경에서 학습한 embodied agent의 실제 로봇 배포, 드물고 위험한 이벤트 시뮬레이션 등 광범위한 응용을 가능하게 하여 AI 학습의 효율성과 안전성을 크게 향상시킬 수 있다.
- **Approach**: 다양한 데이터셋(로봇 데이터, 인간 활동, 파노라마 스캔, 텍스트-이미지 데이터 등)을 통합하기 위해 모든 행동을 T5 임베딩과 discretized 제어값으로 정규화하고, 이를 조건으로 하는 video diffusion model을 observation prediction 프레임워크로 학습한다. Autoregressive rollout을 통해 장기간 일관성 있는 시뮬레이션을 가능하게 한다.

## Achievement

![Figure 3](figures/fig3.webp)

*Figure 3: Action-rich simulations. UniSim can support manipulation actions such as “cut carrots”, “wash*

- **다양한 데이터셋 통합**: 이질적인 6가지 데이터 타입(시뮬레이션, 로봇, 인간활동, 파노라마, 텍스트-이미지)을 unified action-in-video-out 인터페이스로 통합하여 다중 모달 상호작용을 지원
- **장기 일관성 생성**: Observation prediction model의 autoregressive rollout을 통해 비디오 생성 경계를 넘어 일관성 있는 8단계 이상의 장기 상호작용 시뮬레이션 달성
- **Zero-shot sim-to-real transfer**: UniSim에서만 학습한 vision-language policy와 RL 기반 저수준 제어 정책이 추가 학습 없이 실제 로봇에서 동작
- **다양한 응용 가능성**: 드물거나 위험한 이벤트 생성, 비디오 캡셔닝 모델 학습 등 embodied learning 이외의 광범위한 활용 사례 시연

## How

![Figure 2](figures/fig2.webp)

*Figure 2: Training and inference of UniSim. UniSim is a video diffusion model trained to predict the*

- 각 데이터셋의 행동을 T5 language model 임베딩과 discretized control values로 변환하여 unified continuous action space 구성
- Panorama 스캔에서 camera pose 정보를 이용해 'turn left' 같은 행동 레이블 생성", '인간활동 비디오에서 분류 레이블을 텍스트 행동으로 변환하고 프레임 레이트 조정
- Video diffusion model을 조건부 생성 모델로 사용하여 과거 관측(ht−1)과 행동(at−1)을 입력받아 다음 비디오 프레임 예측
- 이전 프레임을 초기 노이즈와 연결하여 autoregressive하게 다음 세그먼트 생성함으로써 장기간 일관성 유지
- Hindsight relabeling을 통해 high-level vision-language policy 학습
- Model-based RL을 이용한 low-level 로봇 제어 정책 학습

## Originality

- **첫 번째 universal simulator 시도**: 다양한 데이터 모달리티를 단일 action-in-video-out 인터페이스로 통합한 최초의 대규모 interactive simulator
- **이질적 데이터셋 오케스트레이션**: 각 데이터셋이 제공하는 서로 다른 정보 차원(객체, 행동, 모션, 언어)을 체계적으로 활용하는 방법론
- **Observation prediction 프레임워킹**: Video diffusion을 observation prediction 문제로 재구성하여 autoregressive long-horizon 시뮬레이션 가능하게 함
- **Unified action representation**: 텍스트, 로봇 제어, camera 모션 등 이질적인 행동을 단일 임베딩 공간으로 매핑

## Limitation & Further Study

- **제한된 모달리티 범위**: 음성 시뮬레이션 미지원, 정적 이미지를 단일 프레임 비디오로 취급하여 실제 모션 정보 부족
- **Dataset 품질 의존성**: 각 데이터셋의 이질성과 불균형이 최종 성능에 미치는 영향에 대한 분석 부족
- **현실성 평가 부재**: '현실과 거의 구별되지 않는 비디오'를 주장하나 정량적 평가 메트릭 제한적", '**Sim-to-real 일반화 범위**: 제시된 로봇 실험이 제한적이며, 다양한 환경과 작업에 대한 실제 로봇 검증 부족
- **후속 연구**: 더 높은 해상도 생성, 물리적 정확성 향상, 더 다양한 로봇과 환경에서의 검증, 음성 및 촉각 정보 통합

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 이질적인 다중 데이터셋을 unified 인터페이스로 통합하여 interactive real-world simulator를 구축한 의미 있는 작업으로, video diffusion model을 활용한 기술적 구현과 다양한 응용 가능성을 보여준다. 다만 현실성 검증의 정량성과 실제 로봇 환경에서의 광범위한 검증이 추가되면 더욱 강력한 기여가 될 수 있다.

## Related Papers

- 🔄 다른 접근: [[papers/1467_Manipulate-Anything_Automating_Real-World_Robots_using_Visio/review]] — 두 논문 모두 로봇 조작을 위한 시뮬레이션과 데이터 생성을 다루지만, 하나는 범용 시뮬레이터에, 다른 하나는 VLM 기반 자동화에 집중합니다.
- 🏛 기반 연구: [[papers/1360_Diffusion_Models_Are_Real-Time_Game_Engines/review]] — 실시간 게임 엔진으로서의 diffusion 모델이 상호작용 시뮬레이터의 핵심 기술적 기반을 제공합니다.
- 🧪 응용 사례: [[papers/1421_Genie_Sim_30__A_High-Fidelity_Comprehensive_Simulation_Platf/review]] — 고충실도 시뮬레이션 플랫폼이 멀티모달 AI 에이전트의 훈련과 평가 환경을 제공합니다.
- 🏛 기반 연구: [[papers/1631_World_Models/review]] — 월드 모델의 기본 개념이 실제 세계 상호작용을 시뮬레이션하는 범용 시뮬레이터의 이론적 토대가 됩니다.
- 🔄 다른 접근: [[papers/1467_Manipulate-Anything_Automating_Real-World_Robots_using_Visio/review]] — 두 논문 모두 로봇을 위한 시뮬레이션과 데이터 생성을 다루지만, 하나는 VLM 기반 자동화에, 다른 하나는 범용 시뮬레이터에 집중합니다.
- 🔗 후속 연구: [[papers/1347_D2E_Scaling_Vision-Action_Pretraining_on_Desktop_Data_for_Tr/review]] — Learning Interactive Real-World Simulators는 D2E의 데스크톱 데이터를 상호작용적 실세계 시뮬레이터 학습으로 확장한다
- 🔄 다른 접근: [[papers/1387_EWMBench_Evaluating_Scene_Motion_and_Semantic_Quality_in_Emb/review]] — Learning Interactive Real-World Simulators도 embodied world modeling의 품질 평가를 다룬다.
