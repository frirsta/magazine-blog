# Magazine 
Magazine is a website where people share and get inspired by interior designs. The website is targeted toward those who want to share, read and learn about interior design. The website is useful for tho.se who want to know what is trending right now. 
All website users can create an account and share what their homes look like or anything regarding interior design.

The website owner can delete comments and posts, if it is inappropriate. This is done from the Admin Dashboard that is only accessible to the Website owner when they log in.

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
<img src="static/img/readme/github_board.png" alt="github board" style="width: 100%">
</details>
<br>

### Models Graph
I have used Graph models to render a graphical overview of the blog models. It shows how the models are connected to each other in the database.
I used [Dreampuf](https://dreampuf.github.io/GraphvizOnline/#digraph%20G%20%7B%0A%0A%20%20subgraph%20cluster_0%20%7B%0A%20%20%20%20style%3Dfilled%3B%0A%20%20%20%20color%3Dlightgrey%3B%0A%20%20%20%20node%20%5Bstyle%3Dfilled%2Ccolor%3Dwhite%5D%3B%0A%20%20%20%20a0%20-%3E%20a1%20-%3E%20a2%20-%3E%20a3%3B%0A%20%20%20%20label%20%3D%20%22process%20%231%22%3B%0A%20%20%7D%0A%0A%20%20subgraph%20cluster_1%20%7B%0A%20%20%20%20node%20%5Bstyle%3Dfilled%5D%3B%0A%20%20%20%20b0%20-%3E%20b1%20-%3E%20b2%20-%3E%20b3%3B%0A%20%20%20%20label%20%3D%20%22process%20%232%22%3B%0A%20%20%20%20color%3Dblue%0A%20%20%7D%0A%20%20start%20-%3E%20a0%3B%0A%20%20start%20-%3E%20b0%3B%0A%20%20a1%20-%3E%20b3%3B%0A%20%20b2%20-%3E%20a3%3B%0A%20%20a3%20-%3E%20a0%3B%0A%20%20a3%20-%3E%20end%3B%0A%20%20b3%20-%3E%20end%3B%0A%0A%20%20start%20%5Bshape%3DMdiamond%5D%3B%0A%20%20end%20%5Bshape%3DMsquare%5D%3B%0A%7D) to translate the DOT language into the graph.

# Wireframes
I have used [Miro](https://miro.com/) to create WireFrames for the project.
The website have some differences.
<details><summary>Wireframes</summary>

<div style="display: flex; align-items: start;">
<img src="static/img/readme/home_desktop.jpg" alt="home page on desktop screen" style="width: 40%">
<img src="static/img/readme/home_ipad.jpg" alt="home page on ipad screen" style="width: 30%">
<img src="static/img/readme/home_phone.jpg" alt="home page on phone screen" style="width: 20%">
</div>

<br>

<div style="display: flex; align-items: start;">
<img src="static/img/readme/blog_desktop.jpg" alt="blog page on desktop screen" style="width: 40%">
<img src="static/img/readme/blog_ipad.jpg" alt="blog page on ipad screen" style="width: 30%">
<img src="static/img/readme/blog_phone.jpg" alt="blog page on phone screen" style="width: 20%">
</div>

<div style="display: flex; align-items: start;">
<img src="static/img/readme/post_detail_desktop.jpg" alt="post_detail page on desktop screen" style="width: 40%">
<img src="static/img/readme/post_detail_ipad.jpg" alt="post_detail page on ipad screen" style="width: 30%">
<img src="static/img/readme/post_detail_phone.jpg" alt="post_detail page on phone screen" style="width: 20%">
</div>


<img src="static/img/readme/signup.jpg" alt="signup page on all screens" style="width: 100%">

<img src="static/img/readme/login.jpg" alt="login page on all screens" style="width: 100%">

<img src="static/img/readme/profile.jpg" alt="profile page on all screens" style="width: 100%">

<img src="static/img/readme/edit_profile.jpg" alt="profile page on all screens" style="width: 100%">

<img src="static/img/readme/create_post.jpg" alt="create post page on all screens" style="width: 100%">

<div style="display: flex; align-items: start;">
<img src="static/img/readme/change_password_desktop.jpg" alt="change_password page on desktop screen" style="width: 40%">
<img src="static/img/readme/change_password_ipad.jpg" alt="change_password page on ipad screen" style="width: 30%">
<img src="static/img/readme/change_password_phone.jpg" alt="change_password page on phone screen" style="width: 20%">
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

* The footer
  * The footer links to Magazine's social media accounts.

### The Landing/home page
  * The landing page has an image of furniture and text that says 'MAGAZINE' and 'Interior & Lifestyle' This lets the user know what the website is about.
  * The home page displays the six latest posts made so the user can see what the latest interior trends are and also so they can see examples of what type of content they will find on the page. 

 
 ### Blog

 * The blog page displays all posts made with the latest ones on top of the page.


### Sign up
* The SignUp page displays a form where the user writes their information to create an account.

### Log in
* The log in page displays a form where the user writes their username and password to log in to their account.

### Profile
* The profile page displays the user profile picture, user bio and three buttons.
    * The Edit Profile button leads to the edit profile page where they can add a profile picture and write text about themselves.
    * The Change password button leads to a page where they can change their password.
    * The My Posts button leads to a page where they can find all posts they have created.

### Create Post
* In the create post page a user can create a post by adding text and image to the create post form. The form has four fields.
    * Title | Name of the blog post.
    * Article description | Description of the article. This is the first thing the user reads before deciding what post to read more about.
    * Content | The post content.
    * Image | The image that will be posted with the post text content.



### Admin Dashboard
* In the admin the website owner can see how many posts have been made, how many accounts have been created and how many comments have been made.
* On this page the owner can find all posts, who the author is, the title, the article description, the date it was created and the content.
    * The owner can Delete posts from this page.
* On this page the owner can find all the comments, the name of who has created the comment, the date the comment was created, the comment content, and what post it was commented on.
    * The owner can delete comments from this page.

### Features left to Implement

## Testing
[responsivedesignchecker](https://www.responsivedesignchecker.com/)
[HTML validator](https://validator.w3.org/)
<img src="static/img/readme/testing/html_validator.png" alt="html validator" style="width: 100%">
[CSS validator](https://jigsaw.w3.org/css-validator/)
<img src="static/img/readme/testing/css_validator.png" alt="css validator" style="width: 100%">
[Jshint](https://jshint.com/)
<img src="static/img/readme/testing/js_validator.png" alt="js validator" style="width: 100%">

### Lighthouse
The website has also been tested with the Chrome developer tool Google Lighthouse. It has been tested for desktop and for mobile. What was tested:

* Performance
* Accessibility
* Best Practices
* SEO (Search engine optimisation)
<br>

<details><summary>Lighthouse</summary>

### Home page 
#### Desktop
<img src="static/img/readme/testing/lighthouse/home_desktop.png" alt="lighthouse score for home page on desktop device" style="width: 100%">

#### Mobile
<img src="static/img/readme/testing/lighthouse/home_mobile.png" alt="lighthouse score for home page on mobile device" style="width: 100%">

<br>

### Blog page 
#### Desktop
<img src="static/img/readme/testing/lighthouse/blog_desktop.png" alt="lighthouse score for blog page on desktop device" style="width: 100%">

#### Mobile
<img src="static/img/readme/testing/lighthouse/blog_mobile.png" alt="lighthouse score for blog page on mobile device" style="width: 100%">

### Signup page 
#### Desktop
<img src="static/img/readme/testing/lighthouse/signup_desktop.png" alt="lighthouse score for signup page on desktop device" style="width: 100%">

#### Mobile
<img src="static/img/readme/testing/lighthouse/signup_mobile.png" alt="lighthouse score for signup page on mobile device" style="width: 100%">

### Login page 
#### Desktop
<img src="static/img/readme/testing/lighthouse/login_desktop.png" alt="lighthouse score for login page on desktop device" style="width: 100%">

#### Mobile
<img src="static/img/readme/testing/lighthouse/login_mobile.png" alt="lighthouse score for login page on mobile device" style="width: 100%">

### Create post page 
#### Desktop
<img src="static/img/readme/testing/lighthouse/create_post_desktop.png" alt="lighthouse score for create_post page on desktop device" style="width: 100%">

#### Mobile
<img src="static/img/readme/testing/lighthouse/create_post_mobile.png" alt="lighthouse score for create_post page on mobile device" style="width: 100%">

### Profile page 
#### Desktop
<img src="static/img/readme/testing/lighthouse/profile_desktop.png" alt="lighthouse score for profile page on desktop device" style="width: 100%">

#### Mobile
<img src="static/img/readme/testing/lighthouse/profile_mobile.png" alt="lighthouse score for profile page on mobile device" style="width: 100%">

### Edit profile page 
#### Desktop
<img src="static/img/readme/testing/lighthouse/edit_profile_desktop.png" alt="lighthouse score for edit_profile page on desktop device" style="width: 100%">

#### Mobile
<img src="static/img/readme/testing/lighthouse/edit_profile_mobile.png" alt="lighthouse score for edit_profile page on mobile device" style="width: 100%">

### Change password page 
#### Desktop
<img src="static/img/readme/testing/lighthouse/change_password_desktop.png" alt="lighthouse score for change_password page on desktop device" style="width: 100%">

#### Mobile
<img src="static/img/readme/testing/lighthouse/change_password_mobile.png" alt="lighthouse score for change_password page on mobile device" style="width: 100%">

### User posts page 
#### Desktop
<img src="static/img/readme/testing/lighthouse/user_posts_desktop.png" alt="lighthouse score for user_posts page on desktop device" style="width: 100%">

#### Mobile
<img src="static/img/readme/testing/lighthouse/user_posts_mobile.png" alt="lighthouse score for user_posts page on mobile device" style="width: 100%">

### Admin page 
#### Desktop
<img src="static/img/readme/testing/lighthouse/admin_desktop.png" alt="lighthouse score for admin page on desktop device" style="width: 100%">

#### Mobile
<img src="static/img/readme/testing/lighthouse/admin_mobile.png" alt="lighthouse score for admin page on mobile device" style="width: 100%">


</details>

<br>

## Technologies Used
* Python
* Django
* HTML5 - For structure of the website
* CSS3 - For styling of the website
* GitHub - Used to host the website
* GitPod - For deployment of the website
* [Miro](https://miro.com/) - For creating the Wireframes

### Libraries
* pip3 install Pillow
* pip3 install 'django<4' gunicorn
* pip3 install dj_database_url==0.5.0 psycopg2
* pip3 install dj3-cloudinary-storage
* pip install django-extensions
* pip install pyparsing pydot
* pip3 freeze --local > requirements.txt
<!-- 
python3 manage.py graph_models --pydot -a -g -o my_project_visualized.png
/manage.py graph_models -a > my_project.dot
--> 

### Validators

### Unfixed Bugs


## Deployment

<details><summary>Deployment</summary>

Create a GitHub repository from the Code Institute template and click 'Use this template'
<img src="static/img/deployment/step-1.png" alt="step of deployment" style="width: 100%">
<br>
Add a repository name and then click 'Create repository from template'
<img src="static/img/deployment/step-2.png" alt="step of deployment" style="width: 100%">
<br>
When the repository is created click 'Gitpod'
<img src="static/img/deployment/step-3.png" alt="step of deployment" style="width: 100%">
<br>

In the terminal type the following commands to install Django and its supporting libraries:

<img src="static/img/deployment/deployment-1.png" alt="'pip3 install 'django<4' gunicorn' typed in the terminal" style="width: 100%">
<img src="static/img/deployment/deployment-2.png" alt="'pip3 install dj_database_url==0.5.0 psycopg2' typed in the terminal" style="width: 100%">
<img src="static/img/deployment/deployment-3.png" alt="'pip3 install dj3-cloudinary-storage typed' in the terminal" style="width: 100%">
<br>
After the libraries have been installed type the following command to create a requirements.txt file
<img src="static/img/deployment/deployment-4.png" alt="'pip3 freeze --local > requirements.txt' typed in the terminal" style="width: 100%">
<img src="static/img/deployment/step-5.png" alt="step of deployment" style="width: 100%">

<br>
Create the Django project by typing the following command
<img src="static/img/deployment/step-6.png" alt="step of deployment" style="width: 100%">
After typing the command this 'blog' folder with files will be displayed in the directory
<img src="static/img/deployment/step-7.png" alt="step of deployment" style="width: 100%">
  
<br>
Create the Django application by typing the following command
<img src="static/img/deployment/step-8.png" alt="step of deployment" style="width: 100%">
After typing the command this 'magazine' with files will be displayed in the directory
<img src="static/img/deployment/step-9.png" alt="step of deployment" style="width: 100%">

<br>

In the settings.py in the blog folder add the application (add 'magazine') to the 'INSTALLED_APPS' section as shown in following image
<img src="static/img/deployment/step-10.png" alt="step of deployment" style="width: 100%">
<br>

In the terminal type 'python3 manage.py migrate'
<img src="static/img/deployment/step-11.png" alt="step of deployment" style="width: 100%">  
<br>

In the terminal type 'python3 manage.py runserver' and click 'Open Browser'
<img src="static/img/deployment/step-12.png" alt="step of deployment" style="width: 100%">  
<br>
The following image is what the website will look like
<img src="static/img/deployment/step-13.png" alt="step of deployment" style="width: 100%">  

<br>

Create or login to [Heroku](https://www.heroku.com/)

In the heroku Website click 'New' and after click 'Create new app'
<img src="static/img/deployment/step-14.png" alt="step of deployment" style="width: 100%">  

<br>

Write the app name, choose a region and then click 'Create app' 
<img src="static/img/deployment/step-15.png" alt="step of deployment" style="width: 100%">  
<br>

In the application website click 'Deploy' on the navigation menu
<img src="static/img/deployment/step-16.png" alt="step of deployment" style="width: 100%">  
<br>

In the 'Deploy' page follow these steps:
  1 Click the GitHub logo
  2 Search for the GitHub repository that was made for this project
  3 When the repository is found click 'Connect'
<img src="static/img/deployment/step-17.png" alt="step of deployment" style="width: 100%">  
<br>

<img src="static/img/deployment/step-18.png" alt="step of deployment" style="width: 100%">

### Create database

[ElephantSQL](https://www.elephantsql.com/) 
Start with clicking 'Create New Instance'
<img src="static/img/deployment/elephantsql.png" alt="step of deployment" style="width: 100%"> 

<br>

Enter a name for the database and then click 'Select Region'
<img src="static/img/deployment/step-19.png" alt="step of deployment" style="width: 100%">  
<br>

Select a region and then click Review
<img src="static/img/deployment/step-20.png" alt="step of deployment" style="width: 100%">  
<br>

Review the information and click 'Create Instance'
<img src="static/img/deployment/step-21.png" alt="step of deployment" style="width: 100%">  
<br>

When the instance is created it will be displayed on top of the list of created instances
Click the instance that has been created
<img src="static/img/deployment/step-22.png" alt="step of deployment" style="width: 100%">
<br>

Copy the Url
<img src="static/img/deployment/step-23.png" alt="step of deployment" style="width: 100%"> 
<br>

Create a 'env.py' file on the top level directory
<img src="static/img/deployment/step-24.png" alt="step of deployment" style="width: 100%"> 
<br>

In the 'env.py' file add the following text
<img src="static/img/deployment/step-25.png" alt="step of deployment" style="width: 100%"> 
<br>

Add the following text and in the red area paste the Url copied from the instance that was created in [ElephantSQL](https://www.elephantsql.com/)
<img src="static/img/deployment/step-26.png" alt="step of deployment" style="width: 100%"> 
  
<br>

In the 'settings.py' file copy the value of 'SECRET_KEY' (The secret key is removed from image because it has to be kept secret)
<img src="static/img/deployment/step-27.png" alt="step of deployment" style="width: 100%"> 
<br>

In the 'env.py' file add the following text and paste the secret key as value
<img src="static/img/deployment/step-28.png" alt="step of deployment" style="width: 100%"> 
<br>

Add the following text on top of the 'setting.py' file
<img src="static/img/deployment/step-29.png" alt="step of deployment" style="width: 100%"> 
<br>

Add the following replace the value of 'SECRET_KEY' and add the following text
<img src="static/img/deployment/step-30.png" alt="step of deployment" style="width: 100%"> 
<br>

  1 Comment out the database that is in the 'settings.py' file
  2 Add the following text to connect the new database
<img src="static/img/deployment/step-31.png" alt="step of deployment" style="width: 100%"> 
<br>

In the terminal type the following command
<img src="static/img/deployment/step-32.png" alt="step of deployment" style="width: 100%"> 
<br>

In [ElephantSQL](https://www.elephantsql.com/) in the instance that was created click 'Browser' 
<img src="static/img/deployment/step-33.png" alt="step of deployment" style="width: 100%"> 
<br>

In the 'Browser' page click 'Table queries' and the database will be displayed
<img src="static/img/deployment/step-34.png" alt="step of deployment" style="width: 100%"> 

<br>

In the application in heroku click 'Settings' in the navigation menu. After click 'Reveal Config Vars'
Add the following keys and in the red area add their values
<img src="static/img/deployment/step-35.png" alt="step of deployment" style="width: 100%"> 

[Cloudinary](https://cloudinary.com/) Create an account or log in to cloudinary.

<br>

In 'API Environment variable' copy the value as shown below
<img src="static/img/deployment/step-36.png" alt="step of deployment" style="width: 100%"> 
<br>

In the 'env.py' file add 'os.environ["CLOUDINARY_URL"]' and paste the link that was copied from cloudinary
<img src="static/img/deployment/step-37.png" alt="step of deployment" style="width: 100%"> 
<br>

In the 'settings.py' file add 'cloudinary_storage' and 'cloudinary' as shown below
<img src="static/img/deployment/step-38.png" alt="step of deployment" style="width: 100%"> 
<br>

Add the following text in the 'settings.py' file
<img src="static/img/deployment/step-39.png" alt="step of deployment" style="width: 100%"> 
<br>

Add the following text as shown below in the 'settings.py' file
<img src="static/img/deployment/step-40.png" alt="step of deployment" style="width: 100%"> 
<br>

Add the following text as shown below in the 'settings.py' file
<img src="static/img/deployment/step-41.png" alt="step of deployment" style="width: 100%"> 
<br>

Create these folders on the top level directory
<img src="static/img/deployment/step-43.png" alt="step of deployment" style="width: 100%"> 
<br>


Creata a 'Procfile' file on the top level directory
<img src="static/img/deployment/step-44.png" alt="step of deployment" style="width: 100%"> 
<br>

In the 'Procfile' file add the following text.
<img src="static/img/deployment/step-45.png" alt="step of deployment" style="width: 100%">
After push the project to GitHub.
<br>

In the application in Heroku navigate to the deploy page and scroll to the bottom of the page
<img src="static/img/deployment/step-46.png" alt="step of deployment" style="width: 100%"> 
<br>

Click 'Deploy Branch'
Wait for the GitHub branch to be deployed and then click 'View App'
<img src="static/img/deployment/step-48.png" alt="step of deployment" style="width: 100%"> 
<br>

This is what the app will look like when its successfully deployed
<img src="static/img/deployment/step-49.png" alt="step of deployment" style="width: 100%"> 

</details>
<br>


## Credits
* https://dontrepeatyourself.org/post/django-blog-tutorial-part-1-project-configuration/
### Content
### Media
#### Images
* Image by rawpixel.com https://www.rawpixel.com/image/6012980/illustration-png-social-media-logo
* Bild av Olena Bohovyk: https://www.pexels.com/sv-se/foto/romantisk-mork-vinter-hus-5686478/
* Bild av Maria Orlova: https://www.pexels.com/sv-se/foto/kreativ-vagg-hus-vaxt-4915834/
* Bild av PNW Production: https://www.pexels.com/sv-se/foto/sang-vaxt-vit-design-8251666/
* Bild av Maksim Goncharenok: https://www.pexels.com/sv-se/foto/tra-vagg-bord-lyx-4352247/
* Bild av Nugroho  Wahyu: https://www.pexels.com/sv-se/foto/inne-tra-design-rum-3119180/ hero image
## Bugs
In the forms errors never showed on the page. In stackoverflow I finally found a solution.

* https://stackoverflow.com/questions/64054215/display-django-registration-form-errors




