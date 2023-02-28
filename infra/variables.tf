variable "region" {
  description = "Região aonde o Lambda irá ser deployado"
  default     = "sa-east-1"
  type        = string
}

variable "profile" {
  description = "Profile da conta AWS"
  default     = "default"
  type        = string
}

variable "project_name" {
  description = "Name of project and Lambda"
  default     = "building-app"
  type        = string
}

variable "runtime" {
  description = "valor do runtime do lambda"
  default     = "python3.9"
  type        = string
}

variable "alias" {
  description = "valor do alias e ambiente"
  default     = "dev"
  type        = string
}