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

### Option 1: Using SQL commands in pgAdmin or psql

```
-- Create the user
CREATE USER ev_data_user WITH PASSWORD 'ev_password';

-- Create the database with the user as owner
CREATE DATABASE ev_data WITH OWNER ev_data_user;
```

After connecting to the ev_data database, you may need to run:

```
GRANT ALL ON SCHEMA public TO ev_data_user;
```

### Option 2: Using command line

```
# Create user (interactive password prompt)
createuser --pwprompt ev_data_user
# When prompted, enter 'ev_password' as the password

# Create database with owner
createdb --owner=ev_data_user ev_data
```

## **6. Load data into PostgreSQL**

From the scripts folder, execute:

```
python scripts/load_to_postgres.py
```
