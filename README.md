- [x] 实现SumDP算法
  - [x] 证明SumDP算法的理论分析和实验误差匹配（在notebook中有具体解释）

- [x] 进行实验评估
  - [x] 找三个kaggle数据集，导入进行error评估
  - [x] 实现拉普拉斯算法
  - [x] 对两个算法进行误差分析

---

>后半部分comment

   - [x] laplace代码实现部分done, see in tree structure
   - [x] 误差分析部分done, see in tree structure, `errors_compare.ipynb`
   - [x] datasets folder contains datasets used in experiment 
   - [x] translate all comments into english, except `SumDP_error.ipynb`and `docs folder`
   - [ ] report
   - [x] merge branch 



## Envorment

```bash
pip install -r requirements.txt
```

## File Structure

```csharp
DP_PROJECT
│   README.md
│   requirements.txt
│
├── algorithm
│   ├── laplace_module.py       (new)
│   ├── sum_dp_module.py        # contains the core `SumDP` class implementation
│   └── __init__.py
│
├── error_evaluation
│   ├── laplace_eva.py          (new)
│   ├── SumDP_eva.py            # error‐analysis code
│   └── __init__.py
│
├── notebook_test
│   ├── errors_compare.ipynb    (new)  # comparison of Laplace vs. SumDP errors
│   └── SumDP_error.ipynb       # detailed SumDP usage examples
│
├── datasets
│   ├── insurance.csv
│   ├── loan_data.csv
│   ├── readme.md
│   └── StudentsPerformance.csv
│
└── docs
    ├── Sum estimation under differential privacy (proof and formula design).md
    ├── Sum estimation under differential privacy.pdf
    ├── Paper explanation.md
    └── Paper explanation.pdf

```

- **`sum_dp_module.py`**: Implements the `SumDP` class (the core algorithm).
- **`error_evaluation/SumDP_eva.py`**: Contains the error‐analysis implementation.
- **Notebooks**
  - `SumDP_error.ipynb`: Detailed code examples for calling and testing SumDP.
  - `errors_compare.ipynb`: End‐to‐end reproduction of both Laplace and SumDP error experiments.

## Reproduction

To reproduce all experiments, open the notebooks in the `notebook_test` folder:

- `errors_compare.ipynb`
- `SumDP_error.ipynb`

Ensure that your Jupyter kernel is using the environment installed via:

```bash
pip install -r requirements.txt
```

