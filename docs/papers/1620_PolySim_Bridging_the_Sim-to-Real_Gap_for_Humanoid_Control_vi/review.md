# PolySim: Bridging the Sim-to-Real Gap for Humanoid Control via Multi-Simulator Dynamics Randomization

> **저자**: Zixing Lei, Zibo Zhou, Sheng Yin, Yueru Chen, Qingyao Xu, Weixin Li, Yunhong Wang, Bowei Tang, Wei Jing, Siheng Chen | **날짜**: 2025-10-02 | **URL**: [https://arxiv.org/abs/2510.01708](https://arxiv.org/abs/2510.01708)

---

## Essence

![Figure 2](figures/fig2.webp)

*Fig. 2: Visual illustration of PolySim. The pink star denotes*

PolySim은 여러 이질적인 시뮬레이터를 병렬로 활용하여 훈련하는 플랫폼으로, 단일 시뮬레이터의 귀납적 편향을 완화하고 현실 세계로의 전이 갭을 줄인다.

## Motivation

- **Known**: 시뮬레이션 기반 인간형 로봇 제어는 RL과 고충실도 시뮬레이터 발전으로 진전되었으나, 단일 시뮬레이터 훈련은 그 시뮬레이터의 모델링 가정을 상속받아 현실 세계와의 갭이 발생한다.
- **Gap**: 기존 domain randomization 방법은 매개변수 수준에서만 무작위화를 수행하므로 시뮬레이터의 기본 transition model을 벗어나지 못하며, 단일 시뮬레이터의 구조적 한계를 극복하지 못한다.
- **Why**: 인간형 로봇은 고차원이고 접촉이 많아 현실 데이터 수집이 비용이 크므로, 여러 시뮬레이터를 활용한 효과적인 현실 전이는 실제 배포에 필수적이다.
- **Approach**: PolySim은 다중 시뮬레이터로부터 병렬 환경을 동시에 실행하여 dynamics 수준의 domain randomization을 구현하고, 훈련-시뮬레이션 분리 아키텍처와 unified simulator router를 통해 이질적 시뮬레이터를 통합한다.

## Achievement

![Figure 4](figures/fig4.webp)

*Fig. 4: Success rate on seen and unseen simulators under*

- **이론적 분석**: PolySim이 매개변수 수준 무작위화보다 시뮬레이터 귀납적 편향에 대해 더 타이트한 상한을 제공함을 증명
- **Sim-to-sim 성능**: MuJoCo 평가에서 IsaacSim 베이스라인 대비 52.8% 실행 성공률 개선
- **Zero-shot 현실 배포**: 추가 fine-tuning 없이 실제 Unitree G1 humanoid에 성공적으로 배포

## How

![Figure 3](figures/fig3.webp)

*Fig. 3: System overview of the proposed parallel multi-simulator RL framework (Mode III). Left (Training Framework):*

- Training-Simulation Isolation: TrainClient와 SimServer를 분리하여 시뮬레이터와 RL 학습자를 독립적으로 실행하고 GPU 리소스 경쟁을 완화
- Simulator Router: 이질적 시뮬레이터의 장면 매개변수, API, 수치 규범을 통일하여 invariant semantics 제공
- GPU Pass-through Communication: NCCL을 통한 원격 프로시저 호출로 데이터를 GPU에 유지하여 고처리량 병렬 훈련 실현
- Physics Harmonization: 각 시뮬레이터에서 최대한 정렬된 장면 구성
- API Translation: 공통 인터페이스 노출 및 일관된 관찰-행동-보상 신호 전달
- Numerical Normalization: 신경망 행동이 각 엔진에 올바르게 해석되도록 보장

## Originality

- 기존 cross-simulator 프레임워크(HumanoidVerse, MetaSim)와 달리 단일 훈련 루프 내에서 실시간 병렬 cross-simulator RL 최적화 구현
- Dynamics 수준의 domain randomization 개념 도입으로 기존 매개변수 수준 무작위화의 한계 극복
- 클라이언트-서버 아키텍처 및 GPU pass-through RPC를 통해 이질적 시뮬레이터의 효율적 병렬 실행 실현

## Limitation & Further Study

- 여러 시뮬레이터 통합의 계산 비용 증가 및 리소스 요구사항에 대한 상세 분석 부족
- 현실 배포는 단일 로봇(Unitree G1)에서만 검증되어 다양한 플랫폼에서의 일반화 가능성 미확인
- Simulator router의 physics harmonization이 모든 이질적 시뮬레이터 쌍에서 동등한 효과를 보이는지 불명확
- 후속 연구: 더 많은 실제 로봇 플랫폼에서의 배포 검증, 시뮬레이터 수 증가에 따른 성능 포화 분석, online system identification과의 결합 탐색

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: PolySim은 다중 시뮬레이터 병렬 훈련을 통해 simulator inductive bias를 근본적으로 완화하는 혁신적 접근법이며, 견고한 이론적 근거와 실제 배포 성공으로 humanoid control의 현실 전이 문제 해결에 중요한 기여를 한다.
