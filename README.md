# AWS: aws-ip-ranges

A simple command-line utility to list, filter and check the current list of
AWS Public IP Address Ranges.


## Install

To install:

    pip install aws-ip-ranges


## Usage

Simple usage:

    # list
    aws-ip-ranges list

    # filter: by region, by service, or both
    aws-ip-ranges list service=ec2
    aws-ip-ranges list region=sa-east-1
    aws-ip-ranges list region=sa-east-1 service=ec2

    # check: that IP belongs to AWS?
    aws-ip-ranges check 177.71.207.128

    # download: get json file
    aws-ip-ranges download


## More...


## References

[Download: JSON file](https://ip-ranges.amazonaws.com/ip-ranges.json)

[Doc: AWS IP Address Ranges](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html)

[Blog: AWS Public IP Address Ranges Now Available](https://aws.amazon.com/blogs/aws/aws-ip-ranges-json/)


## License

This is free software, and may be redistributed under the terms specified in
the LICENSE file.

