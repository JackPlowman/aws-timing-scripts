# AWS Timing Scripts

This repository contains a collection of scripts that can be used to time various AWS operations. The scripts are written in Python and use the Boto3 library to interact with AWS services.

## Prerequisites

`uv` is required to run the scripts.

## Running the scripts

To run a script, use the following command:

```bash
uv run timing_scripts/<script_name>.py
```

Note: This script will install the required dependencies in a virtual environment.

## Scripts

- `time_lambda_durations.py` - Times the duration of a Lambda function invocation.
- `time_sfn_durations.py` - Times the duration of a Step Functions execution.

## Contributing

We welcome contributions to the project. Please read the [Contributing Guidelines](docs/CONTRIBUTING.md) for more information.
