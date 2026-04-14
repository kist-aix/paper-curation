---
title: "1512_PaLM-E_An_Embodied_Multimodal_Language_Model"
authors:
  - "Danny Driess"
  - "Fei Xia"
  - "Mehdi S. M. Sajjadi"
  - "Corey Lynch"
  - "Aakanksha Chowdhery"
date: "2023.03"
doi: ""
arxiv: ""
score: 4.0
essence: "PaLM-E는 시각, 상태 추정, 텍스트 입력을 멀티모달 문장으로 인터리빙하여 LLM에 직접 통합하는 embodied multimodal language model이다. 이를 통해 로봇 조작 계획, VQA, 캡셔닝 등 다양한 embodied reasoning 작업을 수행할 수 있다."
tags:
  - "cat/Embodied_Navigation_and_Planning"
  - "sub/Embodied_Visual_Reasoning"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Driess et al._2023_PaLM-E An Embodied Multimodal Language Model.pdf"
---

# PaLM-E: An Embodied Multimodal Language Model

> **저자**: Danny Driess, Fei Xia, Mehdi S. M. Sajjadi, Corey Lynch, Aakanksha Chowdhery, Brian Ichter, Ayzaan Wahid, Jonathan Tompson, Quan Vuong, Tianhe Yu, Wenlong Huang, Yevgen Chebotar, Pierre Sermanet, Daniel Duckworth, Sergey Levine, Vincent Vanhoucke, Karol Hausman, Marc Toussaint, Klaus Greff, Andy Zeng, Igor Mordatch, Pete Florence | **날짜**: 2023-03-06 | **URL**: [https://arxiv.org/abs/2303.03378](https://arxiv.org/abs/2303.03378)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: PaLM-E is a single general-purpose multimodal language model for embodied reasoning tasks, visual-language tas*

PaLM-E는 시각, 상태 추정, 텍스트 입력을 멀티모달 문장으로 인터리빙하여 LLM에 직접 통합하는 embodied multimodal language model이다. 이를 통해 로봇 조작 계획, VQA, 캡셔닝 등 다양한 embodied reasoning 작업을 수행할 수 있다.

## Motivation

- **Known**: LLM은 복잡한 추론 작업에 뛰어나지만 현실 세계의 grounding이 부족하다. 기존 visual-language model은 VQA 같은 표준 작업에는 잘 작동하지만 로보틱 추론 작업에는 직접 적용할 수 없다.
- **Gap**: LLM과 현실의 연속적인 센서 모달리티 간의 연결고리가 부족하며, 기존 visual-language model이 로봇 작업에 효과적이지 못하다. embodied agent의 다양한 센서 입력을 end-to-end로 처리하는 통합 모델이 필요하다.
- **Why**: 로봇 제어 및 현실 세계의 기하학적 구성을 이해하려면 텍스트만으로는 불충분하며, 시각과 물리적 센서 정보를 직접 처리할 수 있는 모델이 필수적이다. 이는 로보틱스, 컴퓨터 비전 분야의 실질적 응용을 가능하게 한다.
- **Approach**: 사전학습된 LLM(PaLM)에 ViT와 같은 인코더를 주입하여 이미지와 상태 추정값을 텍스트 토큰과 동일한 잠재 임베딩 공간에 임베드한다. 멀티모달 문장을 Transformer의 self-attention으로 처리하고 end-to-end로 인코더를 학습한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: PaLM-E-562B can do zero-shot multimodal chain-of-thought reasoning, can tell visually-conditioned jokes given *

- **확장 가능한 모델 성능**: PaLM-E-562B는 OK-VQA 벤치마크에서 state-of-the-art 성능을 달성했으며, 로봇 작업 학습에서도 뛰어난 데이터 효율성을 보여줌
- **다중 도메인 양성 이전**: 인터넷 규모의 언어, 시각, visual-language 데이터로 공동 학습하면 로봇 작업 성능이 향상되며 한두 개의 예시로도 새로운 객체에 일반화 가능
- **광범위한 멀티모달 추론 능력**: zero-shot multimodal chain-of-thought 추론, OCR-free 수학 추론, 다중 이미지 추론, visually-conditioned 농담 생성 등 다양한 작업 수행
- **다중 구현(embodiment) 지원**: 두 개의 실제 로봇을 포함한 여러 로봇 플랫폼에서 작동하며 순차적 의사결정 기능 수행

## How

![Figure 1](figures/fig1.webp)

*Figure 1: PaLM-E is a single general-purpose multimodal language model for embodied reasoning tasks, visual-language tas*

- 사전학습된 540B PaLM LLM을 기반으로 22B ViT 인코더를 통합하여 이미지를 임베드
- 멀티모달 입력(이미지, 상태 벡터, 텍스트)을 interleaved 시퀀스로 표현하여 LLM의 self-attention에 공급
- 로봇 조작 계획(TAMP), tabletop 조작, mobile 조작, VQA, 캡셔닝 등 다양한 embodied 작업에 대해 end-to-end 학습
- 멀티태스크 학습 전략으로 여러 도메인 데이터를 함께 학습하여 positive transfer 유도
- 서로 다른 인코더 설계(standard vs. object-centric ViT), LLM 동결 여부 등의 변형 실험을 통해 설계 선택 검증

## Originality

- **최초의 대규모 embodied multimodal LLM**: 시각, 연속 상태, 텍스트를 동시에 처리하는 end-to-end 통합 모델로 기존 LLM-정책 인터페이싱 방식과 구별됨
- **멀티모달 chain-of-thought의 신규 입증**: 기존 zero-shot CoT는 언어 전용이었으나, 본 논문은 end-to-end 모델에서 처음으로 multimodal 데이터에 적용
- **대규모 멀티모달 아키텍처**: 540B LLM과 22B ViT의 통합으로 당시 보고된 가장 큰 vision-language 모델 구성
- **실제 로봇에서의 closed-loop 검증**: 두 개의 실제 로봇 플랫폼에서 실제 성능 검증으로 현실성 증명

## Limitation & Further Study

- **계산 비용 미분석**: 562B 모델의 실제 추론 시간, 메모리 요구사항, 배포 가능성 등에 대한 논의 부족
- **센서 모달리티 제한**: 현재 이미지와 저차원 상태 벡터만 처리하며, 포인트 클라우드, 라이다 등 다른 센서 유형 지원 부재
- **로봇 작업의 제한된 범위**: 대부분의 실험이 테이블탑 조작에 집중되어 있으며, 더 복잡한 다체 상호작용이나 동적 환경에서의 성능 미평가
- **일반화 한계 분석 부족**: zero-shot 일반화가 작동하는 조건과 실패하는 조건에 대한 체계적 분석 부재
- **후속연구 방향**: 다중 센서 모달리티 통합, 더 큰 규모의 로봇 데이터셋 구축, 실시간 추론 최적화 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: PaLM-E는 LLM을 실제 로봇 제어에 처음으로 의미있게 적용한 획기적 연구로, 멀티모달 입력의 end-to-end 처리와 다중 도메인 양성 이전을 통해 embodied AI 분야의 새로운 패러다임을 제시한다. 562B 규모의 대규모 모델 구축과 실제 로봇 검증, 다양한 멀티모달 추론 능력의 입증은 매우 인상적이며, 로봇공학과 비전-언어 모델 분야에 상당한 영향을 미칠 것으로 예상된다.

## Related Papers

- 🔗 후속 연구: [[papers/1421_Genie_Sim_30__A_High-Fidelity_Comprehensive_Simulation_Platf/review]] — Helix의 일반화된 휴머노이드 비전-언어-액션 모델이 PaLM-E의 embodied multimodal language model을 휴머노이드 로봇에 특화하여 발전시킨다.
- 🏛 기반 연구: [[papers/1281_Being-H0_Vision-Language-Action_Pretraining_from_Large-Scale/review]] — Being-H0의 대규모 비전-언어-액션 사전학습이 PaLM-E의 멀티모달 언어 모델 통합 방법론의 기초를 제공한다.
- 🧪 응용 사례: [[papers/1438_InternVLA-M1_A_Spatially_Guided_Vision-Language-Action_Frame/review]] — InternVLA-M1의 spatially guided framework가 PaLM-E의 embodied multimodal reasoning을 실제 로봇 조작 작업에 구체적으로 적용한다.
- 🔗 후속 연구: [[papers/1586_TidyBot_Personalized_Robot_Assistance_with_Large_Language_Mo/review]] — TidyBot의 개인화된 로봇 지원이 PaLM-E의 멀티모달 언어 모델 기반 embodied AI 능력을 특정 도메인(정리)에 특화시킨 확장
- 🏛 기반 연구: [[papers/1384_Endowing_GPT-4_with_a_Humanoid_Body_Building_the_Bridge_Betw/review]] — PaLM-E의 embodied multimodal 언어 모델이 BiBo의 GPT-4 활용 방법론에 기초가 된다.
