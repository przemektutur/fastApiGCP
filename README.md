# READ ME PLEASE ;)

### REST API

# Project Overview

This project demonstrates a RESTful API for managing Curriculum Vitae (CV) 

entries, showcasing CRUD operations (Create, Read, Update, Delete) on a 

database. It's written in Python, leveraging FastAPI for the web framework 

and SQLAlchemy for ORM interactions with the database. Initially set up with 

SQLite for demonstration, it's intended to migrate to PostgreSQL on Google 

Cloud Platform (GCP) for production. The application will be containerized 

using Docker, enhancing deployment flexibility and scalability.

## Architecture

The application's architecture is designed to be modular and scalable, 

following microservices principles and ready for deployment in a Kubernetes 

cluster. Below is a high-level overview of the components:

- **FastAPI Application**: Serves as the core of the project, handling HTTP 

requests, executing business logic, and performing CRUD operations on the 

database through SQLAlchemy.

- **SQLAlchemy**: Acts as the ORM layer, abstracting database interactions 

and ensuring compatibility with different database systems, like SQLite and 

PostgreSQL.

- **Database**: Stores CV data. SQLite is used for initial development and 

testing, with plans to use PostgreSQL in the production environment on GCP.

- **Docker**: Containerizes the FastAPI application, ensuring consistent 

environments across development, testing, and production.

- **Kubernetes**: Orchestrates the deployment, scaling, and management of 

the containerized application, utilizing Pods, Services, and Deployments 

for a robust and scalable system.

### Deployment Flow

1. **Development**: The application is developed locally, using SQLite for 

ease of setup and rapid testing.

2. **Containerization**: The application is packaged into a Docker container, 

encapsulating dependencies and runtime environment.

3. **Deployment to Kubernetes**: The Dockerized application is deployed to a 

Kubernetes cluster. This could be a local cluster (e.g., minikube) or a 

cloud-based one (GCP).

4. **Kubernetes Orchestration**: Kubernetes manages the application's 

lifecycle, from scaling based on load to rolling updates for new versions.


## Features

- **RESTful API**: Exposes endpoints for managing CV entries, adhering to 

REST principles for ease of use and integration.

- **CRUD Operations**: Supports full lifecycle management of CV data, 

including creating, viewing, updating, and deleting entries.

- **Database Abstraction**: Utilizes SQLAlchemy for ORM, facilitating future 

migrations to other database systems like PostgreSQL without significant code 

changes.

- **Containerization and Orchestration**: Leverages Docker and Kubernetes for 

scalable, reliable deployment and management of the application.

## Future Enhancements

- **Authentication and Authorization**: Implement mechanisms to secure the 

API, ensuring that only authorized users can perform certain operations.

- **CI/CD Integration**: Set up continuous integration and deployment pipelines

 for automated testing and deployment.

- **Advanced Features**: Considering adding advanced functionalities like 

search, pagination, and filtering for the API endpoints.


```marmaid
graph LR
    user[User] -->|REST API Calls| fa[FastAPI Application]
    fa -->|ORM| sqla[SQLAlchemy]
    sqla -->|SQLite/PostgreSQL| db[(Database)]
    fa -->|Dockerized| docker[Docker Container]
    docker -->|Deployed in| k8s[Kubernetes Cluster]
    k8s -->|Manages| pods[Pods]
    k8s -->|Exposes| svc[Service]
    k8s -->|Orchestrates| deploy[Deployment]
```

### Dependencies

pip install -r requirements.txt

### Rurn program:

On your system run:

```Bash
uvicorn app:app --reload
```

On local web browser app is available on the:

```Python
http://127.0.0.1:8000
```

### Curriculum vitate

JSON input/output).

Please checkout the code..

Create payload example:

```Json

{
  "name": "Przemysław Tutur",
  "email": "przemektutur@poczta.fm",
  "experience": [
    {
      "company": "Dell Technologies",
      "position": "Consultant",
      "from_date": "2022-02-01",
      "description": "Automation, migration, DevOps and Python development. Architecture"
    },
    {
      "company": "Accenture Sp. z o.o.",
      "position": "Tech Arch Delivery Team Lead",
      "from_date": "2017-11-01",
      "to_date": "2022-02-01",
      "description": "DDI, Networking, Teamleading, Python automation and tests"
    },
    {
      "company": "Cubiware Sp. z o.o.",
      "position": "Support Engineer",
      "from_date": "2013-08-01",
      "to_date": "2017-10-01",
      "description": "Linux and database administration (MySQL/PostgreSQL), Presales"
    }
  ],
  "education": [
    {
      "institution": "Polish-Japanese Academy of Information Technology",
      "degree": "Big Data - Collections of Large Data",
      "from_date": "2023-01-01",
      "to_date": "2024-01-01"
    },
    {
      "institution": "West Pomeranian University of Technology",
      "degree": "Telecommunications and Electronics",
      "from_date": "2009-01-01",
      "to_date": "2013-01-01"
    },
    {
      "institution": "Szczecin Technical University",
      "degree": "Chemical Organic Technology",
      "from_date": "2002-01-01",
      "to_date": "2007-01-01"
    }
  ],
  "skills": [
    {
      "name": "Programming",
      "level": "Python, Bash, PowerShell, C#"
    },
    {
      "name": "OS",
      "level": "Linux, Windows"
    },
    {
      "name": "Networking",
      "level": "Routing, Switching, Automation, Loadbalancing"
    },
    {
      "name": "Database",
      "level": "MySQL/SQL"
    },
    {
      "name": "Cloud",
      "level": "AZ-104, AZ-303 (Azure Certificates 2021/22)"
    },
    {
      "name": "Additional",
      "level": "Machine Learning, Git, Ansible, Docker, Kubernetes"
    },
    {
      "name": "Languages",
      "level": "English (Advanced), Chinese (Basic), Polish (Native), Russian (Basic)"
    }
  ]
}

```

### Pictures

Picasso pictures of working app ;)

Create request:

![CREATE SEND](pictures/POST001.png)

Create response:

![CREATE RECEIVED](pictures/POST002.png)

Get request

![GET SEND](pictures/GET001.png)

Get response:

![GET RECEIVED](pictures/GET002.png)

Update request

![PUT SEND](pictures/PUT001.png)

Update response:

![PUT RECEIVED](pictures/PUT002.png)

Delete request

![Delete SEND](pictures/DEL001.png)

Delete response:

![Delete RECEIVED](pictures/DEL002.png)

