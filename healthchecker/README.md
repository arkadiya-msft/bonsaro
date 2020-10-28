# Building

```bash
docker build -t <YOUR_DOCKER_REGISTRY>/healthchecker:latest .

e.g.
docker build -t bonsaro.azurecr.io/healthchecker:latest .
```

# Pushing

```bash
docker push <YOUR_DOCKER_REGISTRY>/healthchecker:latest

e.g.
docker push bonsaro.azurecr.io/healthchecker:latest
```

# Deploying

```bash
helm install healthchecker ./charts --set image.repository=<YOUR_DOCKER_REGISTRY>/healthchecker --set image.tag=latest

e.g.
helm install healthchecker ./charts --set image.repository=bonsaro.azurecr.io/healthchecker --set image.tag=latest
```