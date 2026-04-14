---
title: "1521_Learning_Differentiable_Reachability_Maps_for_Optimization-b"
authors:
  - "Masaki Murooka"
  - "Iori Kumagai"
  - "Mitsuharu Morisawa"
  - "Fumio Kanehiro"
date: "2025.08"
doi: "10.48550/arXiv.2508.11275"
arxiv: ""
score: 4.0
essence: "휴머노이드 로봇의 운동 계획 계산 비용을 줄이기 위해 신경망 또는 SVM을 이용해 학습한 미분 가능한 reachability map을 제안하고, 이를 연속 최적화 제약조건으로 활용하여 발걸음 계획, 다중 접촉 운동 계획, loco-manipulation 계획 등을 효율적으로 해결한다."
tags:
  - "cat/Humanoid_Locomotion_Control_Systems"
  - "sub/Humanoid_Locomotion_Learning"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Murooka et al._2025_Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation.pdf"
---

# Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation

> **저자**: Masaki Murooka, Iori Kumagai, Mitsuharu Morisawa, Fumio Kanehiro | **날짜**: 2025-08-15 | **DOI**: [10.48550/arXiv.2508.11275](https://doi.org/10.48550/arXiv.2508.11275)

---

## Essence


휴머노이드 로봇의 운동 계획 계산 비용을 줄이기 위해 신경망 또는 SVM을 이용해 학습한 미분 가능한 reachability map을 제안하고, 이를 연속 최적화 제약조건으로 활용하여 발걸음 계획, 다중 접촉 운동 계획, loco-manipulation 계획 등을 효율적으로 해결한다.

## Motivation

- **Known**: 로봇의 kinematic reachability를 나타내기 위해 그리드 기반의 이산 reachability map이 널리 사용되어 왔으며, 연속 최적화 기반 운동 계획에서는 box나 convex polyhedron으로 접근 가능 영역을 근사한다.
- **Gap**: 이산 reachability map은 궤적 검증에는 유용하나 궤적 최적화에 사용할 수 없고, 근사 형태는 접근 가능 영역을 보수적으로 제한하며 방향 제약 표현이 불명확하다는 문제가 있다.
- **Why**: 미분 가능한 reachability map을 제약조건으로 활용하면 역기구학을 반복적으로 풀지 않으면서도 정확한 접근 가능성 조건을 연속 최적화에 직접 임베드할 수 있어 휴머노이드 로봇의 복잡한 운동 계획 계산 비용을 크게 줄일 수 있다.
- **Approach**: binary classification 문제로 reachability 학습을 공식화하고, NN (multilayer perceptron)과 SVM을 이용하여 task space에서 연속이고 미분 가능한 scalar-valued function을 학습한 후, 이를 연속 최적화 문제의 제약조건으로 통합하여 다양한 humanoid 운동 계획을 수행한다.

## Achievement


- **Differentiable reachability map 제안**: 기존의 이산 reachability map과 달리 task-space 좌표에 대해 연속이고 미분 가능한 representation으로, 임의의 형태의 접근 가능 영역을 유연하게 표현 가능
- **두 가지 학습 모델**: NN과 SVM 모두 효과적으로 작동하며, 밀도 추정 기반 접근법(GMM 등)의 문제점을 피함
- **다양한 운동 계획 문제 해결**: footstep planning, multi-contact motion planning, loco-manipulation planning 등 복잡한 humanoid 운동 계획을 효율적으로 수행
- **계산 비용 감소**: 반복적인 역기구학 계산을 피하고 task-space 최적화로 joint-space 최적화보다 효율적인 해를 생성

## How


- task space의 end-effector pose들로부터 로봇 kinematic model을 이용해 reachable/unreachable 샘플 데이터셋 생성
- binary classification 문제로 공식화하여 yi ∈ {−1, 1} 레이블 할당
- NN의 경우 fully connected layers와 ReLU 활성화 함수를 가진 MLP 구조 사용, 선형 출력층으로 실수값 scalar 생성
- SVM의 경우 RBF kernel 등을 활용하여 비선형 분류 경계 학습
- 학습된 reachability map fR(r)을 제약조건 fR(r) ≥ 0으로 연속 최적화 문제에 임베드
- trajectory optimization, footstep planning 등 다양한 문제에서 제약조건으로 활용

## Originality

- 이산 reachability map을 연속이고 미분 가능한 함수로 변환하여 최적화 기반 계획에 직접 사용 가능하게 함
- binary classification을 통해 GMM 기반 밀도 추정의 한계(task-space 샘플 밀도가 reachability와 상관없을 수 있음)를 극복
- NN과 SVM 두 가지 학습 모델을 비교 검증하며 유연한 접근 제시
- 위치와 방향을 모두 포함하는 task space에서 arbitrarily shaped feasible regions를 표현 가능

## Limitation & Further Study

- 학습 데이터의 샘플링 해상도가 reachability map 정확도에 영향을 미치는데, 고차원 task space에서 필요한 샘플 개수가 기하급수적으로 증가 가능
- SE(3) 같은 비유클리드 공간에서의 학습 및 제약 표현 방법에 대한 상세한 논의 부족
- 학습된 map의 경계 부근에서 미분 가능성이 완벽한지, 수치 최적화에서의 수렴성에 대한 이론적 보장 부재
- 후속연구: 고차원 task space에서의 효율적 샘플링 전략, 적응형 샘플링을 통한 학습 효율성 개선, manifold 구조를 고려한 학습 방법 개발

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이산 reachability map의 한계를 극복하고 연속 최적화에 직접 활용 가능한 미분 가능한 reachability map을 제안한 점에서 매우 창의적이며, 다양한 humanoid 운동 계획 문제에 적용 가능해 실무적 가치가 높다. 다만 고차원 공간에서의 샘플링 효율성과 이론적 수렴성 보장에 대한 심화 논의가 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/1322_Cost-Matching_Model_Predictive_Control_for_Efficient_Reinfor/review]] — 모델 예측 제어의 효율성을 위한 비용 매칭 접근법이 reachability map 기반 최적화의 이론적 배경을 제공함
- 🔄 다른 접근: [[papers/1408_Full-Order_Sampling-Based_MPC_for_Torque-Level_Locomotion_Co/review]] — 두 논문 모두 휴머노이드 locomotion을 위한 최적화 기반 제어를 다루지만, learned reachability vs full-order sampling이라는 다른 접근법을 사용함
- 🔗 후속 연구: [[papers/1444_Language_to_Rewards_for_Robotic_Skill_Synthesis/review]] — 계층적 계획과 제어 프레임워크를 미분가능한 도달성 맵을 통해 더욱 효율적으로 구현할 수 있는 발전된 형태를 제시함
