---
title: "1601_UniSkill_Imitating_Human_Videos_via_Cross-Embodiment_Skill_R"
authors:
  - "Hanjung Kim"
  - "Jaehyun Kang"
  - "Hyolim Kang"
  - "Meedeum Cho"
  - "Seon Joo Kim"
date: "2025.05"
doi: ""
arxiv: ""
score: 4.0
essence: "UniSkill은 대규모의 라벨 없는 교차-구현(cross-embodiment) 비디오 데이터로부터 구현-무관한 스킬 표현을 학습하여, 인간 비디오 시연으로부터 추출한 스킬을 로봇 정책으로 직접 전이할 수 있는 프레임워크이다."
tags:
  - "cat/Embodied_Navigation_and_Planning"
  - "sub/Robotic_Foundation_Generalization"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kim et al._2025_UniSkill Imitating Human Videos via Cross-Embodiment Skill Representations.pdf"
---

# UniSkill: Imitating Human Videos via Cross-Embodiment Skill Representations

> **저자**: Hanjung Kim, Jaehyun Kang, Hyolim Kang, Meedeum Cho, Seon Joo Kim, Youngwoon Lee | **날짜**: 2025-05-13 | **URL**: [https://arxiv.org/abs/2505.08787](https://arxiv.org/abs/2505.08787)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: The overview of UniSkill. (a) Inverse Skill Dynamics (ISD) and Forward Skill Dynamics*

UniSkill은 대규모의 라벨 없는 교차-구현(cross-embodiment) 비디오 데이터로부터 구현-무관한 스킬 표현을 학습하여, 인간 비디오 시연으로부터 추출한 스킬을 로봇 정책으로 직접 전이할 수 있는 프레임워크이다.

## Motivation

- **Known**: 기존 방법들은 인간-로봇 스킬 전이를 위해 paired 데이터셋, 다중 카메라 설정, 또는 장면과 작업 정렬이 필요했다. 최근 연구들은 명시적 라벨 없이 스킬 표현을 학습하려 시도했으나, 데이터 수집에 제약이 남아있다.
- **Gap**: 기존의 XSkill 등 방법은 여전히 인간과 로봇 비디오 간 암묵적 정렬을 가정하거나 특정 환경과 작업에 제한된다. 웹 규모의 임의 비디오 데이터로부터 실제 정렬 제약 없이 스킬을 학습하는 방법이 부족하다.
- **Why**: 로봇 학습의 데이터 부족 문제를 해결하기 위해 대규모 인간 비디오를 활용할 수 있다면, 로봇의 다양한 작업 학습을 크게 확장할 수 있다. 이는 로봇 학습의 확장성과 실용성을 크게 향상시킨다.
- **Approach**: UniSkill은 Inverse Skill Dynamics(ISD)와 Forward Skill Dynamics(FSD)를 joint training하여 비디오의 동적 변화(temporally distant frames 간)를 인코딩하고, 이미지 편집 파이프라인을 활용해 동적 영역을 강조한다. 이를 통해 구현-무관한 스킬 표현을 학습하고, 학습된 스킬로 조건화된 로봇 정책을 훈련한다.

## Achievement

![Figure 3](figures/fig3.webp)

*Figure 3: Overview of our tabletop experiments. (a) Average results on the tabletop benchmark using*

- **embodiment-agnostic 스킬 표현 학습**: 라벨 없이 대규모 비디오 데이터로부터 구현 간 공통 스킬 표현 추출
- **인간-로봇 imitation 성공**: 시뮬레이션과 실제 환경에서 인간 비디오로부터 추출한 스킬로 로봇이 행동 재현
- **스케일러빌리티**: Something-Something V2, H2O, DROID, Bridge V2, LIBERO 등 다양한 public 데이터셋 활용 가능
- **정렬 제약 제거**: 인간-로봇 비디오 정렬이나 task/scene 정렬 불필요
- **robustness 및 compositional 능력**: 미학습 객체와 복합 작업에 대한 우수한 성능

## How

![Figure 2](figures/fig2.webp)

*Figure 2: The overview of UniSkill. (a) Inverse Skill Dynamics (ISD) and Forward Skill Dynamics*

- **Inverse Skill Dynamics (ISD)**: 비디오의 temporally distant frames 쌍 (I_t, I_{t+k})으로부터 스킬 표현 z_t 추출
- **Forward Skill Dynamics (FSD)**: 스킬 표현 z_t로부터 미래 프레임 I_{t+k}를 재구성하여 dynamics 정보 인코딩
- **이미지 편집 파이프라인**: 동적 영역을 강조하고 정적 콘텐츠는 억제하여 embodiment-agnostic 패턴 추출
- **joint training**: ISD와 FSD를 함께 훈련하여 상호 감시 신호 제공
- **Skill-conditioned policy**: 추출된 스킬 표현으로 조건화된 로봇 정책 π(o_t, z_t) 훈련
- **Inference**: 인간 비디오로부터 연속적으로 스킬을 추출하고 로봇 정책에 입력하여 sequential execution

## Originality

- **predictive representation 접근**: XSkill의 clustering 기반과 달리, future frame forecasting으로 스킬 학습하여 데이터 정렬 필요성 완전 제거
- **이미지 편집 파이프라인 활용**: 동적 영역 강조를 통한 embodiment-agnostic 특징 추출의 창의적 활용
- **라벨-무관성**: 임의의 웹 규모 비디오 데이터 활용으로 최대 확장성 달성
- **구현 다양성**: 인간, Franka, WidowX 등 다양한 embodiment 간 스킬 공유 실증

## Limitation & Further Study

- **평가 범위**: 실험이 주로 테이블탑 조작 작업에 제한되어, 이동 로봇이나 다른 도메인 적용 가능성 미확인
- **스킬 해석성**: 학습된 스킬 표현의 의미론적 해석이 명확하지 않을 수 있음 (FSD 가시화로 부분적 설명)
- **temporal distance k 선택**: 최적의 temporal distance k 결정 기준이나 민감도 분석 미흡
- **비디오 품질 의존성**: 저해상도나 모션 블러가 있는 비디오에 대한 robust성 미평가
- **후속 연구**: (1) 더 복잡한 다체 조작이나 동적 환경에서의 성능 검증, (2) 언어 지시와의 결합, (3) 온라인 적응 학습 메커니즘 개발

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: UniSkill은 데이터 정렬 제약을 제거하고 웹 규모 비디오를 활용한 cross-embodiment 스킬 학습의 새로운 패러다임을 제시하며, 실험적으로 인간-로봇 imitation의 가능성을 입증한 의미 있는 연구이다. 다만 평가 범위의 확대와 더 복잡한 작업에 대한 검증이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/1594_Transferring_Foundation_Models_for_Generalizable_Robotic_Man/review]] — cross-embodiment 기반 일반화를 위해 UniSkill은 skill representation 학습을, Transferring Foundation Models는 foundation model 전이를 사용하는 다른 접근법
- 🏛 기반 연구: [[papers/1522_Learning_from_Massive_Human_Videos_for_Universal_Humanoid_Po/review]] — UniSkill의 human video demonstration이 Learning from Massive Human Videos의 대규모 인간 행동 데이터 활용 방법론을 기반으로 구현
- 🧪 응용 사례: [[papers/1460_LLM3Large_Language_Model-based_Task_and_Motion_Planning_with/review]] — UniSkill의 cross-embodiment transfer가 Human-Humanoid Cross-Embodiment 연구의 실제 구현체로서 humanoid 로봇 정책 학습에 직접 활용 가능
- 🔄 다른 접근: [[papers/1594_Transferring_Foundation_Models_for_Generalizable_Robotic_Man/review]] — foundation model 기반 일반화를 위해 Transferring Foundation Models는 언어-추론 기반 분할을, UniSkill은 cross-embodiment 표현 학습을 사용하는 다른 접근법
