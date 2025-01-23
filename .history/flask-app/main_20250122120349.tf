provider "aws" {
  region = "us-east-1" # Adjust to your desired region
}

resource "aws_security_group" "apache_sg" {
  name        = "apache-server-sg"
  description = "Allow HTTP and SSH access"

  ingress {
    description = "Allow HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Allow SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow all outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "Apache-SG"
  }
}

resource "aws_instance" "apache_server" {
  ami           = "ami-0df8c184d5f6ae949" 
  instance_type = "t2.micro"
  key_name      = "key-gen"
  security_groups = [aws_security_group.apache_sg.name]

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y httpd
              systemctl enable httpd
              systemctl start httpd
              EOF

  tags = {
    Name = "Apache-Server"
  }
}

output "public_ip" {
  value = aws_instance.apache_server.public_ip
}

resource "local_file" "output_ip" {
  content  = aws_instance.apache_server.public_ip
  filename = "public_ip.txt"
}
