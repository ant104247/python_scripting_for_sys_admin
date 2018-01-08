#!/usr/bin/python

import os

# stage = os.environ["STAGE"].upper()
stage = (os.getenv("STAGE") or "developement").upper()

output = "We're running is %s" %  stage

if stage.startswith("PROD"):
	output = "Danger !!! - " + output

print(output)