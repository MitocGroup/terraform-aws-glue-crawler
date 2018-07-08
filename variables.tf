variable "aws_region" {
  description = "AWS Region"
  default = "us-east-1"
}

variable "crawler_name" {
  description = "Crawler Name"
  default = "my_crawler"
}

variable "crawler_description" {
  description = "Crawler Description"
  default = "Managed by TerraHub"
}

variable "crawler_role" {
  description = "Crawler Role"
  default = "arn:aws:iam::111111111111:role/my_role"
}

variable "data_source_path" {
  description = "S3 Source Path"
  default = ""
}

variable "data_source_exclusion" {
  description = "Exclusions in S3 Path (not implimented)"
  type        = "list"
}

variable "database_name" {
  description = "Database Name"
  default = ""
}

variable "table_prefix" {
  description = "Table Prefix"
  default = ""
}

variable "schedule" {
  description = "Schedule, a cron expresion in form of cron(15 12 * * ? *) "
  default = ""
}
