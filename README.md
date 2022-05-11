# CultObj

Project started: http://127.0.0.1:8008

## Install
#### 0. Create .env

Rename EXAMPLE.env to .env and change example-data.

#### 1. Install docker and docker-compose

If you have docker и docker-compose, use next step. Else: use official [docs](https://docs.docker.com/engine/install/).

#### 2. Build Docker container
```bash
docker-compose build
```
#### 3. Run Docker container
```bash
docker-compose up
```
### 4. Stop Docker container
```bash
docker-compose down
```

## Use

### Run
```bash
sudo docker-compose exec web bash
```

#### 1. Create migrations
```bash
python manage.py makemigrations main
```

#### 2. Migrate
```bash
python manage.py migrate
```

#### 3. Create Superuser Django
```bash
python manage.py createsuperuser
```

#### 4. Initial start-data:
```bash
python manage.py load_init_data
```

#### 5. Include static file
```bash
python manage.py collectstatic
```
