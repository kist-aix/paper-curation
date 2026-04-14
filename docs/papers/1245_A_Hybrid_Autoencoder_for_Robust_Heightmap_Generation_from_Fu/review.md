---
title: "1245_A_Hybrid_Autoencoder_for_Robust_Heightmap_Generation_from_Fu"
authors:
  - "Dennis Bank"
  - "Joost Cordes"
  - "Thomas Seel"
  - "Simon F. G. Ehlers"
date: "2026.02"
doi: ""
arxiv: ""
score: 4.0
essence: "인도체형 로봇의 보행을 위해 LiDAR와 깊이 카메라 데이터를 융합하여 높이맵을 생성하는 하이브리드 Encoder-Decoder Structure를 제안하며, CNN과 GRU를 결합한 구조로 멀티모달 데이터를 처리한다."
tags:
  - "cat/Multimodal_Vision-Language_Policy_Learning"
  - "sub/Multimodal_Terrain_Perception"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Bank et al._2026_A Hybrid Autoencoder for Robust Heightmap Generation from Fused Lidar and Depth Data for Humanoid Ro.pdf"
---

# A Hybrid Autoencoder for Robust Heightmap Generation from Fused Lidar and Depth Data for Humanoid Robot Locomotion

> **저자**: Dennis Bank, Joost Cordes, Thomas Seel, Simon F. G. Ehlers | **날짜**: 2026-02-05 | **URL**: [https://arxiv.org/abs/2602.05855](https://arxiv.org/abs/2602.05855)

---

## Essence


인도체형 로봇의 보행을 위해 LiDAR와 깊이 카메라 데이터를 융합하여 높이맵을 생성하는 하이브리드 Encoder-Decoder Structure를 제안하며, CNN과 GRU를 결합한 구조로 멀티모달 데이터를 처리한다.

## Motivation

- **Known**: 기존 시스템은 단일 센서 기반 파이프라인에 의존하거나 SLAM, elevation mapping 등 계산 집약적인 기법을 사용하며, 깊이 카메라는 조명에 민감하고 LiDAR는 지연 시간이 크다.
- **Gap**: 멀티모달 센서 융합을 통한 로봇 중심의 높이맵 생성과 시간적 일관성을 동시에 보장하는 학습 기반 프레임워크의 부재.
- **Why**: 인도체형 로봇의 안정적인 보행은 신뢰성 있는 지형 인식이 필수적이며, 멀티모달 융합은 단일 센서의 한계를 극복하고 더 정확한 지형 재구성을 가능하게 한다.
- **Approach**: CNN 인코더로 공간 특징을 추출하고 GRU 코어로 시간적 일관성을 유지하는 하이브리드 아키텍처를 구축하여, 구면 투영으로 처리한 LiDAR와 깊이 카메라 데이터를 융합하며, PPO 기반 강화학습 정책과 통합한다.

## Achievement


- **멀티모달 융합의 성능 개선**: 깊이 카메라 단독 대비 7.2%, LiDAR 단독 대비 9.9% 재구성 정확도 향상
- **시간적 드리프트 감소**: 3.2초 시간 문맥 통합을 통한 지도 작성 드리프트 감소
- **최적화된 높이맵 표현**: 6-8 cm 격자 간격에서 안정적인 보행 정책 수렴 달성
- **실시간 처리 가능성**: 구면 투영과 CNN 기반 처리로 자원 제한 환경에서의 확장성 확보

## How


- Intel RealSense 깊이 카메라(160×120 해상도)와 LIVOX MID-360 LiDAR(276×40 구면 투영)에서 분리된 CNN 인코더로 특징 추출
- 각 모달리티에서 256차원 잠재 표현 생성 후 선형 변환과 계층 정규화를 통해 멀티모달 융합
- 로봇 상태 벡터(IMU 기반 선형/각속도, 위치, 방향) 및 이전 타임스텝 높이맵 예측을 추가 입력으로 통합
- GRU 기반 재귀 디코더에서 시간적 문맥을 학습하여 로봇 중심 높이맵 재구성
- PPO 강화학습으로 높이맵 기반 보행 정책 학습, 대칭성과 발 접촉 슬라이딩 페널티를 포함한 보상 설계
- LiDAR 구면 투영 전처리: 행 단위 갭 채우기, 최근접 이웃 채우기, 3×3 메디안 필터 적용 및 0.2-3.0 m 범위 클리핑

## Originality

- 멀티모달 센서 융합을 위한 CNN-GRU 하이브리드 아키텍처로 공간 특징과 시간적 일관성을 동시에 처리
- 구면 투영을 통한 효율적인 LiDAR 전처리로 계산 복잡도 감소와 CNN 호환성 향상
- 로봇 중심의 로컬 높이맵을 중간 표현으로 활용하여 지각과 제어의 모듈식 분리 달성
- 높이맵 격자 해상도(7 cm)와 강화학습 정책의 수렴 관계를 체계적으로 분석

## Limitation & Further Study

- 센서 캘리브레이션, 가우시안 잡음, 반사 표면 등 실제 환경의 도전 요소에 대한 정량적 평가 부족
- Isaac Lab 시뮬레이션 환경에서의 결과이며 실제 로봇 하드웨어에서의 성능 검증 미흡
- GRU의 메모리 길이(3.2초)가 장시간 지형 변화에 대한 적응성에 미치는 영향 분석 부재
- 다양한 센서 조합(예: 스테레오 카메라, 구조화된 광)에 대한 확장성과 일반화 성능 미검증
- 후속연구: 실제 동적 환경에서의 온라인 학습, 전이 학습을 통한 다양한 로봇 플랫폼 적응, 센서 고장 시 복원력 평가

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 멀티모달 센서 융합과 시간적 모델링을 결합한 창의적인 접근으로 인도체형 로봇의 지형 인식 성능을 크게 향상시켰으며, 구면 투영의 효율성과 강화학습 정책의 통합이 잘 구성되어 있으나, 실제 로봇 실험 검증과 실환경 도전 요소 분석이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/1352_DemoDiffusion_One-Shot_Human_Imitation_using_pre-trained_Dif/review]] — 둘 다 humanoid 로봇의 지형 인식을 다루지만 하이브리드 오토인코더는 LiDAR+depth 융합을, DPL은 depth-only 접근법을 사용한다.
- 🔗 후속 연구: [[papers/1323_CReF_Cross-modal_and_Recurrent_Fusion_for_Depth-conditioned/review]] — CReF의 cross-modal fusion 기법이 LiDAR와 깊이 카메라 데이터 융합에서 더 효과적인 multimodal 처리를 제공할 수 있다.
- 🧪 응용 사례: [[papers/1411_Gallant_Voxel_Grid-based_Humanoid_Locomotion_and_Local-navig/review]] — Gallant의 voxel grid 기반 네비게이션 시스템이 높이맵 생성 결과를 실제 humanoid 보행 제어에 활용할 수 있다.
- 🏛 기반 연구: [[papers/1268_An_Empirical_Evaluation_of_Four_Off-the-Shelf_Proprietary_Vi/review]] — 상용 VIO 시스템의 성능 벤치마크가 LiDAR와 깊이 카메라 융합 시스템의 비교 기준을 제공한다.
- 🔄 다른 접근: [[papers/1352_DemoDiffusion_One-Shot_Human_Imitation_using_pre-trained_Dif/review]] — 둘 다 humanoid depth perception이지만 DPL은 depth-only 접근법을, 하이브리드 오토인코더는 LiDAR+depth 융합을 사용한다.
- 🔄 다른 접근: [[papers/1323_CReF_Cross-modal_and_Recurrent_Fusion_for_Depth-conditioned/review]] — 둘 다 depth 기반 humanoid locomotion이지만 CReF는 cross-modal fusion을, 하이브리드 오토인코더는 LiDAR+depth 융합을 사용한다.
