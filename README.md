# AAKAAR DOCUMENTATION

**Domain:** 
**Client:** 
**Summary:** 

## Build Status
- Tasks passed: 4
- Tasks failed: 6
- Files generated: 9

## Architecture
- **BRD Parser**: Extracts relevant information from a BRD document
- **Requirements Extractor**: Extracts requirements from the parsed BRD document
- **Scope Definer**: Defines the scope of the project based on the extracted requirements
- **SOW Generator**: Generates a Statement of Work (SOW) based on the defined scope
- **Lead Architect**: Designs the architecture of the web application based on the SOW
- **WBS Planner**: Creates a Work Breakdown Structure (WBS) based on the designed architecture
- **Database Agent**: Creates the database schema based on the WBS
- **Backend Agent**: Creates the backend API based on the database schema
- **Frontend Agent**: Creates the frontend UI based on the backend API
- **DevOps Agent**: Creates the CI/CD pipelines based on the frontend UI
- **Critic Agent**: Reviews the web application based on the CI/CD pipelines
- **Delivery Agent**: Delivers the web application based on the review
- **Pattern Librarian**: Updates the pattern library based on the delivered web application

## Tech Stack
- **Backend**: Python 3.10 with Flask 2.0
- **Frontend**: JavaScript with React 18
- **Database**: PostgreSQL 14
- **CI/CD**: Jenkins 2.3