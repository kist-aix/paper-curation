---
title: "1399_From_Seeing_to_Doing_Bridging_Reasoning_and_Decision_for_Rob"
authors:
  - "Yifu Yuan"
  - "Haiqin Cui"
  - "Yibin Chen"
  - "Zibin Dong"
  - "Fei Ni"
date: "2025.05"
doi: ""
arxiv: ""
score: 4.0
essence: "FSD는 Vision-Language Model에 spatial relationship reasoning을 통한 중간 표현(visual aids) 생성을 추가하여, 로봇 조작에서 zero-shot 일반화 성능을 획기적으로 향상시키는 모델이다."
tags:
  - "cat/Embodied_Navigation_and_Planning"
  - "sub/Language-Grounded_Action_Planning"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yuan et al._2025_From Seeing to Doing Bridging Reasoning and Decision for Robotic Manipulation.pdf"
---

# From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation

> **저자**: Yifu Yuan, Haiqin Cui, Yibin Chen, Zibin Dong, Fei Ni, Longxin Kou, Jinyi Liu, Pengyi Li, Yan Zheng, Jianye Hao | **날짜**: 2025-05-13 | **URL**: [https://arxiv.org/abs/2505.08548](https://arxiv.org/abs/2505.08548)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1 Overview of FSD. FSD unlocks visual aids reasoning and generation through Spatial Relationship*

FSD는 Vision-Language Model에 spatial relationship reasoning을 통한 중간 표현(visual aids) 생성을 추가하여, 로봇 조작에서 zero-shot 일반화 성능을 획기적으로 향상시키는 모델이다.

## Motivation

- **Known**: Vision-Language-Action(VLA) 모델은 VLM을 기반으로 로봇 조작을 수행하지만, embodied 데이터셋의 부족과 이질성으로 인해 unseen scenario에서 robust zero-shot 성능을 달성하지 못하고 있다.
- **Gap**: 현재 VLA 모델들은 데이터 부족과 embodiment 이질성 문제를 해결하지 못해 새로운 시나리오에 일반화되지 않으며, visual understanding과 robotic action 사이의 연결고리가 부족하다.
- **Why**: 로봇 조작의 일반화는 다양한 환경과 작업에 적응할 수 있는 embodied AI의 핵심이며, spatial reasoning을 통한 중간 표현은 embodiment에 무관한 unified 지식 표현을 제공할 수 있다.
- **Approach**: FSD는 Spatial Relationship-Focused CoT(SrCoT)를 통해 객체 좌표와 공간 관계를 reasoning anchor로 사용하여 visual aids(spatial affordance boxes/points, visual traces)를 생성하고, 계층적 데이터 파이프라인과 self-consistency 메커니즘으로 학습한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1 Overview of FSD. FSD unlocks visual aids reasoning and generation through Spatial Relationship*

- **Spatial reasoning 벤치마크 성과**: 8개 벤치마크에서 spatial reasoning과 embodied reference 능력에 outstanding performance 달성
- **Zero-shot 로봇 조작 성능**: SimplerEnv에서 40.6%, 실제 로봇 8개 task에서 72% 성공률로 기존 baseline 대비 30% 향상
- **Visual aids generation benchmark**: 300개 수작업 주석 이미지로 구성된 VABench 제안
- **Cross-embodiment 일반화**: Visual aids를 통해 robot embodiment에 무관한 일반화 달성

## How

![Figure 3](figures/fig3.webp)

*Figure 3 Inspired by the process of human reasoning, FSD uses a spatial relationship graph as an anchor to derive*

- **SrCoT(Spatial Relationship-Focused CoT)**: 객체 중심 좌표와 spatial relationships을 reasoning anchor로 하는 multi-step reasoning을 통해 visual aids 생성
- **Hierarchical data construction pipeline**: Large-scale embodied datasets과 common sense data를 결합한 weak-to-strong capability enhancement training
- **Self-consistency mechanism**: Spatial coordinates를 visual signals과 align하여 understanding과 generation 능력 강화
- **Visual aids definition**: Spatial affordance boxes([x1, y1, x2, y2]), spatial affordance points, visual traces를 정규화된 이미지 좌표([0, 1000]²)로 정의
- **Zero-shot deployment**: 생성된 visual aids를 기반으로 simple planning methods를 통해 action 실행

## Originality

- **SrCoT의 novel한 적용**: 기존 CoT를 spatial relationship 기반으로 확장하여 embodied AI에 맞춤형 reasoning 프레임워크 제시
- **Visual aids 통합 접근**: Spatial affordances와 visual traces를 unified framework로 결합하여 embodiment-agnostic 표현 실현
- **Reasoning-driven 패러다임**: 데이터 부족 문제를 해결하기 위해 순수 data-driven 접근에서 reasoning-driven 생성 방식으로 전환
- **VABench 벤치마크**: Visual aids generation의 정확성을 평가할 수 있는 최초의 도전적 벤치마크 제안

## Limitation & Further Study

- **Real robot 평가의 제한**: 8개 task만으로 평가되었으며, 더 다양한 실제 로봇 환경에서의 성능 검증 필요
- **Computational cost 분석 부재**: SrCoT 추론 및 visual aids 생성의 computational overhead에 대한 상세한 분석 및 최적화 방안 미제시
- **Visual occlusion 처리**: 부분적으로 가려진 객체나 복잡한 scene에서의 spatial reasoning 성능 한계 가능성
- **Language instruction 복잡도**: 매우 복잡하거나 암시적인 spatial relationship을 포함한 instruction에 대한 일반화 성능 미평가
- **후속연구 방향**: (1) 더 다양한 embodiment(휴머노이드, 이동형 조작 로봇)에 대한 확장, (2) Dynamic scene에서의 temporal visual traces 예측, (3) Self-consistency 메커니즘의 이론적 기반 강화

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: FSD는 spatial reasoning을 통한 visual aids 생성으로 로봇 조작의 일반화 문제를 창의적으로 해결하며, 다양한 벤치마크와 실제 로봇 환경에서 검증된 우수한 성과를 보여준다. ICLR 2026 발표 논문으로서 embodied AI의 중요한 진전을 제시한다.

## Related Papers

- 🏛 기반 연구: [[papers/1370_DoReMi_Grounding_Language_Model_by_Detecting_and_Recovering/review]] — DoReMi의 계획-실행 제약조건이 FSD의 spatial relationship reasoning 활용에 기반한다.
- 🔗 후속 연구: [[papers/1422_Hi_Robot_Open-Ended_Instruction_Following_with_Hierarchical/review]] — Hi Robot의 복잡한 지시사항 처리가 FSD의 zero-shot 일반화를 발전시킨다.
- 🔄 다른 접근: [[papers/1467_Manipulate-Anything_Automating_Real-World_Robots_using_Visio/review]] — Manipulate-Anything도 vision model을 통한 로봇 조작의 일반화를 다룬다.
- 🔗 후속 연구: [[papers/1370_DoReMi_Grounding_Language_Model_by_Detecting_and_Recovering/review]] — FSD의 spatial reasoning을 통한 제약조건 생성이 DoReMi의 실행 제약조건 감지를 발전시킨다.
