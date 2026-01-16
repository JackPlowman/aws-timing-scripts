# /// script
# requires-python = "~=3.14"
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
lambda_client = client("lambda")
if "LAMBDA_NAME" not in environ:
    msg = "LAMBDA_NAME not found in environment variables"
    raise ValueError(msg)

durations: list[float] = []

for counter in range(10):
    start_time = time.time()
    lambda_client.invoke(
        FunctionName=environ["LAMBDA_NAME"], InvocationType="RequestResponse"
    )
    end_time = time.time()
    duration = end_time - start_time
    # to 3 decimal places
    duration = round(duration, 3)
    durations.append(duration)
    if counter == 0:
        print(f"Cold start duration: {duration} seconds")
    else:
        print(f"Hot start {counter} duration: {duration} seconds")

# Store results in a DataFrame
dataframe = pd.DataFrame({"Duration": durations})
print(dataframe)
# Average all but first duration
dataframe = dataframe.iloc[1:]
avg_duration = dataframe["Duration"].mean()
print(f"Average duration: {avg_duration} seconds")
