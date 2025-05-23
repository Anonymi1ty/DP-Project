
## Environment

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
│   ├── laplace_module.py       # contains the core `Laplace` class implementation
│   ├── sum_dp_module.py        # contains the core `SumDP` class implementation
│   └── __init__.py
│
├── error_evaluation
│   ├── laplace_eva.py          # error-analysis baseline code
│   ├── SumDP_eva.py            # error‐analysis code
│   └── __init__.py
│
├── notebook_test
│   ├── errors_compare.ipynb    # comparison of Laplace vs. SumDP errors
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

