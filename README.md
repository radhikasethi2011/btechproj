# Classification of Highly Interacting Regions of the Genome with Explainable AI

## Overview

This project aims to identify regions governing gene regulation and classify them as highly interacting or non-interacting using Explainable AI. By examining these sequences, we can classify genomic regions and determine influential genomic properties in the transformation of a cell into a diseased state.

## Objectives

- Model biological sequencing and DNA data to understand their underlying properties and patterns.
- Use deep learning algorithms to distinguish highly interacting regions and their boundaries.
- Classify genomic sequences as potentially interacting or non-interacting.
- Identify traits of highly interacting regions that make them more interactive.
- Understand how these specific regions influence gene regulation.
- Find genomic sequence properties that influence a cell's transformation into a diseased cell.

## Tech Stack

- **Programming Languages:** Python
- **Libraries and Frameworks:** TensorFlow, Keras, Sklearn, Matplotlib, Seaborn
- **Tools:** Jupyter Notebook, Git
- **Data:** Sub-kb Hi-C in D. melanogaster, ChIP-seq data from ENCODE project

## Methodology

### Phase 1 - Markov Models

#### Architecture

1. **Preprocessing Flow:**
   - Generate dummy data with a probability of 0.25 for each nucleotide.
   - Create files embedding highly interacting regions using random functions.
   
2. **Training and Testing:**
   - Train highly interacting region Markov models on respective files.
   - Perform cross-validation and visualize results with AUC ROC curves, accuracy, and F1 scores.

### Phase 2 - Deep Learning

#### Deep Learning Model

- **Model Architecture:**
  - Conv1D layers with Batch Normalization and LeakyReLU activation
  - MaxPooling1D and Dropout layers to prevent overfitting
  - Dense layers for final classification

#### Training and Testing

- Perform cross-validation on simulated and real datasets.
- Evaluate the model using metrics such as accuracy, AUC, and ROC curves.

## Results

### Markov Models

- **Simulated Data:**
  - Generated dummy data with embedded highly interacting regions.
  - Cross-validation results showing accuracy and AUC scores.

### Deep Learning

- **Simulated Data:**
  - Achieved high testing accuracy with consistent results across folds.
- **Drosophila Data:**
  - Moderate accuracy indicating room for improvement.

## Directory Structure

- **Data/**: Contains all datasets and related files.
  - **fruitfly/**: Data specific to fruit flies.
    - **Fruitfly Bed files/**: BED files for different shifts.
    - **Fruitfly Datasets/**: Dataset files for different shifts.
    - **Fruitfly Fasta/**: FASTA files for different shifts.
  - **deepbind-exe-file/**: Contains input files for DeepBind executions.
  - **dummy_markov_data/**: Contains Markov model data.
  
- **colab_files/**: Contains Jupyter notebooks for various data processing and analysis tasks.
  
- **\_\_MACOSX/**: Contains system files for macOS, which are not needed for the project execution.

## Setup and Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the project directory**:
    ```bash
    cd btechproj-main
    ```

3. **Install required dependencies**:
    - Ensure you have Python installed.
    - Install dependencies using `pip`:
      ```bash
      pip install -r requirements.txt
      ```
    - Alternatively, if a `requirements.txt` file is not provided, manually install dependencies mentioned in the notebooks and scripts.

## Data Description

- **Fruitfly Data**: This includes BED, FASTA, and dataset files for different shifts (e.g., shift_200, shift_500).
  - **BED files**: Contains genomic regions data.
  - **FASTA files**: Contains sequences of DNA.
  - **Dataset files**: Contains various datasets used for analysis.

- **DeepBind Data**: Input files for running DeepBind, a tool for predicting protein binding.

- **Markov Model Data**: Files related to Markov models used in the analysis.

## Jupyter Notebooks

Located in the `colab_files/` directory, these notebooks provide various analyses and processing steps, such as:
- Markov models with cross-validation
- TensorFlow and PyTorch implementations
- Binding site predictions
- Pipelines for converting BED to FASTA and other tasks

## Usage

1. **Running Jupyter Notebooks**:
    - Navigate to the `colab_files/` directory:
      ```bash
      cd colab_files
      ```
    - Start Jupyter Notebook:
      ```bash
      jupyter notebook
      ```
    - Open the desired notebook and follow the instructions within.

2. **Data Processing Scripts**:
    - Data processing scripts are located within the `Data/` directory. Run these scripts as needed for your analysis.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any inquiries or issues, please contact [Your Name] at [your-email@example.com].
