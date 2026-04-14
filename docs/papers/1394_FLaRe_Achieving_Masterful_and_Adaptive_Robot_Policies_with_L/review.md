---
title: "1394_FLaRe_Achieving_Masterful_and_Adaptive_Robot_Policies_with_L"
authors:
  - "Jiaheng Hu"
  - "Rose Hendrix"
  - "Ali Farhadi"
  - "Aniruddha Kembhavi"
  - "Roberto Martin-Martin"
date: "2024.09"
doi: ""
arxiv: ""
score: 4.0
essence: "FLaRe는 대규모 다중 작업 Behavior Cloning으로 사전학습된 로봇 정책을 Reinforcement Learning으로 효과적으로 미세조정하는 프레임워크로, 그래디언트 안정화 기법을 통해 성능 정체를 극복한다."
tags:
  - "cat/Robotic_Foundation_Model_Development"
  - "sub/Cross-Domain_Robot_Learning"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Hu et al._2024_FLaRe Achieving Masterful and Adaptive Robot Policies with Large-Scale Reinforcement Learning Fine-.pdf"
---

# FLaRe: Achieving Masterful and Adaptive Robot Policies with Large-Scale Reinforcement Learning Fine-Tuning

> **저자**: Jiaheng Hu, Rose Hendrix, Ali Farhadi, Aniruddha Kembhavi, Roberto Martin-Martin, Peter Stone, Kuo-Hao Zeng, Kiana Ehsani | **날짜**: 2024-09-25 | **URL**: [https://arxiv.org/abs/2409.16578](https://arxiv.org/abs/2409.16578)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1: FLaRe is a simple but effective approach for*

FLaRe는 대규모 다중 작업 Behavior Cloning으로 사전학습된 로봇 정책을 Reinforcement Learning으로 효과적으로 미세조정하는 프레임워크로, 그래디언트 안정화 기법을 통해 성능 정체를 극복한다.

## Motivation

- **Known**: Behavior Cloning 기반의 기초 모델(RT-1, RT-2, RT-X, SPOC 등)들이 많이 제안되었지만, 직접 배포 시 미지의 상태와 작업에서 성능이 부족하다.
- **Gap**: 기존의 BC 정책에 RL을 적용한 시도들이 있었으나 대규모 네트워크 미세조정에서는 BC에서 RL로의 급격한 전환으로 인한 그래디언트 문제로 실패하며, 실제 로봇 실험이 부족하다.
- **Why**: 로봇의 배포 성능을 획기적으로 향상시키면서도 학습 효율성을 유지할 수 있다면 실제 로봇 시스템의 일반화 능력을 크게 개선할 수 있기 때문이다.
- **Approach**: 대규모 다중 작업 BC 정책을 기초로 시뮬레이션 환경에서 대규모 RL 미세조정을 수행하되, 소규모 학습률, Actor-Critic 분리, On-Policy 알고리즘(PPO), 엔트로피 보너스 제거 등의 안정화 기법을 적용한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Fig. 1: FLaRe is a simple but effective approach for*

- **시뮬레이션 성능**: 장기 수평 모바일 조작 작업에서 79.5%의 평균 성공률 달성, 이전 최고 성능 대비 +23.6% 절대 개선
- **실제 로봇 성능**: 80.7% 평균 성공률 달성, 선행 연구 대비 +30.7% 절대 개선
- **학습 효율성**: 이전 최고 성능 방법 대비 15배 빠른 학습 시간, 희소 보상만으로 학습 가능
- **일반화**: BC 학습 데이터에 없는 새로운 작업으로 일반화 가능
- **적응성**: 하루 미만의 미세조정으로 새로운 구체형(embodiment)과 행동에 신속히 적응

## How

![Figure 2](figures/fig2.webp)

*Fig. 2: FLaRe introduces a series of design choices that help stabilize the RL training process, including 1) fine-tunin*

