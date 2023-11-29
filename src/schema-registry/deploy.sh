#!/bin/bash

echo "pull confluent kafka image from docker hub..."
docker pull confluentinc/cp-kafka:7.5.0

echo "Pull confluent schema-registry"
docker pull confluentinc/cp-schema-registry:7.5.0

docker compose -f compose.yaml up -d



