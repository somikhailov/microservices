# microservices

![Build status](https://github.com/somikhailov/microservices/actions/workflows/main.yml/badge.svg?branch=main)

This project contains simple microservice app, which deployed in kubernetes cluster with helm and helmfile. 

## Diagram

![web app scheme](/diagrams/microservices.png)


---
## Usage

set variables

| Name                   | Description          | Example                                  |
| ---------------------- | -------------------- | ---------------------------------------- |
| DOCKER_USERNAME        | your docker login    | user                                     |
| DOCKER_PASSWORD        | your docker password | strongP@ssw0rd                           |
| KUBE_CONFIG_BASE64_DATA| kubeconfig in base64 | eW91ciBrdWJlY29uZmlnIGluIGJhc2U2NAo..... |


### For running local pipeline

> for local running variables stores in `.secrets`

```bash
act
```

for running job 
```bash
act -j deploy
```

### For running microservices on local machine

```
docker-compose up -d --build
```

---
## Installation

* docker - [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)
* helm - [https://helm.sh/docs/intro/install/](https://helm.sh/docs/intro/install/).
* helmfile - [https://github.com/roboll/helmfile](https://github.com/roboll/helmfile).
* act - [https://github.com/nektos/act](https://github.com/nektos/act).

## License
[MIT](https://choosealicense.com/licenses/mit/)