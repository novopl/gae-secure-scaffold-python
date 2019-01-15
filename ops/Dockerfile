FROM google/cloud-sdk:alpine

WORKDIR /app

# Copy pelconf.yaml so we can detect all devrequirements for peltak commands -
# `peltak devrequirements` output will always depend on the current
# configuration.
ADD pelconf.yaml /app/pelconf.yaml

RUN \
    gcloud components install app-engine-python app-engine-python-extras; \
    python -m ensurepip; \
    pip install "peltak~=0.24.5"; \
    pip install unittest2 $(peltak devrequirements);

CMD dev_appserver.py /app
