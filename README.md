# Welcome to my Cloud Resume!

This project is a cloud-based resume website hosted on AWS. Check it out at https://resume.faisalorainan.cloud. A PDF version is available [here](https://github.com/ps-the-aux/cloud-resume-frontend/blob/main/resume_website/Faisal_Orainan_Resume.pdf).

<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/ps-the-aux/cloud-resume-frontend/blob/main/images/resume_workflow.png">
  <img alt="frontend cloud diagram" src="https://github.com/ps-the-aux/cloud-resume-frontend/blob/main/images/resume_workflow.png">
</picture>

### Repository Overview

This repository contains the static front-end files for my resume website. These include the HTML, CSS, and JavaScript that create its design and functionality.

### Purpose

The front-end portion of the website is separated into this repository to leverage a CI/CD pipeline configured through a YAML file using GitHub Actions.

The website files are stored in the cloud, specifically in an S3 bucket. As changes are made to the resume/website, a combination of the HTML, CSS, JavaScript files are changed to update the website in real time. 

### GitHub Actions Workflow

- __Deploy Frontend Changes to S3__: The workflow automates the deployment of frontend updates to an S3 bucket.

- __Environment Variables__: Key details such as the `AWS_S3_BUCKET`,  `AWS_REGION`, and `CLOUDFRONT_DISTRIBUTION_ID` are passed as environment variables.

- __Permissions__: The GitHub Actions job is configured with the appropriate token and role permissions to write the updated files to the S3 bucket.

- __CloudFront Cache Invalidation__: To ensure that changes are visible in real time (instead of the typical 24-hour delay), the workflow includes a step to invalidate the CloudFront cache, allowing immediate updates.

By isolating the front-end code, it allows for streamlined updates, continuous integration, and automated deployment, ensuring the website stays current with minimal manual intervention.

