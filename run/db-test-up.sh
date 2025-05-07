#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$SCRIPT_DIR/.."

# Navigate to the bin directory (where docker-compose.yaml and Dockerfile are)
cd "$SCRIPT_DIR" || { echo "Failed to change directory to $SCRIPT_DIR"; exit 1; }
DB_NAME="gap_python_ai_workshop_test" DB_USERNAME=$DB_USERNAME DB_PASSWORD=$DB_PASSWORD docker-compose up -d
cd "$PROJECT_ROOT" || { echo "Failed to change directory to $PROJECT_ROOT"; exit 1; }

