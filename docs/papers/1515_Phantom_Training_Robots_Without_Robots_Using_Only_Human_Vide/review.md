---
title: "1515_Phantom_Training_Robots_Without_Robots_Using_Only_Human_Vide"
authors:
  - "Marion Lepert"
  - "Jiaying Fang"
  - "Jeannette Bohg"
date: "2025.03"
doi: ""
arxiv: ""
score: 4.0
essence: "로봇 하드웨어 없이 인간 비디오 데모만으로 로봇 정책을 학습하는 Phantom 방법을 제안하며, 데이터 편집 기법을 통해 인간-로봇 간의 embodiment gap을 극복하고 zero-shot 배포를 달성한다."
tags:
  - "cat/Humanoid_Teleoperation_and_Interaction"
  - "sub/Human-Robot_Data_Collection"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Lepert et al._2025_Phantom Training Robots Without Robots Using Only Human Videos.pdf"
---

# Phantom: Training Robots Without Robots Using Only Human Videos

> **저자**: Marion Lepert, Jiaying Fang, Jeannette Bohg | **날짜**: 2025-03-02 | **URL**: [https://arxiv.org/abs/2503.00779](https://arxiv.org/abs/2503.00779)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1: Overview of learning from human videos. Our method enables training robot policies without collecting any robot *

로봇 하드웨어 없이 인간 비디오 데모만으로 로봇 정책을 학습하는 Phantom 방법을 제안하며, 데이터 편집 기법을 통해 인간-로봇 간의 embodiment gap을 극복하고 zero-shot 배포를 달성한다.

## Motivation

- **Known**: 로봇 데이터 수집은 비용이 많이 들고 확장이 어려우며, 기존 human-to-robot 학습 방법들은 로봇 데이터와의 co-training이 필요하다. 최근 robot-to-robot cross-embodiment learning에서 data-editing 기법이 성공을 보였으나 human-to-robot 설정에는 적응되지 않았다.
- **Gap**: 인간 비디오만으로 로봇 정책을 학습할 수 있는 완전한 방법이 부재하며, 특히 closed-loop 제어와 변형 가능한 객체를 모두 처리하면서 로봇 데이터에 의존하지 않는 접근법이 없다.
- **Why**: 로봇 데이터 수집의 비용과 물류적 어려움을 제거하면 전 세계 누구나 RGBD 카메라만으로 데이터 수집에 참여할 수 있어 다양하고 규모 있는 데이터 확보가 가능해진다.
- **Approach**: 인간 비디오에서 hand pose estimator로 손 포즈를 추출하여 로봇 액션으로 변환하고, inpainting으로 인간의 손을 제거한 후 렌더링된 로봇 팔을 합성하여 데이터 편집을 수행한다. 이 augmented 데이터로 imitation learning 정책을 학습하고 실제 로봇에 zero-shot 배포한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Fig. 1: Overview of learning from human videos. Our method enables training robot policies without collecting any robot *

- **로봇 데이터 완전 제거**: 로봇 데이터 수집 없이도 6가지 작업에서 높은 성공률 달성
- **확장 가능한 데이터 수집**: RGBD 카메라만으로 누구나 다양한 환경에서 데모 수집 가능
- **Closed-loop 제어**: open-loop 실행 제한 없이 폐루프 정책 배포 가능
- **다양한 객체 처리**: 경직된 객체, 변형 가능한 객체, 다중 객체 모두 지원
- **분포 외 일반화**: 미처본 환경에서의 일반화 능력 입증
- **로봇 무관 데이터**: 수집된 데이터를 다양한 로봇 플랫폼에 적용 가능

## How

![Figure 2](figures/fig2.webp)

*Fig. 2: Overview of our data-editing pipeline for learning robot policies from human videos. During training, we first e*

- HaMeR를 이용한 hand pose estimation으로 각 프레임의 손 포즈 추정
- Inpainting 기법으로 인간 손을 이미지에서 제거
- 추정된 hand pose를 기반으로 로봇 팔의 posed 3D 모델을 렌더링하여 합성
- Hand pose로부터 로봇 관절 각도(joint angles)로의 변환을 통한 로봇 액션 추출
- Augmented dataset으로 imitation learning 정책 학습
- Test time에 실제 로봇 관측에 가상 로봇을 overlay하여 visual consistency 보장
- 학습된 정책의 zero-shot 배포

## Originality

- **처음으로 순수 인간 데이터만 사용**: 로봇 co-training 없이 인간-로봇 transfer 달성
- **Data editing의 새로운 적용**: Robot-to-robot에서 성공한 inpainting + virtual overlay 기법을 human-to-robot에 창의적으로 적응
- **Hand pose 기반 액션 추출**: Proprioceptive 정보 부재 상황에서 간단하면서도 효과적인 액션 추출 방법 제시
- **포괄적 평가**: 폐루프 제어, 변형 가능한 객체, 다중 객체를 모두 고려한 평가 수행

## Limitation & Further Study

- **Pinch grasp 제한**: 엄지손가락과 검지손가락 pinch grasp만 지원하여 다양한 그래스 타입에 미적용
- **Hand pose estimation 의존성**: HaMeR 모델의 성능에 크게 의존하며 occlusion이나 복잡한 상황에서 실패 가능
- **Precision 손실**: 인간 데모의 내재적 부정확성으로 인해 높은 정밀도가 필요한 작업에서 성능 저하 가능
- **Third-person view 요구**: RGBD 카메라의 고정된 제3자 시점에서만 작동하여 egocentric view 미지원
- **렌더링 품질에 민감**: 가상 로봇의 렌더링 현실성이 정책 성능에 영향을 미칠 수 있음
- **후속 연구 방향**: First-person view 지원, 다양한 그래스 타입 확장, egocentric human video 활용, 더욱 정교한 hand pose estimation 기법 통합

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 연구는 로봇 데이터 의존성을 완전히 제거하면서도 실용적인 성과를 달성했으며, 데이터 편집 기법의 창의적 적용으로 로봇 학습의 확장성을 혁신적으로 개선한 중요한 기여다. 다만 pinch grasp 제한과 hand pose estimation에 대한 의존성이 실제 적용의 폭을 제한한다.

## Related Papers

- 🔄 다른 접근: [[papers/1501_Is_imitation_learning_the_route_to_humanoid_robots/review]] — 둘 다 VR 텔레오퍼레이션에서 신경망 정책을 다루지만 서로 다른 접근 방식이나 개선사항을 제시한다
- 🔗 후속 연구: [[papers/1441_Heavy_lifting_tasks_via_haptic_teleoperation_of_a_wheeled_hu/review]] — 기본적인 적응 학습을 haptic 피드백과 무거운 물체 조작으로 확장했다
- 🏛 기반 연구: [[papers/1452_HMC_Learning_Heterogeneous_Meta-Control_for_Contact-Rich_Loc/review]] — adaptive neural control의 개념이 heterogeneous meta-control의 기반이 된다
- 🔗 후속 연구: [[papers/1337_DexMimicGen_Automated_Data_Generation_for_Bimanual_Dexterous/review]] — 인간 비디오만으로 로봇 정책을 학습하는 Phantom 방식을 데이터 생성 관점에서 확장한 DexMimicGen과 공통된 접근법을 갖는다.
- 🏛 기반 연구: [[papers/1372_DROID_A_Large-Scale_In-The-Wild_Robot_Manipulation_Dataset/review]] — 로봇 하드웨어 없이 인간 시연으로 학습하는 Phantom의 핵심 데이터셋 구축 철학이 EgoMimic의 egocentric 비디오 기반 모방학습과 일치한다.
- 🔄 다른 접근: [[papers/1522_Learning_from_Massive_Human_Videos_for_Universal_Humanoid_Po/review]] — 로봇 없이 인간 비디오로 정책 학습하는 Phantom과 대규모 인간 비디오로 휴머노이드 정책을 학습하는 접근법이 동일한 문제를 다룬다.
- 🔗 후속 연구: [[papers/1441_Heavy_lifting_tasks_via_haptic_teleoperation_of_a_wheeled_hu/review]] — Learning Adaptive Neural Teleoperation의 힘 적응 개념을 무거운 물체 조작에 특화하여 적용했다
- 🔗 후속 연구: [[papers/1452_HMC_Learning_Heterogeneous_Meta-Control_for_Contact-Rich_Loc/review]] — 기존 텔레오퍼레이션의 힘 제어를 heterogeneous meta-control로 확장했다
- 🔄 다른 접근: [[papers/1501_Is_imitation_learning_the_route_to_humanoid_robots/review]] — 둘 다 VR 텔레오퍼레이션에서 신경망 정책을 다루지만 서로 다른 접근 방식이나 관점을 제시한다
- 🔄 다른 접근: [[papers/1588_OKAMI_Teaching_Humanoid_Robots_Manipulation_Skills_through_S/review]] — 단일 RGB-D 비디오로 휴머노이드 조작을 학습하는 OKAMI와 인간 비디오만으로 로봇 정책을 훈련하는 Phantom이 동일한 비디오 기반 학습 문제를 다룬다.
