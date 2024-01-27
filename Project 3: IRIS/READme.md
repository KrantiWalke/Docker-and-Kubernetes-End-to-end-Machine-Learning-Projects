# IMP commands:

1. Writing the Docker File (Dockerfile.txt)
2. Building the docker Image:

In CMD:

$docker build -t gliris .  (do not forget "." for local dir)

-> Note:see the dockers
$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                           NAMES
d1442c19c708   gltest    "flask run --host=0.…"   4 hours ago      Up 4 hours      0.0.0.0:8111->8111/tcp          zen_franklin

$docker images
REPOSITORY               TAG       IMAGE ID       CREATED         SIZE
gltest                   latest    e6a26378dc4e   3 hours ago     1.41GB
gliris                   latest    643d08d10ae2   3 hours ago     1.43GB

3. Running our app
-> running the dockers:
$docker run -p 3456:80 gliris

 docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                           NAMES
180495ead6cc   gliris    "/entrypoint.sh /sta…"   32 minutes ago   Up 32 minutes   443/tcp, 0.0.0.0:3456->80/tcp   sharp_volhard
d1442c19c708   gltest    "flask run --host=0.…"   4 hours ago      Up 4 hours      0.0.0.0:8111->8111/tcp          zen_franklin

# Check if it is working:
on: http://localhost:3456/isAlive
Should show "true"

To check prediction:
$ curl -X POST http://localhost:3456/predict -H "Content-Type: application/json" -d '[8.9,7.0,7.1,7.8]'

# For GCP:

$docker tag gliris gcr.io/iris123-412522/gliris

$gcloud docker push gcr.io/iris123-412522/gliris
OR
$docker push gcr.io/iris123-412522/gliris


1. Open Google Cloud Console
2. Create new Project (e.g iris123)
3. Check the image loaded in container Registry (e.g gliris)
4. Open Kubernetes Engine -> Kubernetes clusters -> deploy ->  in New container select Existing container image -> give image path (e.g gliris) -> Continue for Configuration -> Continue for Expose (optional)

5. Check prediction on external server: My Load Balancer IP-> 35.239.142.220

$curl -X POST 35.239.142.220:80/predict -H "Content-Type: application/json" -d '[8.9,7.0,7.1,7.8]'
