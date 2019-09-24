Project to test mailjet usage from a docker container (runned on a Kubernetes cluster)

# Setup

```bash
mkvirtualenv mailjet3 -p python3.7
# pip install mailjet_rest
pip install -r requirements.txt
```

# Build and push image on docker hub

```bash
docker build . -t kristoyoyo/mailjet-sender:[tagname]
docker image push kristoyoyo/mailjet-sender:[tagname]
```

# Deploy on a Kubernetes cluster

## Create pod manifest

```bash
export API_KEY=xxx
export API_SECRET=xxx
export FROM=me@mycompany
export TO=me@mycompany
cat test-pod-mailjet-manifest.yml | envsubt > test-pod-mailjet.yml 
```

## Create pod on Kubernetes

```bash
kubectl apply -f test-pod-mailjet.yml
```

## Create SSH tunnel with pod to get access to pod on locahost

```bash
kubectl port-forward po/test-mail 2500:25
```

Note : keep that session opened and follow this instruction on another terminal session.

## Test to send a mail with nc command

```bash
nc 127.0.0.1 2500
HELO MOTO
MAIL FROM:<me@mycompany>
RCPT TO:<to@mycompany>
DATA
Date: Thu, 21 May 2016 05:33:29 -0700
From: YOHAN<me@mycompany>
Subject: Mail sent from a pod in Kubernetes
To: to@mycompany
Hello, this is just a mail sent from test-mail pod on Kubernetes cluster. It confirm network config is OK.
.
```
