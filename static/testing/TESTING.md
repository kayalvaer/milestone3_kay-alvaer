## USER STORIES

1. As a user, I want to easily understand the main purpose of the site and learn more about the organisation.

- **TEST**: After the users load the page the first thing sees on the home page is a brief explanation of what they will 
encounter on the website.

2. As a user, I want to easily to sign up to the website.

- **TEST**: Also in the home, there are two buttons redirecting to the Sign Up page and large screens and one button on small screens.

3. As a user, I want to easily log in on my account.

- **TEST**: With two clicks the users can easily login into their accounts.

4. As a user, I want to write personal summaries and main insights about the books I'm reading or already read

- **TEST**: After the user creates an account or login into it, they will be redirected to the Profile page, where they 
create personal book reviews, they write whatever they want in these reviews.

5. As a user, I want to create a list of books and share with other users.

- **TEST**: On the Best Books page, the users can create any lists of books they want. When creating the list they have 
the option to share it or not, if they decide to share, it will be seen by other users on the Discover page.

6. As a user, I want to find list of books from other people and get inspired to read other books.

- **TEST**: As mention before, on the Discover page the users can see lists of books shared by other users. Clicking 
on the lists the users will be redirected to a page where they can see the books. BY clicking on one of the books they will be 
redirect to a page where they can see the books in more detail and also buttons that will redirect to a vendor.

7. As a user, I want to easily find a way to buy the books in the lists.

- **TEST**: When the user adds a new book to a list, there is an input field where they can add the URL to a vendor, the 
users can add up to three vendors for future comparison.

8. As a user, I want to easily update or delete old book summaries and lists of books.

- **TEST**: There are buttons where the user can update or delete any book summary or list of books they want. It's important to 
say that if the user decides to share a list of books, only the creator of the list will be able to update or delete the list. 

## Navigation links redirect to the desired pages
- Checked if all links in the navigation bar and check if they redirect to the desired pages.
- Checked if the social links on the footer redirect to the desired page.
- **Home Page**:
    - Checked if the Sign-Up button redirects to the Sign Up page.
- **Sign Up/Login Pages**:
    - Checked if the Sign-Up and Log in anchor redirect to the desired pages.
- **Profile Page**:
    - Checked if Add Book Button display the Add Book modal when clicked.
    - Checked if by clicking and cover of the book reviews redirect to the desired page.
- **View Book Page**:
    - Checked if the Done, Edit and Delete button work properly.
- **Best Books Page**:
    - Checked if the Add List Button displays the Add List modal when clicked.
    - Checked if the See Books button redirects to the desired page:
    - Checked if by clicking in the list name the user is redirected to the same page if the user clicked in the See Books button.
- **View List Page**:
    - Checked if the Done, Edit and Delete button work properly.
    - Checked if the user is redirected to the correct page when clicking and a book cover.
- **Book Info Page**:
    - Checked if the Done, Edit and Delete button work properly.
    - Checked if the buy buttons redirect to the desired pages.
- **Discover Page**:
    - Checked if the See Books button redirects to the desired page:
    - Checked if by clicking in the list name the user is redirected to the same page if the user clicked in the See Books button.
    
## Pages contain all content and functionalities work as desired
### Home
- Verified if the Sign-Up button only appears if the user is not already logged in.
### Sign Up/Log In
- Checked if a user attempt to sign up or log in with a special character and ensure an error message displays for each field 
alerting the user of valid form input. 
- Checked if a flash message displays if the user enters a user that already exists or the incorrect username and/or password.
### Profile
- Checked if a flash message encouraging the user to add the first book summary after sign up displays.
![Message been displayed when a new user login into their account for the first time](../images/testing/new_user.png)
- Checked if the Add Book modal works and add the book summary into the database.
- Checked in the random quotes displays randomly on large screens.
### View Book
- Checked if the delete book functionality works.
- Checked if the edit book functionality works.
### Best Books
- Checked if a message, encouraging the user to create their first list, displays when the user hasn't created the first list yet.
![Message been displayed when user haven't created a list yet](../images/testing/new_user_list.png)
- Checked if the "share" option is on the list will appear in the Discover Page.
### View List
- Checked if the modal add book into the list works.
- Checked if the delete list functionality works.
- Checked if the edit list functionality works.
### Discover
- Search functionality:
    - Checked if when click to submit with no entries in the search field a message display to the user fill in the field.
    - Checked if entering a valid keyword the page returns the relevant content containing that keyword.
    - Checked if entering a non-valid the keyword the page returns "No results found".
    - Checked if the Reset button resets the page when clicked as desired.
- Check if "Unfortunately, username hasn't added any book to the list yet." message is been displayed when a list is been shared 
but has no book in it yet.
- Checked if when the user is redirected to the View List page the Add Book, Edit and Delete buttons are not been displayed as 
only the creator of the list can use these buttons.
- Made the same test as the above in the Book Info page.
### 404
- Verified 404 page is displayed if navigate to an invalid link.
- Check if the Bring Me Back button redirect to the home page.
### 500
- Verified if 500 page displays when an internal error happened.

## Responsive Test
- Test responsiveness of website on all screen sizes using different browsers(Google Chome, Opera, Firefox and Microsoft Edge)
    - Using Devtools test if everything displays as it should from 300px width up to 1920px.
- Viewed of different physical devices: Iphone 8(375px), Iphone 11(414px), Xiaomi Redmi 9(393px), medium laptop(1280px), 
large desktop screen(1920px).
- Repeat test in all pages.