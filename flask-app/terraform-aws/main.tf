provider "aws" {
  region = "us-east-1" # Change to your preferred region, 6, 25/1 deploy.
}
terraform {
  backend "s3" {
    bucket         = "docker-badger-gifs"   # Your existing S3 bucket name
    key            = "terraform/terraform.tfstate"  # State file location inside the bucket
    region         = "us-east-1"  # Update if your bucket is in a different region
    encrypt        = true
  }
}
resource "aws_security_group" "flask_sg" {
  name        = "flask-sg"
  description = "Security group for Flask app"

  lifecycle {
    create_before_destroy = true
  }

  ingress {
    from_port   = 5001
    to_port     = 5001
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "apache_server" {
  ami           = "ami-0df8c184d5f6ae949" # Amazon Linux 2 AMI (update if needed)
  instance_type = "t2.micro"
  key_name      = var.key_name # Reference your existing key pair by name

  security_groups = [aws_security_group.flask_sg.name]

  iam_instance_profile = "access-to-s3" # Reference the existing IAM instance profile directly

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y git docker
              systemctl start docker
              systemctl enable docker
              usermod -aG docker ec2-user
              newgrp docker
              yum install -y libxcrypt-compat

              curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
              chmod +x /usr/local/bin/docker-compose
              
              mkdir -p /home/ec2-user/flask-app
              git clone https://github.com/yonatanhavasov/devops.course.git /home/ec2-user/flask-app
              aws s3 cp s3://docker-badger-gifs/.env /home/ec2-user/flask-app/flask-app/.env
              cd /home/ec2-user/flask-app/flask-app
              
              docker-compose pull
              docker-compose up -d 
              EOF
}

output "instance_public_ip" {
  value       = aws_instance.apache_server.public_ip
  description = "Public IP of the EC2 instance"
}