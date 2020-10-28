# Building

```bash
docker build -t bonsaidev.azurecr.io/bonsai/health_checker:dev .
```

# Running Locally

```bash
docker run -d --name health_checker bonsaidev.azurecr.io/bonsai/health_checker:dev <address>
```

# Deploying

```bash
helm install healthcheckerpy ./health_checker --set target_address=<address>
```
