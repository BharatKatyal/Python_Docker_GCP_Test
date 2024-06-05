# Dockerize a Python web app

## 1. Create the app locally 

```console
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install fastapi uvicorn
```

Try it:

```console

uvicorn main:app --reload
```




####### END


```console
$ uvicorn app.main:app --port 80
```

Save dependencies:

```console
$ pip freeze > requirements.txt
```

## 2. Build the Docker image

```console
$ docker build -t docker-image-test . 
```

Note that we use a `.dockerignore` file to ignore certain files/folders.

## 3. Run the Docker image

Normal:

```console
$ docker run -p 80:80 docker-image-test . 
```

Run in background and give a name:

```console
$ docker run -d --name myfastapicontainer -p 80:80 fastapi-image
```

`-p 80:80`: Map the port from outside to the port from the container

Host in Dockerfile must be:

`host: 0.0.0.0`: "placeholder", it tells a server to listen for and accept connections from any IP address ("all IPv4 addresses on the local machine").
# Python_Docker
# Google_Submission
# Google_Submission



docker build -t gctest .

cloud builds submit --region=us-central1 --tag us-central1-docker.pkg.dev/bk-ml-commons-test/bk-mlcommons-opensource/bktest-image:v1



docker logs <CONTAINER_ID>

docker build -t sample-container .

docker run -d -p 5000:5000 --env-file .env  sample-container


docker build -t order-processor .


docker run -v $(pwd)/orders.csv:/app/orders.csv gctest /app/orders.csv 2024-01-01 2024-03-31 submission123



gcloud artifacts repositories create bk-mlcommons-opensource --repository-format-docker --location=us-central1 --description="docker test container gcp"

gcloud artifacts repositories create bk-mlcommons-opensource --repository-format=docker --location=us-central1 --description="docker test container gcp"


gcloud builds submit --region=us-central1 --tag us-central1-docker.pkg.dev/bk-ml-commons-test/bk-mlcommons-opensource/bktest-image:v1

gcloud run deploy --image=us-central1-docker.pkg.dev/bk-ml-commons-test/bk-mlcommons-opensource/bktest-image:v1


gcloud builds submit --region=us-central1 --tag us-central1-docker.pkg.dev/bk-ml-commons-test/bk-mlcommons-opensource/bktest-image:v2

gcloud run deploy --image=us-central1-docker.pkg.dev/bk-ml-commons-test/bk-mlcommons-opensource/bktest-image:v2


Working Command
docker run -v $(pwd)/orders.csv:/app/orders.csv gctest python process_orders.py /app/orders.csv 2024-01-01 2024-03-31 submission123
# Python_Docker_GCP_Test
# Python_Docker_GCP_Test
