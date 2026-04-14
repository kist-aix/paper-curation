---
title: "1437_Hand-Eye_Autonomous_Delivery_Learning_Humanoid_Navigation_Lo"
authors:
  - "Sirui Chen"
  - "Yufei Ye"
  - "Zi-Ang Cao"
  - "Jennifer Lew"
  - "Pei Xu"
date: "2025.08"
doi: ""
arxiv: ""
score: 4.0
essence: "HEAD는 모듈식 접근으로 고수준 정책과 저수준 정책을 분리하여, 인간 동작 데이터와 egocentric vision으로부터 humanoid의 네비게이션, 로컬모션, 리칭 능력을 학습한다."
tags:
  - "cat/Humanoid_Teleoperation_and_Interaction"
  - "sub/Real-World_Humanoid_Skills"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chen et al._2025_Hand-Eye Autonomous Delivery Learning Humanoid Navigation, Locomotion and Reaching.pdf"
---

# Hand-Eye Autonomous Delivery: Learning Humanoid Navigation, Locomotion and Reaching

> **저자**: Sirui Chen, Yufei Ye, Zi-Ang Cao, Jennifer Lew, Pei Xu, C. Karen Liu | **날짜**: 2025-08-05 | **URL**: [https://arxiv.org/abs/2508.03068](https://arxiv.org/abs/2508.03068)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: System overview: HEAD consists of a high-level policy with two modules, navigation*

HEAD는 모듈식 접근으로 고수준 정책과 저수준 정책을 분리하여, 인간 동작 데이터와 egocentric vision으로부터 humanoid의 네비게이션, 로컬모션, 리칭 능력을 학습한다.

## Motivation

- **Known**: 기존 visual navigation 방법은 로봇을 point mass로 추상화하여 2D 평면 움직임에만 초점을 맞추며, humanoid의 전신 협조 제어와 3D 공간 네비게이션에 대한 연구는 부족하다.
- **Gap**: Humanoid 로봇이 인간 환경에서 네비게이션과 리칭을 동시에 수행하기 위한 3D 전신 제어 방법이 부재하며, 이질적인 인간 데이터 소스를 효율적으로 활용하는 방법론이 필요하다.
- **Why**: Humanoid 로봇의 실용적 배치를 위해 복잡한 인간 환경에서의 자율 물체 전달 능력이 필수적이며, 학습 기반의 접근이 전통적 제어 방법보다 더 일반화 가능한 솔루션을 제공할 수 있다.
- **Approach**: 고수준 정책은 Aria glasses로부터 수집한 인간 데이터로 head와 hand의 목표 위치/방향을 학습하고, 저수준 전신 컨트롤러는 대규모 motion capture 데이터로 GAN 기반 imitation RL을 통해 3점(eyes, left/right hands) 추적을 학습한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: System overview: HEAD consists of a high-level policy with two modules, navigation*

- **모듈식 아키텍처**: Ego-centric vision perception과 물리적 행동을 분리하여 이질적 데이터 소스의 유연한 활용과 새로운 장면으로의 확장성을 실현
- **GAN 기반 전신 제어**: Spatially sparse한 3점 목표 추적으로부터 human-like 동작을 생성하는 discriminator 기반 imitation RL 프레임워크 개발
- **상하체 협조 학습**: 독립적인 두 개의 discriminator로 상체와 하체를 별도로 보상하여 동시 작업 수행 능력 향상
- **실세계 배포 성공**: Unitree G1 humanoid 로봇에서 인간 실내 공간에서의 네비게이션 및 리칭 성능 입증
- **데이터 혼합 활용**: 대규모 인간 탐색 데이터, 중규모 환경별 시연, 소량의 로봇 경험을 결합하여 generalization과 domain adaptation 달성

## How

![Figure 2](figures/fig2.webp)

*Figure 2: System overview: HEAD consists of a high-level policy with two modules, navigation*

- 고수준 정책: RGB egocentric 이미지를 입력받아 head 위치/방향과 hand 위치/방향을 예측하는 navigation 모듈과 model-based reaching 모듈로 구성
- 저수준 컨트롤러: 5시간 규모의 retargeted human motion capture 데이터로부터 GAN-like 목적함수를 통해 3점 추적 정책 학습
- Root-free 정책: 세계 좌표계에서의 root position/velocity 대신 navigation goal과 onboard camera로부터 전역 정보 추론
- Sparse target tracking: 전신 tracking 대신 3개 키포인트만 명시하여 데이터 요구량 감소 및 일반화 성능 향상
- 혼합 학습 데이터: Internet-scale 인간 탐색 데이터(generalization), 환경별 데이터(perception domain shift), 로봇 경험(embodiment gap) 활용

## Originality

- Head와 wrist orientation 추적 포함으로 비틀림(twisting) 같은 고급 조작 스킬 가능
- Sparse 3-point 인터페이스로 VR/AR 기기로부터 쉽게 수집 가능한 인간 데이터 활용
- GAN 기반 imitation RL을 whole-body tracking에 적용하여 분포 모방 학습
- Dual discriminator 구조로 상하체 독립적 보상을 통한 협조 제어
- Real-world humanoid 로봇 배포로 시뮬레이션-실제 간극 실증

## Limitation & Further Study

- 5시간 규모의 motion capture 데이터는 상대적으로 작으며, 더 다양한 동작 범위 확보 필요
- Domain shift 완화를 위해 환경별 중규모 데이터와 로봇 경험이 필수적으로 필요한 점은 실용성 제약
- Root position/velocity 추정 정확도에 의존하는 문제는 부분적으로만 해결됨
- 실세계 실험이 단일 Unitree G1 로봇에서만 진행되어 다양한 humanoid 형태에 대한 일반화 미확인
- 고수준 정책의 장기 네비게이션 능력 평가가 제한적이며, 대규모 실내 공간에서의 성능 검증 부재

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: HEAD는 modular 설계로 이질적 인간 데이터를 효율적으로 활용하면서도 GAN 기반 whole-body imitation RL과 dual discriminator를 통해 humanoid의 3D 네비게이션과 리칭을 통합적으로 학습하는 혁신적 프레임워크이며, 실제 로봇 배포로 실용성을 입증했다.

## Related Papers

- 🏛 기반 연구: [[papers/1373_EgoVLA_Learning_Vision-Language-Action_Models_from_Egocentri/review]] — HEAD의 egocentric vision 기반 navigation과 reaching 학습은 EgoVLA의 Vision-Language-Action 모델이 실제 환경에서 구현될 때의 핵심 기술적 기반입니다.
- 🔄 다른 접근: [[papers/1417_Generalizable_Humanoid_Manipulation_with_3D_Diffusion_Polici/review]] — HEAD의 모듈식 고저수준 정책 분리와 3D Diffusion Policy의 통합적 접근법은 humanoid loco-manipulation을 위한 서로 다른 아키텍처 설계 철학을 보여줍니다.
- 🔗 후속 연구: [[papers/1373_EgoVLA_Learning_Vision-Language-Action_Models_from_Egocentri/review]] — EgoVLA의 Vision-Language-Action 모델과 retargeting 기술은 HEAD의 egocentric vision 기반 navigation과 reaching 능력을 언어 지시까지 확장할 수 있습니다.
- 🔗 후속 연구: [[papers/1417_Generalizable_Humanoid_Manipulation_with_3D_Diffusion_Polici/review]] — 3D Diffusion Policy 기반 일반화 가능한 조작 기술은 HEAD의 모듈식 고수준-저수준 정책 분리 구조와 결합하여 더욱 복합적인 loco-manipulation 작업을 수행할 수 있습니다.
- 🔗 후속 연구: [[papers/1627_What_Matters_in_Building_Vision-Language-Action_Models_for_G/review]] — InternVLA-A1이 RoboVLMs 프레임워크의 핵심 요소들을 통합하여 더 포괄적인 VLA 모델로 발전시킨 연구
- 🏛 기반 연구: [[papers/1610_Visual_Embodied_Brain_Let_Multimodal_Large_Language_Models_S/review]] — VeBrain의 multimodal integration이 InternVLA-A1의 unified understanding과 generation 능력을 embodied control에 적용하는 기반을 제공
- 🏛 기반 연구: [[papers/1528_Learning_Humanoid_End-Effector_Control_for_Open-Vocabulary_V/review]] — HERO의 비전-언어 기반 휴머노이드 제어가 Hand-Eye 자율 배송 시스템의 기본 프레임워크를 제공한다.
- 🔄 다른 접근: [[papers/1576_MobileH2R_Learning_Generalizable_Human_to_Mobile_Robot_Hando/review]] — 모바일 로봇 핸드오버를 위한 MobileH2R과 자율 배송을 위한 Hand-Eye 시스템이 모두 인간-로봇 상호작용 문제를 다룬다.
- 🔄 다른 접근: [[papers/1511_LangWBC_Language-directed_Humanoid_Whole-Body_Control_via_En/review]] — InternVLA-A1과 유사하게 언어-비전-행동 통합을 다루지만 CVAE 기반 전신 제어에 특화된 접근법을 제시함
