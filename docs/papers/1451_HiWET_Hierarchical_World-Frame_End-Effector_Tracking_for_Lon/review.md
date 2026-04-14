---
title: "1451_HiWET_Hierarchical_World-Frame_End-Effector_Tracking_for_Lon"
authors:
  - "Zhanxiang Cao"
  - "Liyun Yan"
  - "Yang Zhang"
  - "Sirui Chen"
  - "Jianming Ma"
date: "2026.02"
doi: "10.48550/arXiv.2602.06341"
arxiv: ""
score: 4.0
essence: "HiWET는 휴머노이드 로봇의 장기 조작 작업을 위해 world-frame 기반 end-effector 추적을 수행하는 계층적 강화학습 프레임워크를 제안하며, Kinematic Manifold Prior(KMP)를 통해 조작 매니폴드를 학습 공간에 임베딩한다."
tags:
  - "cat/Humanoid_Locomotion_Control_Systems"
  - "sub/Humanoid_Locomotion_Learning"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Cao et al._2026_HiWET Hierarchical World-Frame End-Effector Tracking for Long-Horizon Humanoid Loco-Manipulation.pdf"
---

# HiWET: Hierarchical World-Frame End-Effector Tracking for Long-Horizon Humanoid Loco-Manipulation

> **저자**: Zhanxiang Cao, Liyun Yan, Yang Zhang, Sirui Chen, Jianming Ma, Tianyue Zhan, Shengcheng Fu, Yufei Jia, Cewu Lu, Yue Gao | **날짜**: 2026-02-06 | **DOI**: [10.48550/arXiv.2602.06341](https://doi.org/10.48550/arXiv.2602.06341)

---

## Essence

![Figure 2](figures/fig2.webp)

*Fig. 2.*

HiWET는 휴머노이드 로봇의 장기 조작 작업을 위해 world-frame 기반 end-effector 추적을 수행하는 계층적 강화학습 프레임워크를 제안하며, Kinematic Manifold Prior(KMP)를 통해 조작 매니폴드를 학습 공간에 임베딩한다.

## Motivation

- **Known**: 휴머노이드 전신 동작 제어는 강화학습과 모방학습으로 발전했으며, 명령 기반 loco-manipulation 프레임워크들이 end-effector 제어를 가능하게 했다. 다만 대부분의 기존 방법들은 body-centric 좌표계를 사용하여 누적 world-frame drift를 보정할 수 없다.
- **Gap**: 기존 imitation 방법들은 joint-space 오차를 최적화하므로 end-effector 추적 정확도를 보장하지 못하고, command-driven 방법들은 body-centric 프레임으로 인해 legged locomotion의 누적 drift와 high-frequency oscillation에 대응하지 못한다.
- **Why**: 휴머노이드가 정적 reach workspace를 벗어난 작업을 수행할 때 base transport와 arm coordination이 필수적이며, world-frame 기반 명시적 reasoning이 이를 해결할 수 있기 때문에 중요하다.
- **Approach**: HiWET은 high-level policy가 world-frame 좌표에서 subgoal(base velocity, body height, local end-effector target)을 생성하고 low-level policy가 이를 joint command로 변환하는 계층적 구조를 채택한다. KMP를 통해 residual learning으로 kinematically valid한 행동을 유도한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Fig. 1.*

- **World-frame 계층적 제어**: Upper-body manipulation과 lower-body locomotion을 명시적 spatial interface로 조정하여 world-frame consistency를 달성하고 base transport로 작업 영역을 능동적으로 변형
- **Kinematic Manifold Prior**: Residual action space 내에 KMP를 통합하여 high-speed kinematic reference를 제공하고 exploration dimensionality를 감소시켜 kinematically invalid behavior를 완화
- **Sim-to-real 성공**: Simulation에서 12.4 mm world-frame tracking error를 달성하고 zero-shot transfer로 물리적 휴머노이드에서 diverse limb configuration 하에 stable locomotion 입증

## How

![Figure 2](figures/fig2.webp)

*Fig. 2.*

- Semi-Markov Decision Process(Semi-MDP) 기반 계층적 강화학습 모델 설계로 long-horizon manipulation 목표와 instantaneous stability constraint를 조화
- High-level world-frame command policy는 K step마다 base-relative hand pose subgoal 생성
- Low-level whole-body tracking policy는 high frequency에서 subgoal을 joint-space target으로 변환하며 PD controller와 직접 인터페이싱
- KMP는 pretrained kinematic reference를 제공하고 residual action으로 dynamic adaptability 보존
- Two-stage training: Stage 1에서 tracker는 history encoder와 state estimator를 통해 base-relative end-effector command 추적 학습, Stage 2에서 commander는 world-frame target을 base-frame subgoal로 변환
- Command dataset을 IK error와 manipulability로 필터링한 importance sampling과 uniform random sampling 혼합으로 학습 안정화

## Originality

- Body-centric 대신 world-frame 기반 end-effector tracking으로 cumulative drift 문제를 근본적으로 해결하는 문제 재정의
- Kinematic Manifold Prior를 residual learning 형태로 action space에 임베딩하여 exploration 효율을 크게 향상
- Hierarchical 구조에서 global spatial reasoning과 dynamic execution을 명시적으로 분리하여 상위-하위 신체 coordination을 체계화
- Zero-shot sim-to-real transfer 성공으로 simulation-only learning의 실용성 입증

## Limitation & Further Study

- 실험은 Humanoid 플랫폼 내에서만 검증되었으며 다른 legged humanoid 아키텍처에 대한 일반화 가능성 미검증
- World-frame tracking 정확도(12.4 mm)는 높지만 극도로 정밀한 micro-manipulation 작업에는 추가 개선 필요
- KMP pretraining이 필요하므로 초기 학습 비용이 높을 수 있으며, training dataset 구축(IK error/manipulability 필터링)의 manual effort 필요
- Long-horizon 작업 평가가 simulation 중심이므로 real-world에서의 long-duration task 성능과 robustness에 대한 더 광범위한 검증 필요
- Base-relative end-effector command 생성 시 end-effector reachability에 대한 명시적 제약이 부재하여 unreachable command 가능성 존재

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: HiWET은 world-frame 기반 명시적 공간 reasoning과 KMP를 통한 효율적 학습을 결합하여 휴머노이드 loco-manipulation의 오래된 문제를 근본적으로 해결한다. Sim-to-real 성공과 우수한 tracking 정확도는 실용적 가치를 입증하며, hierarchical control 설계는 향후 복잡한 humanoid 제어에 영향을 미칠 것으로 예상된다.

## Related Papers

- 🏛 기반 연구: [[papers/1434_H2-COMPACT_Human-Humanoid_Co-Manipulation_via_Adaptive_Conta/review]] — HiWET의 world-frame end-effector tracking은 H2-COMPACT의 협력적 조작에서 정확한 접촉 궤적 생성에 필요한 기술이다.
- 🔄 다른 접근: [[papers/1471_Humanoid_Policy__Human_Policy/review]] — 두 논문 모두 상체 조작을 다루지만, HiWET는 world-frame tracking에, Humanoid Policy는 시간 궤적 최적화에 초점을 둔다.
- 🔗 후속 연구: [[papers/1587_Object-Centric_Dexterous_Manipulation_from_Human_Motion_Data/review]] — HiWET의 장기 조작 능력은 object-centric dexterous manipulation을 통해 더욱 정교한 물체 조작으로 발전할 수 있다.
- 🔄 다른 접근: [[papers/1392_FALCON_Learning_Force-Adaptive_Humanoid_Loco-Manipulation/review]] — 둘 다 하체-상체 협응을 다루지만 FALCON은 dual-agent 접근, HiWET은 계층적 end-effector 추적 방식을 사용한다.
- 🔗 후속 연구: [[papers/1434_H2-COMPACT_Human-Humanoid_Co-Manipulation_via_Adaptive_Conta/review]] — H2-COMPACT의 계층적 정책 구조는 HiWET의 world-frame end-effector tracking을 협력적 조작 환경으로 확장한다.
- 🔄 다른 접근: [[papers/1471_Humanoid_Policy__Human_Policy/review]] — 두 논문 모두 상체 조작을 다루지만, Humanoid Policy는 시간 최적화에, HiWET는 world-frame tracking에 초점을 둔다.
- 🔗 후속 연구: [[papers/1302_Adapt3R_Adaptive_3D_Scene_Representation_for_Domain_Transfer/review]] — HiWET는 Adapt3R의 3D 표현을 실제 로봇의 world-frame 추적으로 확장한다
