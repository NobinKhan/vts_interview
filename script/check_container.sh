#!/bin/bash

set -e

DOCKER_SERVICES=$(docker compose ps -a --services)

while read -r service_name; do
  # Perform actions for each service (e.g., restart)
  CONTAINER_STATUS=$(docker inspect --format={{.State.Status}} $service_name)
  if [[ "$CONTAINER_STATUS" == "running" ]]; then
    echo "Container '$service_name' is running."
  else
    echo "Container '$service_name' is not running."
    exit 1
  fi
done <<< "$DOCKER_SERVICES"
