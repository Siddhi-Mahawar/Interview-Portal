# Interview-Portal

# Overview
- [Introduction](#introduction)
- [Goals](#goals)
- [Structure](#structure)
- [Instructions](#instructions)
- [Demos](#demos)
- [Technologies Used](#technologies-used)

# Introduction

Interview-Portal is a simple django web application for conducting interviews. 

It is segregated into three parts:
1. Interviewer
2. Interviewee
3. Company Admin

Company Admin can add interviewers as well as interviewees. Interviewer can create a room for interview and both interviewer and interviewee can login with their temporary credentials. The implementation strives to be simple and free of unnecessary dependencies.

# Goals

1. Register to the platform (for company admins only, add some unique verification checks)

2. Ability for company admins to add their employees/interviewers and provide them login credentials.

3. Login for admins and interviewers.

4. Interviewers can generate Interview URLs (to be unique) for the candidates.

5. Interview URLs to be valid from a given point (no one can open it pre maturely)

6. Generate Temporary login credentials for candidates. (to be valid for a certain time)

7. Information filling by candidates on login.

8. Area for questions and separate are for coding editor.

9. Simultaneous real time editing on same editor window by both.

10. Ability to choose different programming languages.

11. Ability to compile and run the program.

12. Ability for interviewer to lock the editor and code compilation and execution.

13. Ability to add questions before to be imported during the interview.

# Structure

- `/Login App` for the Company Admin which will be verified by the super admin

- `/interviewer` App for the interviewer which contains all the details and functionalities

- `/interviewee`  App for the interviewee which contains all the details and functionalities

- `/editor` App for the editor which have all the languages supported by the editor

# Instructions

1. Install Python vesion 3.9+
   
2. Install Django version 3.1+

3. Fork and clone repository

4. Run the website `python manage.py runserver`

5. Login on the link `http://127.0.0.1:8000/`

# Demos

# Technologies Used

- Front-end: JavaScript, Bootstrap, jQuery, HTML, CSS

- Back-end: Django

- Libraries: Firepad
