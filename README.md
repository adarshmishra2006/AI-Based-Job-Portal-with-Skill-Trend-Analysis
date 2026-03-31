# Job Portal Analyzer

Job Portal Analyzer is a menu-driven application developed using Python and SQLite that simulates the core functionality of a job portal. It allows applicants to register with their skills and experience, while recruiters can efficiently search and filter candidates based on specific requirements. The system also keeps track of skill demand based on recruiter activity, helping in identifying current job market trends.

This project demonstrates how structured data can be stored, processed, and utilized to support decision-making in a real-world scenario such as recruitment systems.

---

## Objectives

* To develop a job portal system using Python and SQLite
* To manage applicant data efficiently
* To enable recruiters to filter candidates based on skill and experience
* To track and analyze skill demand trends
* To demonstrate database operations such as insert, search, update, and delete

---

## Features

* Applicant registration with multiple skills
* Recruiter-based candidate filtering
* Experience-based eligibility checking
* Displays only relevant skill in output
* Tracks frequency of skill searches
* Shows top 5 most in-demand skills
* Allows applicants to delete their records
* Input validation for reliable execution
* Clean tabular output using PrettyTable

---

## Technologies Used

| Technology  | Description                                                           |
| ----------- | --------------------------------------------------------------------- |
| Python      | Used for implementing the application logic and menu-driven interface |
| SQLite      | Used as a lightweight database to store and manage data               |
| PrettyTable | Used to display output in a structured tabular format                 |

---

## System Design

The system follows a simple menu-driven architecture. Users interact with the system by selecting options, and the corresponding operations are performed on the database.

### Database Structure

#### Applicant Table

| Field Name     | Description                             |
| -------------- | --------------------------------------- |
| id             | Unique identifier for each applicant    |
| name           | Name of the applicant                   |
| experience     | Years of experience                     |
| skill          | Skills stored as comma-separated values |
| contact_number | Contact details                         |

---

#### Skills Table

| Field Name   | Description                                 |
| ------------ | ------------------------------------------- |
| skill_name   | Name of the skill                           |
| search_count | Number of times the skill has been searched |

---

## Working Principle

1. The user runs the program and selects an option from the menu.

2. If the applicant chooses to apply for a job:

   * Details such as name, experience, and contact number are entered
   * Multiple skills are selected from a predefined list
   * Data is stored in the applicant table

3. If a recruiter searches for candidates:

   * Required skill and minimum experience are entered
   * The system filters candidates based on matching criteria
   * Only eligible candidates are displayed

4. Every time a skill is searched:

   * Its search count is incremented in the skills table

5. The trend analyzer:

   * Retrieves and displays the top 5 most searched skills

6. Applicants can also delete their records using their name and contact number

---

## Key Functionalities Explained

### Apply for Job

This module allows applicants to enter their personal and professional details. Multiple skills can be selected, which are stored in a structured format. This helps in creating a comprehensive applicant profile.

---

### Recruit Applicant

This module enables recruiters to find suitable candidates by specifying required skills and experience. The system filters applicants based on these conditions and displays only relevant matches.

---

### Trend Analyzer

The system keeps track of how frequently each skill is searched. Based on this data, it identifies and displays the top 5 most in-demand skills, helping in understanding current market trends.

---

### Delete Application

Applicants can remove their data from the system by providing their name and contact number. This ensures basic data management functionality.

---

## Advantages

* Simple and easy to use
* Efficient data storage using SQLite
* Supports multiple skills per applicant
* Provides insight into trending job skills
* Demonstrates real-world application of database systems

---

## Limitations

* Command-line based interface
* No authentication or security features
* Skills stored as text instead of normalized structure
* Not suitable for large-scale deployment

---

## Future Enhancements

* Graphical User Interface (GUI) for better usability
* Login system for applicants and recruiters
* Resume upload and management
* Candidate ranking system based on multiple parameters
* Job recommendation system
* Predictive analysis for future skill demand

---

## Learning Outcomes

* Understanding of database operations (CRUD)
* Implementation of menu-driven programs
* Data filtering using logical conditions
* Handling structured data efficiently
* Identifying patterns based on user activity

---

## Conclusion

The Job Portal Analyzer project successfully demonstrates how Python and SQLite can be used together to build a functional job portal system. It highlights the importance of data organization, filtering logic, and trend tracking. The project also provides a strong foundation for building more advanced systems involving intelligent data analysis and decision-making.
