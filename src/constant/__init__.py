import os


AWS_S3_BUCKET_NAME = 'wafer-fault'
MONGO_DATABASE_NAME = 'Sensor'
MONGO_COLLECTION_NAME ='waferfault'

TARGET_COLUMN = 'quality'
MONGO_DB_URL = "mongodb+srv://Jaypawar:Jaypawar@sensorcluster.amryw.mongodb.net/?retryWrites=true&w=majority"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = '.pkl'

artifact_folder = 'artifacts'