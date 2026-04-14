---
title: "1394_FARM_Frame-Accelerated_Augmentation_and_Residual_Mixture-of-"
authors:
  - "Tan Jing"
  - "Shiting Chen"
  - "Yangfan Li"
  - "Weisheng Xu"
  - "Renjing Xu"
date: "2025.08"
doi: ""
arxiv: ""
score: 4.0
essence: "물리 기반 휴머노이드 제어에서 저동역 일상 동작은 잘 추적하지만 고동역 폭발적 동작에 취약한 문제를 해결하기 위해, Frame-Accelerated Augmentation과 Residual Mixture-of-Experts를 결합한 FARM 프레임워크를 제안한다."
tags:
  - "cat/Motion_Generation_and_Simulation"
  - "sub/Dynamic_Motion_Retargeting"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jing et al._2025_FARM Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic.pdf"
---

# FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control

> **저자**: Tan Jing, Shiting Chen, Yangfan Li, Weisheng Xu, Renjing Xu | **날짜**: 2025-08-27 | **URL**: [https://arxiv.org/abs/2508.19926](https://arxiv.org/abs/2508.19926)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Comparison between FARM and the baseline FC on two high-dynamic motions. FARM accurately completes both*

물리 기반 휴머노이드 제어에서 저동역 일상 동작은 잘 추적하지만 고동역 폭발적 동작에 취약한 문제를 해결하기 위해, Frame-Accelerated Augmentation과 Residual Mixture-of-Experts를 결합한 FARM 프레임워크를 제안한다.

## Motivation

- **Known**: UHC, PHC, PHC+, MaskedMimic 등의 최신 물리 기반 휴머노이드 컨트롤러들은 AMASS 데이터셋에서 97-100% 추적 성공률을 달성했으나, AMASS가 저동역 일상 동작으로 편중되어 있어 고동역 동작 일반화에 한계가 있다.
- **Gap**: 기존 연구들은 고동역 폭발적 동작(예: 도약, 회전)에 대한 명시적 고려 없이 저동역 데이터로만 학습되었으며, 고동역 휴머노이드 동작을 위한 공개 벤치마크 데이터셋이 존재하지 않는다.
- **Why**: 로봇공학과 캐릭터 애니메이션에서 실제 배포를 위해서는 일상 동작뿐 아니라 복잡한 고동역 동작을 안정적으로 제어할 수 있는 통합 컨트롤러가 필수적이다.
- **Approach**: Frame-accelerated augmentation으로 저동역 데이터를 고동역 패턴으로 변환하여 학습 노출을 확대하고, Residual MoE의 Speed-Aware Router와 Dynamic Expert-Assignment를 통해 동작 강도에 따라 동적으로 네트워크 용량을 할당한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: Comparison between FARM and the baseline FC on two high-dynamic motions. FARM accurately completes both*

- **HDHM 데이터셋 구축**: 3593개의 물리적으로 타당한 고동역 클립으로 구성된 첫 번째 공개 고동역 휴머노이드 동작 벤치마크 제시
- **추적 성공률 개선**: 기존 FC 베이스라인 대비 고동역 동작에서 42.8% 추적 실패율 감소
- **오차 감소**: 전체 평균 관절 위치 오차(MPJPEg) 14.6% 감소 달성
- **저동역 성능 보존**: 저동역 동작에서 거의 완벽한 추적 정확도 유지

## How

![Figure 2](figures/fig2.webp)

*Figure 2: Overview of the FARM pipeline. Failure cases are*

- Frame-Accelerated Augmentation: AMASS 데이터에서 프레임 갭을 1.25×로 균등 가속하여 hard sample 채굴, 학습 시 1.0-1.5× 범위로 랜덤 가속 적용
- Base Controller: 기존 FC(Fully Constrained) 컨트롤러를 저동역 기준선으로 사용
- Residual MoE 아키텍처: 기본 컨트롤러의 출력에 추가 처리 용량을 적응적으로 할당
- Speed-Aware Router(SAR): 동작의 동역 강도(per-frame 평균 관절 속도)를 기반으로 모션을 계층화하여 각 강도 대역을 dedicated expert 부분으로 라우팅
- Dynamic Expert-Assignment(DEA): 저동역 세그먼트에서는 최소 expert만 활성화, 고동역으로 갈수록 점진적으로 더 많은 expert 활성화
- Goal-Conditioned RL 학습: PPO 알고리즘으로 각 타임스텝에서 관찰과 모션 목표에 조건화된 정책 최적화

## Originality

- Frame-accelerated augmentation 개념: 저동역 데이터를 고동역 동작 패턴으로 변환하는 새로운 데이터 증강 기법의 창안
- Dynamic Expert-Assignment 메커니즘: 기존 MoE의 고정된 expert 할당 방식에서 벗어나 동작 강도에 따라 동적으로 expert 개수를 조절하는 혁신적 접근
- HDHM 벤치마크: 고동역 휴머노이드 제어 분야를 위한 최초의 체계적으로 큐레이션된 공개 데이터셋 개발
- Speed-Aware Router 설계: 동작 강도 기반 계층적 라우팅으로 저동역과 고동역 모션을 명시적으로 분리하는 구조

## Limitation & Further Study

- 평가가 평탄한 지형에만 제한되어 있으며, 불규칙한 지형이나 환경 상호작용이 있는 현실 시나리오에서의 성능 검증 필요
- Hard sample 채굴 시 1.25× 고정 가속도 사용으로 인한 임의성—최적의 가속도 인수에 대한 민감도 분석 부족
- HDHM 데이터셋의 규모(3593개)가 AMASS(10k+ 시퀀스)에 비해 상대적으로 작으며, 다양한 캐릭터와 신체 구조에 대한 일반화 검증 제한
- Residual MoE의 expert 개수, 라우터 임계값 등 하이퍼파라미터 선택에 대한 상세 ablation 부재
- **후속 연구**: (1) 불규칙 지형 및 실제 로봇 환경에서의 전이 학습, (2) 다양한 신체 형태와 질량 분포에 대한 적응성 개선, (3) 더 큰 규모의 고동역 데이터셋 구축

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 물리 기반 휴머노이드 제어의 오래된 과제인 고동역 동작 추적 문제에 대해 Frame-Accelerated Augmentation과 Residual MoE라는 우아하고 효과적인 솔루션을 제시하며, 동시에 첫 번째 공개 고동역 벤치마크를 기여함으로써 학계에 상당한 임팩트를 미칠 수 있는 논문이다.

## Related Papers

- 🔗 후속 연구: [[papers/1283_Benchmarking_Humanoid_Imitation_Learning_with_Motion_Difficu/review]] — humanoid imitation learning의 어려운 동작 처리를 전문가 혼합으로 해결한다
- 🔄 다른 접근: [[papers/1392_FALCON_Learning_Force-Adaptive_Humanoid_Loco-Manipulation/review]] — 고동역 humanoid 제어를 다른 적응적 학습 방법으로 접근한다
- 🏛 기반 연구: [[papers/1265_AMO_Adaptive_Motion_Optimization_for_Hyper-Dexterous_Humanoi/review]] — adaptive motion optimization의 기본 개념을 제공하는 연구다
