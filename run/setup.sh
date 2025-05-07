#!/bin/bash

# ------------------------------------------------------------------------------
# Prompt for Credentials
read -p "Enter DB_USERNAME: " DB_USERNAME
read -s -p "Enter DB_PASSWORD: " DB_PASSWORD
echo ""  # Move to the next line after password input

# Get the directory where this script is located (which is also where docker-compose.yaml is)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$SCRIPT_DIR/.."

# ------------------------------------------------------------------------------
# Let's create the .env file for the test environment
file_env="$PROJECT_ROOT/.env"
if [ ! -f "$file_env" ]; then
    cat > "$file_env" <<EOF
DB_USERNAME=$DB_USERNAME
DB_PASSWORD=$DB_PASSWORD
DB_HOST=localhost
DB_PORT=5432
DB_NAME=gap_python_ai_workshop_dev
EOF

    echo ".env created successfully."
else
    echo ".env already exists. No action taken."
fi

# ------------------------------------------------------------------------------
# Let's create the tests/.env file for the test environment
file_test_env="$PROJECT_ROOT/tests/.env"
if [ ! -f "$file_test_env" ]; then
    cat > "$file_test_env" <<EOF
DB_USERNAME=$DB_USERNAME
DB_PASSWORD=$DB_PASSWORD
DB_HOST=localhost
DB_PORT=5432
DB_NAME=gap_python_ai_workshop_test
EOF

    echo "tests/.env created successfully."
else
    echo "tests/.env already exists. No action taken."
fi

# ------------------------------------------------------------------------------
# Install the requirements
pip install -r "$PROJECT_ROOT/requirements.txt"

# ------------------------------------------------------------------------------
# Set up the test database
DB_USERNAME=$DB_USERNAME DB_PASSWORD=$DB_PASSWORD "$SCRIPT_DIR/db-test-up.sh"

# ------------------------------------------------------------------------------
# Final message
echo "Setup complete. Execute pytest to run the tests."

