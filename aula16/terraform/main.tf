# main.tf or providers.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0" # Use a version compatible with your setup, or a specific version
    }
  }
}

provider "aws" {
  region = "us-east-1" # <--- IMPORTANT: Change this to your desired AWS region (e.g., sa-east-1 for Brazil)
}

resource "aws_security_group" "insecure_sg" {
  name = "insecure-web-server-sg"
  description = "Permite acesso Web e SSH"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["189.20.30.40/32"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["189.20.30.40/32"] # Violação!
  }
}

