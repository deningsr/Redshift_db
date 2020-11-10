## Udacity Data Engineering NanoDegree Project 3: Distributed Computing / AWS Redshift

#### Project rubric can be found here: https://review.udacity.com/#!/rubrics/2501/view

## Purpose

#### This project is intended to display my knowledge of AWS Redshift, S3 and the appropriate times to use them.

#### This project includes further work for imaginary startup Sparkify. The company has been expanding rapidly and their data needs have increased as a result. The solution presented to them involves migrating their datasets to the cloud so they can be accessed across the entire organization.

#### AWS Redshift has been deemed the best place to host their data, which is stored in S3. This data will be copied into staging tables and then populated into the appropriate fact and dimension tables.

## Running the Project

#### This repository contains three scripts that execute the process above and should be run the order below:

* <code>create_tables.py</code>: Drops any existing tables and creates new ones from queries found in <code>sql_queries.py</code>

* <code>sql_queries.py</code>: Create and insert statements are found here and are executed in the <code>create_tables.py</code> file

* <code>etl.py</code>: Connects to the AWS Redshift Cluster and implements the tables created in <code>create_tables.py</code>

