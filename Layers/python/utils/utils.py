import boto3, datetime, csv
from pytz import timezone

# Method Name : selectS3FileListToJson
# param       : s3_bucket_name, stage_s3_bucket_data_dir, objPath
# return      : json
# Description : param에 해당하는 s3 File List 데이타 Json 조회 (1일 이내 LastModified Data)
def selectS3FileListToJson(s3_bucket_name, stage_s3_bucket_data_dir, objPath):
    file_list = []
    s3_resource = boto3.client('s3')
    obj_list = s3_resource.list_objects_v2(Bucket=s3_bucket_name, Prefix=stage_s3_bucket_data_dir)
    tzkr = timezone('Asia/Seoul')
    oneDaysAgo = datetime.datetime.now(tzkr) - datetime.timedelta(days=1)
    # LastModified 오름차순 정렬
    obj_list = sorted(obj_list['Contents'], key=lambda x: x['LastModified'], reverse=True)

    for file in obj_list:
        LastModifiedDate = file['LastModified'].astimezone(tzkr) 
        if LastModifiedDate > oneDaysAgo:
            file_list.append(
                {
                    "file_name"     : file['Key'].split('/')[3], 
                    "last_modified" : (LastModifiedDate).strftime('%Y-%m-%d %H:%M:%S'), 
                    "download_url"  : objPath+file['Key']
                }
            )
    return file_list

# Method Name : uploadS3FileTupleToCSV
# param       : s3_bucket_name, filePath, fileName, tupleData
# return      : bool
# Description : tuple Data를 csv로 변환하여 S3에 데이타 업로드
def uploadS3FileTupleToCSV(s3_bucket_name, filePath, fileName, tupleData):
    s3_resource = boto3.client('s3')
    try:
        with open("/tmp/" + fileName, "w") as file:
            csv_writer = csv.writer(file)
            for t in tupleData:
                csv_writer.writerow(t) 
        res = s3_resource.upload_file("/tmp/" + fileName, s3_bucket_name, filePath + fileName)
        return True
    except Exception as ex:
        print("error: " + ex.__str__())
    return False