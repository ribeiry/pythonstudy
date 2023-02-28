data "archive_file" "zip" {
  type        = "zip"
  source_dir  = "../python/"
  output_path = "../python/package-management.zip"
}

resource "aws_lambda_function" "package-building" {
  filename      = "../python/package-management.zip"
  function_name = var.project_name
  runtime       = var.runtime
  timeout       = 10
  role          = aws_iam_role.lambda_role.arn
  handler       = "main.handler"
}

resource "aws_lambda_alias" "alias_dev" {
  name             = var.alias
  function_name    = aws_lambda_function.package-building.arn
  function_version = "$LATEST"
}