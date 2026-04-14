# Vision in Action: Learning Active Perception from Human Demonstrations

> **저자**: Haoyu Xiong, Xiaomeng Xu, Jimmy Wu, Yifan Hou, Jeannette Bohg, Shuran Song | **날짜**: 2025-06-18 | **URL**: [https://arxiv.org/abs/2506.15666](https://arxiv.org/abs/2506.15666)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Vision in Action (ViA) uses an active head*

ViA는 6-DoF 로봇 넥과 VR 텔레오퍼레이션 인터페이스를 통해 인간의 능동적 지각 전략을 직접 학습하여 이중팔 조작 로봇의 성능을 향상시키는 시스템이다.

## Motivation

- **Known**: 로봇 조작 학습에서 손목 카메라나 고정 카메라가 일반적으로 사용되며, 능동적 지각은 로봇공학에서 오래된 연구 주제이다.
- **Gap**: 기존 로봇 시스템은 인간의 자연스러운 시선 이동(탐색, 추적, 초점)을 포착하지 못하며, 시각적 폐색 상황에서 인간과 로봇의 관찰 공간 불일치 문제가 있다.
- **Why**: 능동적 지각은 인간의 조작 능력의 핵심이며, 이를 로봇에 구현하면 폐색된 환경에서의 복잡한 조작 작업 성능을 크게 향상시킬 수 있다.
- **Approach**: 6-DoF 로봇 팔을 로봇 넥으로 활용하고, 3D 장면 표현을 중간 매개체로 사용하여 VR 텔레오퍼레이션에서 지연 시간을 최소화하며, 행동 복제를 통해 인간 시연으로부터 능동적 지각 정책을 학습한다.

## Achievement

![Figure 5](figures/fig5.webp)

*Figure 5: Policy Learning Camera Setup Comparison Results. We report stage-wise success rates across*

- **유연한 6-DoF 로봇 넥**: 기존 2-DoF 넥 대비 인간 상체 움직임을 효과적으로 재현
- **중간 3D 표현 기반 VR 인터페이스**: RGB 직접 스트리밍 방식의 motion-to-photon 지연 문제를 해결하여 VR 멀미 제거
- **45% 성공률 향상**: 기존 손목 카메라 및 고정 카메라 대비 시각적 폐색이 있는 세 가지 조작 작업에서 성능 개선
- **학습된 능동적 지각 전략**: 탐색, 추적, 초점 조정 등 인간의 복잡한 지각 행동을 행동 복제로 자동 학습

## How

![Figure 2](figures/fig2.webp)

*Figure 2: VR Teleoperation Comparison. [Left] Traditional RGB streaming suffers from motion-to-photon*

- ARX5 6-DoF 로봇 팔을 로봇 넥으로 설치하고 카메라를 엔드 이펙터에 장착
- RGB-D 데이터로부터 월드 프레임 포인트 클라우드 스트리밍
- 사용자의 최신 헤드 포즈를 기반으로 실시간 view rendering 수행
- 로봇의 헤드 및 팔 움직임을 비동기적으로 업데이트하여 지연 시간 감소
- 공유 관찰 공간(shared observation space)에서 인간 시연자가 로봇과 동일한 시각으로 조작 수행
- 행동 복제(behavior cloning)로 visuomotor policy 학습

## Originality

- **6-DoF 팔을 로봇 넥으로 활용**: 기존 연구와 달리 복잡한 생체역학 설계 대신 상용 로봇 팔 재활용으로 단순성과 유연성 확보
- **중간 3D 표현 기반 VR 텔레오퍼레이션**: 직접 RGB 스트리밍 대신 3D 장면 표현으로 motion-to-photon 지연 완전히 해결
- **공유 관찰 공간 개념**: 인간이 로봇과 동일한 시점에서 시연하도록 강제하여 인간-로봇 관찰 불일치 문제를 근본적으로 제거
- **능동적 지각의 end-to-end 학습**: 손으로 설계한 saliency 휴리스틱이나 uncertainty reduction 대신 실제 인간 시연으로부터 직접 학습

## Limitation & Further Study

- 세 가지 제한된 조작 작업에서만 평가되었으며 더 다양한 시나리오에서의 일반화 성능 미검증
- 인간 텔레오퍼레이션 데이터 수집의 확장성 문제: 각 작업마다 충분한 인간 시연 데이터 필요
- 3D 포인트 클라우드 표현이 빠르게 변하는 동적 환경에서의 한계 미분석
- 정책이 훈련 데이터와 크게 다른 환경이나 객체 구성에 대한 적응성 불명확
- **후속 연구**: 다양한 조작 도메인으로 확대, 더 적은 인간 시연으로 학습 가능한 방법 개발, 동적 환경 대응 능력 강화, 도메인 일반화 성능 평가

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: ViA는 능동적 지각, VR 텔레오퍼레이션, 이중팔 조작을 효과적으로 통합한 혁신적 시스템으로, 중간 3D 표현을 통한 지연 시간 해결과 공유 관찰 공간 개념이 특히 창의적이며, 시각적 폐색이 있는 복잡한 실제 작업에서 실질적인 성능 향상을 달성했다.
