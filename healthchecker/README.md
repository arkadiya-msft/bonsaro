# Building

```bash
docker build -t bonsaro.azurecr.io/healthchecker:latest .
```

# Deploying

```bash
helm install healthchecker ./charts
```