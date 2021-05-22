#!/bin/sh

docker-compose down
rm -rf .env clef.sh deploy.sh docker-compose.yaml tearsheet.txt prometheus/prometheus.yml monBee.err monBee.sh

echo "The hive data directory has not been removed."
