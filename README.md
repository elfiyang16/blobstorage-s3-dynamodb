#### Dynamodb --S3

S3 is good for object/blob storage, but for efficient query/lookup of file, it's better to store the metadata to DynamoDB.

This small project is to upload images to s3, which upon upload,, will trigger the lambda to download the file to its temporary storage `/tmp` and extract the metadata using `PIL` and tag the file, and save in DynamoDB.

Lastly, a quickly comparison on different lambda storage: https://aws.amazon.com/blogs/compute/choosing-between-aws-lambda-data-storage-options-in-web-apps/
For this use case, it should be fine with the /tmp, though with a quite tight upper bound (especially on image files), while EFS costs money :).
