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

#There is no validation for any of the APIs, so regardless of the data you provide, some APIs will always return a success response. There are many negative cases, but I did not write them all.


