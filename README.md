# UOCIS322 - Project 4 #
Brevet time calculator.

## Overview

Provides a lightweight webserver for a RUSA ACP controle time calculator with flask and ajax.

## Webpage

Contains a table of with columns for distance, location, and opening/closing times for each controle.
Entering data into the distance columns will autofill the opening and closing times for that controle.

## Breakdown

- app.ini: Provides a fallback configuration file.
- credentials-skel.ini: Provides a template credentials config file for the serverhost to fill out.
- flask_brevets.py: Contains the bulk of the code for the webserver.
- src/acp_times.py: Contains the algorythm for calculating ACP Controle times.
- src/config.py: Contains the configuration parsing algorythm.
- templates/...: Contains the website page templates.

### ACP controle times

That's *"controle"* with an *e*, because it's French, although "control" is also accepted. Controls are points where a rider must obtain proof of passage, and control[e] times are the minimum and maximum times by which the rider must arrive at the location.

The algorithm for calculating controle times is described here [https://rusa.org/pages/acp-brevet-control-times-calculator](https://rusa.org/pages/acp-brevet-control-times-calculator). Additional background information is given here [https://rusa.org/pages/rulesForRiders](https://rusa.org/pages/rulesForRiders). The description is ambiguous, but the examples help. Part of finishing this project is clarifying anything that is not clear about the requirements, and documenting it clearly.  

We are essentially replacing the calculator here [https://rusa.org/octime_acp.html](https://rusa.org/octime_acp.html). We can also use that calculator to clarify requirements and develop test data.  

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.
