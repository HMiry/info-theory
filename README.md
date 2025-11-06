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

Interactive GUI for calculating Shannon entropy of discrete random variables.

**Features:**
- Input probability vector for n discrete outcomes
- Automatic validation that probabilities sum to 1 and are non-negative
- Real-time entropy calculation
- PMF visualization with bar chart
- Support for arbitrary number of outcomes

**Key Concepts:** Shannon entropy, discrete probability distributions, maximum entropy principle

---

### Problem 2A: Channel Capacity Calculator
**File:** `ex2_a.mlapp`

GUI for calculating channel capacity given a transition probability matrix.

**Features:**
- Input transition probability matrix
- Iterative optimization using Blahut-Arimoto algorithm
- Outputs channel capacity and optimal input distribution
- Convergence visualization

**Test Cases:** Binary symmetric channel, binary erasure channel, noiseless channel

**Key Concepts:** Channel capacity, mutual information, optimization algorithms

---

### Problem 3A: Text Entropy Rate Analyzer
**File:** `ex3_a.mlapp`

GUI for analyzing entropy rate of ASCII text through n-gram analysis.

**Features:**
- Multi-line text input
- Configurable n-gram order (1 to 6 or more)
- Computes entropy rate per symbol
- Outputs decreasingly sorted probability distribution
- Comparison across different orders

**Analysis:**
- Order 1: Individual character frequencies
- Order 2 and higher: Bigrams and higher-order dependencies
- Demonstrates redundancy in natural language

**Key Concepts:** Entropy rate, n-gram models, text compression, statistical language modeling

---

### Problem 4A: Entropy of Specific Discrete Distributions
**Deliverable:** Analytical and numerical solutions in LaTeX report

For each distribution, determine whether analytical or numerical solution is appropriate:

#### 4A.1: Geometric-like Distribution
Distribution proportional to exponential decay
- **Solution:** Analytical using geometric series
- **Parameter range:** Alpha greater than zero

#### 4A.2: Gaussian-like Discrete Distribution
Distribution proportional to exponential of negative x-squared
- **Solution:** Numerical (rapidly converging series, truncate at suitable maximum)
- **Typical result:** Entropy approximately 1.52 bits

#### 4A.3: Zipf Distribution
Distribution with power-law decay
- **Solution:** Case-dependent
  - For alpha greater than 1: Semi-analytical using Riemann zeta function
  - For alpha less than or equal to 1: Numerical (series diverges, requires truncation)
- **Applications:** Word frequencies, power laws in nature

#### 4A.4: Finite Zipf Distribution
Power-law distribution over finite range
- **Solution:** Analytical (finite sum)
- **Special case:** When alpha equals zero, reduces to uniform distribution

#### 4A.5: Modified Geometric Distribution
Distribution with inverse power decay
- **Case alpha = 1:** Numerical (harmonic series diverges)
- **Case alpha = 2:** Semi-analytical (normalization constant is pi-squared over 6)

**Deliverables:** Mathematical derivations, MATLAB/Python code, plots of entropy vs parameters

---

## Part B: Continuous Random Variables and Quantization

### Problem 1B: Differential Entropy Calculator
**File:** `ex3_b.mlapp`

GUI for computing differential entropy of continuous random variables.

**Features:**
- Common distributions dropdown (Uniform, Gaussian, Exponential, Laplace)
- Custom symbolic expression input
- Integration range selection (infinite or finite bounds)
- Symbolic and numerical integration methods
- PDF visualization and normalization check

**Known Results:**
- Uniform distribution: entropy is logarithm of interval width
- Gaussian distribution: entropy depends on variance
- Exponential distribution: entropy depends on rate parameter

**Key Concepts:** Differential entropy, continuous probability, numerical integration

---

### Problem 2B: Lloyd-Max Quantizer Algorithm
**Implementation:** GUI or documented Jupyter Notebook

Optimal scalar quantization algorithm minimizing mean-squared error.

