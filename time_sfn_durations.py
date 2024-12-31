# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "boto3",
#     "pandas",
# ]
# ///

import time
from os import environ

import pandas as pd
from boto3 import client

# Get configuration for run
sfn_client = client("stepfunctions")
if "STEP_FUNCTION_ARN" not in environ:
    msg = "STEP_FUNCTION_ARN not found in environment variables"
    raise ValueError(msg)

durations = []

for counter in range(10):
    start_time = time.time()
    sfn_client.start_sync_execution(stateMachineArn=environ["STEP_FUNCTION_ARN"])
    end_time = time.time()
    duration = end_time - start_time
    # to 3 decimal places
    duration = round(duration, 6)
    durations.append(duration)
    if counter == 0:
        print(f"Cold start duration: {duration} seconds")
    else:
        print(f"Hot start {counter} duration: {duration} seconds")

# Store results in a DataFrame
dataframe = pd.DataFrame(durations, columns=["Duration"])
print(dataframe)
# Average all but first duration
dataframe = dataframe.iloc[1:]
avg_duration = dataframe["Duration"].mean()
print(f"Average duration: {avg_duration} seconds")
