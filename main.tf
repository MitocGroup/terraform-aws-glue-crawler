resource "null_resource" "crawler" {
  provisioner "local-exec" {
    when    = "create"
    command = "touch ${path.module}/scripts/create.lock"
  }

  provisioner "local-exec" {
    when    = "destroy"
    command = "python ${path.module}/scripts/destroy.py ${var.crawler_name} ${var.aws_region}"
  }
}
