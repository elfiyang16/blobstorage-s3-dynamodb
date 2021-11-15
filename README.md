#### Dynamodb --S3

S3 is good for object/blob storage, but for efficient query/lookup of file, it's better to store the metadata to DynamoDB.
There's also problem with concurrency, as if 2 processor upload one object, the object will end of with 2 versions. 

DynamoDB on the other hand, is good for query/lookup but it has a max size/record which is 400KB. 

This small project is to upload images to s3, which upon upload, will trigger the lambda to download the file to its temporary storage `/tmp` and extract the metadata using `PIL` and tag the file, and save in DynamoDB.

Lastly, a quickly comparison on different lambda storage: https://aws.amazon.com/blogs/compute/choosing-between-aws-lambda-data-storage-options-in-web-apps/
For this use case, it should be fine with the /tmp, though with a quite tight upper bound (especially on image files), while EFS costs money :).


-- Update 15th Nov

TODO: to make it a proper data store:
Add more complex logic to the business layer. 

Upon upload:
- assign a proper key to the object (S3 is partitioned by prefix), upload to s3
- if s3 upload succeeds, save the metadata to DynamoDB

Upon retrieval:
- read the record from DynamoDB and extract the object key
- download from s3
