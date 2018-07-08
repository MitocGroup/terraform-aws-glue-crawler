data "external" "aws-glue-crawler" {
  program = ["python", "${path.module}/scripts/apply.py"]

  query = {
    aws_region            = "${var.aws_region}"
    crawler_name          = "${var.crawler_name}"
    crawler_description   = "${var.crawler_description}"
    crawler_role          = "${var.crawler_role}"
    data_source_path      = "${var.data_source_path}"
    data_source_exclusion = "${join(",",var.data_source_exclusion)}"
    database_name         = "${var.database_name}"
    table_prefix          = "${var.table_prefix}"
    schedule              = "${var.schedule}"
    action_path           = "${path.module}/scripts/create.lock"
    crawler               = "${null_resource.crawler.id}"
  }
}