**Algorithm Steps:**
1. **Nearest Neighbor:** Assign input values to closest quantization level
2. **Centroid Update:** Compute optimal quantization levels as conditional expectations
3. **Iterate** until convergence

**Features:**
- Input: PDF specification and number of quantization levels
- Outputs: optimal quantization levels, decision boundaries, minimum distortion
- Visualizations: PDF with levels overlay, quantizer staircase function, convergence plot

**Test Cases:** Uniform (equally-spaced levels), Gaussian (more levels at center), Exponential (asymmetric quantizer)

**Key Concepts:** Quantization, Lloyd algorithm, rate-distortion theory

---

### Problem 3B: LBG Vector Quantization Algorithm
**Implementation:** GUI or documented Jupyter Notebook

2D vector quantization using Linde-Buzo-Gray algorithm (extension of k-means clustering).

**Algorithm Steps:**
1. **Initialization:** Generate initial codeword vectors (multiple random trials)
2. **Classification:** Assign grid points to nearest codeword using Euclidean distance
3. **Centroid Update:** Recompute codewords as weighted centroids of assigned points
4. **Iterate** until convergence

**PDF Discretization:**
- Approximate continuous 2D PDF on square grid
- Grid with configurable resolution
- Compute probability mass at each grid point
- Normalize to ensure probabilities sum to one

**Features:**
- Input: 2D PDF, codebook size, grid resolution
- Multiple random initializations to find global optimum
- Outputs: optimal codebook, minimum distortion across trials

**Visualizations:**
1. Distortion vs trial number showing best initialization
2. Optimal codebook points with Voronoi regions on PDF contour
3. Convergence curve for best trial

**Test Cases:** 2D Gaussian, mixture of Gaussians, uniform over bounded region

**Key Concepts:** Vector quantization, k-means clustering, codebook design, Voronoi regions

---

### Problem 4B: Differential Entropy of Specific Distributions
**Files:** `ex4.1_b.nb`, `ex4.2_b.nb`, `ex4.3_b.nb` (Mathematica notebooks)

Analytical derivations for three continuous distributions:

#### 4B.1: Laplace Distribution
Double exponential distribution symmetric around zero
- **Result:** Analytical entropy formula involving scale parameter
- **Applications:** Robust statistics, image compression, sparse signal processing

#### 4B.2: Gamma Distribution
Generalized exponential distribution over positive reals
- **Result:** Entropy formula involving shape and rate parameters, uses digamma function
- **Special case:** When shape equals 1, reduces to exponential distribution

#### 4B.3: Rayleigh Distribution
Distribution of magnitude of 2D Gaussian random vector
- **Result:** Entropy formula with scale parameter
- **Applications:** Wireless fading channels, wind speed modeling, signal processing

**Deliverables:** Complete symbolic derivations, numerical verification, parameter analysis plots

---

## Submission Requirements

**Deliverables:**
- All MATLAB `.mlapp` files or equivalent Python notebooks
- Mathematica `.nb` files for Problem 4B
- Comprehensive LaTeX report as `group<number>.pdf`
- Everything compressed into `group<number>.zip`

**Report Structure:**
1. Introduction
2. Part A - Problem 1 (Discrete Entropy GUI)
3. Part A - Problem 2 (Channel Capacity)
4. Part A - Problem 3 (Text Entropy Rate)
5. Part A - Problem 4 (Discrete Distributions)
6. Part B - Problem 1 (Differential Entropy GUI)
7. Part B - Problem 2 (Lloyd-Max Algorithm)
8. Part B - Problem 3 (LBG Algorithm)
9. Part B - Problem 4 (Continuous Distributions)
10. Conclusions and References

**Submission:** Upload through Politecnico di Torino web portal (no email submissions accepted).

**Course Information:**
- **Course:** Information Theory for Data Science
- **Instructor:** Prof. Giorgio Taricco
- **Institution:** Politecnico di Torino - DET

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
