# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "boto3",
#     "pandas",
# ]
# ///

import pandas as pd
from boto3 import client
from os import environ
import time

# Get configuration for run
sfn_client = client("stepfunctions")
if "STEP_FUNCTION_ARN" not in environ:
    raise ValueError("STEP_FUNCTION_ARN not found in environment variables")

durations = []

for i in range(10):
    start_time = time.time()
    response = sfn_client.start_sync_execution(
        stateMachineArn=environ["STEP_FUNCTION_ARN"]
    )
    end_time = time.time()
    duration = end_time - start_time
    # to 3 decimal places
    duration = round(duration, 6)
    durations.append(duration)
    if i == 0:
        print(f"Cold start duration: {duration} seconds")
    else:
        print(f"Hot start {i} duration: {duration} seconds")

# Store results in a DataFrame
df = pd.DataFrame(durations, columns=["Duration"])
print(df)
# Average all but first duration
df = df.iloc[1:]
avg_duration = df["Duration"].mean()
print(f"Average duration: {avg_duration} seconds")
