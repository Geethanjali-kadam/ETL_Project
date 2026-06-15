# ETL Project

## Project Overview

This project demonstrates an End-to-End ETL (Extract, Transform, Load) pipeline developed using Python. The project extracts data from CSV files and REST APIs, transforms and validates the data, cleans missing values, and loads the processed data into a SQLite database.

The project also includes advanced concepts such as API pagination, SQLAlchemy ORM, Upsert operations, Pydantic models, logging, exception handling, and unit testing using Pytest.

---

## Features

* Extract data from CSV files
* Extract data from REST APIs
* Transform data using Pandas
* Validate data and detect missing values
* Clean missing or invalid data
* Load data into SQLite database
* Use SQLAlchemy ORM for database operations
* Implement Upsert functionality
* Perform API Pagination
* Use Pydantic for data validation
* Implement Logging and Error Handling
* Write Unit Tests using Pytest

---

## Technologies Used

| Technology | Purpose                              |
| ---------- | ------------------------------------ |
| Python     | Programming Language                 |
| Pandas     | Data Manipulation and Transformation |
| SQLite     | Database                             |
| SQLAlchemy | ORM for Database Operations          |
| Requests   | API Calls                            |
| Pydantic   | Data Validation                      |
| Pytest     | Unit Testing                         |
| Git        | Version Control                      |
| GitHub     | Code Repository                      |

---

## Project Structure

ETL_Project

├── Data/

│   ├── customers.csv

│   └── payments.csv

├── extract.py

├── transform.py

├── validate.py

├── data_cleaning.py

├── load.py

├── api_extract.py

├── pagination.py

├── upsert.py

├── model.py

├── config.py

├── error_handling.py

├── logging_example.py

├── sqlalchemy_demo.py

├── calculator.py

├── test_calculator.py

├── test_model.py

├── cleaned_data.csv

├── final_data.csv

├── api_data.csv

├── pagination_data.csv

├── README.md

└── .gitignore
ETL Workflow
CSV/API Data
↓
Extract Data
↓
Transform Data
↓
Validate Data
↓
Clean Data
↓
Load Data into SQLite Database
↓
Upsert Records
↓
API Pagination
↓
Unit Testing
↓
End-to-End Testing

Modules Explanation

1. Extract Module

* Reads customer and payment data from CSV files.
* Merges datasets using customer_id.

2. Transform Module

* Performs data transformations.
* Renames columns and formats data.

3. Validation Module

* Checks for missing values.
* Verifies data quality.

4. Data Cleaning Module

* Replaces missing values with default values.
* Cleans inconsistent records.

5. Load Module

* Loads cleaned data into SQLite database.

6. API Extraction Module

* Fetches data from REST APIs using Requests library.

 7. Pagination Module

* Retrieves API data page by page.

8. SQLAlchemy Module

* Demonstrates ORM concepts.
* Creates database models and performs CRUD operations.
9. Upsert Module

* Updates existing records or inserts new records.

10. Testing Module

* Performs unit testing using Pytest.
* Ensures project reliability.

---

## Team Members

1. kadam Geethanjali
2. Adudodla Sreeja
3. Patro Bhanupraksh
4. Sanapala Purna Sai Chandu

---

## GitHub Repository

This project is maintained using Git and GitHub for version control and collaboration.
