docker-compose -f local.yml run django pip list --outdated --format=columns > output\outdated3.txt
echo "Wrote file to output\outdated3.txt"
