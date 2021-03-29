#!/usr/bin/env bash

images=(
    'quay.io/guanwang/logger:v1.4'
)
for image in ${images[@]}; do
    docker build -t "$image" .
    docker push "$image"
done
