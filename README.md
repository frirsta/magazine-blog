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
<br>

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
https://www.responsivedesignchecker.com/
https://validator.w3.org/
https://jigsaw.w3.org/css-validator/



## Technologies Used
* Python
* Django
* HTML5 - For structure of the website
* CSS3 - For styling of the website
* GitHub - Used to host the website
* GitPod - For deployment of the website
* Miro - For creating the Wireframes
miro.com
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
Step 1
step 2
step3
Step 4 
* pip3 install 'django<4' gunicorn
* pip3 install dj_database_url==0.5.0 psycopg2
* pip3 install dj3-cloudinary-storage
step 5
pip3 freeze --local > requirements.txt

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




