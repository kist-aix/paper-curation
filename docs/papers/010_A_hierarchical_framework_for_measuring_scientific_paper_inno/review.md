# A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs

> **저자**: Bowen Zhi | **날짜**: 2025-11-25 | **URL**: [https://arxiv.org/abs/2512.00077](https://arxiv.org/abs/2512.00077)

---

## Essence

![Figure 2](figures/fig2.png)

*Figure 2.1: The composite robot model used in the simulation, illustrating (a) the Unitree H1*

초과 사지(Supernumerary Limbs)가 장착된 인형형 로봇의 안정적인 보행을 위해 학습 기반 저수준 보행 제어와 모델 기반 고수준 동적 평형 제어를 결합한 계층적 제어 아키텍처를 제시한다.

## Motivation

- **Known**: Deep Reinforcement Learning은 복잡한 로봇 보행 제어에 효과적이며, 추가 사지를 정적 앵커나 각운동량 제어용으로 활용하는 연구가 존재한다.
- **Gap**: 다목적 인형형 팔과 같은 무거운 초과 사지가 생성하는 연속적이고 큰 동적 간섭을 관리하면서 동시에 보행을 유지하는 일반화된 제어 전략이 부족하다.
- **Why**: 초과 사지는 로봇의 조작 능력을 크게 향상시키지만, 동적 불안정성을 야기하므로, 이를 해결함으로써 단일 플랫폼에서 조작과 이동을 동시에 수행할 수 있는 다용도 휴머노이드 로봇 개발이 가능해진다.
- **Approach**: Unitree H1 로봇에 대해 PPO와 모방 학습을 통한 DRL 기반 보행 정책을 학습하고, 초과 사지의 구성을 실시간 CoM 피드백에 따라 조정하는 독립적인 모델 기반 동적 평형 제어기를 개발하여 두 제어기를 계층적으로 통합한다.

## Achievement

![Figure 3](figures/fig3.png)

*Figure 3.1: Training performance of the PPO agent over 500 million environment steps. (a)*

- **DRL 기반 저수준 보행 제어**: PPO 알고리즘과 커리큘럼 학습을 통해 Unitree H1용 안정적인 보행 정책을 개발하였다.
- **모델 기반 고수준 동적 평형 제어기**: CoM과 CoS 피드백을 기반으로 초과 사지 구성을 능동적으로 조정하여 보행 중 동적 불안정성을 완화한다.
- **계층적 제어 프레임워크 검증**: 세 가지 조건(기준선, 정적 페이로드, 동적 평형)에서 평가 결과, 동적 평형 제어기가 정적 페이로드 대비 CoM 궤적의 DTW 거리를 47% 감소시켰다.
- **개선된 보행 패턴**: 동적 평형 제어가 기준선에 더 유사한 보행 패턴을 생성하고, 지면 반발력(GRF)의 조정된 anti-phase 패턴을 달성하였다.

## How

![Figure 2](figures/fig2.png)

*Figure 2.1: The composite robot model used in the simulation, illustrating (a) the Unitree H1*

- **시스템 아키텍처**: 저수준 DRL 기반 보행 제어와 고수준 모델 기반 동적 평형 제어로 구성된 계층적 구조
- **저수준 제어**: Proximal Policy Optimization(PPO) 알고리즘으로 모방 학습을 통해 보행 정책 학습, 커리큘럼 학습으로 초과 사지의 질량과 자세를 점진적으로 도입
- **고수준 제어**: 실시간 상태 추정을 바탕으로 CoM 위치에 따라 초과 사지의 관절각을 조정하는 모델 기반 제어기
- **제어 통합**: 저수준 보행 정책의 출력과 고수준 평형 제어기의 명령을 적절히 융합하여 최종 관절 토크 생성
- **평가 메트릭**: Dynamic Time Warping(DTW) 거리, Center of Mass 궤적 분석, 보행 재안정화 성능, Ground Reaction Forces 패턴 분석

## Originality

- 기존 초과 사지 연구는 정적 브레이싱 또는 특수화된 비인형형 부속물에 초점을 맞춘 반면, 본 연구는 다목적 인형형 팔을 보행 중 능동적 평형 보조에 활용하는 일반화된 접근법을 제시한다.
- 학습 기반과 모델 기반 제어를 명확하게 분리하여 계층적으로 통합하는 방식은 복잡한 로봇 제어 문제에 대한 실용적인 해결책을 제공한다.
- 커리큘럼 학습을 통한 점진적 초과 사지 도입 전략은 DRL 정책의 강건성을 향상시키는 효과적인 방법론이다.

## Limitation & Further Study

- **시뮬레이션 기반 평가**: 물리 기반 시뮬레이션 환경(MuJoCo)에서만 검증되었으며, 실제 하드웨어 플랫폼에서의 성능 검증이 필요하다.
- **환경 제한**: 평탄한 보행 환경에서만 평가되었으며, 불규칙한 지형이나 외부 외란에 대한 강건성 평가가 부족하다.
- **초과 사지 구성**: 고정된 초과 사지 형태와 질량에 대해서만 평가되었으며, 다양한 초과 사지 구성에 대한 일반화 가능성이 불명확하다.
- **제어 파라미터**: 모델 기반 평형 제어기의 게인 튜닝 과정과 최적화 과정이 상세히 기술되지 않았다.
- **후속 연구**: 실제 로봇 플랫폼에서의 구현 및 검증, 다양한 지형과 동적 외란에 대한 성능 평가, 초과 사지 구성의 자동 최적화 방법 개발이 필요하다.

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 초과 사지가 장착된 인형형 로봇의 보행 안정성 문제를 해결하기 위해 계층적 제어 구조를 통해 학습 기반과 모델 기반 제어를 효과적으로 결합한 독창적인 접근법을 제시하며, 47% DTW 거리 감소 등 정량적 성과를 입증했다. 다만 실제 하드웨어 검증과 복잡한 환경에서의 평가가 필요하다.
