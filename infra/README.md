## Installing on KinD

### Prerequisites
- Helm version 3.8.0 or later 

```shell
./infra/kind-deploy.sh
```

## Connect to Superset Dashboard UI

```shell
kubectl port-forward service/superset 8088:8088 --namespace superset
# Open http://127.0.0.1:8088/
```
