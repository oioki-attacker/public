#!/usr/bin/env python3

import sentry_sdk

sentry_sdk.init(
    dsn="https://3d91f9ed5844b014dbef345d2c4b9ffd@o4506140671803392.ingest.sentry.io/4506535411515392",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

def core(a, b):
    if b > 0:
        return a / b;
    return a / b;

if __name__ == '__main__':
    print(core(1, 0))