- **기초 모델 선택**: 대규모 다중 작업 BC로 사전학습된 Transformer 정책을 시작점으로 사용
- **시뮬레이션 규모 확대**: 광범위한 시뮬레이션 환경에서 대규모 RL 미세조정 수행
- **안정화 기법 적용**:
- - 소규모 학습률(2e-5) 사용으로 급격한 그래디언트 업데이트 방지
- - Actor와 Critic 네트워크 분리로 정책 업데이트 안정성 향상
- - On-Policy PPO 알고리즘 사용으로 오프-정책 방법의 불안정성 회피
- - 엔트로피 보너스 비활성화로 정책 활동 제약 완화
- **희소 보상 활용**: 복잡한 보상 엔지니어링 없이 자연언어 지시사항에 대한 이진 완료 신호만 사용

## Originality

- **규모의 확장**: 기존 연구들은 소규모 네트워크와 단일 작업에만 검증했으나, FLaRe는 대규모 Transformer 기반 정책 미세조정을 성공적으로 수행
- **실제 로봇 검증**: 시뮬레이션뿐만 아니라 실제 로봇(Stretch RE-1, LoCoBot)에서의 광범위한 실험 수행
- **다중 작업 일반화**: BC 데이터에 없는 새로운 작업으로의 일반화 능력 입증
- **체계적 안정화 기법**: BC-to-RL 전환 시 발생하는 그래디언트 붕괴 문제를 명확히 진단하고 일련의 설계 선택으로 해결
- **교차 구체형 전이**: 서로 다른 로봇 플랫폼 간의 신속한 적응 능력 시연

## Limitation & Further Study

- **환경 제약**: 주로 모바일 조작 작업에 초점을 맞추었으며, 다른 로봇 작업 도메인(예: 미세 조작, 보행)에의 적용 검증 필요
- **보상 함수 의존성**: 희소 보상 사용이 강점이지만, 여전히 작업 완료 여부를 판단할 수 있는 명확한 보상 신호 필요
- **시뮬레이션-현실 격차**: 시뮬레이션에서 미세조정한 정책을 실제 로봇에 배포할 때 도메인 적응 메커니즘의 세부 사항 부족
- **계산 비용**: 대규모 환경에서의 RL 미세조정이 여전히 상당한 GPU 자원 요구
- **후속 연구 방향**: (1) 더 복잡한 보상 함수 없이 학습하는 방법, (2) 시뮬레이션-현실 전이 개선, (3) 다양한 로봇 플랫폼과 작업 도메인으로의 확장, (4) 메타학습을 통한 더 신속한 적응

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: FLaRe는 대규모 로봇 정책 미세조정의 실질적 문제들을 명확히 진단하고 체계적인 설계 선택으로 해결하여, 시뮬레이션과 실제 로봇 모두에서 획기적인 성능 향상을 달성했다. 특히 그래디언트 안정화 기법과 대규모 RL 훈련의 성공적 적용은 로봇 기초 모델 분야의 중요한 진전을 나타낸다.

## Related Papers

- 🏛 기반 연구: [[papers/1345_DiffCoTune_Differentiable_Co-Tuning_for_Cross-domain_Robot_C/review]] — 대규모 사전학습된 정책의 RL 미세조정이 differentiable co-tuning의 성능 안정화 기법 제공
- 🔗 후속 연구: [[papers/1409_GR-2_A_Generative_Video-Language-Action_Model_with_Web-Scale/review]] — FLaRe의 gradient 안정화 기법이 GR-2와 같은 generative VLA 모델의 미세조정에 적용
- 🔄 다른 접근: [[papers/1345_DiffCoTune_Differentiable_Co-Tuning_for_Cross-domain_Robot_C/review]] — cross-domain 성능 향상을 위해 gradient 기반 자동 튜닝과 RL 미세조정의 상호보완적 접근
- 🔄 다른 접근: [[papers/1409_GR-2_A_Generative_Video-Language-Action_Model_with_Web-Scale/review]] — web-scale 사전학습 기반 generative 접근과 behavior cloning + RL 미세조정의 상이한 학습 전략
