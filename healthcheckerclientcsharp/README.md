# Building

```bash
docker build -t <YOUR_DOCKER_REGISTRY>/healthcheckerclientcsharp:latest .

e.g.
docker build -t bonsaro.azurecr.io/healthcheckerclientcsharp:latest .
```

# Pushing

```bash
docker push <YOUR_DOCKER_REGISTRY>/healthcheckerclientcsharp:latest

e.g.
docker push bonsaro.azurecr.io/healthcheckerclientcsharp:latest
```

# Deploying

```bash
helm install healthcheckerclientcsharp ./charts --set image.repository=<YOUR_DOCKER_REGISTRY>/healthcheckerclientcsharp --set image.tag=latest

e.g.
helm install healthcheckerclientcsharp ./charts --set image.repository=bonsaro.azurecr.io/healthcheckerclientcsharp --set image.tag=latest
```