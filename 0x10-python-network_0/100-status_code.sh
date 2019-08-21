#!/bin/bash
# sends a request to a URL passed as an argument and displays only the status code response
curl -sI "$1" | grep HTTP/1.0| cut -d " " -f2
