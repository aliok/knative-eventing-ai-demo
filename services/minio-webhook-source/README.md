# Pre-requisites
This service gets events from Minio, converts them to CloudEvents and pushes them to the given sink.

# Running locally

Setup virtual environment:
```shell
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:
```shell
pip install -r requirements.txt
```

Run:
```shell
K_SINK="https://webhook.site/48cdb072-bcf8-470e-8746-90ac76415316" \
POD_NAME="my-pod" \
POD_NAMESPACE="my-namespace" \
flask --app func --debug run
```

Test:
```shell
curl localhost:5000 -i -X POST -H "Content-Type: application/json" -d '{"EventName":"s3:ObjectCreated:Put","Key":"ai-demo/service.yaml","Records":[{"eventVersion":"2.0","eventSource":"minio:s3","awsRegion":"","eventTime":"2023-09-26T09:38:47.702Z","eventName":"s3:ObjectCreated:Put","userIdentity":{"principalId":"minio"},"requestParameters":{"principalId":"minio","region":"","sourceIPAddress":"[::1]"},"responseElements":{"x-amz-id-2":"dd9025bab4ad464b049177c95eb6ebf374d3b3fd1af9251148b658df7ac2e3e8","x-amz-request-id":"178869619B8B3C05","x-minio-deployment-id":"639f7c63-1965-4710-b8fe-e6b1b47e2e09","x-minio-origin-endpoint":"https://minio.minio-operator.svc.cluster.local"},"s3":{"s3SchemaVersion":"1.0","configurationId":"Config","bucket":{"name":"ai-demo","ownerIdentity":{"principalId":"minio"},"arn":"arn:aws:s3:::ai-demo"},"object":{"key":"service.yaml","size":576,"eTag":"702314f405adeaa9aa042985692cd49e","contentType":"text/yaml","userMetadata":{"content-type":"text/yaml"},"sequencer":"178869619ED32F87"}},"source":{"host":"[::1]","port":"","userAgent":"MinIO (linux; amd64) minio-go/v7.0.63 mc/DEVELOPMENT.GOGET"}}]}'
```

See the outcome at https://webhook.site/#!/48cdb072-bcf8-470e-8746-90ac76415316/9f30a497-8b43-49a9-8f4b-25f1a2366bfe/1

# Running with Docker

Set your Docker repo override:
```shell
export DOCKER_REPO_OVERRIDE=docker.io/aliok
```


Build the image:
```shell
docker build . -t ${DOCKER_REPO_OVERRIDE}/minio-webhook-service
```

Run the image:
```shell
docker run --rm \
-p 5000:5000 \
-e K_SINK="https://webhook.site/48cdb072-bcf8-470e-8746-90ac76415316" \
-e POD_NAME="my-pod" \
-e POD_NAMESPACE="my-namespace" \
${DOCKER_REPO_OVERRIDE}/minio-webhook-service
```

Test:
```shell
curl localhost:5000 -i -X POST -H "Content-Type: application/json" -d '{"EventName":"s3:ObjectCreated:Put","Key":"ai-demo/service.yaml","Records":[{"eventVersion":"2.0","eventSource":"minio:s3","awsRegion":"","eventTime":"2023-09-26T09:38:47.702Z","eventName":"s3:ObjectCreated:Put","userIdentity":{"principalId":"minio"},"requestParameters":{"principalId":"minio","region":"","sourceIPAddress":"[::1]"},"responseElements":{"x-amz-id-2":"dd9025bab4ad464b049177c95eb6ebf374d3b3fd1af9251148b658df7ac2e3e8","x-amz-request-id":"178869619B8B3C05","x-minio-deployment-id":"639f7c63-1965-4710-b8fe-e6b1b47e2e09","x-minio-origin-endpoint":"https://minio.minio-operator.svc.cluster.local"},"s3":{"s3SchemaVersion":"1.0","configurationId":"Config","bucket":{"name":"ai-demo","ownerIdentity":{"principalId":"minio"},"arn":"arn:aws:s3:::ai-demo"},"object":{"key":"service.yaml","size":576,"eTag":"702314f405adeaa9aa042985692cd49e","contentType":"text/yaml","userMetadata":{"content-type":"text/yaml"},"sequencer":"178869619ED32F87"}},"source":{"host":"[::1]","port":"","userAgent":"MinIO (linux; amd64) minio-go/v7.0.63 mc/DEVELOPMENT.GOGET"}}]}'
```

See the outcome at https://webhook.site/#!/48cdb072-bcf8-470e-8746-90ac76415316/9f30a497-8b43-49a9-8f4b-25f1a2366bfe/1
