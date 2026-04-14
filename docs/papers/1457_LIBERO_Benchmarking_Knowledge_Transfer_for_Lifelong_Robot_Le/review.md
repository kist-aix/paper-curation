---
title: "1457_LIBERO_Benchmarking_Knowledge_Transfer_for_Lifelong_Robot_Le"
authors:
  - "Bo Liu"
  - "Yifeng Zhu"
  - "Chongkai Gao"
  - "Yihao Feng"
  - "Qiang Liu"
date: "2023.06"
doi: ""
arxiv: ""
score: 4.0
essence: "로봇 조작 작업에서 선언적 지식과 절차적 지식의 전이를 함께 다루는 생애 주기 학습(LLDM)을 벤치마킹하기 위해 LIBERO 벤치마크를 제안한다. 130개의 절차적으로 생성된 작업과 고품질 시연 데이터를 제공하여 LLDM의 주요 5가지 연구 주제를 조사한다."
tags:
  - "cat/Task-Oriented_Skill_Acquisition"
  - "sub/Task_Learning_Benchmarks"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liu et al._2023_LIBERO Benchmarking Knowledge Transfer for Lifelong Robot Learning.pdf"
---

# LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning

> **저자**: Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone | **날짜**: 2023-06-05 | **URL**: [https://arxiv.org/abs/2306.03310](https://arxiv.org/abs/2306.03310)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Top: LIBERO has four procedurally-generated task suites: LIBERO-SPATIAL, LIBERO-*

로봇 조작 작업에서 선언적 지식과 절차적 지식의 전이를 함께 다루는 생애 주기 학습(LLDM)을 벤치마킹하기 위해 LIBERO 벤치마크를 제안한다. 130개의 절차적으로 생성된 작업과 고품질 시연 데이터를 제공하여 LLDM의 주요 5가지 연구 주제를 조사한다.

## Motivation

- **Known**: 이미지와 텍스트 도메인의 생애 주기 학습은 선언적 지식 전이에 초점을 맞춰왔다. 멀티태스크 학습과 기존 lifelong learning 방법들이 존재하지만, 로봇 조작 의사결정에서의 절차적 지식 전이는 충분히 연구되지 않았다.
- **Gap**: 의사결정 도메인에서 선언적 지식과 절차적 지식을 동시에 전이하는 방법, 효과적인 정책 아키텍처와 알고리즘, 작업 순서에 대한 견고성 등에 대한 체계적 분석이 부족하다.
- **Why**: 로봇이 다양한 조작 작업을 순차적으로 학습할 때 이전 지식의 망각을 방지하면서 새로운 지식을 습득해야 하며, 이는 실제 로봇 배포에서 매우 중요한 문제이다.
- **Approach**: 절차 생성 파이프라인을 통해 무한정의 작업을 생성할 수 있도록 설계하고, 4개의 작업 스위트(총 130개)를 구성하여 다양한 분포 변화를 분석한다. 여러 정책 아키텍처와 lifelong learning 알고리즘을 비교하는 광범위한 실험을 수행한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: Top: LIBERO has four procedurally-generated task suites: LIBERO-SPATIAL, LIBERO-*

- **벤치마크 플랫폼 구축**: 객체, 공간 관계, 목표, 다양한 배경에서의 지식 전이를 각각 조사할 수 있는 4개의 절차적으로 생성된 작업 스위트(130개 작업) 제공
- **아키텍처 설계 인사이트**: Transformer가 시간 정보 추상화에 우수하고, Vision Transformer는 풍부한 시각 정보, CNN은 절차적 지식이 필요한 작업에 효과적임을 발견
- **알고리즘 성능 분석**: 기존 lifelong learning 방법들(ER, PACKNET 등)이 망각 방지에는 효과적이지만 forward transfer에서는 sequential finetuning에 비해 성능이 낮음을 실증
- **사전학습 효과 분석**: 감독학습 기반 사전학습이 후속 LLDM 성능을 오히려 저해할 수 있음을 보여주는 예상 외의 발견
- **고품질 데이터셋 제공**: 모든 130개 작업에 대해 인간이 텔레작동으로 수집한 시연 데이터를 제공하여 샘플 효율성 지원

## How

![Figure 2](figures/fig2.webp)

*Figure 2: LIBERO’s procedural generation pipeline: Extracting behavioral templates from a large-*

- Ego4D 대규모 인간 활동 데이터셋에서 행동 템플릿을 추출하여 작업 지시사항 생성
- 작업 설명을 기반으로 PDDL 기술을 활용하여 객체, 레이아웃, 초기 상태, 목표 조건 명시
- LIBERO-SPATIAL, LIBERO-OBJECT, LIBERO-GOAL(각 10개 작업)에서 단일 유형의 지식 전이를 개별적으로 분석하고 LIBERO-100(100개 작업)에서 혼합 지식 전이를 조사
- Behavioral cloning을 활용한 lifelong imitation learning 설정에서 비교 가능한 조건 하에 여러 알고리즘과 아키텍처 조합 평가
- 작업 순서 변경(random shuffling)을 통해 task ordering에 대한 견고성 검증

## Originality

- 로봇 조작에서 선언적 지식과 절차적 지식의 전이를 명확히 구분하여 다루는 첫 번째 체계적인 벤치마크 제시
- 절차 생성 파이프라인을 통해 무한정의 작업 생성이 가능하도록 설계하여 기존 고정 크기 벤치마크의 한계 극복
- LLDM을 위한 5가지 핵심 연구 주제(지식 전이, 아키텍처 설계, 알고리즘 설계, 작업 순서 견고성, 사전학습 효과)를 명시적으로 정의하고 체계적으로 조사
- Sequential finetuning이 기존 lifelong learning 방법을 능가한다는 반직관적 발견과 사전학습의 부정적 영향 등 예상 외의 통찰 제시

## Limitation & Further Study

- 시뮬레이션 기반 환경으로 제한되어 실제 로봇 시스템에서의 성능 전이 여부가 미불명
- Behavioral cloning 기반 접근으로 sparse reward 강화학습 세팅은 다루지 못함
- 작업이 동일한 상태 공간, 행동 공간, 수평선을 공유한다는 가정이 실제 로봇 배포 시나리오의 다양성을 제한
- 현재 3가지 신경 아키텍처(CNN, RNN, Transformer)와 5가지 알고리즘만 평가되어 향후 더 다양한 아키텍처와 최신 알고리즘 추가 필요
- Language embedding의 효과가 task ID와 유사한 수준이라는 결과가 의외인데, 더 정교한 언어 처리 방법 연구 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: LIBERO는 로봇 조작에서의 생애 주기 학습을 체계적으로 연구하기 위한 중요한 벤치마크를 제공하며, 절차적으로 생성된 작업과 명확하게 정의된 5가지 연구 주제를 통해 LLDM의 여러 중요한 측면에 대한 인사이트를 제공한다.

## Related Papers

- 🔗 후속 연구: [[papers/1325_CALVIN_A_Benchmark_for_Language-Conditioned_Policy_Learning/review]] — LIBERO가 CALVIN의 언어 조건부 정책 학습을 생애주기 학습 관점으로 확장하여 지식 전이와 지속적 학습을 포괄적으로 다룬다
- 🏛 기반 연구: [[papers/1462_LOTUS_Continual_Imitation_Learning_for_Robot_Manipulation_Th/review]] — LIBERO의 선언적/절차적 지식 전이 프레임워크가 LOTUS의 지속적 모방 학습에 필요한 지식 표현과 전이 방법론의 이론적 기반을 제공한다
- 🔄 다른 접근: [[papers/1312_ARNOLD_A_Benchmark_for_Language-Grounded_Task_Learning_With/review]] — LIBERO와 ARNOLD 모두 로봇 학습 벤치마크이지만, 생애주기 지식 전이 vs 언어 기반 작업 학습이라는 서로 다른 평가 초점을 가진다
- 🔗 후속 연구: [[papers/1462_LOTUS_Continual_Imitation_Learning_for_Robot_Manipulation_Th/review]] — LOTUS의 지속적 모방 학습이 LIBERO의 생애주기 학습 벤치마크에서 제시한 지식 전이 문제를 실제 물리 로봇에서 해결하는 구체적 알고리즘을 제공한다
- 🏛 기반 연구: [[papers/1621_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Ro/review]] — LIBERO의 평생 로봇 학습 지식 전이 벤치마크가 VLABench의 Vision-Language-Action 모델 능력 평가에 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/1325_CALVIN_A_Benchmark_for_Language-Conditioned_Policy_Learning/review]] — LIBERO가 CALVIN의 언어 조건부 정책 학습을 생애주기 학습과 지식 전이 관점으로 확장하여 더 포괄적인 평가를 가능하게 한다
