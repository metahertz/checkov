FROM python:3.7-alpine

RUN apk update && apk add --no-cache git util-linux bash 

RUN pip install --no-cache-dir -U checkov
RUN wget -q -O get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
RUN chmod 700 get_helm.sh
RUN VERIFY_CHECKSUM=false ./get_helm.sh

COPY ./github_action_resources/entrypoint.sh /entrypoint.sh
COPY ./github_action_resources/checkov-problem-matcher.json /usr/local/lib/checkov-problem-matcher.json
COPY ./github_action_resources/checkov-problem-matcher-softfail.json /usr/local/lib/checkov-problem-matcher-softfail.json

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
