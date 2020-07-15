# Load Testing Framework Using Locust

## Setup
Locust is supported on Python 3.6, 3.7 and 3.8.

1. Clone the repo.

        cd load_testing_locust

2. If using virtualenv(recommended):

        virtualenv .env && source .env/bin/activate && pip3 install -r requirements.txt

3. Without virtualenv:

        pip3 install -r requirements.txt

## Usage

#### Web UI
Run `locust` command from project root. The web interface should start at localhost:8089. Open this page and specify number of users, hatch rate and host name before starting the test.

#### Command Line
Run the following command to start locust without the web UI:
    
    locust --host <hostname> -u <number of total users> -r <hatch rate> -t <run time> --headless

For more options, use `locust --help`
