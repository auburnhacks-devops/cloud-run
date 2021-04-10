# Cloud Run Hello World Sample

This sample shows how to deploy a Hello World application to Cloud Run.

[![Run in Google Cloud][run_img]][run_link]

[run_img]: https://storage.googleapis.com/cloudrun/button.svg
[run_link]: https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=https://github.com/GoogleCloudPlatform/python-docs-samples&cloudshell_working_dir=run/allneeded

## Build

```
docker build --tag allneeded:python .
```

## Run Locally

```
docker run --rm -p 9090:8080 -e PORT=8080 allneeded:python
```

## Test

```
pytest
```

_Note: you may need to install `pytest` using `pip install pytest`._

## Deploy

```sh
# Set an environment variable with your GCP Project ID
export GOOGLE_CLOUD_PROJECT=<PROJECT_ID>

# Submit a build using Google Cloud Build
gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/allneeded

# Deploy to Cloud Run
gcloud run deploy allneeded \
--image gcr.io/${GOOGLE_CLOUD_PROJECT}/allneeded
```


For more details on how to work with this sample read the [Python Cloud Run Samples README](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/run)
