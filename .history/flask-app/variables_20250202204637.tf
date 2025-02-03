variable "key_name" {
  description = "The name of the key pair to use for the EC2 instance"
  type        = string
}


variable "docker_username" {
  description = "DockerHub username"
  type        = string
}

variable "db_user" {
  description = "Database user"
  type        = string
}

variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true
}

variable "db_host" {
  description = "Database host"
  type        = string
}

variable "db_name" {
  description = "Database name"
  type        = string
}

variable "port" {
  description = "Application port"
  type        = string
}