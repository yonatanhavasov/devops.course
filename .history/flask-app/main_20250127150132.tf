provider "aws" {
  region = "us-east-1"
}


resource "aws_security_group" "flask_sg" {
  name        = "flask-server-sg"
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
    Name = "Flask-SG"
  }
}

resource "aws_instance" "flask_server" {
  ami           = "ami-0df8c184d5f6ae949" # Amazon Linux 2 AMI (Region-specific)
  instance_type = "t2.micro"
  key_name      = var.key_name
  security_groups = [aws_security_group.flask_sg.name]

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y docker
              systemctl enable docker
              systemctl start docker

              # Install Docker Compose
              curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-\$(uname -s)-\$(uname -m)" -o /usr/local/bin/docker-compose
              chmod +x /usr/local/bin/docker-compose
              EOF

  provisioner "file" {
    source      = "docker-compose.yml"
    destination = "/home/ec2-user/docker-compose.yml"
  }

  provisioner "file" {
    source      = "Dockerfile"
    destination = "/home/ec2-user/Dockerfile"
  }

  provisioner "remote-exec" {
    inline = [
      "cd /home/ec2-user",
      "docker-compose up -d"
    ]

    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = file("~/.ssh/id_rsa") # Path to your private key
      host        = self.public_ip
    }
  }

  tags = {
    Name = "Flask-Server"
  }
}

output "public_ip" {
  value = aws_instance.flask_server.public_ip
}
