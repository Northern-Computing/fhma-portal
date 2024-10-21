## FHMA Portal

## Install

#### Spin up postgres container with basic configuration

```bash
docker run --name fhma-portal -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=fhma-portal -p 127.0.0.1:5433:5432 -d postgres
```

### Create python virtual environment

```bash
python3 -m venv venv
```

### Activate virtual environment

```bash
source venv/bin/activate
```

### Source the environment variables

```bash
export $(grep -v '^#' .env | xargs)
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python manage.py runserver
```

## How to create a django app

```bash
python manage.py startapp <app_name>
```

Then add the app to the installed apps in the settings.py file

```python
INSTALLED_APPS = [
    ...
    '<app_name>',
]
```
