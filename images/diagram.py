from diagrams import Diagram, Cluster
from diagrams.aws.network import Route53, CloudFront
from diagrams.aws.security import CertificateManager
from diagrams.aws.storage import SimpleStorageServiceS3
from diagrams.aws.mobile import APIGateway
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.onprem.vcs import Github



with Diagram("Resume Workflow", show=False):
    dns = Route53("resume.faisalorainan.cloud")
    acm = CertificateManager("ACM")

    with Cluster("Front-end"):
        frontend = CloudFront("CloudFront OAI") >> SimpleStorageServiceS3("HTML, CSS, JS")
    
    with Cluster("Back-end"):
        backend = APIGateway("API Gateway") >> Lambda("Lambda Functions") >> Dynamodb("Site Visit Count Table")

    dns - acm
    dns >> frontend >> Github("Github Frontend Repo")
    dns >> backend >> Github("Github Backend Repo")
    