# Building

```bash
docker build -t <YOUR_DOCKER_REGISTRY>/healthcheckerclientpy:latest .

e.g.
docker build -t bonsaro.azurecr.io/healthcheckerclientpy:latest .
```

# Pushing

```bash
docker push <YOUR_DOCKER_REGISTRY>/healthcheckerclientpy:latest

e.g.
docker push bonsaro.azurecr.io/healthcheckerclientpy:latest
```

# Deploying

```bash
helm install healthcheckerclientpy ./charts --set image.repository=<YOUR_DOCKER_REGISTRY>/healthcheckerclientpy --set image.tag=latest

e.g.
helm install healthcheckerclientpy ./charts --set image.repository=bonsaro.azurecr.io/healthcheckerclientpy --set image.tag=latest
```