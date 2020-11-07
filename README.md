## Udacity Data Engineering NanoDegree Project 3: Distributed Computing / AWS Redshift

#### Project rubric can be found here: https://review.udacity.com/#!/rubrics/2501/view

#### This project continues the work for imaginary startup Sparkify. The company has been expanding rapidly and their data needs have therefore increased as well. The solution presented to them involves migrating their datasets to the cloud so they can be accessed across the entire organization.

#### AWS Redshift has been deemed the best place to host their data, which is stored in S3. This data will be copied into staging tables and then populated into the appropriate fact and dimension tables.

#### This repository contains three scripts that execute the proces above and can all be run in the MacOS Terminal or Windows Command Line in the order below:

* <code>create_tables.py</code>: Drops any existing tables and creates new ones from queries found in the sql_queries.py file
* <code>sql_queries.py</code>: Create and Insert statements are found here and are executed in the create_tables.py file
* <code>etl.py</code>: Connecets to the AWS Redshift Cluster and implements the tables created in create_tables.py

#### The above scripts can be run in the command line preceeded by 'python'.

