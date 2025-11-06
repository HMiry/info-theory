# Information Theory & Cryptography Course

This repository contains assignments and exercises for an Information Theory and Cryptography course, covering fundamental concepts in entropy, information theory, stream ciphers, and block cipher encryption modes.

## 📚 Table of Contents

- [Overview](#overview)
- [Assignment 1: Entropy and Information Theory](#assignment-1-entropy-and-information-theory)
- [Assignment 2: MATLAB Applications](#assignment-2-matlab-applications)
- [Assignment 3: Cryptography](#assignment-3-cryptography)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)

## 🎯 Overview

This project explores key concepts in information theory and cryptography through practical implementations and theoretical exercises. The assignments cover entropy calculations, probability distributions, decision trees, stream ciphers (LFSR/NLFSR), and block cipher encryption modes.

## 📊 Assignment 1: Entropy and Information Theory

### Exercise 1: Entropy of Random Variables
**File:** `exe1.ipynb`

- Plots entropy as a function of all possible probability vectors for a 3-outcome random variable
- Visualizes entropy over the probability simplex using 2D contour plots
- Implements iterative averaging procedure starting from non-uniform distribution
- Demonstrates convergence toward uniform distribution and maximum entropy

**Key Concepts:** Shannon entropy, probability simplex, maximum entropy principle

### Exercise 2: Climate Data Analysis
**File:** `exe2.ipynb`

- Analyzes daily climate time series data from Delhi using Kaggle dataset
- Implements temperature binning and probability distribution calculation
- Computes entropy evolution over time as data accumulates
- Visualizes entropy trends in climate data

**Key Concepts:** Empirical probability distributions, time series analysis, entropy in real-world data

### Exercise 3: Maximum Entropy Principle
**File:** `exe3.ipynb`

- Implements the principle of maximum entropy with constraints
- Solves for probability distributions with fixed mean values
- Uses numerical methods to find optimal β parameter
- Compares distributions with different mean constraints (above, equal to, and below arithmetic mean)
- Visualizes how mean constraints affect probability distributions

**Key Concepts:** Lagrange multipliers, constrained optimization, exponential distributions

### Exercise 4: Information Gain & Decision Trees
**File:** `exe4.ipynb`

- Analyzes e-commerce customer data (10 customers with multiple features)
- Calculates information gain and gain ratio for feature selection
- Implements entropy-based decision tree metrics
- Determines best splitting attribute for classification
- **Features analyzed:** Page Views, Time on Site, Age Group, Country
- **Target variable:** Purchase decision (Yes/No)

**Key Concepts:** Information gain, intrinsic value, gain ratio, decision tree algorithms

### Exercise 5: Kullback-Leibler Divergence
**File:** `exe5.ipynb`

- Compares empirical probability distributions with theoretical distributions
- Calculates KL divergence from uniform distribution
- Finds optimal binomial distribution parameters using KL minimization
- Visualizes probability mass functions and divergence values
- Uses optimization to find best-fit binomial distribution (p parameter)

**Key Concepts:** KL divergence, distribution fitting, statistical distance measures

### Exercise 6: Permutation Entropy
**File:** `exe6.ipynb`

- Implements normalized permutation entropy for time series analysis
- Uses sliding window approach (N_w = 512, order m = 3)
- Generates random data series (10,000 points)
- Introduces structured patterns in specific segments (indices 3000-4000)
- Detects anomalies and structural changes through entropy analysis
- Visualizes entropy evolution to identify non-random patterns

**Key Concepts:** Permutation entropy, complexity analysis, anomaly detection, time series analysis

### Exercise 7: Decision Tree Classifier
**Files:** `exe7Ass1Es7.mlx`, `exe7Classifier.m`

- MATLAB implementation of a decision tree classifier
- Uses three features for binary classification
- Interactive input system for feature values
- Implements hierarchical decision rules

**Key Concepts:** Classification algorithms, decision rules, MATLAB programming

## 🖥️ Assignment 2: Information Theory GUIs and Analytical Solutions

This assignment implements interactive MATLAB GUI applications for entropy calculations, channel capacity, quantization algorithms, and text analysis, combined with analytical solutions for specific probability distributions. Divided into **Part A** (discrete random variables) and **Part B** (continuous random variables and quantization).

### Files
- `ES1A.mlapp` - Discrete RV Entropy Calculator GUI
- `ex2_a.mlapp` - Channel Capacity Calculator GUI
- `ex3_a.mlapp` - Text Entropy Rate Analyzer GUI
- `ex3_b.mlapp` - Differential Entropy Calculator GUI
- `ex4.1_b.nb` - Laplace Distribution Analysis (Mathematica)
- `ex4.2_b.nb` - Gamma Distribution Analysis (Mathematica)
- `ex4.3_b.nb` - Rayleigh Distribution Analysis (Mathematica)

**Technologies:** MATLAB R2016a+ with App Designer, Mathematica. Alternative: Python Jupyter Notebooks with equivalent GUI functionality.

---

## Part A: Discrete Random Variables

### Problem 1A: Discrete Random Variable Entropy Calculator
**File:** `ES1A.mlapp`

Interactive GUI for calculating Shannon entropy H(X) = -Σ p(x) log₂(p(x)) of discrete random variables.

**Features:**
- Input probability vector for n discrete outcomes
- Automatic validation (Σpᵢ = 1, all pᵢ ≥ 0)
- Real-time entropy calculation
- PMF visualization (bar chart)
- Support for arbitrary number of outcomes

**Key Concepts:** Shannon entropy, discrete probability distributions, maximum entropy principle

---

### Problem 2A: Channel Capacity Calculator
**File:** `ex2_a.mlapp`

GUI for calculating channel capacity C = max I(X;Y) given a transition probability matrix P.

**Features:**
- Input transition probability matrix P(Y|X)
- Iterative optimization (Blahut-Arimoto algorithm)
- Outputs: channel capacity, optimal input distribution
- Convergence visualization

**Test Cases:** Binary symmetric channel (BSC), binary erasure channel (BEC), noiseless channel

**Key Concepts:** Channel capacity, mutual information, optimization algorithms

---

### Problem 3A: Text Entropy Rate Analyzer
**File:** `ex3_a.mlapp`

GUI for analyzing entropy rate of ASCII text through n-gram analysis.

**Features:**
- Multi-line text input
- Configurable n-gram order (1-6+)
- Computes entropy rate: H_rate = H(Xⁿ) / n
- Outputs decreasingly sorted probability distribution
- Comparison across different orders

**Analysis:**
- Order 1: Individual character frequencies
- Order 2+: Bigrams and higher-order dependencies
- Demonstrates redundancy in natural language

**Key Concepts:** Entropy rate, n-gram models, text compression, statistical language modeling

---

### Problem 4A: Entropy of Specific Discrete Distributions
**Deliverable:** Analytical and numerical solutions in LaTeX report

For each distribution, determine analytical vs numerical solution approach:

#### 4A.1: Geometric-like Distribution
p(x) ∝ exp(-αx), x = 0, 1, 2, ...
- **Solution:** Analytical (geometric series)
- **Entropy:** H(X) = [q log₂(q) - log₂(1-q)] / (1-q) where q = exp(-α)
- **Parameter range:** α > 0

#### 4A.2: Gaussian-like Discrete Distribution
p(x) ∝ exp(-x²), x = 0, 1, 2, ...
- **Solution:** Numerical (rapidly converging series, truncate at x_max)
- **Typical result:** H(X) ≈ 1.52 bits

#### 4A.3: Zipf Distribution
p(x) ∝ x⁻ᵅ, x = 1, 2, 3, ...
- **Solution:** Case-dependent
  - α > 1: Semi-analytical using ζ(α) (Riemann zeta function)
  - α ≤ 1: Numerical (series diverges, requires truncation)
- **Applications:** Word frequencies, power laws

#### 4A.4: Finite Zipf Distribution
p(x) ∝ x⁻ᵅ, x = 1, ..., N
- **Solution:** Analytical (finite sum)
- **Special case:** α = 0 gives uniform, H(X) = log₂(N)

#### 4A.5: Modified Geometric Distribution
p(x) ∝ 1/(1+x)ᵅ, x = 0, 1, 2, ... for α = 1, 2
- **α = 1:** Numerical (harmonic series diverges)
- **α = 2:** Semi-analytical (Z = π²/6, numerical entropy calculation)

**Deliverables:** Mathematical derivations, MATLAB/Python code, plots of H(X) vs parameters

---

## Part B: Continuous Random Variables and Quantization

### Problem 1B: Differential Entropy Calculator
**File:** `ex3_b.mlapp`

GUI for computing differential entropy h(X) = -∫ f(x) log₂(f(x)) dx.

**Features:**
- Common distributions dropdown (Uniform, Gaussian, Exponential, Laplace)
- Custom symbolic expression input
- Integration range: (-∞, +∞) or finite bounds
- Symbolic and numerical integration methods
- PDF visualization and normalization check

**Known Formulas:**
- Uniform [a,b]: h(X) = log₂(b-a)
- Gaussian N(μ,σ²): h(X) = ½ log₂(2πeσ²)
- Exponential Exp(λ): h(X) = log₂(e/λ)

**Key Concepts:** Differential entropy, continuous probability, numerical integration

---

### Problem 2B: Lloyd-Max Quantizer Algorithm
**Implementation:** GUI or documented Jupyter Notebook

Optimal scalar quantization algorithm minimizing mean-squared error (MSE).

**Algorithm:**
1. **Nearest Neighbor:** Assign points to closest quantization level
2. **Centroid Update:** qᵢ = E[X | tᵢ₋₁ < X ≤ tᵢ]
3. **Iterate** until convergence

**Features:**
- Input: PDF, number of levels K
- Outputs: optimal quantization levels, decision boundaries, minimum distortion
- Visualizations: PDF with levels, quantizer function, convergence plot

**Test Cases:** Uniform (equally-spaced levels), Gaussian (more levels at center), Exponential (asymmetric)

**Key Concepts:** Quantization, Lloyd algorithm, rate-distortion theory

---

### Problem 3B: LBG Vector Quantization Algorithm
**Implementation:** GUI or documented Jupyter Notebook

2D vector quantization using Linde-Buzo-Gray algorithm (k-means clustering for vectors).

**Algorithm:**
1. **Initialization:** K random codeword vectors (multiple trials)
2. **Classification:** Assign grid points to nearest codeword
3. **Centroid Update:** Recompute weighted centroids
4. **Iterate** until convergence

**PDF Discretization:**
- Approximate f(x,y) on N×N grid
- Grid points: xᵢ = xₘᵢₙ + i·Δₓ, yⱼ = yₘᵢₙ + j·Δᵧ
- Probability masses: p(xᵢ,yⱼ) = f(xᵢ,yⱼ)·Δₓ·Δᵧ (normalized)

**Features:**
- Input: 2D PDF, codebook size K, grid resolution
- Multiple random initializations
- Outputs: optimal codebook, minimum distortion

**Visualizations:**
1. Distortion vs trial number
2. Optimal codebook with Voronoi regions on PDF contour
3. Convergence curve

**Test Cases:** 2D Gaussian, mixture of Gaussians, uniform over region

**Key Concepts:** Vector quantization, k-means clustering, codebook design

---

### Problem 4B: Differential Entropy of Specific Distributions
**Files:** `ex4.1_b.nb`, `ex4.2_b.nb`, `ex4.3_b.nb` (Mathematica)

Analytical derivations for three continuous distributions:

#### 4B.1: Laplace Distribution
f(x) = (λ/2) exp(-λ|x|), x ∈ (-∞, +∞)
- **Entropy:** h(X) = log₂(2e/λ) = 1 + log₂(2/λ)
- **Applications:** Robust statistics, image compression

#### 4B.2: Gamma Distribution
f(x) = (λᵏ/Γ(k)) xᵏ⁻¹ exp(-λx), x > 0
- **Entropy:** h(X) = k + log₂(Γ(k)/λᵏ) + (1-k)·ψ(k)/log(2)
- ψ(k) is digamma function
- **Special case:** k=1 gives Exponential

#### 4B.3: Rayleigh Distribution
f(x) = (x/σ²) exp(-x²/2σ²), x > 0
- **Entropy:** h(X) = log₂(σ) + ½log₂(2πe) - ½
- **Applications:** Wireless fading channels, magnitude of 2D Gaussian

**Deliverables:** Symbolic derivations, numerical verification, parameter analysis plots

---

## Submission Requirements

**Deliverables:**
- All MATLAB `.mlapp` files or Python notebooks
- Mathematica `.nb` files
- LaTeX report as `group<number>.pdf`
- Compress everything into `group<number>.zip`

**Report Structure:**
1. Introduction
2-5. Part A Problems (1A-4A)
6-9. Part B Problems (1B-4B)
10. Conclusions and References

**Submission:** Upload through Politecnico di Torino web portal (no email submissions).

**Course:** Information Theory for Data Science, Prof. Giorgio Taricco, Politecnico di Torino - DET

## 🔐 Assignment 3: Cryptography

### Exercise 1: Stream Ciphers - LFSR & NLFSR
**Files:** `ex1_stream_ciphers.ipynb`, `StreamCiphers.tex`, `Question1.tex`, `part1.py`

#### Part A: Linear Feedback Shift Register (LFSR)
- Implements LFSR with m=10 cells and polynomial description: **D¹⁰ + D³ + 1**
- Generates M-sequence of N=1023 bits (maximum period)
- Analyzes M-sequence properties:
  - **0/1 distribution:** Verifies N₁ = N₀ + 1 (512 ones, 511 zeros)
  - **Run analysis:** Validates ideal run properties for binary sequences
  - **Autocorrelation:** R(τ) = N for τ=0, R(τ) = -1 for τ≠0
- Converts binary sequence to bipolar representation (-1, +1)
- Plots first 20 bits and complete autocorrelation function

#### Part B: Breaking Linear LFSR (Chosen Plaintext Attack)
- Intercepts 40-bit key portion: `1010100010000001101010010111011000101110`
- Implements attack algorithm using binary linear system solving in GF(2)
- Tests increasing LFSR sizes (m = 3 to 20)
- Successfully breaks the cipher and finds:
  - **Polynomial:** D¹⁹ + D⁵ + D² + D + 1
  - **Number of cells:** m = 19
- Predicts next 20 bits of the key stream

#### Part C: Nonlinear Feedback Shift Register (NLFSR)
- Implements NLFSR to improve security over linear LFSR
- **Feedback function:** f(x₀, x₁, x₂, x₃, x₄) = x₀ ⊕ x₁ ⊕ x₃ ⊕ (x₁ · x₃)
- Demonstrates nonlinearity: M(S₁ ⊕ S₂) ≠ M(S₁) ⊕ M(S₂)
- Compares LFSR vs NLFSR resistance to cryptanalysis
- Achieves maximum period (2ᵐ - 1 = 31 bits)

**Key Concepts:** Pseudorandom sequence generation, cryptanalysis, stream ciphers, GF(2) arithmetic, primitive polynomials

### Block Cipher Encryption Modes
**File:** `part1.py`

#### Implemented Encryption Modes:
1. **ECB (Electronic Codebook Mode)**
   - Encrypts identical plaintext blocks to identical ciphertext blocks
   - Demonstrates pattern preservation vulnerability
   - Shows visual patterns in encrypted images

2. **CBC (Cipher Block Chaining Mode)**
   - Each block depends on previous ciphertext block
   - Uses initialization vector (IV)
   - Better security than ECB

3. **CTR (Counter Mode)**
   - Stream cipher mode of operation
   - Uses nonce/counter for each block
   - Parallelizable encryption/decryption

#### Features:
- **Image encryption:** Works with PPM (Portable Pixmap) format
- **Padding:** PKCS7 padding for block alignment
- **AES-128:** Uses 128-bit keys (16 bytes)
- **Comparison tools:** Byte-level difference analysis
- **Key sensitivity test:** Modifies 3 bits and compares results
- **Incorrect IV/nonce test:** Demonstrates importance of correct parameters

#### Experiments:
1. Encrypts Tux image with all three modes
2. Decrypts with correct parameters
3. Tests avalanche effect (3-bit key modification)
4. Tests incorrect IV (CBC) and incorrect nonce (CTR)
5. Quantifies differences in decrypted images

**Key Concepts:** Block ciphers, AES, encryption modes, avalanche effect, cryptographic protocols

### Theoretical Presentations
**Files:** `Question1.tex`, `StreamCiphers.tex`

LaTeX presentations covering:
- **TLS Protocol:** Handshake, cipher suites, forward secrecy
- **RSA and Diffie-Hellman:** Key exchange algorithms
- **Stream Cipher Security:** LFSR properties and attacks
- **Mathematical foundations:** Discrete logarithm, prime factorization

## 🛠️ Technologies Used

### Python
- **NumPy** - Numerical computations and array operations
- **Matplotlib** - Data visualization and plotting
- **Pandas** - Data manipulation and analysis
- **SciPy** - Scientific computing and optimization
- **cryptography** - AES encryption implementation
- **Jupyter Notebook** - Interactive development environment

### MATLAB
- MATLAB R2016a or later
- App Designer
- Symbolic Math Toolbox

### Mathematica
- Wolfram Mathematica

### LaTeX
- Beamer class for presentations
- Mathematical typesetting

## 🚀 Getting Started

### Prerequisites

```bash
# Python 3.8 or higher
python --version

# Install required Python packages
pip install numpy matplotlib pandas scipy cryptography jupyter
```

### Running Python Notebooks

```bash
# Navigate to the project directory
cd info-theory

# Launch Jupyter Notebook
jupyter notebook

# Open any .ipynb file from the assignments
```

### Running Python Scripts (Assignment 3)

```bash
cd info-theory/assignment3

# Ensure you have a Tux.ppm image file in the directory
python part1.py

# Encrypted images will be saved in 'encryption/' folder
# Decrypted images will be saved in 'decryption/' folder
```

### MATLAB Files

```matlab
% Open MATLAB
% Navigate to assignment2 folder
% Double-click any .mlapp file to open in App Designer
% Or run from command window:
run('ES1A.mlapp')
```

### LaTeX Documents

```bash
cd info-theory/assignment3

# Compile LaTeX presentations
pdflatex Question1.tex
pdflatex StreamCiphers.tex
```

## 📝 Key Learning Outcomes

1. **Information Theory Fundamentals**
   - Understanding entropy as a measure of uncertainty
   - Maximum entropy principle and its applications
   - Information gain for feature selection

2. **Probability & Statistics**
   - Probability distributions and their properties
   - KL divergence for distribution comparison
   - Statistical analysis of time series data

3. **Cryptography**
   - Stream cipher design and cryptanalysis
   - Block cipher modes of operation
   - Security vulnerabilities and countermeasures
   - AES encryption in different modes

4. **Practical Skills**
   - Python scientific computing stack
   - Data visualization techniques
   - MATLAB application development
   - Mathematical typesetting with LaTeX

## 📖 References

- Shannon, C.E. "A Mathematical Theory of Communication" (1948)
- Cover, T.M. & Thomas, J.A. "Elements of Information Theory"
- Dubrova, E. "A List of Maximum Period NLFSRs" (for NLFSR implementations)
- NIST guidelines for AES encryption modes
- Kaggle: Daily Climate Time Series Data

## 👤 Author

**HMiry**

Repository: [info-theory](https://github.com/HMiry/info-theory)

---

## 📄 License

This project is created for educational purposes as part of an Information Theory and Cryptography course.

---

**Last Updated:** November 2025
