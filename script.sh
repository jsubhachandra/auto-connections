#!/usr/bin/env bash
source /home/pi/daily-automation/env/bin/activate && python /home/pi/daily-automation/main.py && curl https://hc-ping.com/03e6994d-c67f-48f4-bd55-d57ff8ff60bb > /dev/null
