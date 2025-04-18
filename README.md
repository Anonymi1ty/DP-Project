- [x] 实现SumDP算法
  - [x] 证明SumDP算法的理论分析和实验误差匹配（在notebook中有具体解释）

- [x] 进行实验评估
  - [x] 找三个kaggle数据集，导入进行error评估
  - [x] 实现拉普拉斯算法
  - [x] 对两个算法进行误差分析

## 后半部分comment

   - laplace代码实现部分done, see in tree structure
   - 误差分析部分done, see in tree structure, `errors_compare.ipynb`
   - datasets folder contains datasets used in experiment 
   - translate all comments into english, except `SumDP_error.ipynb`and `docs folder`
   - [ ] report
   - [ ] merge branch 





文件结构：

```
DP PROJECT
│   README.md
│   
├───algorithm
│   │   laplace_module.py (new added)
│   │   sum_dp_module.py
│   │   __init__.py
│   │
│   ├───error_evaluation
│   │   │   laplace_eva.py (new added)
│   │   │   SumDP_eva.py
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           laplace_eva.cpython-311.pyc
│   │           SumDP_eva.cpython-311.pyc
│   │           __init__.cpython-311.pyc
│   │
│   ├───notebook_test
│   │       errors_compare.ipynb (new added)
│   │       SumDP_error.ipynb
│   │
│   └───__pycache__
│           sum_dp_module.cpython-311.pyc
│           __init__.cpython-311.pyc
│
├───datasets 
│       insurance.csv
│       loan_data.csv
│       readme.md
│       StudentsPerformance.csv
│
└───docs
        差分隐私下的和估计(证明部分和公式设计).md
        差分隐私下的和估计.pdf
        论文解释.md
        论文解释.pdf

```

`sum_dp_module.py`文件中的`SumDP class`是算法具体实现

`error_evaluation`文件下的`SumDP_eva.py`是误差分析代码实现

`SumDP_error.ipynb`: notebook中写了详细的调用计算示例，调用可以查看

> 后续实验代码你们可以自行调整一下，保证易读就行（我这边整理的是error_evaluation文件下实现的是Evaluation的具体代码）

## 后半部分实现细节

1. **数据预处理与设置参数**
   - 选择至少三个Kaggle上公开的隐私敏感数据集，这些数据集应包含数值型特征，能够作为求和查询的对象。
   - 针对每个数据集，确定一个上界 U（例如，对于收入数据，U可以是一个保守的最大值），同时计算数据的真实最大值 Max(D)。（注意：我们的SumDP协议的优势在于误差依赖于Max(D)，而拉普拉斯机制误差依赖于U）
2. **实现两种机制**
   - **拉普拉斯机制（Laplace Mechanism）：**
      对于求和问题，直接在真实总和上添加尺度为 U/ε 的拉普拉斯噪声。
   - **选定技术（例如SumDP协议）：**
      根据我们的设计，在用户端对数据进行分区（例如对数域分割），在各个子区间上分别执行BaseSumDP，然后在分析器端使用噪声敏感的阈值选择方法得到一个剪切阈值τ，再聚合所有子区间的噪声和，得到最终求和结果。其理论误差为 $O(Max(D)·ln(log U)/ε)$ 
3. **实验设置与评价指标**
   - 对每个数据集，在不同的隐私预算ε（例如0.2、1、5等）下运行两种机制，并重复多次（例如50次实验）以统计平均误差。
   - 记录评价指标，如绝对误差、相对误差等。
   - 可以绘制错误随ε变化的曲线，以及不同数据集在同一ε下的比较图。
4. **理论与实验结果对比**
   - 分析实验结果时，重点说明在大多数实际数据中，Max(D)远小于U，因此SumDP协议能利用这一点获得较小的噪声量，误差明显低于直接采用拉普拉斯机制的 O(U/ε) 误差。
   - 同时，讨论当ε变化时，两种方法的误差随之变化的趋势是否符合理论（例如：误差均呈现 1/ε 衰减）。
   - 如果可能，进一步讨论不同数据集之间由于数据分布不同（例如数据的偏斜、稀疏性）对误差的影响，验证理论上剪切机制在实例自适应性方面的优势。


   