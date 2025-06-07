terraform {
  required_version = ">= 1.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

data "aws_caller_identity" "current" {}

variable "aws_region" {
  type = string
  default = "us-east-1"
}

resource "aws_iam_role" "ec2_role" {
  name = "ec2-logging-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action    = "sts:AssumeRole",
      Effect    = "Allow",
      Principal = { Service = "ec2.amazonaws.com" }
    }]
  })

  tags = {
    Name        = "EC2 Logging Role"
    Environment = "dev"
  }
}

resource "aws_iam_role_policy" "logs_policy" {
  name = "allow-cloudwatch-logs"
  role = aws_iam_role.ec2_role.id

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect   = "Allow",
      Action   = [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      Resource = "arn:aws:logs:${var.aws_region}:${data.aws_caller_identity.current.account_id}:log-group:/aws/ec2/*"
    }]
  })
}

resource "aws_iam_instance_profile" "ec2_profile" {
  name = "ec2-instance-profile"
  role = aws_iam_role.ec2_role.name
}

resource "aws_instance" "ec2" {
  ami           = "ami-02457590d33d576c3" # Amazon Linux 2 (us-east-1)
  instance_type = "t2.micro"

  iam_instance_profile = aws_iam_instance_profile.ec2_profile.name

  metadata_options {
    http_tokens   = "required"     # habilita IMDSv2
    http_endpoint = "enabled"
  }

  monitoring = true                # habilita detailed monitoring

  ebs_optimized = true            # habilita EBS otimizado

  root_block_device {
    volume_type           = "gp3"
    volume_size           = 8
    delete_on_termination = true
    encrypted             = true  # habilita criptografia
  }

  tags = {
    Name = "EC2WithIAMRole"
  }
}

