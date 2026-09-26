# AI-Powered Data Analysis & SQL Assistant

An interactive data analysis application built with **Python, Pandas, SQLite, Streamlit, Plotly, and Ollama**. The application allows users to upload CSV or Excel datasets, perform automated exploratory analysis, generate visualizations and insights, execute SQL queries, and ask questions about their data using natural language.

## Project Overview

The **AI-Powered Data Analysis & SQL Assistant** combines traditional data analysis techniques with a locally running Large Language Model (LLM).

Instead of manually writing SQL queries for every question, users can ask questions in natural language. The application uses **Ollama with the Qwen 2.5 7B model** to convert the question into a SQLite-compatible SQL query and execute it against the uploaded dataset.

The project is designed to demonstrate practical skills in:

* Data Analysis
* Python Programming
* Pandas
* SQL
* SQLite
* Data Visualization
* Streamlit
* Large Language Models
* Natural Language to SQL
* Local LLM Integration

---

## Key Features

### 1. Dataset Upload

Upload datasets in:

* CSV
* Excel (`.xlsx`)

The application automatically loads the dataset using Pandas.

### 2. Dataset Profiling

The application provides an overview of the uploaded dataset, including:

* Number of rows
* Number of columns
* Missing values
* Duplicate rows
* Numerical columns
* Categorical columns
* Unique values
* Data types

### 3. Statistical Analysis

Automatically generates statistical summaries for numerical columns, including:

* Count
* Mean
* Standard deviation
* Minimum
* Maximum
* Quartiles

### 4. Missing Value Analysis

The application identifies columns containing missing values and calculates the missing-value percentage.

### 5. Duplicate Detection

Automatically checks the dataset for duplicate records.

### 6. Automatic Data Visualizations

The application generates visualizations based on the dataset structure.

Supported visualizations include:

* Numerical distributions
* Categorical distributions
* Scatter plots
* Correlation heatmaps

The visualizations are generated using **Plotly**.

### 7. Automatic Data Insights

The system generates basic analytical observations such as:

* Dataset size
* Missing-value status
* Duplicate records
* Numerical column statistics
* Most frequent categorical values
* Strong numerical correlations

### 8. SQL Analysis

The uploaded Pandas DataFrame is converted into an in-memory **SQLite database**.

Users can execute SQL `SELECT` queries directly against the uploaded dataset.

Example:

```sql
SELECT *
FROM data
LIMIT 10;
```

### 9. Natural Language to SQL

The application allows users to ask questions using normal English.

Example:

```text
What is the average salary?
```

The Ollama LLM converts the question into SQL:

```sql
SELECT AVG(salary) AS average_salary
FROM data;
```

The generated SQL is then executed against the SQLite database.

### 10. Local LLM Integration

The project uses:

* Ollama
* Qwen 2.5 7B

The LLM runs locally rather than requiring a paid external API.

This allows the application to perform natural-language SQL generation using a locally hosted model.

### 11. SQL Safety

The SQL execution layer restricts queries to `SELECT` statements.

This prevents generated queries from performing operations such as:

```text
INSERT
UPDATE
DELETE
DROP
CREATE
ALTER
```

---

# System Workflow

```text
                ┌─────────────────────┐
                │   Upload Dataset    │
                │    CSV / Excel      │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Pandas Loading    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │  Data Profiling     │
                │  Statistics         │
                │  Missing Values     │
                │  Duplicates         │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Visualizations      │
                │ & Data Insights     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   SQLite Database   │
                └──────────┬──────────┘
                           │
                 ┌─────────┴─────────┐
                 │                   │
                 ▼                   ▼
        ┌────────────────┐   ┌─────────────────┐
        │ Manual SQL     │   │ Natural Language│
        │ Query          │   │ Question        │
        └───────┬────────┘   └────────┬────────┘
                │                     │
                │                     ▼
                │             ┌───────────────┐
                │             │ Ollama /      │
                │             │ Qwen 2.5 7B   │
                │             └───────┬───────┘
                │                     │
                │                     ▼
                │             ┌───────────────┐
                │             │ SQL Generation│
                │             └───────┬───────┘
                │                     │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ SQLite Execution    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Query Results       │
                │ in Streamlit        │
                └─────────────────────┘
```

---

# Technology Stack

| Technology   | Purpose                             |
| ------------ | ----------------------------------- |
| Python       | Core programming language           |
| Pandas       | Data loading and analysis           |
| NumPy        | Numerical operations                |
| SQLite       | SQL-based dataset analysis          |
| Plotly       | Interactive visualizations          |
| Streamlit    | Web application interface           |
| Ollama       | Local LLM execution                 |
| Qwen 2.5 7B  | Natural-language SQL generation     |
| Git & GitHub | Version control and project hosting |

---

# Project Structure

```text
AI-Powered-Data-Analysis-SQL-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── agent/
│   ├── __init__.py
│   ├── analysis_agent.py
│   ├── llm.py
│   └── prompts.py
│
├── utils/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── data_loader.py
│   ├── profiler.py
│   ├── sql_engine.py
│   └── visualization.py
│
├── data/
│
└── outputs/
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/khalid-shaik/AI-Powered-Data-Analysis-SQL-Assistant.git
```

