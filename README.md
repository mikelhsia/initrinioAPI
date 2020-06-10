## 0. Prep
1. Anaconda or pure pip
2. Libraries:
   1. python 3.5
   2. numpy
   3. pandas
   4. intrinio-sdk 

## 1. Setup DB
### 1.1. Change DB config file
I'm using **mysql** here in local machine.

`vi setup_db_environment.yaml`

```javascript
HOST: 127.0.0.1
DATABASE: Your_DB_NAME
USER: Your_USERNAME
PASSWORD: Your_PASSWORD
PORT: Your_PORT
```


### 1.2. Create database
```
python3 create_db_database.py
```

## 2. Config the setup file
### 2.1. Register/login to get your intrinio account

`https://intrinio.com/`

### 2.2. Config your intrinio setup file
`vi setup_intrinio_environment.yaml`

```javascript
PRODUCTION_API_KEY: 'Production Key'
SANDBOX_API_KEY: 'Sandbox Key'
USE_PRODUCTION: FALSE
```


## 3. Start importing pricing data

`python3 main.py`