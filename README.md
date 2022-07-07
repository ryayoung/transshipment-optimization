# Transshipment Optimization

*(Python and [Pyomo](https://pyomo.readthedocs.io/en/stable/))*

> A multi-stage transshipment cost minimization problem, in which we send product from plants to distributors, and then from those distributors to warehouses, for the lowest possible cost, while satisfying demand, capacity, and supply constraints.

#### I created [this Python library, `tsopt`](https://github.com/ryayoung/tsopt) to solve this exact type of problem. I'll solve this problem first without it, and then again using the tool I created.

### Dependencies
- [Pyomo](https://pyomo.readthedocs.io/en/stable/) - optimization library
- [GLPK](https://www.gnu.org/software/glpk/) - Linear programming solver. Installing this as a python package might be challenging depending on your system. See instructions below:

- <details>
    <summary><i>Installing GLPK</i></summary>

    - If using a conda environment, run `conda install -c conda-forge glpk`
    - I use standard Python virtual environments, and `pip install` does not work for me (Mac). However, if you're on a Mac, there is an easy solution. Assuming you have [homebrew](https://brew.sh/) installed, run `brew install glpk` and it will be install globally on your system.
    - If the above doesn't work or apply to you, please troubleshoot on google. Good luck!

    </details>


### Problem
- We're given cost and production data for a ski boot manufacturer. There are three manufacturing plants, two distribution centers, and five warehouses.
- We must ship the boots to the warehouses at a minimum cost satisfying the given constraints. Each plant can only produce so much product, the amount of boots passing through the distribution centers has to remain constant (inflow equals outflow), and each warehouse has a minimum quantity needed to satisfy demand.

<img width="400" alt="diagram" src="https://user-images.githubusercontent.com/90723578/177877288-5e4d91aa-05cc-45a4-b99f-fb63152a3e12.png">


### Objectives
1. Determine how many units of product should be sent through *each* location in each stage of the transshipment flow to *minimize cost*, while satisfying all constraints for supply, capacity, and warehouse demand.
2. Find the total cost of the process.
3. Check for slack in the system. 
4. Visualize the decision variables with bar charts.
5. Visualize how overall total cost changes as a function of cost at a single *edge* in the network.
6. Visualize how overall total cost changes as a function of demand (minimum units required) at a warehouse node.