Navigate to the project:

```bash
cd AI-Powered-Data-Analysis-SQL-Assistant
```

---

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, you can activate the environment using:

```powershell
.venv\Scripts\activate.bat
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Ollama Setup

This project uses Ollama to run the LLM locally.

Install Ollama on your system and download the Qwen 2.5 7B model:

```bash
ollama pull qwen2.5:7b
```

Verify that the model is available:

```bash
ollama list
```

You should see:

```text
qwen2.5:7b
```

---

# Run the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

# Example Usage

## Step 1 — Upload Dataset

Upload a CSV or Excel file through the Streamlit interface.

Example:

```text
customer_data.csv
```

---

## Step 2 — Explore the Dataset

The application automatically displays:

```text
Dataset Overview
Column Information
Numerical Statistics
Missing Value Analysis
Column Types
```

---

## Step 3 — View Visualizations

The application automatically generates relevant charts based on the available columns.

Examples:

```text
Salary Distribution
Customer Category Distribution
Age vs Salary
Correlation Heatmap
```

---

## Step 4 — Run SQL Queries

Users can manually enter SQL queries.

Example:

```sql
SELECT COUNT(*) AS total_customers
FROM data;
```

Another example:

```sql
SELECT AVG(balance) AS average_balance
FROM data;
```

---

# Natural Language SQL

The AI section allows users to ask questions without writing SQL.

### User Question

```text
What is the average salary?
```

### LLM Generated SQL

```sql
SELECT AVG(salary) AS average_salary
FROM data;
```

### Result

The application executes the generated SQL against the uploaded dataset and displays the result in Streamlit.

---

# Example Questions

The following types of questions can be asked:

```text
What is the average salary?
```

```text
What is the maximum balance?
```

```text
How many customers are there?
```

```text
What is the total revenue?
```

```text
What is the average transaction amount?
```

```text
How many records are in the dataset?
```

The generated SQL depends on the columns available in the uploaded dataset.

---

# SQL Security

The project includes a basic SQL safety mechanism.

Only queries beginning with:

```sql
SELECT
```

are allowed to execute.

Queries that attempt to modify the database are rejected.

For example, the following operations are not allowed:

```sql
DELETE
```

```sql
UPDATE
```

```sql
INSERT
```

```sql
DROP
```

```sql
ALTER
```

This provides a basic protection layer for LLM-generated SQL.

---

# Application Architecture

The project separates responsibilities into different modules.

### `app.py`

Responsible for:

* Streamlit interface
* File upload
* User interaction
* Displaying analysis results
* Connecting all project components

### `utils/profiler.py`

Responsible for:

* Dataset summary
* Column information
* Statistical analysis
* Missing-value analysis

### `utils/visualization.py`

Responsible for:

* Histograms
* Bar charts
* Scatter plots
* Correlation heatmaps

### `utils/analyzer.py`

Responsible for:

* Automatic dataset insights
* Numerical observations
* Categorical observations
* Correlation analysis

### `utils/sql_engine.py`

Responsible for:

* Creating SQLite database
* Loading DataFrame into SQLite
* Executing SQL queries
* Retrieving table schema
* Restricting execution to SELECT queries

### `agent/llm.py`

Responsible for:

* Connecting the application to Ollama
* Sending prompts to the local Qwen model
* Receiving LLM responses

### `agent/prompts.py`

Responsible for:

* Constructing the Natural Language → SQL prompt
* Providing database schema to the LLM
* Defining SQL generation rules

### `agent/analysis_agent.py`

Responsible for:

* Connecting the prompt system with the LLM
* Generating SQL from user questions
* Cleaning the generated SQL response

---

# Project Highlights

* Automated exploratory data analysis
* Interactive Streamlit dashboard
* Pandas-based data processing
* SQLite-based SQL analysis
* Natural-language SQL generation
* Local LLM integration using Ollama
* Qwen 2.5 7B model integration
* Automated data visualizations
* Missing-value and duplicate analysis
* Basic SQL execution safety

---

# Future Enhancements

Possible improvements include:

* AI-generated explanations of query results
* Advanced data-cleaning recommendations
* SQL query validation
* Conversation memory
* Follow-up questions
* Multi-step analytical agents
* Advanced anomaly detection
* Automated report generation
* Deployment to a cloud environment
* Support for larger datasets
* More advanced LLM tool-calling workflows

---

# Learning Outcomes

This project demonstrates practical experience with:

* Data Analysis
* Python
* Pandas
* SQL
* SQLite
* Data Visualization
* Streamlit
* LLM Integration
* Prompt Engineering
* Natural Language Processing
* Git and GitHub
* Modular Python Development

---

# Author

**Shaik Khalid**

GitHub:
https://github.com/khalid-shaik

```

**One correction before you publish:** your README should describe the project as using **Qwen 2.5 7B through Ollama locally**, not as a cloud AI service. That accurately reflects what you built and also makes the project reproducible for someone cloning the repository.
```
