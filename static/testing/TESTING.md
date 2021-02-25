## USER STORIES

_**As an employee I want:**_

1. - As a user, I want to virtually understand the main purpose of the site and understand the aim of the company services.

- **TEST**: When the site is opened, the home page presents a carousel slide with images related to the services the site hopes to achieve. The search part in the home page also gives the user an idea of the kind of projects we work with. For future development i will restrict the kind of information that can be displayed to a non-user. The current information is safe for an inhouse platform.


2.  - As a user, I want to easily sign up to the website.

- **TEST**: There are two buttons in the home page carousel redirecting to the Register and Sign Up page and the navigation is clearly stated with the same functionality.

3. - As a user, I want to easily Sign in on the site on all pages.

- **TEST**: The two big bright buttons is easily visible for the users to easily login into their accounts.

4. - As a user, I want to be able to and and write epics and user stories after a retrospective, so that if one team member is not available the work can be done.

- **TEST**: Having been registered and being able to login the user is permitted to add new epic list, edit all the added inputs and also delete such. This is open incase one of the members is not availble. 


5. - As a user, I want to view a list of epics and be able to edit or mark them done as per our team´s agreement of finished projects.

- **TEST**: Agile framework have processes that includes defining complete and considering a project done. This is supposed to be agreed upon by the team members and all must adhere to the promise of following it through. Once an epic is completed and after the final retrospective anyone in the team can tick click it as complete. The team share the process. 

6. - As a user, I want to see a list of epics and relevant details for epics so that i know what projets are not completed yet.

- **TEST**: As mention before, projects or epics in an agile team are put forward to the team to make decisions on deadlines and who will take what task.That means that all epics and stories must be transparent when released by the product manager and user stories will help to create the tasks and deadlines.

7. - As a user, I want to update or delete lists as per the team morals.

- **TEST**: There are buttons where the user can update or delete details and it helps if a team members is sick, out of work or just not available 


_**Developer**_

8. - As a developer, I want to provide a platform where the user can add epics. 

- **TEST**: The app provides an option for employees to add epics in the 

8. - As a developer, I want to provide a platform where the CRUD functionality if fulfilled to meet employee expectations.

- **TEST**: 

8. - As a developer, I want to provide a platform where user can see and share new and existing epics.

- **TEST**: 

8. - As a developer, I want to provide a platform which interacts with the users and alerts them, so that they can be aware of their actions.

- **TEST**: 

8. - As a developer, I want to create an enjoyable, and easy to use platform that makes the user enjoy using the site frequently.

- **TEST**: 



## Navigation links redirect to the desired pages
- Confirmed if all links in the navigation bar redirect to the desired pages.
- Tested if the social links on the footer redirect to the desired page.
- **Home Page**:
    - Tested if the Register button redirects to the Sign Up page.
    - Tested if the search button redirects to the seached epics. I have Tv advert as my epic name and it gave me the list.
- **Sign Up/Login Pages**:
    - Tested if the Sign-Up and Log in home page buttons redirect to the desired pages.
- **Employee Profile Page**:
    - Tested if Add Epic Button add data to mongoDB.
    - Tested if by clicking logo and image in employee welcome page redirects me back to home page.
- **View Epics page and Epics manager page**:
    - Confirmed if the Done, Edit and Delete button work properly.
- **Epic Category/products Page**:
    - Tested if the Add List Button add the epics to mongoDB when clicked.
    - Tested if by clicking the cancel page i get redirected to the same page.
- **search function**:
    - Tested if the search section on top of the epic list displays entered request and when reseted it functions well as desired:
    
    
## Pages contain all content and functionalities work as desired
### Home
- Functionality verified if the Sign-Up button only appears if the user is not already logged in. only Sign up and sign in together with home page should be visible.
### Sign Up/Log In
- Tested if when the user attempt to sign up or log in with a special character and ensure an error message displays for each input. 
- Consistant alerting the user of valid form input. 
- Tested if an invalid input flash message displays if the user enters a user that already exists or the incorrect username and/or password.

### Employee Profile
- Tested if a flash message welcoming the user when they sign in or register and redirecting them to welcoming employee page.
- Tested if the Add employee redirect user to register form if the want to help register another person and also adds that to database upon registering a new employee.

### View Epic list
- Tested if the Delete Epic functionality works well.
- Tested if the Edit Epic functionality is valid.
- Tested if the Search Epic functionality works ok.
- Tested if the Reset Epic list functionality works.
- Tested if the Edit button on each individual list accordion redirect user to edit epic form.
- Checked if entering a valid keyword the page returns the relevant content containing that keyword.

### Search Epics functionality
- Search functionality:
- Tested if when user click to submit with no entries in the search field a message display to the user fill in the field.
- Checked if entering a valid keyword the page returns the relevant content containing that keyword.

### 404
- Tested 404 page is displayed if navigate to an invalid link.
- Check if the Back to Home page button redirect to the home page.
### 500
- Tested if 500 page displays when an internal error happened.

## Responsive Test
- Checked the responsiveness of website on all screen sizes using different browsers(Google Chome, Opera, Firefox and Microsoft Edge)
- Using Devtools test if everything displays as it should from 300px width up to 1920px.
- Viewed of different physical devices: Iphone 8(375px), Iphone 11(414px), Iphone 5(320px), medium laptop(1280px) and large desktop screen(1920px).
- Repeat test in all pages.