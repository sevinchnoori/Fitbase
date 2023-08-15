# MySQL + Flask Boilerplate Project

This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 


Project Overview:
Our product, FitBase, aims to organize the system of a newly-opened private gym, FitClub. The product will help the new gym with their struggles of keeping track of their customers, presonal training sessions, class sessions, trainers, and other employees. The product will help marketers market the gym in order to gain new members and keep old members involved. A gym member can access this product in order to gain information on available classes and their profile. Their profile contains member demographics as well as their specific membership plan. Trainers will use the product to view class and personal training information and update their own information (ie: certifications obtained/expired). Meanwhile, gym administration can view managers and the section of the gym they oversee, as well as payroll-related information for their employees. General gym employees can view their own profiles and payroll-related information. 


Technologies we used: 

Technologies we used include DataGrip, Visual Studio Code, AppSmith and Docker. DataGrip was used to create the basis of the database. It hosted entites with corresponding attributes usable by 3 user personas, a trainer, marketing consultant, and gym member. Entities include the personas themselves, membership, products, orders, gyms, and more. These entities also included attributes that are appropriate for the use by and visualization for any of the 3 personas. Also, within DataGrip, we created sample data for the database in order to mock an actual database and showcase the database's usage. Visual Studio Code was used to implement the Python code to showcase the possible usage for 2 of our user personas, the trainer and gym member by bulding out the routes needed for our UI. The ThunderClient extension was used to test the routes of these usages. For example, usages for each user persona include:

Member - 
(1) /postMember: add a new member into the database (themselves)
(2) /orders: get all the orders made
(3) /classNames: get all the classes and their times from the database
(4) /updateType: update the membership 
(5) /membershipPrices: get the costs of all the memberships available
(6) /trainerNames: get the names of all the trainers 
(7) /getPT: get information about all the personal training sessions
(8) /deleteAccount: delete own member account

Trainer - 
(1) /members: get all the different trainers from the database 
(2) /totalseats: get the total number of remaining seats for a class
(3) /contact: get all the different members and their contact info from the database
(4) /managerinfo: get all the different managers from the database
(5) /classinfo: get all the different class information from the database
(6) /updateLast: update the last name of a trainer in the database
(7) /postTrainer: add a new trainer to the database (themselves)
(8) /deleteCertification: delete a trainer to the certification

AppSmith was used to develop the UI of our database and showcase the routes. Overall, Docker was used to ensure that the database within VSCode was working and running. 






