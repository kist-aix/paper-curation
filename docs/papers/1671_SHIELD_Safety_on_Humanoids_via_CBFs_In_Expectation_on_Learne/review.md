# SHIELD: Safety on Humanoids via CBFs In Expectation on Learned Dynamics

> **저자**: Lizhi Yang, Blake Werner, Ryan K. Cosner, David Fridovich-Keil, Preston Culbertson, Aaron D. Ames | **날짜**: 2025-05-16 | **URL**: [https://arxiv.org/abs/2505.11494](https://arxiv.org/abs/2505.11494)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1. A humanoid robot implementing the SHIELD architecture au-*

SHIELD는 학습 기반 휴머노이드 로봇 컨트롤러에 안전 계층을 추가하여 실시간 제약 조건 명시와 확률적 안전 보장을 동시에 제공하는 프레임워크이다. 동적 잔차 모델과 확률적 이산 시간 제어 배리어 함수(S-DTCBF)를 통해 기존 블랙박스 RL 정책을 재학습 없이 안전화한다.

## Motivation

- **Known**: RL 기반 로봇 컨트롤러는 복잡한 작업에서 우수한 성능을 보이지만 공식적 안전 보장이 부족하다. CBF는 정확한 동역학 모델이 있을 때 효과적이지만 humanoid와 같은 복잡한 시스템에는 적용이 어렵다.
- **Gap**: 학습 기반 컨트롤러의 견고한 성능과 형식적 안전 보장 사이의 간극이 존재한다. 기존 모델 기반 방법은 정확한 동역학 모델을 요구하지만 실제 humanoid 시스템에서는 이를 획득하기 어렵다.
- **Why**: Humanoid 로봇이 인간 환경에서 작동해야 하므로 실시간 안전 제약 명시와 강력한 안전 보장이 필수적이다. 동시에 성능을 유지하면서 재학습 없이 새로운 제약을 추가할 수 있어야 한다.
- **Approach**: SHIELD는 세 단계로 구성된다: (1) 사용자가 안전 제약 수학적으로 명시, (2) 실제 하드웨어 데이터로 CVAE 기반 동역학 잔차 모델 학습, (3) 학습된 잔차 분포를 활용하여 S-DTCBF 제약을 만족하도록 참조 신호 생성.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2. SHIELD enables real-world pedestrian avoidance with a humanoid robot, using a “general-purpose” RL policy. Top: *

- **계층적 안전 아키텍처**: 기존 autonomy stack 위에 비침습적(minimally-invasive) 안전 계층을 추가하여 재학습 없이 새로운 제약을 런타임에 명시 가능
- **확률적 안전 보장**: S-DTCBF 공식을 통해 유한 시간 K 스텝 내 제약 위반 확률에 대한 형식적 보증 제공
- **성능-안전 균형**: CVAE 기반 동역학 잔차 모델로 추적 성능 개선과 동시에 확률적 안전 보장 달성
- **실제 humanoid 검증**: Unitree G1 로봇에서 실내/외부 환경에서의 장애물 회피 및 보행자 회피 성공 실증

## How

![Figure 3](figures/fig3.webp)

*Fig. 3. Higher α = L(P, K = 10, h(x0) = 10, δ = 0.01, σ) values*

- 동역학을 full-order Φ(s, a)에서 reduced-order 모델로 근사: x_{k+1} ≈ F(x_k) + G(x_k)u_k + d_k
- 조건부 변분 오토인코더(CVAE)로 동역학 잔차 분포 D 학습 (실제 하드웨어 롤아웃 데이터 활용)
- K-step 종료 확률 정의: P_u(K, x_0) = P{x_k ∉ C for some k ≤ K}로 안전 수량화
- 이산 시간 제어 배리어 함수 조건을 확률적으로 확장하여 h(x_k) ≥ α·h(x_0) 대신 확률 경계 기반 제약 설정
- 온라인에서 CVAE 샘플링을 통해 최소 침투 참조 신호 수정으로 S-DTCBF 제약 만족
- 임베디드 하드웨어에서 계산 가능한 장애물 회피 공식화 제공

## Originality

- 기존 CBF와 달리 안전 계층을 상단(reference signal 수준)에 배치하여 블랙박스 저수준 컨트롤러를 보존
- CVAE를 동역학 잔차 학습뿐 아니라 성능 개선과 안전 보장의 이중 목적으로 활용하는 방식이 새로움
- 확률적 이산 시간 CBF(S-DTCBF) 공식을 복잡한 humanoid 시스템에 처음 적용
- 실제 humanoid 보행 정책의 추적 오류(tracking error) 모델링을 통해 실제 시스템과의 괴리 명시적으로 처리

## Limitation & Further Study

- CVAE 학습에 필요한 실제 하드웨어 데이터 수집의 초기 비용이 높음
- 확률적 보장은 유한 시간(K-step) 범위에만 적용되며, 무한 시간 안전성은 보장하지 않음
- planar single integrator 모델로 단순화하여 humanoid의 전체 동역학 복잡성을 완전히 캡처하지 못할 가능성
- 학습된 CVAE가 훈련 분포 밖의 상황(예: 매우 이례적인 장애물 배치)에서 어떻게 동작하는지 명확하지 않음
- 후속 연구: 고차 동역학 모델 통합, 장기 안전 보장 방법 개발, 여러 제약 조건의 동시 처리 메커니즘

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: SHIELD는 학습 기반 humanoid 컨트롤러의 실제 배포를 위한 현실적이고 실용적인 안전 보장 방법을 제시하며, 데이터 기반과 모델 기반 방법의 간격을 효과적으로 연결한다. 실제 로봇 실험 검증과 함께 이론적 안전 보장을 제공하여 로봇 안전 연구에 상당한 기여를 한다.
