#!/bin/bash
# Takes in a URL, sends a GET request to the URL, displays the body of the response
curl -sX GET 0.0.0.0:5000/route_1 -L 200; echo ""
