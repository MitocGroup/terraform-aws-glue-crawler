#!/usr/bin/env python
'''
Python v2 & v3 compatible script
Terraform external data entity
Create new AWS Glue Crawler
'''
import os
import sys
import json
import time
import boto3

RETRIES = 5
ARGS = json.load(sys.stdin)
IAM = boto3.client(service_name='iam')
GLUE = boto3.client(
    service_name='glue',
    region_name=ARGS['aws_region'],
    endpoint_url='https://glue.{0}.amazonaws.com'.format(ARGS['aws_region']))

def main(retry_iterator=1):
    '''
    Create AWS Glue Crawler
    '''
    crawlers = GLUE.get_crawlers()
    try:
        crawl_exist = False
        for i in crawlers['Crawlers']:
            if i['Name'] == ARGS['crawler_name']:
                crawl_exist = True
                result = "Crawler with this name existed"
    except KeyError as key_error:
        result = key_error

    if crawl_exist is False:
        try:
            GLUE.create_crawler(
                Name=ARGS['crawler_name'],
                Description=ARGS['crawler_description'],
                Role=ARGS['crawler_role'],
                Targets={
                    "S3Targets": [
                        {
                            "Path": ARGS['data_source_path'],
                            "Exclusions": ARGS['data_source_exclusion'].split(",")
                        },
                    ],
                    "JdbcTargets": []
                },
                Schedule=ARGS['schedule'],
                Classifiers=[],
                DatabaseName=ARGS['database_name'],
                TablePrefix=ARGS['table_prefix'],
                SchemaChangePolicy={
                    "UpdateBehavior": "UPDATE_IN_DATABASE",
                    "DeleteBehavior": "DEPRECATE_IN_DATABASE"
                },
                Configuration=""
            )
            result = "Created"
        except Exception as exception:
            time.sleep(retry_iterator ** 2)
            if retry_iterator < RETRIES:
                return main(retry_iterator=retry_iterator + 1)
            raise Exception(exception)
    os.remove(ARGS['action_path'])
    return json.dumps({
        "CrawlerName": ARGS['crawler_name'],
        "Result": result,
        "Retries": str(retry_iterator)
    })

if __name__ == '__main__':
    if os.path.exists(ARGS['action_path']): 
        print(main())
    else:
        print(json.dumps({'Action': 'Not Created'}))
