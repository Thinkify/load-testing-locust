# Load Testing Framework Using Locust

## Setup
Locust is supported on Python 3.6, 3.7 and 3.8.

1. Clone the repo and change directory to project root.

        git clone https://github.com/Thinkify/load_testing_locust.git && cd load_testing_locust

2. Run:

        ./setup.sh

    This takes care of creating a virtualenv, installing all requirements and setting up pre-commit hooks.

## Usage

#### Web UI
Run `locust` command from project root. The web interface should start at localhost:8089. 
Open this page in a browser and specify number of users, hatch rate and host name before starting the test.

#### Command Line
Run the following command to start locust without the web UI:
    
    locust --host <hostname> -u <number of total users> -r <hatch rate> -t <run time> --headless

For more options, use `locust --help`
