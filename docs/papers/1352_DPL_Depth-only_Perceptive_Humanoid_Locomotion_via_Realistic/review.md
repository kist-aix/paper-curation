---
title: "1352_DPL_Depth-only_Perceptive_Humanoid_Locomotion_via_Realistic"
authors:
  - "Jingkai Sun"
  - "Gang Han"
  - "Pihai Sun"
  - "Wen Zhao"
  - "Jiahang Cao"
date: "2025.10"
doi: ""
arxiv: ""
score: 4.0
essence: "휴머노이드 로봇의 깊이 이미지만을 사용한 지형 인식 보행을 위해, 현실적인 깊이 합성과 cross-attention transformer 기반 지형 재구성을 통합한 프레임워크를 제안한다."
tags:
  - "cat/Multimodal_Vision-Language_Policy_Learning"
  - "sub/Multimodal_Terrain_Perception"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Sun et al._2025_DPL Depth-only Perceptive Humanoid Locomotion via Realistic Depth Synthesis and Cross-Attention Ter.pdf"
---

# DPL: Depth-only Perceptive Humanoid Locomotion via Realistic Depth Synthesis and Cross-Attention Terrain Reconstruction

> **저자**: Jingkai Sun, Gang Han, Pihai Sun, Wen Zhao, Jiahang Cao, Jiaxu Wang, Yijie Guo, Qiang Zhang | **날짜**: 2025-10-08 | **URL**: [https://arxiv.org/abs/2510.07152](https://arxiv.org/abs/2510.07152)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1: Overview of the proposed teacher–student distillation framework for humanoid perceptive locomotion. (A) The stud*

휴머노이드 로봇의 깊이 이미지만을 사용한 지형 인식 보행을 위해, 현실적인 깊이 합성과 cross-attention transformer 기반 지형 재구성을 통합한 프레임워크를 제안한다.

## Motivation

- **Known**: 쿼드루페드 로봇의 지형 인식 보행은 발전했으나, 휴머노이드 로봇은 깊이 이미지 기반 end-to-end 학습의 낮은 효율성과 sim-to-real gap, 또는 elevation map 기반 방법의 다중 센서 의존성과 지연 문제로 제약된다.
- **Gap**: 기존 깊이 이미지 기반 방법은 노이즈와 자기 폐색(self-occlusion)에 취약하고 데이터 효율성이 낮으며, elevation map 방법은 전역 위치추정 시스템 없이는 작동하기 어렵다.
- **Why**: 휴머노이드 로봇이 실제 환경의 불규칙한 지형에서 안정적으로 보행할 수 있으려면 단일 깊이 센서만으로 외부 위치추정 없이 효율적으로 지형을 인식하고 적응하는 시스템이 필요하다.
- **Approach**: Blind backbone policy를 elevation map 사전학습으로 가이드하고, multi-modality cross-attention transformer로 노이즈 깊이 이미지에서 지형을 재구성하며, self-occlusion 인식 ray casting과 noise 모델링으로 현실적인 깊이 합성을 수행한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2: Ablation study of the proposed framework across four challenging terrains:*

- **Multi-stage 훈련 프레임워크**: 사전학습된 정책 기반의 end-to-end fine-tuning을 지원하며 외부 위치추정 시스템이 불필요하다.
- **Cross-modal transformer**: 부분적 깊이와 고유수용성(proprioceptive) 입력에서 지형 기하학을 재구성한다.
- **현실적 깊이 합성**: 폐색 인식과 노이즈 모델링을 적용하여 지형 재구성 오류를 30% 이상 감소시킨다.
- **실제 휴머노이드 로봇 검증**: 경사면, 계단, 갭, 불규칙한 야외 지형 등 다양한 환경에서 강건한 보행을 시연한다.

## How

![Figure 3](figures/fig3.webp)

*Fig. 3: The figure illustrates our physically grounded noise pipeline applied to synthetic*

- **Teacher-student 증류 구조**: 사전학습된 blind policy와 vision-based modulator를 결합하여 안정성과 적응성을 동시에 달성
- **Adversarial Motion Prior (AMP) 프레임워크**: 인간 동작 데이터로부터의 discriminator를 사용하여 자연스러운 보행 스타일 유도
- **깊이 이미지 생성**: Ray casting에 self-occlusion geometry와 물리 기반 노이즈 파이프라인을 적용하여 현실적인 센서 관측 합성
- **Cross-attention transformer 구조**: 깊이 시퀀스와 고유수용성 상태 이력을 multimodal fusion하여 구조화된 지형 표현 재구성
- **100Hz 정책 업데이트**: 1.0m × 1.0m 지형맵(5cm 해상도)을 상대 좌표로 인코딩하여 전역 위치 추정 회피

## Originality

- **사전학습 기반 효율화**: Elevation map 기반 사전학습을 활용하여 깊이 이미지 기반 훈련의 샘플 효율성 대폭 개선 (기존 [6]과 차별화)
- **Self-occlusion 인식 합성**: Ray casting에 기하학적 폐색 정보를 통합하여 현실의 깊이 센서 특성을 정밀하게 모사
- **End-to-end fine-tuning 가능**: 깊이 생성 모듈이 정책 end-to-end 미세조정을 지원하므로 재구성 네트워크와 정책 간의 도메인 갭 감소
- **외부 위치 추정 제거**: 부분적 깊이와 고유수용성만으로 로컬 지형 추론하여 복잡한 전역 매핑 시스템 불필요

## Limitation & Further Study

- **깊이 센서 노이즈 한계**: 극단적 조명 또는 반사 재질 환경에서의 깊이 측정 신뢰성 미검증
- **계산 비용 분석 부재**: Teacher-student 증류 및 transformer 추론의 실시간 성능 오버헤드 정량화 부족
- **로컬 지형 표현의 제약**: 1.0m × 1.0m 고정 영역만 처리하므로 장거리 경로 계획 불가
- **후속 연구**: (1) 동적 장애물 회피, (2) 다양한 깊이 센서 하드웨어 적응성, (3) 실외 극단 조건(눈, 모래 등)에서의 강건성 검증, (4) 계산 효율 최적화

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 깊이 이미지 기반 휴머노이드 보행의 오랜 과제(sim-to-real gap, 낮은 효율성, 외부 시스템 의존)를 사전학습, cross-attention, 현실적 합성을 통해 통합적으로 해결하며, 실제 로봇 검증으로 실용성을 입증한 견실한 연구이다.

## Related Papers

- 🔗 후속 연구: [[papers/1588_OKAMI_Teaching_Humanoid_Robots_Manipulation_Skills_through_S/review]] — object-aware retargeting을 통한 OKAMI의 조작 학습이 사전훈련된 확산 모델을 활용한 DemoDiffusion으로 확장될 수 있다.
