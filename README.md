# microservices

This project contains simple microservice app, which deployed in kubernetes cluster with helm and helmfile. 

## Diagram

![web app scheme](/diagrams/microservices.png)


---
## Usage

set variables

| Name                   | Description                    | Example                                  |
| ---------------------- | ------------------------------ | ---------------------------------------- |
| CI_REGISTRY_USER       | your container registry login  | user                                     |
| CI_REGISTRY_TOKEN      | your container registry token  | eW91ciBrdWJlY29uZmlnIGluIGJhc2U2NAo..... |
| KUBE_CONFIG            | kubeconfig in base64           | eW91ciBrdWJlY29uZmlnIGluIGJhc2U2NAo..... |
| GRAFANA_TOKEN          | grafana api key token          | eW91ciBrdWJlY29uZmlnIGluIGJhc2U2NAo..... |
| GRAFANA_DNS_NAME       | grafana dns name (FQDN )       | grafana.example.com                      |     


### For running microservices on local machine

```
docker-compose up -d --build
```

---
## Installation

* docker - [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)
* helm - [https://helm.sh/docs/intro/install/](https://helm.sh/docs/intro/install/).
* helmfile - [https://github.com/roboll/helmfile](https://github.com/roboll/helmfile).

## License
[MIT](https://choosealicense.com/licenses/mit/)