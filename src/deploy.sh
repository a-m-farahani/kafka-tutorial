#!/bin/bash

echo "pull confluent kafka image from docker hub..."
docker pull confluentinc/cp-kafka:7.5.0

echo "pull confluent kafka-connect image from docker hub..."
docker pull confluentinc/cp-kafka-connect:7.5.0

docker compose -f kafka-compose.yaml up -d

