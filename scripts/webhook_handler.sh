#!/bin/sh


# Function to check if TruffleHog is installed
check_trufflehog() {
  if ! command -v trufflehog &>/dev/null; then
    echo "TruffleHog not found. Installing TruffleHog..."
    pip install trufflehog
  fi
}

# Check for TruffleHog installation
check_trufflehog

# Check if the cloned repository directory already exists
if [ -d /testsec ]; then
  echo "Inside the if condition block"
  # Directory exists, so delete it
  rm -rf /testsec
fi

trufflehog git https://github.com/riddhi150390/testsec.git --json > scan_results.json 
chmod 777 scan_results.json


