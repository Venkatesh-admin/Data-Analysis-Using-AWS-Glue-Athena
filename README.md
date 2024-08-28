# Data Pipeline using S3, Glue Crawler, Glue Job, and Athena

## Overview

This project demonstrates how to build a data pipeline for sales data using AWS services such as Amazon S3, AWS Glue (Crawler and Job), and Amazon Athena. The pipeline loads raw data into an S3 bucket, uses a Glue Crawler to catalog the data, transforms the data using a Glue Job, and finally queries the transformed data using Athena.

## Architecture

The pipeline is built using the following AWS services:

- **Amazon S3**: Stores the raw and transformed data.
- **AWS Glue Crawler**: Scans the S3 bucket to automatically create a table schema in the AWS Glue Data Catalog.
- **AWS Glue Job**: Transforms the raw data by applying business logic or data cleansing operations.
- **Amazon Athena**: Queries the transformed data from S3.

## Prerequisites

Before setting up this pipeline, ensure that you have the following:

- An AWS account with the necessary permissions to create and manage S3 buckets, Glue resources, and Athena queries.
- AWS CLI or AWS Management Console access to configure and run AWS services.
- Python installed for script execution (if applicable).

## Steps

### 1. Create an S3 Bucket

1. Create two S3 buckets for input to store raw data and output to store transformed parquet data.
2. Upload the raw data files csv to the bucket.

### 2. Set Up AWS Glue Crawler

1. In AWS Glue, create a Glue Crawler to scan the S3 bucket where the raw data is stored.
2. Configure the Crawler to add tables to a new or existing Glue Database.
3. Run the Crawler to populate the Glue Data Catalog with the table schema.

### 3. Create and Run an AWS Glue Job

1. Create an AWS Glue Job to transform the raw data. This job can be written using PySpark or Python scripts.
2. The job will read the data from the S3 bucket, apply transformations (cleansing), and write the results back to a output S3 location.
3. Run the Glue Job and verify that the transformed data is stored in S3.

### 4. Query Data with Amazon Athena

1. Use Athena to query the transformed data from the S3 bucket.
2. In Athena, create an external table referencing the transformed data location.
3. Write and execute SQL queries to analyze the data.

