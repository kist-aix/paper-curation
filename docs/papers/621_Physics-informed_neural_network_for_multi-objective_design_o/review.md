# Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless Joint Torque Estimation in Humanoid Robots

> **저자**: Ines Sorrentino, Giulio Romualdi, Lorenzo Moretti, Silvio Traversaro, Daniele Pucci | **날짜**: 2025-07-14 | **URL**: [https://arxiv.org/abs/2507.10105](https://arxiv.org/abs/2507.10105)

---

## Essence

![Figure 2](figures/fig2.webp)

*Fig. 2: Block diagram of the multi-layer torque control architecture implemented on the ergoCub humanoid robot. The*

본 논문은 Physics-Informed Neural Networks (PINNs)와 Unscented Kalman Filter (UKF)를 결합하여 휴머노이드 로봇의 관절 토크 센서 없이 전신 토크 제어를 수행하는 프레임워크를 제시한다. 이 방식은 마찰 모델링과 토크 추정을 통합하여 실시간 토크 제어 아키텍처를 구현한다.

## Motivation

- **Known**: 기존 토크 제어는 직접 토크 측정에 의존하거나 Recursive Newton-Euler Algorithm (RNEA) 같은 모델 기반 방법을 사용하며, 마찰 추정은 Coulomb, viscous, LuGre, Stribeck 모델 등을 활용한다.
- **Gap**: floating-base 휴머노이드 로봇에서 실시간 마찰 보상을 위한 PINNs 적용이 거의 미개척 상태이며, 기존 sensorless 토크 제어 방법들은 복잡한 마찰 동역학 및 고비율 감속기의 탄성 변형을 정확히 모델링하지 못한다.
- **Why**: 센서 없는 토크 제어는 비용, 통합 복잡도, 센서 제약을 제거하면서도 동적 환경에서 안전하고 적응적인 인간-로봇 상호작용과 준수성(compliance)을 가능하게 한다.
- **Approach**: PINNs는 모터 및 관절 속도 버퍼를 입력으로 사용하여 비선형 정적 및 동적 마찰을 추정하고, UKF는 PINN 기반 마찰 추정값을 직접 측정 입력으로 활용하여 floating-base 시스템의 관절 토크를 실시간으로 추정한다.

## Achievement

![Figure 4](figures/fig4.webp)

*Fig. 4: CoM tracking comparison: RNEA-PINN (left) vs. UKF-PINN (right). Green rectangles indicate external contacts.*

- **개선된 토크 추적 정확도**: RNEA 대비 토크 추적 RMSE가 감소하고 동적 밸런싱 실험에서 우수한 외란 거부 특성을 달성
- **에너지 효율 향상**: RNEA 대비 향상된 에너지 효율을 달성
- **확장성**: 서로 다른 마찰 특성을 가진 유사 하드웨어 플랫폼 간에 재식별 없이 일관된 성능 유지
- **실시간 제어**: 전신 토크 제어 아키텍처 내에서 실시간 구현 가능
- **비교 우위**: 위치 제어와의 비교 분석에서 제안된 토크 제어 접근법의 장점 입증

## How

![Figure 2](figures/fig2.webp)

*Fig. 2: Block diagram of the multi-layer torque control architecture implemented on the ergoCub humanoid robot. The*

- 모터 및 관절 속도 버퍼를 입력으로 하는 PINN 아키텍처 설계로 정적 마찰 캡처
- 관절 인코더 해상도 제약을 극복하기 위해 smoothing Kalman Filter를 활용한 속도 추정
- PINN으로부터의 마찰 토크 추정값을 UKF의 직접 측정 입력으로 통합
- UKF 공식화를 fixed-base에서 floating-base 시스템으로 확장
- multi-layer 토크 제어 아키텍처 구현으로 전신 시스템 제어
- ergoCub 휴머노이드 로봇에서의 동적 밸런싱 실험을 통한 검증

## Originality

- floating-base 휴머노이드 로봇의 실시간 마찰 보상을 위한 PINNs-UKF 통합 프레임워크는 기존 연구와 구별되는 것으로, 이전 연구들은 주로 오프라인 모델링이나 매개변수 식별에 중점
- 모터 및 관절 속도 버퍼를 활용하여 정적 마찰 추정 능력 강화
- PINN 기반 마찰 추정값을 UKF 측정 입력으로 직접 활용하는 혁신적 통합 방식
- 고비율 감속기(high-ratio harmonic drives)가 있는 전기 모터 시스템을 위한 특화된 설계

## Limitation & Further Study

- 단일 로봇 플랫폼(ergoCub)에서의 검증이 주가 되어 다양한 로봇 형태에 대한 일반화 가능성 미확인
- PINN 네트워크의 학습에 필요한 데이터 수집 및 라벨링 과정, 최적 네트워크 구조 결정 프로세스 상세 기술 부족
- 외부 충격(external contacts) 상황에서의 성능 평가가 제한적이며, 극단적 동역학 환경에서의 견고성 검증 필요
- UKF와 PINN의 매개변수 튜닝에 대한 민감도 분석 미시행
- 후속 연구에서는 다양한 로봇 플랫폼, 극한 환경, 강화학습을 통한 적응적 제어 전략 탐색 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 PINNs과 UKF의 혁신적 통합을 통해 센서 없는 토크 제어라는 실질적 문제를 해결하며, ergoCub에서의 엄밀한 실험 검증과 확장성 시연으로 휴머노이드 로봇의 실시간 준수 제어를 위한 강력한 기초를 제공한다.
