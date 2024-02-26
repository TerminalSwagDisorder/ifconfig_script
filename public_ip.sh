#!/bin/bash

# Function to get the public IP address
get_public_ip() {
    curl -s --max-time 10 https://ifconfig.me
}

# Main loop
previous_ip=""
while true; do
    current_ip=$(get_public_ip)
    exit_status=$?

    if [ $exit_status -ne 0 ]; then
        echo "No connection"
        previous_ip=""
    else
        if [ "$current_ip" != "$previous_ip" ]; then
            echo "$current_ip"
            previous_ip=$current_ip
        # else
            # echo "$current_ip"
        fi
    fi

    sleep 360
done
