# AWS - aws-ip-ranges

A simple command-line utility to list, filter and check current ranges of IP
used by AWS.


## Install

To install:

    pip install aws-ip-ranges


## Usage

Simple usage:

    # list
    aws-ip-ranges list

    # filter: by region, by service, or both
    aws-ip-ranges list region=sa-east-1
    aws-ip-ranges list service=ec2
    aws-ip-ranges list region=sa-east-1 service=ec2

    # check: this IP belongs to AWS?
    aws-ip-ranges check 177.71.207.128


## More...


## License

This is free software, and may be redistributed under the terms specified in the LICENSE file.

