#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME="sample_deployment_image"
CONTAINER_NAME="sample_deployment_container"
PORT_HOST="5555"
PORT_CONTAINER="5555"
LOG_FILE="sample_deploy_log.txt"

echo "=== J1 Lab 6.3.6 Deploy Script ===" | tee "$LOG_FILE"
date | tee -a "$LOG_FILE"
echo "PWD: $(pwd)" | tee -a "$LOG_FILE"
echo | tee -a "$LOG_FILE"

echo "[1] Build image: $IMAGE_NAME" | tee -a "$LOG_FILE"
docker build -t "$IMAGE_NAME" . | tee -a "$LOG_FILE"

echo | tee -a "$LOG_FILE"
echo "[2] Run container: $CONTAINER_NAME" | tee -a "$LOG_FILE"

# Stop & remove als hij al bestaat
docker container rm -f "$CONTAINER_NAME" >/dev/null 2>&1 || true

docker run -d --rm \
  -p "${PORT_HOST}:${PORT_CONTAINER}" \
  --name "$CONTAINER_NAME" \
  "$IMAGE_NAME" | tee -a "$LOG_FILE"

echo | tee -a "$LOG_FILE"
echo "[3] Wait a moment for app to start..." | tee -a "$LOG_FILE"
sleep 2

echo "[4] Test endpoints" | tee -a "$LOG_FILE"
curl -sS "http://127.0.0.1:${PORT_HOST}/health" | tee -a "$LOG_FILE"
echo | tee -a "$LOG_FILE"
curl -sS "http://127.0.0.1:${PORT_HOST}/" | head -n 5 | tee -a "$LOG_FILE"
echo | tee -a "$LOG_FILE"

echo "[5] Gather info (image + container)" | tee -a "$LOG_FILE"
docker image ls | grep "$IMAGE_NAME" | tee -a "$LOG_FILE" || true
docker ps | grep "$CONTAINER_NAME" | tee -a "$LOG_FILE" || true
docker inspect "$CONTAINER_NAME" | head -n 40 | tee -a "$LOG_FILE"

echo | tee -a "$LOG_FILE"
echo "[6] Cleanup container + image" | tee -a "$LOG_FILE"
docker container stop "$CONTAINER_NAME" >/dev/null 2>&1 || true
docker image rm "$IMAGE_NAME" >/dev/null 2>&1 || true

echo "DONE. Log saved to: $LOG_FILE" | tee -a "$LOG_FILE"
