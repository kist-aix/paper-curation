---
title: "1605_VIMA_General_Robot_Manipulation_with_Multimodal_Prompts"
authors:
  - "Yunfan Jiang"
  - "Agrim Gupta"
  - "Zichen Zhang"
  - "Guanzhi Wang"
  - "Yongqiang Dou"
date: "2022.10"
doi: ""
arxiv: ""
score: 4.0
essence: "멀티모달 프롬프트(텍스트와 이미지 혼합)를 사용하여 다양한 로봇 조작 작업을 통일된 시퀀스 모델링 문제로 표현하고, 이를 처리할 수 있는 transformer 기반 로봇 에이전트 VIMA를 제시한다."
tags:
  - "cat/Task-Oriented_Skill_Acquisition"
  - "sub/Hierarchical_Task_Learning"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jiang et al._2022_VIMA General Robot Manipulation with Multimodal Prompts.pdf"
---

# VIMA: General Robot Manipulation with Multimodal Prompts

> **저자**: Yunfan Jiang, Agrim Gupta, Zichen Zhang, Guanzhi Wang, Yongqiang Dou, Yanjun Chen, Li Fei-Fei, Anima Anandkumar, Yuke Zhu, Linxi Fan | **날짜**: 2022-10-06 | **URL**: [https://arxiv.org/abs/2210.03094](https://arxiv.org/abs/2210.03094)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Multimodal prompts for task specification. We observe that many robot manipulation tasks can be expressed as*

멀티모달 프롬프트(텍스트와 이미지 혼합)를 사용하여 다양한 로봇 조작 작업을 통일된 시퀀스 모델링 문제로 표현하고, 이를 처리할 수 있는 transformer 기반 로봇 에이전트 VIMA를 제시한다.

## Motivation

- **Known**: NLP에서 prompt 기반 학습이 성공적인 패러다임으로 확립되었으며, 로봇 조작 작업은 일반적으로 특화된 모델들로 각각 다루어진다.
- **Gap**: 로봇 학습에서 다양한 형태의 작업 명세(언어 지시, 시각적 목표, 시연 모방)를 단일 통합 인터페이스로 표현하고 처리할 수 있는 일반적인 접근법이 부족하다.
- **Why**: 일반화된 로봇 에이전트는 직관적이고 유연한 작업 명세 인터페이스가 필요하며, 이는 복수 작업 학습과 zero-shot 일반화 능력을 가능하게 한다.
- **Approach**: 멀티모달 프롬프트로 표현 가능한 6가지 작업 카테고리를 정의하고, 이에 대응하는 VIMA-BENCH 벤치마크와 encoder-decoder transformer 기반 VIMA 모델을 개발한다.

## Achievement

![Figure 4](figures/fig4.webp)

*Figure 4: Scaling model and data. Top: We compare performance of different methods with model sizes ranging from 2M*

- **멀티모달 프롬프트 정식화**: 간단한 객체 조작, 시각적 목표 도달, 새로운 개념 학습, 비디오 모방, 시각적 제약 만족, 시각적 추론 등 6가지 작업 유형을 통일된 프롬프트 형식으로 표현
- **VIMA-BENCH 벤치마크**: 600K+ 전문가 궤적, 17가지 기본 작업으로부터 수천 개의 절차적으로 생성된 인스턴스, 4단계 평가 프로토콜(객체 배치 → 새로운 조합 → 새로운 객체 → 새로운 작업) 제공
- **VIMA 모델의 성능**: 동일한 학습 데이터에서 경쟁 모델 대비 최대 2.9배 작업 성공률 달성, 10배 적은 데이터로도 2.7배 우수한 성능 달성
- **모델 확장성**: 2M에서 200M 파라미터 범위의 7가지 모델에서 일관된 성능 향상 입증

## How

![Figure 3](figures/fig3.webp)

*Figure 3: VIMA Architecture. We encode the multimodal prompts with a pre-trained T5 model, and condition the*

- Pre-trained 언어 모델로 멀티모달 프롬프트(텍스트와 이미지 토큰의 교차) 인코딩
- 객체 중심 접근: 이미지를 객체 단위로 파싱하여 객체 토큰 시퀀스로 변환 (off-the-shelf 및 도메인 미세조정 detector 사용)
- Transformer decoder: cross-attention과 causal self-attention을 번갈아 사용하여 프롬프트 기반 조건부 학습 수행
- 자동회귀적 행동 출력: 각 환경 상호작용 단계에서 모터 액션 생성
- 이미지 패치 토큰, image Perceiver, decoder-only 조건부 등 대안 설계와 비교 분석

## Originality

- 로봇 조작 작업을 위한 **멀티모달 프롬프트** 개념의 첫 제시 - NLP의 prompt 패러다임을 로봇 학습으로 체계적으로 적용
- **4단계 평가 프로토콜**의 설계 - 점진적으로 강화되는 zero-shot 일반화 능력 측정을 위한 체계적 평가 방식
- **객체 중심 token 표현** - raw 이미지 패치 대신 의미있는 객체 단위로 파싱하여 model scalability 및 data efficiency 향상
- 단일 통합 모델로 **여러 작업 형식 지원** - 기존의 task-specific 아키텍처 대신 sequence modeling 문제로 통일

## Limitation & Further Study

- 시뮬레이션 환경 기반 평가로 실제 로봇 하드웨어 전이(sim-to-real transfer)의 검증 부족
- 객체 감지(object detection)에 의존하므로 감지 오류의 누적 효과에 대한 분석 미흡
- 현재 벤치마크는 탁상 조작(tabletop manipulation) 작업에 제한되어 있으며, 더 복잡한 환경으로의 확장성 미지수
- 멀티모달 프롬프트 길이 제약과 긴 지시의 처리 능력에 대한 논의 부족
- **후속 연구**: 실제 로봇 환경에서의 검증, 더 복잡한 동적 환경 적용, prompt 토큰 효율성 개선, 강화학습 기반 적응 메커니즘 통합

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 멀티모달 프롬프트를 통해 다양한 로봇 조작 작업을 통일된 프레임워크로 표현한 획기적 접근법으로, 체계적인 벤치마크와 함께 높은 일반화 성능을 달성하였다. 로봇 학습의 task specification 문제에 대한 창의적 해결책을 제시하며 개방형 재현 자료를 통해 커뮤니티 기여도 높다.

## Related Papers

- 🏛 기반 연구: [[papers/1516_Plan-Seq-Learn_Language_Model_Guided_RL_for_Solving_Long_Hor/review]] — 멀티모달 프롬프트를 통한 통합 시퀀스 모델링 접근법이 PSL의 LLM 기반 고수준 계획 수립에 이론적 기반을 제공한다.
- 🔄 다른 접근: [[papers/1615_VLA-0_Building_State-of-the-Art_VLAs_with_Zero_Modification/review]] — 로봇 조작에서 VIMA의 멀티모달 프롬프트 기반 transformer와 VLA-0의 단순한 텍스트 액션 표현 방식을 복잡성과 성능 측면에서 비교할 수 있다.
- 🔗 후속 연구: [[papers/1436_HAIC_Humanoid_Agile_Object_Interaction_Control_via_Dynamics-/review]] — InstructVLA의 멀티모달 instruction tuning 방법론을 VIMA의 텍스트-이미지 혼합 프롬프트 처리에 적용하여 더 정교한 명령 이해를 가능하게 한다.
- 🧪 응용 사례: [[papers/1325_CALVIN_A_Benchmark_for_Language-Conditioned_Policy_Learning/review]] — CALVIN 벤치마크의 언어 조건 정책 학습 평가 방법론을 VIMA의 멀티모달 프롬프트 기반 로봇 에이전트 성능 검증에 활용할 수 있다.
- 🏛 기반 연구: [[papers/1516_Plan-Seq-Learn_Language_Model_Guided_RL_for_Solving_Long_Hor/review]] — 멀티모달 프롬프트 기반 로봇 조작을 통합 시퀀스 모델링으로 접근한 VIMA의 방법론이 PSL의 계층적 계획 수립에 이론적 기반을 제공한다.
- ⚖️ 반론/비판: [[papers/1615_VLA-0_Building_State-of-the-Art_VLAs_with_Zero_Modification/review]] — 로봇 조작에서 VLA-0의 단순한 설계 철학과 VIMA의 복잡한 멀티모달 프롬프트 처리 방식을 효율성과 표현력 측면에서 대조할 수 있다.
- 🏛 기반 연구: [[papers/1312_ARNOLD_A_Benchmark_for_Language-Grounded_Task_Learning_With/review]] — VIMA의 멀티모달 프롬프트 기반 조작 방법론이 ARNOLD의 언어 기반 작업 학습 설계에 이론적 기반을 제공한다
