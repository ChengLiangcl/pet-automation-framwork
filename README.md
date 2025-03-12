# PetStore Automation Framework

This project provides automated testing for the **PetStore API** using **Python** and **pytest**.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python** (>= 3.8)
- **pip** (Python package manager)

## Setup

Follow these steps to pull the code and set up the environment:

1. **Go to your desktop**.
2. Run the following command to clone the repository:
   ```bash
   git clone https://github.com/ChengLiangcl/pet-automation-framwork.git
3. Navigate into the project directory:
   ```bash
   cd pet-automation-framework

4. Install the necessary dependencies from the requirements.txt file:
    ```bash
   pip install -r requirements.txt
6. under root directory command to run all the test cases
    ```bash
    pytest

## I would suggest running the test cases separately. It's strange that when running all the test cases together with the pytest command, some cases pass, but others fail. Please follow the instructions below to run each test case separately.

## I would suggest running the test cases separately. It's strange that when running all the test cases together with the pytest command, some cases pass, but others fail. Please follow the instructions below to run each test case separately.

## Running Test Cases Separately
To ensure accurate results, it is recommended to run the test cases separately. Below are the commands for running each test case individually.

### For Windows
```bash
pytest user_test_case\test_user_api_positive.py
pytest user_test_case\test_user_api_negative.py
pytest store_test_case\test_store_positive.py
pytest store_test_case\test_store_negative_cases.py
pytest pet_test_case\test_pet_positive_case.py
pytest pet_test_case\test_negative_case.py

### For macs
```bash
pytest user_test_case/test_user_api_positive.py
pytest user_test_case/test_user_api_negative.py
pytest store_test_case/test_store_positive.py
pytest store_test_case/test_store_negative_cases.py
pytest pet_test_case/test_pet_positive_case.py
pytest pet_test_case/test_negative_case.py
