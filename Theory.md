# Theoretical Background: EcoDecisionSim

## 1. Introduction

In conservation and environmental management, decision-makers often face the dilemma of whether to act immediately to protect or control a biological population or to delay action to gather better information. This trade-off lies at the heart of **decision theory under uncertainty**.

**EcoDecisionSim** models this problem using a simple stochastic **logistic growth model** to simulate population dynamics and applies the concept of **Value of Information (VOI)** to inform decision-making.

---

## 2. Population Dynamics: Logistic Growth Model

The **logistic growth model** is a foundational model in population ecology. It describes how populations grow rapidly when resources are abundant and slow as they approach a **carrying capacity (K)** due to resource limitations.

### The model is defined by the equation:
$$\frac{dN}{dt} = rN\left(1 - \frac{N}{K}\right)$$

Where:
- **N** = Population size
- **r** = Intrinsic growth rate
- **K** = Carrying capacity

In **EcoDecisionSim**, random noise is added to simulate environmental variability, making the model more realistic for real-world ecological decision-making.

---

## 3. Management Interventions

In conservation scenarios, decision-makers may implement actions to:
- Reduce overpopulation of invasive species.
- Boost populations of endangered species.

In the simulation:
- **Without Action:** The population follows natural logistic growth.
- **With Action:** The growth rate is reduced to represent management intervention.

---

## 4. Value of Information (VOI) in Environmental Decision-Making

Decision-makers often operate under uncertainty:
- Uncertainty in population size, growth rate, environmental conditions, or intervention effectiveness.
- Gathering additional information (e.g., ecological surveys, population monitoring) incurs a **cost**.

The **Value of Information (VOI)** quantifies whether it is better to:
1. **Act immediately**, or
2. **Invest in learning first**.

### VOI Formula:
$$
\text{VOI} = (\text{Expected Benefit of Better Decision} \times \text{Probability of Correct Decision}) - \text{Cost of Learning}
$$

A **positive VOI** suggests that it is worthwhile to gather more information before acting. A **negative VOI** suggests immediate action is preferable.

---

## 5. Real-World Applications

The principles demonstrated here apply to:
- **Invasive species management** (e.g., culling, biological control).
- **Endangered species recovery** (e.g., habitat restoration, population reinforcement).
- **Harvest management** (e.g., fisheries, forestry).

In all these cases, **delaying action to reduce uncertainty can sometimes lead to better long-term outcomes—but not always**. Quantifying VOI helps balance this trade-off.

---

## 6. Next Steps and Model Extensions

- Simulate multiple decision scenarios using **Monte Carlo simulation**.
- Introduce **adaptive management strategies** where decisions evolve with incoming data.
- Use **probabilistic forecasting** to improve VOI estimates.

---

*This theoretical note was created as part of a research portfolio for PhD applications in mathematical ecology, conservation decision-making, and environmental management.*
