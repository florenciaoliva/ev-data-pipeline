## **0. Make sure you have the following installed on your system:**

Python 3.8+,
PostgreSQL,
Power BI Desktop,
Git

## **1. Clone the repository**

```
git clone https://github.com/florenciaoliva/ev-data-pipeline.git
```

```
cd ev-data-pipeline
```

## **2. Create a virtual environment**

On Windows:

```
python -m venv venv
```

```
venv\Scripts\activate
```

On macOS/Linux:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

## **3. Install project dependencies**

```
pip install -r requirements.txt
```

## **4. Run the analysis and cleaning scripts**


Execute the following scripts:

```
python scripts/explore_dataset.py
```

```
python scripts/clean.py
```

## **5. Create the database in PostgreSQL**

Ensure that PostgreSQL is installed and the service is running.

Run:
```
psql -U postgres -f sql/setup_database.sql
```

## **6. Load data into PostgreSQL**

Run:

```
python scripts/load_to_postgres.py
```
