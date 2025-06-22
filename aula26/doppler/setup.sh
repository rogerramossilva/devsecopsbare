#!/bin/bash
curl -sLf --retry 3 --retry-delay 2 https://cli.doppler.com/install.sh | sh
doppler login
