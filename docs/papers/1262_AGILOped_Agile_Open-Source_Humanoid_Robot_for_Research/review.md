---
title: "1262_AGILOped_Agile_Open-Source_Humanoid_Robot_for_Research"
authors:
  - "Grzegorz Ficht"
  - "Luis Denninger"
  - "Sven Behnke"
date: "2025.09"
doi: ""
arxiv: ""
score: 4.0
essence: "AGILOped는 오픈소스 휴머노이드 로봇으로, 고성능과 접근성의 간극을 해소하기 위해 3D 프린팅된 부품과 상용 부품으로 제작되어 6,380 USD의 저렴한 가격과 14.5 kg의 가벼운 무게를 실현했다."
tags:
  - "cat/Biomechanical_Robot_Design_Systems"
  - "sub/Aerial_Humanoid_Robotics"
  - "topic/physical-ai"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ficht et al._2025_AGILOped Agile Open-Source Humanoid Robot for Research.pdf"
---

# AGILOped: Agile Open-Source Humanoid Robot for Research

> **저자**: Grzegorz Ficht, Luis Denninger, Sven Behnke | **날짜**: 2025-09-11 | **URL**: [https://arxiv.org/abs/2509.09364](https://arxiv.org/abs/2509.09364)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1: The kinematics, CAD model and constructed version of AGILOped.*

AGILOped는 오픈소스 휴머노이드 로봇으로, 고성능과 접근성의 간극을 해소하기 위해 3D 프린팅된 부품과 상용 부품으로 제작되어 6,380 USD의 저렴한 가격과 14.5 kg의 가벼운 무게를 실현했다.

## Motivation

- **Known**: 최근 휴머노이드 로봇 플랫폼들이 인상적인 동적 성능을 보여주고 있지만, 대부분 폐쇄소스이거나 높은 구입 및 유지비용을 가지고 있어 연구 접근성이 제한적이다.
- **Gap**: 고성능의 동적 능력을 갖춘 휴머노이드 로봇이 존재하지만, 오픈소스이면서 상용 부품으로 이루어지고 연구자들이 쉽게 구축 및 유지할 수 있는 플랫폼의 부재가 있다.
- **Why**: 휴머노이드 로봇 개발의 민주화와 연구의 재현성 향상을 통해 더 많은 연구 그룹이 첨단 인간형 로봇 연구에 접근할 수 있게 하는 것이 중요하다.
- **Approach**: Quasi Direct Drive (QDD) 액추에이터, 3D 프린팅된 플라스틱 부품, 표준 전자 부품을 조합하여 선택적 유연성(selective compliance) 원리를 적용한 최소한의 설계를 통해 저비용 고성능 휴머노이드를 구현했다.

## Achievement

![Figure 1](figures/fig1.webp)

*Fig. 1: The kinematics, CAD model and constructed version of AGILOped.*

- **비용 효율성**: 6,380 USD로 동급의 휴머노이드 로봇 중 가장 저렴하며 가장 가볍다(14.5 kg)
- **접근성**: 완전 오픈소스 설계 파일 공개 및 상용 부품 사용으로 3D 프린터와 기본 도구만으로 제작 가능
- **동적 능력**: 걷기, 점프, 충격 완화, 일어나기 등의 실험을 통해 동적 운동 능력 입증
- **모듈성**: 3D 프린팅 부품의 빠른 교체로 성능 개선 및 새로운 기능 구현 가능
- **운영 편의성**: 110 cm 높이로 단일 사용자가 갠트리 없이 운영 가능

## How


- MyActuator RMD X6-40 QDD 액추에이터 10개로 12개 조인트 구동 (단순성과 비용 효율성 강조)
- 알루미늄 프레임과 PLA/Nylon, TPU 등 3D 프린팅 가능한 플라스틱 및 폴리우레탄의 선택적 유연성 설계
- LiPo 배터리 2개(26.1 V, 4.5 Ah)로 1.5-2.5시간 배터리 수명 제공
- Raspberry Pi 3B+를 기본 컨트롤러로 사용하고 선택적으로 NVIDIA Jetson 탑재 가능
- CAN 통신을 통한 액추에이터 제어 및 위치, 속도, 토크 피드백 수집
- Spring-Loaded Inverted Pendulum (SLIP) 모델 원리와 저관성 다리 설계로 복잡한 제어 없이 동적 운동 달성

## Originality

- QDD 액추에이터의 소형 모터와 2단계 행성 기어박스 조합으로 낮은 회전자 관성(28.8 kg cm²)과 높은 토크(40 Nm)를 동시에 달성
- 알루미늄의 강성과 다양한 경도의 3D 프린팅 플라스틱/폴리우레탄의 유연성을 의도적으로 조합한 선택적 유연성 설계 철학
- 완전 오픈소스이면서 상용 부품만 사용하여 재현성과 접근성을 모두 충족하는 최초의 고성능 휴머노이드
- 낙하 전략 및 충격 완화 메커니즘 연구로 반복적 추락 상황에서의 로봇 내구성 향상 시도

## Limitation & Further Study

- Raspberry Pi 3B+의 제한된 컴퓨팅 능력으로 인한 온보드 제어 복잡도 제약 (고급 기능은 Jetson 필요)
- 1.5-2.5시간 배터리 수명으로 장시간 연속 운동 불가
- 10개 액추에이터로 12개 조인트만 제어하므로 일부 관절의 자유도가 제한적
- 체계적인 낙하 전략 및 충격 완화 설계가 충분히 탐구되지 않았으므로 장기 내구성 검증 필요
- 고급 동적 운동(러닝, 공중제비 등)의 성능 벤치마크 데이터 부족

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: AGILOped는 저비용과 높은 접근성을 유지하면서 진정한 동적 능력을 갖춘 첫 오픈소스 휴머노이드로, 휴머노이드 로봇 연구의 민주화와 재현성 향상에 실질적인 기여를 한다.

## Related Papers

- 🔄 다른 접근: [[papers/1332_Demonstrating_Berkeley_Humanoid_Lite_An_Open-source_Accessib/review]] — 오픈소스 휴머노이드 로봇에서 3D 프린팅 부품 활용과 cycloidal gear 액추에이터의 서로 다른 저비용 구현 방식을 비교할 수 있습니다.
- 🏛 기반 연구: [[papers/1603_ORCA_An_Open-Source_Reliable_Cost-Effective_Anthropomorphic/review]] — 저비용 오픈소스 휴머노이드 설계 철학이 접근 가능한 로봇 손 제작에도 동일하게 적용됩니다.
- 🔗 후속 연구: [[papers/1285_Berkeley_Humanoid_A_Research_Platform_for_Learning-based_Con/review]] — AGILOped의 저비용 설계가 Berkeley Humanoid의 학습 기반 제어 플랫폼으로 확장될 수 있습니다.
- 🔄 다른 접근: [[papers/1332_Demonstrating_Berkeley_Humanoid_Lite_An_Open-source_Accessib/review]] — cycloidal gear 액추에이터와 상용 부품 조합의 서로 다른 저비용 휴머노이드 제작 방식을 비교 연구할 수 있습니다.
- 🧪 응용 사례: [[papers/1379_Embracing_Evolution_A_Call_for_Body-Control_Co-Design_in_Emb/review]] — AGILOped 오픈소스 휴머노이드가 co-design 메커니즘을 실제 플랫폼에 적용하여 검증할 수 있는 실용적 테스트베드를 제공한다
