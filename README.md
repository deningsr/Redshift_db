### Udacity Data Engineering NanoDegree Program: Project 3

### Project rubric can be found here: https://review.udacity.com/#!/rubrics/2501/view

### This project continues the work for imaginary startup Sparkify. The company has been expanding rapidly and their data needs have therefore increased as well.
### The solution presented to them involves migrating their datasets to the cloud so they can be accessed across the entire organization.

### AWS Redshift has been deemed the best place to host their data, which is stored in S3. This data will be copied into staging tables and then populated into the appropriate fact and dimension tables.

### This repository contains three scripts that execute the proces above and can all be run in the MacOS Terminal or Windows Command Line in the order below:

* create_tables.py: Drops any existing tables and creates new ones from queries found in the sql_queries.py file
* sql_queries.py: Create and Insert statements are found here and are executed in the create_tables.py file
* etl.py: Connecets to the AWS Redshift Cluster and implements the tables created in create_tables.py

# The above scripts can be run in the command line preceeded by 'python'. For example, 'python create_tables.py' would execute the create_tables.py file on a MacOs device.

