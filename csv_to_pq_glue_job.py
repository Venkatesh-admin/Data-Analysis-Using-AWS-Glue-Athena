import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame  # Import DynamicFrame

# @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Define the Glue database and table name
database = "sales1"
table_name = "salesinput"

# Load data from Glue Catalog table
dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    database=database,
    table_name=table_name
)

# Convert dynamic frame to a Spark DataFrame for further processing
df = dynamic_frame.toDF()

# Step 1: Remove rows with null values in "quantity" and "unitprice"
new_df = df.na.drop(subset=["quantity", "unitprice"])

# Step 2: Remove duplicate rows
new_df = new_df.dropDuplicates()

# Display the cleaned DataFrame
new_df.show()

# Convert the cleaned DataFrame back to a DynamicFrame
cleaned_dynamic_frame = DynamicFrame.fromDF(new_df, glueContext, "cleaned_dynamic_frame")

# Step 3: Write the cleaned data back to S3 (Parquet format example)
glueContext.write_dynamic_frame.from_options(
    frame=cleaned_dynamic_frame,
    connection_type="s3",
    connection_options={"path": "s3://salesoutput/salesparquet/"},
    format="parquet"
)

# Commit the job
job.commit()
