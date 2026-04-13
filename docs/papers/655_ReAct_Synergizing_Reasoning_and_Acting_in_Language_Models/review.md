# ReAct: Synergizing Reasoning and Acting in Language Models

> **저자**: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao | **날짜**: 2022-10-06 | **URL**: [https://arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629)

---

## Essence

![Figure 1](figures/fig1.png)

*Figure 1: (1) Comparison of 4 prompting methods, (a) Standard, (b) Chain-of-thought (CoT,*

ReAct는 대형 언어 모델이 reasoning trace와 task-specific action을 interleaved manner로 생성하도록 함으로써, 추론과 행동의 시너지를 통해 다양한 언어 이해 및 의사결정 태스크의 성능을 향상시키는 프레임워크이다.

## Motivation

- **Known**: Chain-of-thought prompting은 LLM의 추론 능력을 향상시키지만 외부 정보와 단절되어 hallucination과 error propagation 문제를 야기한다. Action generation 기반 접근법은 상호작용 환경에서 효과적이나 high-level 추론 능력이 부족하다.
- **Gap**: 기존 연구들은 reasoning과 acting을 분리하여 연구했으며, 두 능력을 synergistic하게 결합하여 일반적인 태스크 해결에 활용하는 방법이 부재했다.
- **Why**: 인간의 인지는 verbal reasoning과 task-oriented action을 긴밀히 결합하여 self-regulation, strategy 수립, working memory 유지를 가능하게 하므로, 이를 LLM에 적용하면 해석 가능성, 신뢰성, 강건성이 향상될 수 있다.
- **Approach**: ReAct 프레임워크는 LLM에 대하여 Thought(내부 추론), Action(외부 행동), Observation(환경 반응)을 순환적으로 생성하도록 프롬프트하여, 추론이 행동 계획을 유도·추적·갱신하고 행동이 외부 지식베이스나 환경과 상호작용하게 한다.

## Achievement

![Figure 1](figures/fig1.png)

*Figure 1: (1) Comparison of 4 prompting methods, (a) Standard, (b) Chain-of-thought (CoT,*

- **HotpotQA에서의 성능 향상**: Wikipedia API와의 상호작용을 통해 hallucination과 error propagation을 극복하고 해석 가능한 task-solving trajectory 생성
- **Fever 사실 검증에서의 우수성**: 외부 정보 접근을 통한 정확한 사실 검증 성능 달성
- **ALFWorld 벤치마크**: 모방학습 및 강화학습 기반 방법 대비 34% 절대 성공률 향상 (1-2 shot prompting만으로)
- **WebShop 벤치마크**: 웹 내비게이션 태스크에서 10% 절대 성공률 향상
- **해석 가능성 및 신뢰성 개선**: 내부 추론과 외부 정보의 구분이 명확하여 모델의 의사결정 근거 추적 가능

## How

![Figure 1](figures/fig1.png)

*Figure 1: (1) Comparison of 4 prompting methods, (a) Standard, (b) Chain-of-thought (CoT,*

- LLM에 in-context examples를 포함한 프롬프트로 Thought, Action, Observation의 반복적 생성 유도
- 외부 인터페이스(Wikipedia API, 텍스트 환경 등)와의 상호작용을 통해 실시간 정보 수집
- Thought를 통해 현재 상태 추적, 예외 처리, 계획 갱신을 수행하는 동안 Action으로 외부 환경 쿼리
- Observation에 기반한 adaptive reasoning으로 초기 계획 수정 및 재평가
- CoT와 ReAct의 결합으로 내부 지식과 외부 정보의 균형적 활용

## Originality

- Reasoning과 acting을 prompt-based paradigm으로 처음 체계적으로 통합한 접근
- Interleaved manner의 Thought-Action-Observation 루프 구조로 동적 계획 및 적응적 추론 실현
- Chain-of-thought의 hallucination 문제를 external grounding으로 해결하는 혁신적 방식
- Few-shot prompting만으로 대규모 학습 기반 방법을 초과하는 성능 달성의 실증

## Limitation & Further Study

- **프롬프팅 기반 한계**: 제한된 context window와 prompt 설계의 의존성으로 복잡한 추론과 행동 지원 제약
- **환경 인터페이스 의존성**: Wikipedia API 같은 특정 외부 소스에 대한 높은 의존도
- **확장성 문제**: 더 복잡한 멀티-스텝 태스크나 제약 조건이 많은 환경에서의 성능 미검증
- **오류 누적**: Action 오류가 이후 추론에 영향을 주는 error propagation 여전히 존재 가능
- **후속 연구**: Fine-tuning을 통한 성능 향상 가능성 제시 (초기 실험만 수행), RL과의 결합, 더 많은 태스크에 대한 확장 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: ReAct는 LLM의 추론과 행동을 획기적으로 결합하여 hallucination을 줄이고 해석 가능성을 높이는 중요한 프레임워크이다. Few-shot prompting만으로 대규모 학습 기반 방법을 뛰어넘는 성능을 보여주며, 광범위한 벤치마크에서의 검증과 명확한 제시로 높은 영향력을 가질 것으로 예상된다.
