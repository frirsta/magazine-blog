# Magazine 
Magazine is a website where people share and get inspired by interior designs. The website is targeted toward those who want to share, read and learn about interior design. The website is useful for those who want to know what is trending right now. 
All website users can create an account and share what their homes look like or anything regarding interior design.

The website owner can delete comments and posts, if it is inappropriate. This is done from the Admin Dashboard that is only accessible to the Website owner when they log in.
This is the live link to [Magazine](https://magazine-blog-frirsta.herokuapp.com/)

<img src="readme/all_devices.png" alt="website on all devices" style="width: 100%">


* [**Project**](<#Project>)
* [**Project Management**](<#Project-Management>)
* [**Wireframes**](<#Wireframes>)
* [**User Experience UX**](<#user-experience-ux>)
* [**Features**](<#Features>)
* [**Features left to Implement**](<#Features-left-to-Implement>)
* [**Testing**](<#Testing>)
* [**Technologies Used**](<#Technologies-Used>)
* [**Unfixed Bugs**](<#Unfixed-Bugs>)
* [**Deployment**](<#Deployment>)
* [**Credits**](<#Credits>)
* [**Acknowledgement**](<#Acknowledgement>)

# Project

## Site Owner Goal
The site's Owner's goal is to have a website where people who love interior design can have a space to read about and share their own tips and tricks about interior design. The website will have people inspired and people who inspire.

<br>

## Site User Goal
The site's user goal is to have a place to read about and share their own tips and tricks about interior design.

<br>

# Project Management
I have used the github project board to work with the blog.
<details><summary>GitHub Board</summary>
<img src="readme/github_board.png" alt="github board" style="width: 100%">
</details>
<br>

### Models Graph
I have used Graph models to render a graphical overview of the blog models. It shows how the models are connected to each other in the database.
I used [Dreampuf](https://dreampuf.github.io/GraphvizOnline/#digraph%20G%20%7B%0A%0A%20%20subgraph%20cluster_0%20%7B%0A%20%20%20%20style%3Dfilled%3B%0A%20%20%20%20color%3Dlightgrey%3B%0A%20%20%20%20node%20%5Bstyle%3Dfilled%2Ccolor%3Dwhite%5D%3B%0A%20%20%20%20a0%20-%3E%20a1%20-%3E%20a2%20-%3E%20a3%3B%0A%20%20%20%20label%20%3D%20%22process%20%231%22%3B%0A%20%20%7D%0A%0A%20%20subgraph%20cluster_1%20%7B%0A%20%20%20%20node%20%5Bstyle%3Dfilled%5D%3B%0A%20%20%20%20b0%20-%3E%20b1%20-%3E%20b2%20-%3E%20b3%3B%0A%20%20%20%20label%20%3D%20%22process%20%232%22%3B%0A%20%20%20%20color%3Dblue%0A%20%20%7D%0A%20%20start%20-%3E%20a0%3B%0A%20%20start%20-%3E%20b0%3B%0A%20%20a1%20-%3E%20b3%3B%0A%20%20b2%20-%3E%20a3%3B%0A%20%20a3%20-%3E%20a0%3B%0A%20%20a3%20-%3E%20end%3B%0A%20%20b3%20-%3E%20end%3B%0A%0A%20%20start%20%5Bshape%3DMdiamond%5D%3B%0A%20%20end%20%5Bshape%3DMsquare%5D%3B%0A%7D) to translate the DOT language into the graph.

<img src="readme/graphviz.png" alt="github board" style="width: 100%">

# Wireframes
I have used [Miro](https://miro.com/) to create WireFrames for the project.
The website have some differences.
<details><summary>Wireframes</summary>

<div style="display: flex; align-items: flex-start;">
<img src="readme/home_desktop.jpg" alt="home page on desktop screen" style="width: 40%">
<img src="readme/home_ipad.jpg" alt="home page on ipad screen" style="width: 30%">
<img src="readme/home_phone.jpg" alt="home page on phone screen" style="width: 20%">
</div>

<br>

<div style="display: flex; align-items: flex-start;">
<img src="readme/blog_desktop.jpg" alt="blog page on desktop screen" style="width: 40%">
<img src="readme/blog_ipad.jpg" alt="blog page on ipad screen" style="width: 30%">
<img src="readme/blog_phone.jpg" alt="blog page on phone screen" style="width: 20%">
</div>

<div style="display: flex; align-items: flex-start;">
<img src="readme/post_detail_desktop.jpg" alt="post_detail page on desktop screen" style="width: 40%">
<img src="readme/post_detail_ipad.jpg" alt="post_detail page on ipad screen" style="width: 30%">
<img src="readme/post_detail_phone.jpg" alt="post_detail page on phone screen" style="width: 20%">
</div>


<img src="readme/signup.jpg" alt="signup page on all screens" style="width: 100%">

<img src="readme/login.jpg" alt="login page on all screens" style="width: 100%">

<img src="readme/profile.jpg" alt="profile page on all screens" style="width: 100%">

<img src="readme/edit_profile.jpg" alt="profile page on all screens" style="width: 100%">

<img src="readme/create_post.jpg" alt="create post page on all screens" style="width: 100%">

<div style="display: flex; align-items: flex-start;">
<img src="readme/change_password_desktop.jpg" alt="change_password page on desktop screen" style="width: 40%">
<img src="readme/change_password_ipad.jpg" alt="change_password page on ipad screen" style="width: 30%">
<img src="readme/change_password_phone.jpg" alt="change_password page on phone screen" style="width: 20%">
</div>

<p>

#### Wireframes
</p>
</details>
<br>

# User Experience (UX)
## Site User

| User/Admin | Description |
| --- | --- |
| Site User | As a Site User I can View posts so that I can select one to read |
| Site User | As a site user I can read comments that are made for a specific post so that I can read what people think of the post |
| Site User | As a Site User I can create an account so that I can comment and create content |
| Site User | As a Site User I can create a post so that I can make content for the blog |
| Site User | As a Site User I can comment posts so that I can write what I think about the post and interact with other blog readers |
| Site User | As a site user I can delete comments I have made so that I have control over my comments, and can remove them if I change my mind on the comments |
| Site User | As a Site user I can go to a profile page specifically for me so that I can find all posts created by me |
| Site User | As a Site User I can login so that I can create content for the blog that is connected to my account |
| Site User | As a Site User I can logout so that someone else using my computer can't post from my account |

<br>

## Site Owner

| User/Admin | Description |
| --- | --- |
| Site Owner | All Site User stories apply to the Site Owner |
| Site Owner | As a Site Owner I can go to the Admin Dashboard where I can find all posts made and information about them |
| Site Owner | As a Site Owner I can find all posts and all comments created in one page so that I can manage the content on the website |
| Site Owner | As a Site Owner I can go to the Admin Dashboard where I can find all comments made and information about them |
| Site Owner | As a Site Owner I can I can delete the posts and comments from the admin page so that I can manage a secure environment for the users |

<br>

# Features
<br>

### Features on all pages
* Navigation Bar
  * Featured on all pages. The navigation bar includes links to the logo, homepage, blog page, login page and SignUp page.
  * This allows the user to easily navigate through the website.
  * When the user is logged in the navigation bar also links to Create Post page, Profile page, and it has a Log out link so the user can easily log out from their account.
  * When the website owner is logged in the same links as the logged in user will display as well as an Admin link for the Admin dashboard.
<br>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/navbar.png" alt="navbar page when no user is logged in" style="width: 30%">
<img src="readme/pages/navbar_user.png" alt="navbar page when user is logged in" style="width: 30%">
<img src="readme/pages/navbar_admin.png" alt="navbar page when admin is logged in" style="width: 30%">
</div>

* The footer
  * The footer links to Magazine's social media accounts.
  <div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/footer_mobile.png" alt="footer on mobile screen" style="width: 30%">
<img src="readme/pages/footer_ipad.png" alt="footer on ipad screen" style="width: 30%">
<img src="readme/pages/footer_desktop.png" alt="footer on desktop screen" style="width: 30%">
</div>

### The Landing/home page
  * The landing page has an image of furniture and text that says 'MAGAZINE' and 'Interior & Lifestyle' This lets the user know what the website is about.
  * The home page displays the six latest posts made so the user can see what the latest interior trends are and also so they can see examples of what type of content they will find on the page. 
<br>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/home_mobile.png" alt="home page on mobile screen" style="width: 20%">
<img src="readme/pages/home_ipad.png" alt="home page on ipad screen" style="width: 30%">
<img src="readme/pages/home_desktop.png" alt="home page on desktop screen" style="width: 48%">
</div>
 
### Blog
 * The blog page displays all posts made with the latest ones on top of the page.
 <br>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/blog_mobile.png" alt="blog page on mobile screen" style="width: 20%">
<img src="readme/pages/blog_ipad.png" alt="blog page on ipad screen" style="width: 30%">
<img src="readme/pages/blog_desktop.png" alt="blog page on desktop screen" style="width: 48%">
</div>

### Post detail
* When the user chooses a blog to read they get redirected to the blog posts detail page where they can read the full post.
* They can also read comments and leave comments.
 <br>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/post_detail_mobile.png" alt="post_detail page on mobile screen" style="width: 20%">
<img src="readme/pages/post_detail_ipad.png" alt="post_detail page on ipad screen" style="width: 30%">
<img src="readme/pages/post_detail_desktop.png" alt="post_detail page on desktop screen" style="width: 48%">
</div>

#### Comment section
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/comment_mobile.png" alt="comment page on mobile screen" style="width: 20%">
<img src="readme/pages/comment_ipad.png" alt="comment page on ipad screen" style="width: 30%">
<img src="readme/pages/comment_desktop.png" alt="comment page on desktop screen" style="width: 48%">
</div>

### Sign up
* The SignUp page displays a form where the user writes their information to create an account.
<br>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/signup_mobile.png" alt="signup page on mobile screen" style="width: 20%">
<img src="readme/pages/signup_ipad.png" alt="signup page on ipad screen" style="width: 30%">
<img src="readme/pages/signup_desktop.png" alt="signup page on desktop screen" style="width: 48%">
</div>

### Log in
* The log in page displays a form where the user writes their username and password to log in to their account.
<br>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/login_mobile.png" alt="login page on mobile screen" style="width: 20%">
<img src="readme/pages/login_ipad.png" alt="login page on ipad screen" style="width: 30%">
<img src="readme/pages/login_desktop.png" alt="login page on desktop screen" style="width: 48%">
</div>

### Profile
* The profile page displays the user profile picture, user bio and three buttons.
    * The Edit Profile button leads to the edit profile page where they can add a profile picture and write text about themselves.
    * The Change password button leads to a page where they can change their password.
    * The My Posts button leads to a page where they can find all posts they have created.
    <br>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/profile_mobile.png" alt="profile page on mobile screen" style="width: 20%">
<img src="readme/pages/profile_ipad.png" alt="profile page on ipad screen" style="width: 30%">
<img src="readme/pages/profile_desktop.png" alt="profile page on desktop screen" style="width: 48%">
</div>

### User posts
* The logged in user can find all the posts they have created in this page.
<br>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/user_posts_mobile.png" alt="user_posts page on mobile screen" style="width: 20%">
<img src="readme/pages/user_posts_ipad.png" alt="user_posts page on ipad screen" style="width: 30%">
<img src="readme/pages/user_posts_desktop.png" alt="user_posts page on desktop screen" style="width: 48%">
</div>

### Change Password
* The change password page is where the user can change their password.
<br>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/change_password_mobile.png" alt="change_password page on mobile screen" style="width: 20%">
<img src="readme/pages/change_password_ipad.png" alt="change_password page on ipad screen" style="width: 30%">
<img src="readme/pages/change_password_desktop.png" alt="change_password page on desktop screen" style="width: 48%">
</div>

### Edit Profile
The edit profile page is where the user can add a profile picture, change username and write text about themselves.
<br>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/edit_profile_mobile.png" alt="edit_profile page on mobile screen" style="width: 20%">
<img src="readme/pages/edit_profile_ipad.png" alt="edit_profile page on ipad screen" style="width: 30%">
<img src="readme/pages/edit_profile_desktop.png" alt="edit_profile page on desktop screen" style="width: 48%">
</div>

### Create Post
* In the create post page a user can create a post by adding text and image to the create post form. The form has four fields.
    * Title | Name of the blog post.
    * Article description | Description of the article. This is the first thing the user reads before deciding what post to read more about.
    * Content | The post content.
    * Image | The image that will be posted with the post text content.
<br>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/create_post_mobile.png" alt="create_post page on mobile screen" style="width: 20%">
<img src="readme/pages/create_post_ipad.png" alt="create_post page on ipad screen" style="width: 30%">
<img src="readme/pages/create_post_desktop.png" alt="create_post page on desktop screen" style="width: 48%">
</div>

### Admin Dashboard
* In the admin the website owner can see how many posts have been made, how many accounts have been created and how many comments have been made.
* On this page the owner can find all posts, who the author is, the title, the article description, the date it was created and the content.
    * The owner can Delete posts from this page.
* On this page the owner can find all the comments, the name of who has created the comment, the date the comment was created, the comment content, and what post it was commented on.
    * The owner can delete comments from this page.
<br>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/admin_mobile.png" alt="admin page on mobile screen" style="width: 20%">
<img src="readme/pages/admin_ipad.png" alt="admin page on ipad screen" style="width: 30%">
<img src="readme/pages/admin_desktop.png" alt="admin page on desktop screen" style="width: 48%">
</div>

### 404 page
* This is the page the user get redirected to if the website does not exist.
<br>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/404_mobile.png" alt="404 page on iphonese screen" style="width: 20%">
<img src="readme/pages/404_ipad.png" alt="404 page on ipadair screen" style="width: 30%">
<img src="readme/pages/404_desktop.png" alt="404 page on desktop screen" style="width: 48%">
</div>

# Features left to Implement
* Add more automated testing
* Add search functionality so the user can find posts or other users.

# Testing
[HTML validator](https://validator.w3.org/)
<img src="readme/testing/html_validator.png" alt="html validator" style="width: 100%">
[CSS validator](https://jigsaw.w3.org/css-validator/)
<img src="readme/testing/css_validator.png" alt="css validator" style="width: 100%">
[Jshint](https://jshint.com/)
<img src="readme/testing/js_validator.png" alt="js validator" style="width: 100%">

## Responsiveness Testing
I have tested the responsiveness manually with [DevTool](https://developer.chrome.com/docs/devtools/)

## Browser Compatibility

### Microsoft Edge 109.0.1518.61
### Google Chrome 109.0.5414.75
### Apple Safari 14.2.1

[Code Institute Pep8](https://pep8ci.herokuapp.com/)
<details><summary>Pep8</summary>

## Pep8
### admin.py file
<img src="readme/testing/pep8/pep8_admin.png" alt="python validator admin file" style="width: 100%">

<br>

### forms.py file
<img src="readme/testing/pep8/pep8_forms.png" alt="python validator forms file" style="width: 100%">

<br>

### models.py file
<img src="readme/testing/pep8/pep8_models.png" alt="python validator models file" style="width: 100%">

<br>

### signals.py file
<img src="readme/testing/pep8/pep8_signals.png" alt="python validator signals file" style="width: 100%">

<br>

### urls.py file
<img src="readme/testing/pep8/pep8_urls.png" alt="python validator urls file" style="width: 100%">

<br>

### views.py file
<img src="readme/testing/pep8/pep8_views.png" alt="python validator views file" style="width: 100%">
</details>

## Lighthouse
The website has also been tested with the Chrome developer tool Google Lighthouse. It has been tested for desktop and for mobile. What was tested:

* Performance
* Accessibility
* Best Practices
* SEO (Search engine optimisation)
<br>
<details><summary>Lighthouse</summary>

### Home page 
#### Desktop
<img src="readme/testing/lighthouse/home_desktop.png" alt="lighthouse score for home page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/home_mobile.png" alt="lighthouse score for home page on mobile device" style="width: 100%">

<br>

### Blog page 
#### Desktop
<img src="readme/testing/lighthouse/blog_desktop.png" alt="lighthouse score for blog page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/blog_mobile.png" alt="lighthouse score for blog page on mobile device" style="width: 100%">

### Signup page 
#### Desktop
<img src="readme/testing/lighthouse/signup_desktop.png" alt="lighthouse score for signup page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/signup_mobile.png" alt="lighthouse score for signup page on mobile device" style="width: 100%">

### Login page 
#### Desktop
<img src="readme/testing/lighthouse/login_desktop.png" alt="lighthouse score for login page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/login_mobile.png" alt="lighthouse score for login page on mobile device" style="width: 100%">

### Create post page 
#### Desktop
<img src="readme/testing/lighthouse/create_post_desktop.png" alt="lighthouse score for create_post page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/create_post_mobile.png" alt="lighthouse score for create_post page on mobile device" style="width: 100%">

### Profile page 
#### Desktop
<img src="readme/testing/lighthouse/profile_desktop.png" alt="lighthouse score for profile page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/profile_mobile.png" alt="lighthouse score for profile page on mobile device" style="width: 100%">

### Edit profile page 
#### Desktop
<img src="readme/testing/lighthouse/edit_profile_desktop.png" alt="lighthouse score for edit_profile page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/edit_profile_mobile.png" alt="lighthouse score for edit_profile page on mobile device" style="width: 100%">

### Change password page 
#### Desktop
<img src="readme/testing/lighthouse/change_password_desktop.png" alt="lighthouse score for change_password page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/change_password_mobile.png" alt="lighthouse score for change_password page on mobile device" style="width: 100%">

### User posts page 
#### Desktop
<img src="readme/testing/lighthouse/user_posts_desktop.png" alt="lighthouse score for user_posts page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/user_posts_mobile.png" alt="lighthouse score for user_posts page on mobile device" style="width: 100%">

### Admin page 
#### Desktop
<img src="readme/testing/lighthouse/admin_desktop.png" alt="lighthouse score for admin page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/admin_mobile.png" alt="lighthouse score for admin page on mobile device" style="width: 100%">


</details>

<br>

### Testing with Coverage
Due to prioritizing other tasks, I haven't had time for a lot of testing. Using Coverage, I have tested the Post model. The coverage report shows that 70% of testing has been done.
Below are images of the steps taken for testing the Post model in chronological order
<details><summary>Coverage</summary>

<img src="readme/testing/coverage/1.png" alt="Step 1 of the testing process with coverage" style="width: 70%">

<img src="readme/testing/coverage/2.png" alt="Step 2 of the testing process with coverage" style="width: 70%">

<img src="readme/testing/coverage/3.png" alt="Step 3 of the testing process with coverage" style="width: 70%">

<img src="readme/testing/coverage/4.png" alt="Step 4 of the testing process with coverage" style="width: 70%">

<img src="readme/testing/coverage/5.png" alt="Step 5 of the testing process with coverage" style="width: 70%">
</details>

# Technologies Used
* Python - For functionality of the website
* JavaScript - Used to make website interactive
* Django - Model-View-Template framework
* HTML5 - For structure of the website
* CSS3 - For styling of the website
* GitHub - Used to host the website
* GitPod - For deployment of the website
* [Miro](https://miro.com/) - For creating the Wireframes
* Bootstrap - CSS framwork
* Heroku - The platform where the application is deployed

## Libraries
* pip3 install Pillow -  For ImageField in models.py
* pip3 install 'django<4' gunicorn - Installs Django and Gunicorn is the server that will run in heroku, handles everything that happens between the web server and the web application
* pip3 install dj_database_url==0.5.0 psycopg2 - Installs PostgreSQL and psycopg2
* pip3 install dj3-cloudinary-storage - Cloudinary handles all the static files and the images uploaded by users
* pip install pyparsing pydot - To create a graph of the database
* pip install django-extensions - Supporting library of Graph models
* pip install coverage

# Unfixed Bugs

# Deployment

This website was deployed to [Heroku](https://heroku.com/). To deploy the website follow the steps below:


1. Create a GitHub repository from the Code Institute template and click 'Use this template'.
<details><summary>Heroku Deployment - Step 1:</summary>
<img src="readme/deployment/step-1.png" alt="step of deployment" style="width: 100%">
</details>
<br>

2. Add a repository name and then click 'Create repository from template'.
<details><summary>Heroku Deployment - Step 2:</summary>
<img src="readme/deployment/step-2.png" alt="step of deployment" style="width: 100%">
</details>
<br>

3. When the repository is created, click 'Gitpod'.
<details><summary>Heroku Deployment - Step 3:</summary>
<img src="readme/deployment/step-3.png" alt="step of deployment" style="width: 100%">
</details>
<br>

4. In the terminal type the following commands to install Django and its supporting libraries:
* pip3 install 'django<4' gunicorn
* pip3 install dj_database_url==0.5.0 psycopg2
* pip3 install dj3-cloudinary-storage

<details><summary>Heroku Deployment - Step 4:</summary>
<img src="readme/deployment/deployment-1.png" alt="'pip3 install 'django<4' gunicorn' typed in the terminal" style="width: 100%">
<img src="readme/deployment/deployment-2.png" alt="'pip3 install dj_database_url==0.5.0 psycopg2' typed in the terminal" style="width: 100%">
<img src="readme/deployment/deployment-3.png" alt="'pip3 install dj3-cloudinary-storage typed' in the terminal" style="width: 100%">
</details>
<br>

5. After the libraries have been installed, type the following command to create a requirements.txt file:
* pip3 freeze --local > requirements.txt
<details><summary>Heroku Deployment - Step 5:</summary>
<img src="readme/deployment/deployment-4.png" alt="'pip3 freeze --local > requirements.txt' typed in the terminal" style="width: 100%">
<img src="readme/deployment/step-5.png" alt="step of deployment" style="width: 100%">
</details>

<br>

6. Create the Django project by typing the following command:
* "django-admin startproject PROJECT_NAME ." - Don't forget the dot at the end.
<details><summary>Heroku Deployment - Step 6:</summary>
<img src="readme/deployment/step-6.png" alt="step of deployment" style="width: 100%">
After typing the command this 'blog' folder with files will be displayed in the directory.
<img src="readme/deployment/step-7.png" alt="step of deployment" style="width: 100%">
</details>
  
<br>

7. Create the Django application by typing the following command:
* "python3 manage.py startapp APP_NAME"
<details><summary>Heroku Deployment - Step 7:</summary>
<img src="readme/deployment/step-8.png" alt="step of deployment" style="width: 100%">
After typing the command this 'magazine' with files will be displayed in the directory.
<img src="readme/deployment/step-9.png" alt="step of deployment" style="width: 100%">
</details>

<br>

8. Now the application needs to be added in settings.py. Add the application name to the 'INSTALLED_APPS' section as shown in the following image.
<details><summary>Heroku Deployment - Step 8:</summary>
<img src="readme/deployment/step-10.png" alt="step of deployment" style="width: 100%">
</details>
<br>

9. Next, the first migrations will be made. 
In the terminal type:
* python3 manage.py migrate
<details><summary>Heroku Deployment - Step 9:</summary>
<img src="readme/deployment/step-11.png" alt="step of deployment" style="width: 100%">
</details>  
<br>


10. To see if everything works as expected. In the terminal type:
* 'python3 manage.py runserver' and click 'Open Browser'.
<details><summary>Heroku Deployment - Step 10:</summary>
<img src="readme/deployment/step-12.png" alt="step of deployment" style="width: 100%">
 
<br>

This is what the website will look like.
<img src="readme/deployment/step-13.png" alt="step of deployment" style="width: 100%">
</details>  

<br>

### These following images show the steps taken to create the application on Heroku, connect the database and create the environment. The deployment to GitHub from Heroku will also be shown. 

Create or login to [Heroku](https://www.heroku.com/)

11. On the heroku Website click 'New' and after click 'Create new app'.
<details><summary>Heroku Deployment - Step 11:</summary>
<img src="readme/deployment/step-14.png" alt="step of deployment" style="width: 100%">
</details>  

<br>

12. Write the app name, choose a region and then click 'Create app'. 
<details><summary>Heroku Deployment - Step 12:</summary>
<img src="readme/deployment/step-15.png" alt="step of deployment" style="width: 100%">
</details>  
<br>

13. In the application website click 'Deploy' on the navigation menu.
<details><summary>Heroku Deployment - Step 13:</summary>
<img src="readme/deployment/step-16.png" alt="step of deployment" style="width: 100%">
</details>  
<br>

14. In the 'Deploy' page, follow these steps as shown on the image:
    1. Click the GitHub logo.
    2. Search for the GitHub repository that was made for this project.
    3. When the repository is found click 'Connect'.
  <details><summary>Heroku Deployment - Step 14:</summary>
<img src="readme/deployment/step-17.png" alt="step of deployment" style="width: 100%">
<br>
When the repository is connected, this is what the page look like.
<img src="readme/deployment/step-18.png" alt="step of deployment" style="width: 100%">
</details>

</br>

### Create database
The database used in this website has been created with [ElephantSQL](https://www.elephantsql.com/) and the steps below show how.

15. Start by clicking 'Create New Instance'.
<details><summary>Heroku Deployment - Step 15:</summary>
<img src="readme/deployment/elephantsql.png" alt="step of deployment" style="width: 100%">
</details> 

<br>

16. Enter a name for the database and then click 'Select Region'.
<details><summary>Heroku Deployment - Step 16:</summary>
<img src="readme/deployment/step-19.png" alt="step of deployment" style="width: 100%">
</details>  
<br>

17. Select a region and then click Review.
<details><summary>Heroku Deployment - Step 17:</summary>
<img src="readme/deployment/step-20.png" alt="step of deployment" style="width: 100%">
</details>  
<br>

18. Review the information and click 'Create Instance'.
<details><summary>Heroku Deployment - Step 18:</summary>
<img src="readme/deployment/step-21.png" alt="step of deployment" style="width: 100%">
</details>  
<br>

19. When the instance is created, it will be displayed on top of the list of created instances.
Click the instance that has been created.
<details><summary>Heroku Deployment - Step 19:</summary>
<img src="readme/deployment/step-22.png" alt="step of deployment" style="width: 100%">
</details>
<br>

20. Copy the Url.
<details><summary>Heroku Deployment - Step 20:</summary>
<img src="readme/deployment/step-23.png" alt="step of deployment" style="width: 100%">
</details> 
<br>

21. In GitPod create an 'env.py' file in the top level directory.
<details><summary>Heroku Deployment - Step 21:</summary>
<img src="readme/deployment/step-24.png" alt="step of deployment" style="width: 100%">
</details> 
<br>

22. In the 'env.py' file add the following text.
<details><summary>Heroku Deployment - Step 22:</summary>
<img src="readme/deployment/step-25.png" alt="step of deployment" style="width: 100%">
</details> 
<br>

23. Add the following text in the env.py file:
* Import os
* os.environ["DATABASE_URL"]
* Paste the url that was copied earlier in the red area that is shown below.
<details><summary>Heroku Deployment - Step 23:</summary>
<img src="readme/deployment/step-26.png" alt="step of deployment" style="width: 100%">
</details> 
  
<br>

24. In the 'settings' file, copy the value of 'SECRET_KEY' (The secret key is removed from the image because it has to be kept secret).
<details><summary>Heroku Deployment - Step 24:</summary>
<img src="readme/deployment/step-27.png" alt="step of deployment" style="width: 100%"> 
</details>
<br>

25. Add the following text in the env.py file:
* os.environ["SECRET_KEY"]
* Paste the "SECRET_KEY" value that was copied from the 'settings.py' as value for 'os.environ["SECRET_KEY"]'.
<details><summary>Heroku Deployment - Step 25:</summary>
<img src="readme/deployment/step-28.png" alt="step of deployment" style="width: 100%"> 
</details>
<br>

26. Add the following text on top of the 'setting.py' file:
* import os
* import dj_database_url
* <pre>if os.path.isfile('env.py'):
        import os</pre>
<details><summary>Heroku Deployment - Step 26:</summary>
<img src="readme/deployment/step-29.png" alt="step of deployment" style="width: 100%"> 
</details>
<br>

27. Replace the value of 'SECRET_KEY' in the 'settings.py' file and add the following text:
* os.environ.get('SECRET_KEY')
<details><summary>Heroku Deployment - Step 27:</summary>
<img src="readme/deployment/step-30.png" alt="step of deployment" style="width: 100%"> 
</details>
<br>

28. Comment out the database that is in the 'settings.py' file and add the following text to connect the new database:

  <details><summary>Heroku Deployment - Step 28:</summary>
<img src="readme/deployment/step-31.png" alt="step of deployment" style="width: 100%"> 
</details>
<br>

29. Save all the files and in the terminal type the following command to migrate the changes:
* python3 manage.py migrate.
<details><summary>Heroku Deployment - Step 29:</summary>
<img src="readme/deployment/step-32.png" alt="step of deployment" style="width: 100%"> 
</details>
<br>

30. In the [ElephantSQL](https://www.elephantsql.com/) database click 'Browser'.
<details><summary>Heroku Deployment - Step 30:</summary>
<img src="readme/deployment/step-33.png" alt="step of deployment" style="width: 100%"> 
</details>
<br>

31. In the 'Browser' page, click 'Table queries' and if everything works as expected the database will be displayed.
<details><summary>Heroku Deployment - Step 31:</summary>
<img src="readme/deployment/step-34.png" alt="step of deployment" style="width: 100%"> 
</details>

<br>

32. In the application in Heroku click 'Settings' in the navigation menu. After click 'Reveal Config Vars'. Add the 'DATABASE_URL' and the 'SECRET_KEY', and in the red area add their values.
<details><summary>Heroku Deployment - Step 32:</summary>
<img src="readme/deployment/step-35.png" alt="step of deployment" style="width: 100%"> 
</details>
<br>

### [Cloudinary](https://cloudinary.com/) has been used for image management and the steps below show how the website has been connected to [Cloudinary](https://cloudinary.com/).

Create an account or log in.

<br>

33. In 'API Environment variable' copy the value as shown below.
<details><summary>Heroku Deployment - Step 33:</summary>
<img src="readme/deployment/step-36.png" alt="step of deployment" style="width: 100%">
</details> 
<br>

34. In the 'env.py' file add 'os.environ["CLOUDINARY_URL"]' and paste the link that was copied from Cloudinary.
<details><summary>Heroku Deployment - Step 34:</summary>
<img src="readme/deployment/step-37.png" alt="step of deployment" style="width: 100%">
</details> 
<br>

35. In the 'settings.py' file add 'cloudinary_storage' and 'cloudinary' as shown below to 'INSTALLED_APPS'.
The apps have to be written in the following order:
    1. 'cloudinary_storage'
    2. 'django.contrib.staticfiles'
    3. 'cloudinary'
<details><summary>Heroku Deployment - Step 35:</summary>
<img src="readme/deployment/step-38.png" alt="step of deployment" style="width: 100%">
</details> 
<br>

36. Add the following text in the 'settings.py' file to tell Django where to store static files.
<details><summary>Heroku Deployment - Step 36:</summary>
<img src="readme/deployment/step-39.png" alt="step of deployment" style="width: 100%">
</details> 
<br>

37. Add the following text as shown below in the 'settings.py' file to connect the templates folder.
<details><summary>Heroku Deployment - Step 37:</summary>
<img src="readme/deployment/step-40.png" alt="step of deployment" style="width: 100%">
</details> 
<br>

38. Add 'TEMPLATES_DIR' as the 'DIRS' value in 'TEMPLATES' as shown below.
<details><summary>Heroku Deployment - Step 38:</summary>
<img src="readme/deployment/step-41.png" alt="step of deployment" style="width: 100%">
</details> 
<br>

39. In the 'ALLOWED_HOSTS' add the Heroku app and localhost.
<details><summary>Heroku Deployment - Step 39:</summary>
<img src="readme/allowed_hosts.png" alt="step of deployment" style="width: 100%">
</details> 
<br>

40. Create these folders in the top level directory:
* media
* templates
* static
<details><summary>Heroku Deployment - Step 40:</summary>
<img src="readme/deployment/step-43.png" alt="step of deployment" style="width: 100%">
</details> 
<br>

41. In the application in Heroku in 'Config Vars'. Add 'CLOUDINARY_URL' and as value (the red area) add the url. Also, add the following keys and values:
* key: PORT - value: 8000
* key: DISABLE_COLLECTSTATIC - value: 1
<details><summary>Heroku Deployment - Step 41:</summary>
<img src="readme/deployment/step-44.png" alt="step of deployment" style="width: 100%">
</details> 
<br>

42. Create a 'Procfile' file in the top level directory.
<details><summary>Heroku Deployment - Step 42:</summary>
<img src="readme/deployment/step-44.png" alt="step of deployment" style="width: 100%">
</details> 
<br>

43. In the 'Procfile' file add the following text:
* web: gunicorn PROJECT_NAME.wsgi
<details><summary>Heroku Deployment - Step 43:</summary>
<img src="readme/deployment/step-45.png" alt="step of deployment" style="width: 100%">
</details>
<br>


Save all the files and add, commit and push the project to GitHub by writing these commands:
* git add .
* git commit -m "Deployment Commit"
* git push

44. In the application in Heroku navigate to the deploy page and scroll to the bottom of the page.
<details><summary>Heroku Deployment - Step 44:</summary>
<img src="readme/deployment/step-46.png" alt="step of deployment" style="width: 100%">
</details> 
<br>


45. Click 'Deploy Branch' and wait for the GitHub branch to be deployed and then click 'View App'.
<details><summary>Heroku Deployment - Step 45:</summary>
<img src="readme/deployment/step-48.png" alt="step of deployment" style="width: 100%">
</details> 
<br>

46. This is what the app will look like when it's successfully deployed.
<details><summary>Heroku Deployment - Step 46:</summary>
<img src="readme/deployment/step-49.png" alt="step of deployment" style="width: 100%">
</details> 

<br>


# Credits
Sources that have helped build the website:

[Django blog tutorial](https://dontrepeatyourself.org/post/django-blog-tutorial-part-1-project-configuration/)
In the python files I have left a comment ("# Rouizi") above the functions that I have gotten from the blog tutorial.
<br>
[Class-Based Views](https://ccbv.co.uk/)
From this website I have gotten methods and attributes for the class-based views.

### Content
[Icons8](https://icons8.com/) - Favicon

### Images
[Default Profile Image by rawpixel.com](https://www.rawpixel.com/image/6012980/illustration-png-social-media-logo)
<br>
[Hero Image by Nugroho  Wahyu](https://www.pexels.com/sv-se/foto/inne-tra-design-rum-3119180/)

Bild av Element5 Digital: https://www.pexels.com/sv-se/foto/tra-lampor-skrivbord-lampa-1125136/
Bild av Taryn Elliott: https://www.pexels.com/sv-se/foto/sovrum-interior-heminredning-skandinavisk-4440213/
Bild av Polina Kovaleva: https://www.pexels.com/sv-se/foto/sang-sovrum-lampa-design-5644277/
Bild av Emre Can Acer: https://www.pexels.com/sv-se/foto/tra-bocker-hus-bord-2079249/
Bild av Maksim Goncharenok: https://www.pexels.com/sv-se/foto/tra-vagg-bord-lyx-4352247/
Bild av Jean van der Meulen: https://www.pexels.com/sv-se/foto/hotell-hus-glas-lyx-1457847/
Bild av PNW Production: https://www.pexels.com/sv-se/foto/sang-vaxt-vit-design-8251666/
Bild av Maria Orlova: https://www.pexels.com/sv-se/foto/kreativ-vagg-hus-vaxt-4915834/
Bild av Olena Bohovyk: https://www.pexels.com/sv-se/foto/romantisk-mork-vinter-hus-5686478/
Bild av Zsófia Fehér: https://www.pexels.com/sv-se/foto/byggnad-arkitektur-resa-utomhus-14532811/
Bild av Dilruba Sarıçimen: https://www.pexels.com/sv-se/foto/dryck-dricksglas-vertikalt-skott-narbild-8851505/
Bild av Element5 Digital: https://www.pexels.com/sv-se/foto/tra-lampor-skrivbord-lampa-1125136/
Bild av Max Vakhtbovych: https://www.pexels.com/sv-se/foto/mat-stad-restaurang-manniskor-6434622/
Bild av Pixabay: https://www.pexels.com/sv-se/foto/barnkammare-dekor-design-golv-462235/
Bild av Mathilde Langevin: https://www.pexels.com/sv-se/foto/dekoration-bage-spegel-vas-14320924/
Bild av Vincent Rivaud: https://www.pexels.com/sv-se/foto/hus-lyx-lampa-hem-2227832/
Bild av Victoria Akvarel : https://www.pexels.com/sv-se/foto/hotell-hus-arkitektur-lyx-3315291/
Bild av cottonbro studio: https://www.pexels.com/sv-se/foto/ljus-konst-kontor-vagg-4067759/


# Acknowledgement
This website has been made for my 4th Portfolio Project (Full-Stack Toolkit) - Diploma in Full Stack Software Development at [Code Institute](https://codeinstitute.net/).
I would like to thank my mentor Precious Ijege from Code Institute who helped me develop the website with feedback through the project.