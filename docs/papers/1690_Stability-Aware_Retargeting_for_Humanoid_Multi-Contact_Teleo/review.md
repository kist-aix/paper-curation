---
title: "1690_Stability-Aware_Retargeting_for_Humanoid_Multi-Contact_Teleo"
authors:
  - "Stephen McCrory"
  - "Romeo Orsolino"
  - "Dhruv Thanki"
  - "Luigi Penco"
  - "Robert Griffin"
date: "2025.10"
doi: ""
arxiv: ""
score: 4.0
essence: "휴머노이드 로봇의 다중 접촉 텔레오퍼레이션 중 안정성을 향상시키기 위해 Centroidal stability 기반 retargeting을 제안하며, Linear Program 민감도 분석을 통해 효율적으로 안정성 여유 기울기를 계산한다."
tags:
  - "cat/Other"
  - "topic/humanoid"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/McCrory et al._2025_Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation.pdf"
---

# Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation

> **저자**: Stephen McCrory, Romeo Orsolino, Dhruv Thanki, Luigi Penco, Robert Griffin | **날짜**: 2025-10-05 | **URL**: [https://arxiv.org/abs/2510.04353](https://arxiv.org/abs/2510.04353)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Robot performing a teleoperated manipulation task, in*

휴머노이드 로봇의 다중 접촉 텔레오퍼레이션 중 안정성을 향상시키기 위해 Centroidal stability 기반 retargeting을 제안하며, Linear Program 민감도 분석을 통해 효율적으로 안정성 여유 기울기를 계산한다.

## Motivation

- **Known**: Centroidal 접근법은 비평면 다중 접촉에서 정적 안정성을 검증하는 데 효과적이며, 텔레오퍼레이션은 휴머노이드 로봇에게 참조 모션을 생성하는 강력한 방법이다.
- **Gap**: 기존 텔레오퍼레이션 시스템은 단순한 접촉 조건만 지원하며, 다중 손 접촉과 비평면 표면에서의 안정성 개선을 직접적으로 다루는 프레임워크가 부족하다.
- **Why**: 손 접촉을 포함한 복잡한 다중 접촉 조작 작업에서 모터 토크 포화와 슬립으로 인한 불안정성이 빈번히 발생하므로, 실시간으로 안정성을 보장하는 텔레오퍼레이션 기법이 필수적이다.
- **Approach**: Centroidal stability region과 actuation 제약을 결합한 Linear Program을 통해 안정성 여유를 정의하고, LP 민감도 분석으로 접촉점과 자세에 대한 기울기를 해석적으로 계산하여 공유 제어 기반의 retargeting을 수행한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: Robot performing a teleoperated manipulation task, in*

- **효율적 기울기 계산**: Linear Program 민감도 분석을 적용하여 centroidal stability region의 해석적 기울기를 도출하고 kHz 실시간 속도로 계산 가능
- **공유 제어 기법**: 안정성 여유가 자세에 민감한 상황에서만 자동으로 활성화되는 지능형 retargeting으로 사용자 제어와 로봇 안정성의 균형 달성
- **다중 시나리오 검증**: 시뮬레이션과 하드웨어에서 전방, 상방, 후방 손 접촉 등 다양한 비평면 접촉 조건에서 안정성 여유 증대 입증
- **성능 상관성 증명**: 높은 안정성 여유가 충격 복원력과 관절 토크 여유 개선과 직접적으로 상관됨을 실험적으로 검증

## How

![Figure 3](figures/fig3.webp)

*Figure 3: The 2d stability region encodes both actuation and friction*

- Quasi-static CoM stability region을 Linear Program으로 공식화하고, actuation 제약 조건 J(q)^T_c f을 포함하여 관절 토크 한계 모델링
- LP 민감도 분석 성질(Eq. 5)을 적용하여 안정성 영역 꼭짓점 a*_i에 대한 접촉점 위치 p_k와 전신 자세 q의 기울기 ∇a*_i(p_k), ∇a*_i(q) 도출
- Time-linearization을 통해 constraint matrix A(t)를 매개변수화하고, primal-dual 최적해 x*, y*를 활용하여 기울기 계산 (∂a*/∂θ = -y*^T G x*)
- 안정성 여유 m이 자세 변화에 민감한 방향을 식별하여, 그 방향으로 접촉점과 자세 setpoint를 동적으로 조정하는 shared control 최적화 수행
- 2d stability region을 시각적으로 오퍼레이터에게 제공하여 비평면 다중 접촉 상황에서 직관적 피드백 지원

## Originality

- Centroidal stability analysis와 Linear Program 민감도 분석을 결합하여 효율적 기울기 계산이라는 새로운 기술 기여
- 다중 접촉 텔레오퍼레이션에 stability margin 최적화를 처음으로 명시적으로 적용한 공유 제어 프레임워크
- Actuation-aware stability region (Eq. 2)을 LP 민감도 분석에 통합하여 관절 토크 제약을 동시에 고려하는 실용적 접근
- 비평면 손 접촉 다양한 시나리오(전방, 상방, 후방)에서의 실험적 검증을 통해 일반성 입증

## Limitation & Further Study

- Quasi-static 가정으로 인한 동적 운동(높은 속도의 조작)에 대한 적용 제한
- Time-linearization과 중력 토크 불변 가정(˙b(q)≈0)이 빠른 자세 변화에서 부정확할 수 있음
- 현재 접촉 상태(contact state)가 고정된 상태에서의 retargeting만 고려하며, 접촉 변경 및 진행 중 접촉 전환 시나리오 미포함
- **후속 연구**: 동적 stability 지표 확장, 접촉 순서 계획과의 통합, 충돌 감지 및 적응적 접촉 전환 메커니즘 개발

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 다중 접촉 텔레오퍼레이션에 centroidal 안정성 분석을 효과적으로 통합하고 LP 민감도를 통한 새로운 기울기 계산 방법을 제시하며, 시뮬레이션과 하드웨어 검증으로 실용성을 입증한 견고한 기여.