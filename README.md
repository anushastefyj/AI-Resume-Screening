# AI-Resume-Screening

AI Resume Analyzer and Job Recommendation System
Project Overview

This project is a full stack web application that analyzes uploaded resumes, extracts skills using an AI based Python service, and recommends suitable job roles based on those skills. It demonstrates integration between React frontend, Spring Boot backend, and a Python Flask service.

Project Description
Developed a full stack application to automate resume screening and job role suggestion.
The user uploads a resume through a React based interface.
The resume file is sent to a Spring Boot backend using REST APIs.
The backend forwards the file to a Python Flask service for processing.
The Python service uses natural language processing techniques to extract skills from the resume.
Extracted skills are returned to the Spring Boot backend.
The backend applies a simple matching logic to recommend relevant job roles based on skills.
The final output including extracted skills and job recommendations is displayed in the frontend.
Key Features
Resume upload in PDF format
Skill extraction using Python NLP processing
REST API communication between frontend, backend, and AI service
Job role recommendation based on skill matching
Full stack integration of React, Spring Boot, and Python
Tech Stack

Frontend
React, HTML, CSS, JavaScript

Backend
Spring Boot, REST APIs

AI Service
Python Flask, NLP libraries, PDF parsing tools

How the System Works


User uploads a resume from the frontend
Spring Boot receives the file through an API
The file is sent to a Python service
Python extracts skills from the resume content
Extracted skills are sent back to the backend
Backend generates job recommendations based on skills
Results are displayed in the frontend

Outcome

This project shows how full stack development and AI based text processing can be combined to build an automated resume screening system similar to real world recruitment tools.


<img width="1867" height="829" alt="image" src="https://github.com/user-attachments/assets/7ceb2778-c488-40b7-a173-451148d4e8dd" />

<img width="915" height="874" alt="image" src="https://github.com/user-attachments/assets/0d9fbc4b-3467-4d05-a993-815f6fa7eb38" />


