# Transshipment Optimization
### *Python and [Pyomo](https://pyomo.readthedocs.io/en/stable/)*

> A multi-stage transshipment cost minimization problem, in which we send product from plants to distributors, and then from those distributors to warehouses, for the lowest possible cost, while satisfying demand, capacity, and supply constraints.

#### I created [this Python library, `tsopt`](https://github.com/ryayoung/tsopt) to solve this exact type of problem. I'll solve this problem first without it, and then again using the tool I created.

### Problem
- We're given cost and production data for a ski boot manufacturer. There are three manufacturing plants, two distribution centers, and five warehouses.
- We must ship the boots to the warehouses at a minimum cost satisfying the given constraints. Each plant can only produce so much product, the amount of boots passing through the distribution centers has to remain constant (inflow equals outflow), and each warehouse has a minimum quantity needed to satisfy demand.

<img width="400" alt="diagram" src="https://user-images.githubusercontent.com/90723578/177877288-5e4d91aa-05cc-45a4-b99f-fb63152a3e12.png">


### Research Questions
