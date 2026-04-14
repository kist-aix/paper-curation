# Residual Off-Policy RL for Finetuning Behavior Cloning Policies

> **저자**: Lars Ankile, Zhenyu Jiang, Rocky Duan, Guanya Shi, Pieter Abbeel, Anusha Nagabandi | **날짜**: 2025-09-23 | **URL**: [https://arxiv.org/abs/2509.19301](https://arxiv.org/abs/2509.19301)

---

## Essence

![Figure 2](figures/fig2.webp)

*Fig. 2. Off-policy residual fine-tuning (ResFiT): A two-phase approach using online RL to improve BC policies. First, we*

Behavior Cloning(BC) 정책을 기반으로 Residual Off-Policy RL을 적용하여 샘플 효율적으로 조작 정책을 개선하며, 고자유도 이족 로봇에서의 첫 실시간 RL 학습을 달성했다.

## Motivation

- **Known**: BC는 인간 시연으로부터 강력한 시각-운동 제어 정책을 학습할 수 있으나, 데이터 수집 비용이 높고 성능 포화 현상이 발생한다. RL은 자율 상호작용으로 학습하지만 실제 로봇에서의 샘플 비효율성과 안전 문제가 있다.
- **Gap**: 기존 Residual RL은 시뮬레이션 또는 제약된 설정에만 제한되었으며, 고자유도 이족 조작 시스템에서의 실시간 학습은 부재했다. 또한 현대 BC 아키텍처(action-chunking, diffusion)와의 RL 결합은 구조적으로 어렵다.
- **Why**: BC의 데이터 효율성과 RL의 자율학습 능력을 결합하면 실세계 로봇 학습의 실용성을 크게 향상시킬 수 있으며, 고자유도 조작 작업의 성능 개선이 산업 응용에 중요하다.
- **Approach**: 고정된 BC 정책을 블랙박스 기준으로 하여 Per-step Residual 보정을 off-policy RL로 학습한다. 이는 기본 정책 구조에 무관하며, 샘플 효율적인 off-policy 설계와 희소 이진 보상으로 실시간 배포를 가능하게 한다.

## Achievement

![Figure 5](figures/fig5.webp)

*Fig. 5. Success rates of different approaches on our simulation tasks, showing ResFiT converging to high-performing poli*

- **첫 번째 고자유도 이족 로봇 실시간 RL**: 29-DoF 휠 이족 로봇(5지 손)에서 성공적인 RL 학습 달성
- **샘플 효율성**: 희소 이진 보상 신호만으로 오프폴리시 RL 수행 가능
- **상태-최고 성능**: 시뮬레이션 작업에서 다양한 비전 기반 작업에 대해 SOTA 달성
- **일반화 가능성**: BC 아키텍처 무관하게 적용 가능한 검은상자 방식의 residual learning

## How

![Figure 2](figures/fig2.webp)

*Fig. 2. Off-policy residual fine-tuning (ResFiT): A two-phase approach using online RL to improve BC policies. First, we*

- **Phase 1**: 시연 데이터셋에서 action-chunking을 이용한 BC 정책 학습 및 고정
- **Phase 2**: Per-step residual 보정 정책을 off-policy RL(Q-learning 기반)로 학습
- **Critic 초기화**: 시연 데이터로 critic 워밍업하여 학습 안정성 향상
- **샘플 효율화**: 시연 버퍼를 온라인 RL 단계 전체에서 활용
- **탐색 안정화**: Residual 크기 제어로 기본 정책 근처에서의 안전한 탐색 보장
- **비전 관측**: 고유 감각(proprioception) 및 이미지 관측을 입력으로 사용

## Originality

- **Off-policy Residual RL의 고자유도 실시간 적용**: 기존 Policy Decorator(청크 단위 residual)와 EXPO(상태 기반)의 한계를 극복하고, 시각 기반 고자유도 이족 시스템으로 확장
- **블랙박스 방식**: BC 정책 구조(action-chunking, diffusion 등)에 무관한 설계로 유연성 극대화
- **실시간 배포 검증**: 첫 번째 실제 휴머노이드 5지 손 로봇 RL 학습 시연
- **시연 재활용**: Pre-training, critic 워밍업, 온라인 버퍼로 시연을 다중 목적으로 활용

## Limitation & Further Study

- **초기 BC 정책 의존성**: 기본 정책의 품질이 최종 성능의 상한을 결정하므로 고품질 시연 필요
- **희소 보상 설계**: 작업별 보상 함수 설계의 어려움은 여전히 남아있음
- **확장성 미검증**: 더 높은 자유도 또는 더 복잡한 장기 작업에서의 성능 미확인
- **시뮬레이션-현실 차이**: 시뮬레이션 실험에만 정량적 비교 있으며, 현실 작업은 정성적 결과
- **후속 연구**: 완전 자율 탐색, 멀티태스크 학습, 더 긴 수평선 작업으로의 확장 가능성

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: BC와 off-policy RL을 residual learning으로 효과적으로 결합하여, 고자유도 실시간 로봇 학습의 실용적 경로를 제시했다. 블랙박스 방식의 일반성과 첫 휴머노이드 RL 실증이 로봇 학습 분야에 의미 있는 기여를 이룬다.
