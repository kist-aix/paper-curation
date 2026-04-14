# ActiveUMI: Robotic Manipulation with Active Perception from Robot‑Free Human Demonstrations

> **저자**:  | **날짜**:  | **URL**: [https://activeumi.github.io/](https://activeumi.github.io/)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: VOXPOSER extracts language-conditioned affordances and constraints from LLMs and grounds*

본 논문은 LLM의 affordance 추론 능력과 VLM의 시각적 접지 능력을 결합하여 3D value map을 구성하고, 이를 model-based planning에 활용해 자연언어 지시로부터 로봇 조작 궤적을 zero-shot으로 생성하는 VoxPoser를 제안한다.

## Motivation

- **Known**: LLM은 언어 지시로부터 high-level 추론과 planning을 수행할 수 있으나, 기존 방식들은 미리 정의된 motion primitive에 의존하여 일반화 능력이 제한된다.
- **Gap**: LLM의 open-world 지식을 로봇의 저수준 제어 신호로 직접 변환하기 어렵고, 각 작업마다 새로운 primitive를 설계해야 한다는 병목이 존재한다.
- **Why**: 자연언어로 지정된 다양한 일상적 조작 작업을 학습 데이터 없이 수행할 수 있는 로봇 시스템을 구현하면 로봇의 실용성과 확장성이 크게 향상된다.
- **Approach**: LLM에게 affordance와 constraint를 추론하게 하고, code-writing 능력을 활용하여 VLM(CLIP 등) 및 array operation을 조합해 3D voxel 기반의 reward/cost map을 생성한 후, 이를 MPC 기반의 motion planner에 입력하여 closed-loop 궤적을 합성한다.

## Achievement

![Figure 3](figures/fig3.webp)

*Figure 3: Visualization of composed 3D value maps and rollouts in real-world environments. The top row*

- **Zero-shot 일반화**: 추가 학습 없이 open-set 지시문과 open-set 객체에 대해 다양한 일상 조작 작업 수행
- **3D value map 구성**: LLM이 Python 코드를 통해 VLM과 상호작용하면서 observation space에 affordance와 constraint를 직접 매핑
- **Closed-loop 제어의 견고성**: MPC 기반 planning으로 dynamic perturbation에 대한 robustness 확보
- **Online learning 통합**: 제한된 online 상호작용으로 contact-rich 작업의 dynamics model을 효율적으로 학습 가능
- **대규모 평가**: 시뮬레이션과 실제 로봇 환경에서 광범위한 실험을 통해 방법의 유효성 입증

## How

![Figure 2](figures/fig2.webp)

*Figure 2: Overview of VOXPOSER. Given the RGB-D observation of the environment and a language in-*

- LLM prompt를 통해 자연언어 지시로부터 affordance(e.g., 'drawer handle을 집기') 및 constraint(e.g., 'vase 주변 회피')를 텍스트로 추론", 'LLM이 CLIP 또는 open-vocabulary detector를 호출하는 Python 코드를 생성하여 관련 객체/부위의 공간-기하학적 정보 추출
- 3D voxel space에서 affordance 영역에 높은 value를, constraint 영역에 낮은 value를 할당하여 value map 구성
- 구성된 value map을 objective function으로 하는 MPC(또는 trajectory optimization) solver가 closed-loop으로 로봇 궤적 생성
- Online 상황에서는 limited interaction으로부터 dynamics model을 학습하여 contact-rich 작업의 planning 성능 개선

## Originality

- **LLM의 code-writing 능력 활용**: 기존에는 LLM 출력을 직접 control signal로 사용했으나, 본 논문은 LLM이 Python code를 생성하여 VLM과 array operation을 조합하도록 함으로써 spatial grounding을 가능하게 함
- **3D value map 추상화**: 2D cost map(Sharma et al.)을 3D로 확장하고, 이를 다양한 manipulation task에 대한 통일된 representation으로 제시
- **Training-free 접근**: LLM과 VLM 모두 기존 pre-trained 모델을 사용하며, task-specific 학습을 전혀 하지 않고도 일반화 가능
- **Model-based planning과의 결합**: affordance 기반의 value map이 MPC의 objective로 직접 활용되어 closed-loop robustness 달성

## Limitation & Further Study

- **Task decomposition 의존성**: 고수준 planning(LLM 또는 search-based planner)에 의한 sub-task 분해가 필수이며, 이 단계의 실패는 전체 성능 저하로 이어짐
- **Perception API 정확도**: VLM(CLIP, open-vocabulary detector)의 성능이 최종 value map의 품질을 크게 영향미치므로, 어려운 시각적 장면에서 한계 존재
- **Contact-rich interaction의 학습**: zero-shot으로 해결 불가능한 복잡한 contact-rich 작업은 여전히 online learning을 필요로 함
- **Computational cost**: 매 step마다 LLM query와 VLM 호출이 필요하여 실시간성 제약 가능
- **실험 범위**: 실제 로봇 실험 규모와 상세한 정량적 비교가 논문에 충분히 제시되지 않음; 향후 더 많은 baseline과의 비교 연구 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 LLM의 affordance 추론 능력과 VLM의 시각적 접지를 3D value map으로 통합하는 창의적인 접근법을 제시하며, training-free zero-shot generalization이라는 중요한 성과를 달성한다. 다만 task decomposition의 정확성과 perception API의 성능에 대한 의존도가 높고, 실험의 정량적 평가가 더욱 강화될 필요가 있다.
