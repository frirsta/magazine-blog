# Magazine 
Magazine is a website where people share and get inspired by interior designs. The website is targeted toward those who want to share, read and learn about interior design. The website is useful for those who want to know what is trending right now. 
All website users can create an account and share what their homes look like or anything regarding interior design.

The website owner can delete comments and posts, if it is inappropriate. This is done from the Admin Dashboard that is only accessible to the Website owner when they log in.
This is the live link to [Magazine](https://magazine-5aec9e3ca90c.herokuapp.com/)

<img src="readme/all_devices.png" alt="website on all devices" style="width: 100%">


* [**Project**](<#Project>)
* [**Project Management**](<#Project-Management>)
* [**Wireframes**](<#Wireframes>)
* [**User Experience UX**](<#user-experience-ux>)
* [**Features**](<#Features>)
* [**Features left to Implement**](<#Features-left-to-Implement>)
* [**Testing**](<#Testing>)
* [**Bugs**](<#Bugs>)
* [**Technologies Used**](<#Technologies-Used>)
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

</p>
</details>
<br>

# User Experience (UX)
## Site User

| User/Admin | Description |
| --- | --- |
| Site User | As a Site User, I can View posts so that I can select one to read |
| Site User | As a site user, I can read comments that are made for a specific post so that I can read what people think of the post |
| Site User | As a Site User, I can create an account so that I can comment and create content |
| Site User | As a Site User, I can create a post so that I can make content for the blog |
| Site User | As a Site User, I can comment on posts so that I can write what I think about the post and interact with other blog readers |
| Site User | As a site user, I can delete comments I have made so that I have control over my comments, and can remove them if I change my mind in the comments |
| Site User | As a Site user, I can go to a profile page specifically for me so that I can find all posts created by me |
| Site User | As a Site User, I can log in so that I can create content for the blog that is connected to my account |
| Site User | As a Site User, I can log out so that someone else using my computer can't post from my account |

<br>

## Site Owner

| User/Admin | Description |
| --- | --- |
| Site Owner | All Site User stories apply to the Site Owner |
| Site Owner | As a Site Owner, I can go to the Admin Dashboard where I can find all posts made and information about them |
| Site Owner | As a Site Owner, I can find all posts and all comments created on one page so that I can manage the content on the website |
| Site Owner | As a Site Owner, I can go to the Admin Dashboard where I can find all comments made and information about them |
| Site Owner | As a Site Owner, I can delete the posts and comments from the admin page so that I can manage a secure environment for the users |

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
<details><summary>Navbar</summary>

#### Navbar
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/menu_desktop.png" alt="navbar page on a desktop device" style="width: 30%">
<img src="readme/pages/menu_ipad.png" alt="navbar page on an ipad device" style="width: 30%">
<img src="readme/pages/menu_mobile.png" alt="navbar page on a mobile device" style="width: 30%">
</div>

#### User Navbar
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/user_menu_desktop.png" alt="navbar page on a desktop device when a user is logged in" style="width: 30%">
<img src="readme/pages/user_menu_ipad.png" alt="navbar page on an ipad device when a user is logged in" style="width: 30%">
<img src="readme/pages/user_menu_mobile.png" alt="navbar page on a mobile device when a user is logged in" style="width: 30%">
</div>

#### Admin Navbar
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/admin_menu_desktop.png" alt="navbar page on a desktop device when the admin is logged in" style="width: 30%">
<img src="readme/pages/admin_menu_ipad.png" alt="navbar page on an ipad device when the admin is logged in" style="width: 30%">
<img src="readme/pages/admin_menu_mobile.png" alt="navbar page on a mobile device when the admin is logged in" style="width: 30%">
</div>
</details>

* The footer
  * The footer links to Magazine's social media accounts.
<details><summary>Footer</summary>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/footer_mobile.png" alt="footer on mobile screen" style="width: 30%">
<img src="readme/pages/footer_ipad.png" alt="footer on ipad screen" style="width: 30%">
<img src="readme/pages/footer_desktop.png" alt="footer on desktop screen" style="width: 30%">
</div>

</details>

### The Landing/home page
  * The landing page has an image of furniture and text that says 'MAGAZINE' and 'Interior & Lifestyle' This lets the user know what the website is about.
  * The home page displays the six latest posts made so the user can see what the latest interior trends are and also so they can see examples of what type of content they will find on the page. 
<br>
<details><summary>Home</summary>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/home_mobile.png" alt="home page on mobile screen" style="width: 20%">
<img src="readme/pages/home_ipad.png" alt="home page on ipad screen" style="width: 30%">
<img src="readme/pages/home_desktop.png" alt="home page on desktop screen" style="width: 48%">
</div>
</details
 
### Blog
 * The blog page displays all posts made with the latest ones on top of the page.
 <br>
<details><summary>Blog</summary>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/blog_mobile.png" alt="blog page on mobile screen" style="width: 20%">
<img src="readme/pages/blog_ipad.png" alt="blog page on ipad screen" style="width: 30%">
<img src="readme/pages/blog_desktop.png" alt="blog page on desktop screen" style="width: 48%">
</div>
</details

### Post detail
* When the user chooses a blog to read they get redirected to the blog post detail page where they can read the full post.
* They can also read comments and leave comments.
 <br>
<details><summary>Post detail</summary>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/post_detail_mobile.png" alt="post_detail page on mobile screen" style="width: 20%">
<img src="readme/pages/post_detail_ipad.png" alt="post_detail page on ipad screen" style="width: 30%">
<img src="readme/pages/post_detail_desktop.png" alt="post_detail page on desktop screen" style="width: 48%">
</div>
</details

#### Comment section
<details><summary>Comment section</summary>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/comment_mobile.png" alt="comment page on mobile screen" style="width: 20%">
<img src="readme/pages/comment_ipad.png" alt="comment page on ipad screen" style="width: 30%">
<img src="readme/pages/comment_desktop.png" alt="comment page on desktop screen" style="width: 48%">
</div>
</details

### Sign up
* The SignUp page displays a form where the user writes their information to create an account.
<br>
<details><summary>Sign up</summary>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/signup_mobile.png" alt="signup page on mobile screen" style="width: 20%">
<img src="readme/pages/signup_ipad.png" alt="signup page on ipad screen" style="width: 30%">
<img src="readme/pages/signup_desktop.png" alt="signup page on desktop screen" style="width: 48%">
</div>
</details

### Log in
* The log in page displays a form where the user writes their username and password to log in to their account.
<br>
<details><summary>Log in</summary>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/login_mobile.png" alt="login page on mobile screen" style="width: 20%">
<img src="readme/pages/login_ipad.png" alt="login page on ipad screen" style="width: 30%">
<img src="readme/pages/login_desktop.png" alt="login page on desktop screen" style="width: 48%">
</div>
</details

### Profile
* The profile page displays the user profile picture, user bio and three buttons.
    * The Edit Profile button leads to the edit profile page where they can add a profile picture and write text about themselves.
    * The Change password button leads to a page where they can change their password.
    * The My Posts button leads to a page where they can find all posts they have created.
    <br>
<details><summary>Profile</summary>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/profile_mobile.png" alt="profile page on mobile screen" style="width: 20%">
<img src="readme/pages/profile_ipad.png" alt="profile page on ipad screen" style="width: 30%">
<img src="readme/pages/profile_desktop.png" alt="profile page on desktop screen" style="width: 48%">
</div>
</details

### User posts
* The logged in user can find all the posts they have created in this page.
<br>
<details><summary>User posts</summary>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/user_posts_mobile.png" alt="user_posts page on mobile screen" style="width: 20%">
<img src="readme/pages/user_posts_ipad.png" alt="user_posts page on ipad screen" style="width: 30%">
<img src="readme/pages/user_posts_desktop.png" alt="user_posts page on desktop screen" style="width: 48%">
</div>
</details

### Change Password
* The change password page is where the user can change their password.
<br>
<details><summary>Change Password</summary>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/change_password_mobile.png" alt="change_password page on mobile screen" style="width: 20%">
<img src="readme/pages/change_password_ipad.png" alt="change_password page on ipad screen" style="width: 30%">
<img src="readme/pages/change_password_desktop.png" alt="change_password page on desktop screen" style="width: 48%">
</div>
</details>

### Edit Profile
The edit profile page is where the user can add a profile picture, change username and write text about themselves.
<br>
<details><summary>Edit Profile</summary>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/edit_profile_mobile.png" alt="edit_profile page on mobile screen" style="width: 20%">
<img src="readme/pages/edit_profile_ipad.png" alt="edit_profile page on ipad screen" style="width: 30%">
<img src="readme/pages/edit_profile_desktop.png" alt="edit_profile page on desktop screen" style="width: 48%">
</div>
</details>

### Create Post
* In the create post page a user can create a post by adding text and image to the create post form. The form has four fields.
    * Title | Name of the blog post.
    * Article description | Description of the article. This is the first thing the user reads before deciding what post to read more about.
    * Content | The post content.
    * Image | The image that will be posted with the post text content.
<br>
<details><summary>Create Post</summary>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/create_post_mobile.png" alt="create_post page on mobile screen" style="width: 20%">
<img src="readme/pages/create_post_ipad.png" alt="create_post page on ipad screen" style="width: 30%">
<img src="readme/pages/create_post_desktop.png" alt="create_post page on desktop screen" style="width: 48%">
</div>
</details>

### Edit Post
* In the edit post page a user can edit the posts they have created.

<br>
<details><summary>Edit Post</summary>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/edit_post_mobile.png" alt="edit_post page on mobile screen" style="width: 20%">
<img src="readme/pages/edit_post_ipad.png" alt="edit_post page on ipad screen" style="width: 30%">
<img src="readme/pages/edit_post_desktop.png" alt="edit_post page on desktop screen" style="width: 48%">
</div>
</details>

### User post confirm delete page
* When a site user deletes a post, they get redirected to this page to confirm they want to delete the post.
<br>
<details><summary>Post confirm delete</summary>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/delete_post_user_mobile.png" alt="post_confirm_delete page on mobile screen" style="width: 20%">
<img src="readme/pages/delete_post_user_ipad.png" alt="post_confirm_delete page on ipad screen" style="width: 30%">
<img src="readme/pages/delete_post_user_desktop.png" alt="post_confirm_delete page on desktop screen" style="width: 48%">
</div>
</details>

### User comment confirm delete page
* When a site user deletes a comment, they get redirected to this page to confirm they want to delete the comment.
<br>
<details><summary>Comment confirm delete</summary>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/delete_comment_user_mobile.png" alt="comment_confirm_delete page on mobile screen" style="width: 20%">
<img src="readme/pages/delete_comment_user_ipad.png" alt="comment_confirm_delete page on ipad screen" style="width: 30%">
<img src="readme/pages/delete_comment_user_desktop.png" alt="comment_confirm_delete page on desktop screen" style="width: 48%">
</div>
</details>

### Admin Dashboard
* In the admin the website owner can see how many posts have been made, how many accounts have been created and how many comments have been made.
* On this page the owner can find all posts, who the author is, the title, the article description, the date it was created and the content.
    * The owner can Delete posts from this page.
* On this page the owner can find all the comments, the name of who has created the comment, the date the comment was created, the comment content, and what post it was commented on.
    * The owner can delete comments from this page.
<br>
<details><summary>Admin Dashboard</summary>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/admin_mobile.png" alt="admin page on mobile screen" style="width: 20%">
<img src="readme/pages/admin_ipad.png" alt="admin page on ipad screen" style="width: 30%">
<img src="readme/pages/admin_desktop.png" alt="admin page on desktop screen" style="width: 48%">
</div>
</details>

### Admin post confirm delete page
* When the admin/site owner deletes a post from the admin page, they get redirected to this page to confirm they want to delete the post.
<br>
<details><summary>Post confirm delete</summary>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/admin_delete_post_mobile.png" alt="admin_post_confirm_delete page on mobile screen" style="width: 20%">
<img src="readme/pages/admin_delete_post_ipad.png" alt="admin_post_confirm_delete page on ipad screen" style="width: 30%">
<img src="readme/pages/admin_delete_post_desktop.png" alt="admin_comment_confirm_delete page on desktop screen" style="width: 48%">
</div>
</details>

### Admin comment confirm delete page
* When the admin/site owner deletes a comment from the admin page, they get redirected to this page to confirm they want to delete the comment.
<br>
<details><summary>Comment confirm delete</summary>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/admin_delete_comment_mobile.png" alt="admin_comment_confirm_delete page on mobile screen" style="width: 20%">
<img src="readme/pages/admin_delete_comment_ipad.png" alt="admin_comment_confirm_delete page on ipad screen" style="width: 30%">
<img src="readme/pages/admin_delete_comment_desktop.png" alt="admin_comment_confirm_delete page on desktop screen" style="width: 48%">
</div>
</details>

### 404 page
* This is the page the user gets redirected to if the website does not exist.
<br>
<details><summary>404</summary>
<div style="display: flex; align-items: flex-start; justify-content: space-between;">
<img src="readme/pages/404_mobile.png" alt="404 page on mobile screen" style="width: 20%">
<img src="readme/pages/404_ipad.png" alt="404 page on ipad screen" style="width: 30%">
<img src="readme/pages/404_desktop.png" alt="404 page on desktop screen" style="width: 48%">
</div>
</details>


# Features left to Implement
* Add more automated testing
* Add search functionality so the user can find posts or other users.

# Testing
## [CSS validator](https://jigsaw.w3.org/css-validator/)
<img src="readme/testing/css_validator.png" alt="css validator" style="width: 100%">
<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

<p>
<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
</p>
      

## [Jshint](https://jshint.com/)
<img src="readme/testing/js_validator.png" alt="js validator" style="width: 100%">

## [HTML validator](https://validator.w3.org/)
<details><summary>HTML Validator</summary>

### Home page
<img src="readme/testing/html_validator/html_validator_home.png" alt="home page html validator" style="width: 100%">

### Blog page
<img src="readme/testing/html_validator/html_validator_blog.png" alt="blog page html validator" style="width: 100%">

### Post detail page
<img src="readme/testing/html_validator/html_validator_post_detail.png" alt="post_detail page html validator" style="width: 100%">

### Login page
<img src="readme/testing/html_validator/html_validator_login.png" alt="login page html validator" style="width: 100%">

### Signup page
<img src="readme/testing/html_validator/html_validator_signup.png" alt="signup page html validator" style="width: 100%">

### Create post page
<img src="readme/testing/html_validator/html_validator_create_post.png" alt="create_post page html validator" style="width: 100%">

### Profile page
<img src="readme/testing/html_validator/html_validator_profile.png" alt="profile page html validator" style="width: 100%">

### User posts page
<img src="readme/testing/html_validator/html_validator_user_posts.png" alt="user_posts page html validator" style="width: 100%">

### Edit profile page
<img src="readme/testing/html_validator/html_validator_edit_profile.png" alt="edit_profile page html validator" style="width: 100%">

### Password change page
<img src="readme/testing/html_validator/html_validator_password_change.png" alt="password_change page html validator" style="width: 100%">

### Admin page
<img src="readme/testing/html_validator/html_validator_admin.png" alt="admin page html validator" style="width: 100%">

### 404 page
<img src="readme/testing/html_validator/html_validator_404.png" alt="404 page html validator" style="width: 100%">

</details>

## Responsiveness Testing
I have tested the responsiveness manually with [DevTool](https://developer.chrome.com/docs/devtools/)


| Desktop  | Width | |
| ------------- | ------------- | ------------- |
| Laptop L | Width: 1440px | Pass |
| Laptop: | Width: 1348px | Pass  |
| Laptop: | Width: 1024px | Pass  |


| Tablet  | Width | |
| ------------- | ------------- | ------------- |
| Ipad Air | Width: 820px | Pass  |
| Ipad Mini | Width: 768px | Pass  |
| Ipad Pro | Width: 1024px | Pass  | 
| Nest Hub | Width: 1024px | Pass |
| Nest Hub Max | Width: 1280px | Pass  |
| Surface Pro 7 | Width: 912px | Pass  |
| Surface Pro 7 | Width: 912px | Pass  |

| Mobile  | Width | |
| ------------- | ------------- | ------------- |
| Iphone 6/7/8 | Width: 375px | Pass  |
| Iphone 6/7/8 Plus: | Width: 414px | Pass  |
| Iphone SE | Width: 375px | 
| Iphone XR | Width: 414px | Pass | 
| Iphone 12 PRO: | Width: 390px | Pass |
| Surface Duo | Width: 540px | Pass |
| Galaxy s8+ | Width: 360px | Pass |
| Samsung Galaxy A51/71 | Width: 412px  | Pass |
 
## Browser Compatibility
I have tested the browser manually on these browsers:
### Microsoft Edge 109.0.1518.61
### Google Chrome 109.0.5414.75
### Apple Safari 14.2.1

<br>

## [Python Validation](https://pep8ci.herokuapp.com/)

<details><summary>Python Validation</summary>

### admin.py file
<img src="readme/testing/pep8/pep8_admin.png" alt="python validator admin file" style="width: 100%">

<br>

### forms.py file
<img src="readme/testing/pep8/pep8_forms.png" alt="python validator forms file" style="width: 100%">

<br>

### models.py file
<img src="readme/testing/pep8/pep8_models.png" alt="python validator models file" style="width: 100%">
I could not fix the length of the link because it would stop working.

<br>

### signals.py file
<img src="readme/testing/pep8/pep8_signals.png" alt="python validator signals file" style="width: 100%">

<br>

### urls.py file
<img src="readme/testing/pep8/pep8_urls.png" alt="python validator urls file" style="width: 100%">

<br>

### views.py file
<img src="readme/testing/pep8/pep8_views.png" alt="python validator views file" style="width: 100%">

<br>

### model.py file
<img src="readme/testing/pep8/pep8_model.png" alt="python validator model file" style="width: 100%">

<br>

### apps.py file
<img src="readme/testing/pep8/pep8_apps.png" alt="python validator apps file" style="width: 100%">
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
<img src="readme/testing/lighthouse/lighthouse_desktop_home.png" alt="lighthouse score for home page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/lighthouse_mobile_home.png" alt="lighthouse score for home page on mobile device" style="width: 100%">

<br>

### Blog page 
#### Desktop
<img src="readme/testing/lighthouse/lighthouse_desktop_blog.png" alt="lighthouse score for blog page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/lighthouse_mobile_blog.png" alt="lighthouse score for blog page on mobile device" style="width: 100%">

### Post Detail
#### Desktop
<img src="readme/testing/lighthouse/lighthouse_desktop_post_detail.png" alt="lighthouse score for post_detail page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/lighthouse_mobile_post_detail.png" alt="lighthouse score for post_detail page on mobile device" style="width: 100%">

### Signup page 
#### Desktop
<img src="readme/testing/lighthouse/lighthouse_desktop_signup.png" alt="lighthouse score for signup page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/lighthouse_mobile_signup.png" alt="lighthouse score for signup page on mobile device" style="width: 100%">

### Login page 
#### Desktop
<img src="readme/testing/lighthouse/lighthouse_desktop_login.png" alt="lighthouse score for login page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/lighthouse_mobile_login.png" alt="lighthouse score for login page on mobile device" style="width: 100%">

### Create post page 
#### Desktop
<img src="readme/testing/lighthouse/lighthouse_desktop_create_post.png" alt="lighthouse score for create_post page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/lighthouse_mobile_create_post.png" alt="lighthouse score for create_post page on mobile device" style="width: 100%">

### Profile page 
#### Desktop
<img src="readme/testing/lighthouse/lighthouse_desktop_profile.png" alt="lighthouse score for profile page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/lighthouse_mobile_profile.png" alt="lighthouse score for profile page on mobile device" style="width: 100%">

### Edit profile page 
#### Desktop
<img src="readme/testing/lighthouse/lighthouse_desktop_edit_profile.png" alt="lighthouse score for edit_profile page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/lighthouse_mobile_edit_profile.png" alt="lighthouse score for edit_profile page on mobile device" style="width: 100%">

### Change password page 
#### Desktop
<img src="readme/testing/lighthouse/lighthouse_desktop_change_password.png" alt="lighthouse score for change_password page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/lighthouse_mobile_change_password.png" alt="lighthouse score for change_password page on mobile device" style="width: 100%">

### User posts page 
#### Desktop
<img src="readme/testing/lighthouse/lighthouse_desktop_user_posts.png" alt="lighthouse score for user_posts page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/lighthouse_mobile_user_posts.png" alt="lighthouse score for user_posts page on mobile device" style="width: 100%">

### Admin page 
#### Desktop
<img src="readme/testing/lighthouse/lighthouse_desktop_admin_page.png" alt="lighthouse score for admin page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/lighthouse_mobile_admin_page.png" alt="lighthouse score for admin page on mobile device" style="width: 100%">

### User Confirm post delete
#### Desktop
<img src="readme/testing/lighthouse/lighthouse_desktop_user_delete_post.png" alt="lighthouse score for user post_confirm_delete page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/lighthouse_mobile_user_delete_post.png" alt="lighthouse score for user post_confirm_delete page on mobile device" style="width: 100%">

### User Confirm comment delete
#### Desktop
<img src="readme/testing/lighthouse/lighthouse_desktop_user_delete_comment.png" alt="lighthouse score for admin comment_confirm_delete page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/lighthouse_mobile_user_delete_comment.png" alt="lighthouse score for admin comment_confirm_delete page on mobile device" style="width: 100%">

### Confirm post delete Admin
#### Desktop
<img src="readme/testing/lighthouse/lighthouse_desktop_admin_delete_post.png" alt="lighthouse score for admin post_confirm_delete page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/lighthouse_mobile_admin_delete_post.png" alt="lighthouse score for admin post_confirm_delete page on mobile device" style="width: 100%">

### Confirm comment delete Admin
#### Desktop
<img src="readme/testing/lighthouse/lighthouse_desktop_admin_delete_comment.png" alt="lighthouse score for admin comment_confirm_delete page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/lighthouse_mobile_admin_delete_comment.png" alt="lighthouse score for admin comment_confirm_delete page on mobile device" style="width: 100%">

### 404 page
#### Desktop
<img src="readme/testing/lighthouse/lighthouse_desktop_error.png" alt="lighthouse score for error page on desktop device" style="width: 100%">

#### Mobile
<img src="readme/testing/lighthouse/lighthouse_mobile_error.png" alt="lighthouse score for error page on mobile device" style="width: 100%">

</details>

<br>

## Testing with Coverage
Due to prioritizing other tasks, I haven't had time for a lot of testing. Using Coverage, I have tested the Post model. The coverage report shows that 70% of testing has been done.
Below are images of the steps taken for testing the Post model in chronological order
<details><summary>Coverage</summary>

<img src="readme/testing/coverage/1.png" alt="Step 1 of the testing process with coverage" style="width: 70%">

<img src="readme/testing/coverage/2.png" alt="Step 2 of the testing process with coverage" style="width: 70%">

<img src="readme/testing/coverage/3.png" alt="Step 3 of the testing process with coverage" style="width: 70%">

<img src="readme/testing/coverage/4.png" alt="Step 4 of the testing process with coverage" style="width: 70%">

<img src="readme/testing/coverage/5.png" alt="Step 5 of the testing process with coverage" style="width: 70%">
</details>

## User story testing

### Site User

**Site User** As a Site User, I can View posts so that I can select one to read.
* In the home page there are six posts that the user can choose to read.
* On the blog page all posts are available to the user.
<br>

**Site User** As a site user, I can read comments that are made for a specific post so that I can read what people think of the post.
* In a blog post detail page a user can leave a comment and also read comments made on that specific blog post.
<br>

**Site User** As a Site User, I can create an account so that I can comment and create content.
* In the navigation menu there is a link to Sign up.
<br>

**Site User** As a Site User, I can log in so that I can create content for the blog that is connected to my account.
* In the navigation menu there is a link to Log in.
<br>

**Site User** As a Site User, I can create a post so that I can make content for the blog. 
* When the user has created an account or logged in they can create their own blog posts.

<br>

**Site User** As a Site User, I can comment on posts so that I can write what I think about the post and interact with other blog readers.
* When the user has created an account or logged in they can comment on blog posts.

<br>

**Site User** As a site user, I can delete comments I have made so that I have control over my comments, and can remove them if I change my mind in the comments.
* When a user is logged in and has created a comment, the comment appears under the blog post details page and the comments the logged in user has made have a delete button so the user can delete their own comments.
<br>

**Site User** As a Site user, I can go to a profile page specifically for me so that I can find all posts created by me.
* When a user is logged in the navigation menu on top of the page displays a 'Profile' link where the user can add a profile image, add text about themselves, change their password and they can find all the posts they have made.
<br>

**Site User** As a Site User, I can log out so that someone else using my computer can't post from my account.
* In the navigation menu there is a link to Logout.

<br>

### Site Owner

**Site Owner** All Site User stories apply to the Site Owner.

**Site Owner** As a Site Owner, I can go to the Admin Dashboard where I can find all posts made and information about them.
* In the navigation menu there is a link to the admin page.
<br>

**Site Owner** As a Site Owner, I can find all posts and all comments created on one page so that I can manage the content on the website.
* In the admin page there are 3 boxes with the number of users, posts and comments on them. There are also three buttons below that show all details about posts, comments and users.
<br>

**Site Owner** As a Site Owner, I can go to the Admin Dashboard where I can find all posts made and information about them.
* On the admin page there is a button with 'All Posts' text on it. When the button is clicked, all information about the posts are displayed. The post author, the post title, the article description, a button that redirects the Site owner to the blog post detail page, the date the post was made and a delete button so the site owner can delete the post from the admin dashboard are displayed when the button is clicked.
<br>

**Site Owner** As a Site Owner, I can go to the Admin Dashboard where I can find all comments made and information about them.
* On the admin page there is a button with 'All Comments' text on it. When the button is clicked, all information about the comments are displayed. The comment content, the post title of the post that has been commented under, the name of the user that has created the comment, the date the comment was made and a delete button so the site owner can delete the comment from the admin dashboard are displayed when the button is clicked. 
<br>

**Site Owner** As a Site Owner, I can go to the Admin Dashboard where I can find all users and information about them.
* In the admin page there is a button with 'All Users' text on it. When the button is clicked, all information about the users are displayed. When the button is clicked the user name, email and date of when the user was created is displayed.
<br>

**Site Owner** As a Site Owner, I can delete the posts and comments from the admin page so that I can manage a secure environment for the users.
* In the admin page the site owner can delete the posts and comments made.  

<br>


# Bugs
When testing the html in [HTML validator](https://validator.w3.org/), the error shown in the image appeared.
<img src="readme/testing/bugs/html_validator_signup_error.png" alt="bug in html validator when testing signup page" style="width: 100%">
I had forgotten that I had added a label attribute to the SignUp form in forms.py.
<img src="readme/testing/bugs/signup_error.png" alt="bug in signup form in forms.py" style="width: 100%">
The bug is now corrected.
<img src="readme/testing/bugs/signup_error_fixed.png" alt="signup form fixed" style="width: 100%">


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
* pip3 install Pillow -  For ImageField in models.py.
* pip3 install 'django<4' gunicorn - Installs Django and Gunicorn is the server that will run in heroku, handles everything that happens between the web server and the web application.
* pip3 install dj_database_url==0.5.0 psycopg2 - Installs PostgreSQL and psycopg2.
* pip3 install dj3-cloudinary-storage - Cloudinary handles all the static files and the images uploaded by users.
* pip install pyparsing pydot - To create a graph of the database.
* pip install django-extensions - Supporting library of Graph models.
* pip install coverage - For testing the app model.

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
<pre>
"pip3 install 'django<4' gunicorn"
"pip3 install dj_database_url==0.5.0 psycopg2"
"pip3 install dj3-cloudinary-storage"
</pre>
<details><summary>Heroku Deployment - Step 4:</summary>
<img src="readme/deployment/deployment-1.png" alt="'pip3 install 'django<4' gunicorn' typed in the terminal" style="width: 100%">
<img src="readme/deployment/deployment-2.png" alt="'pip3 install dj_database_url==0.5.0 psycopg2' typed in the terminal" style="width: 100%">
<img src="readme/deployment/deployment-3.png" alt="'pip3 install dj3-cloudinary-storage typed' in the terminal" style="width: 100%">
</details>
<br>

5. After the libraries have been installed, type the following command to create a requirements.txt file:
<pre>
"pip3 freeze --local > requirements.txt"
</pre>
<details><summary>Heroku Deployment - Step 5:</summary>
<img src="readme/deployment/deployment-4.png" alt="'pip3 freeze --local > requirements.txt' typed in the terminal" style="width: 100%">
<img src="readme/deployment/step-5.png" alt="step of deployment" style="width: 100%">
</details>

<br>

6. Create the Django project by typing the following command:
<pre>
"django-admin startproject PROJECT_NAME ."
</pre> - Don't forget the dot at the end.
<details><summary>Heroku Deployment - Step 6:</summary>
<img src="readme/deployment/step-6.png" alt="step of deployment" style="width: 100%">
After typing the command this 'blog' folder with files will be displayed in the directory.
<img src="readme/deployment/step-7.png" alt="step of deployment" style="width: 100%">
</details>
  
<br>

7. Create the Django application by typing the following command:
<pre>
"python3 manage.py startapp APP_NAME"
</pre>
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
<pre>
"python3 manage.py migrate"
</pre>
<details><summary>Heroku Deployment - Step 9:</summary>
<img src="readme/deployment/step-11.png" alt="step of deployment" style="width: 100%">
</details>  
<br>


10. To see if everything works as expected. In the terminal type:
<pre>
"'python3 manage.py runserver' and click 'Open Browser'"
</pre>
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
<pre>
    1. Click the GitHub logo.
    2. Search for the GitHub repository that was made for this project.
    3. When the repository is found click 'Connect'.
    </pre>
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
<pre>"Import os"
"os.environ["DATABASE_URL"]"
Paste the url that was copied earlier in the red area that is shown below.
</pre>
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
<pre>
"os.environ["SECRET_KEY"]"
Paste the "SECRET_KEY" value that was copied from the 'settings.py' as value for 'os.environ["SECRET_KEY"]'.
</pre>
<details><summary>Heroku Deployment - Step 25:</summary>
<img src="readme/deployment/step-28.png" alt="step of deployment" style="width: 100%"> 
</details>
<br>

26. Add the following text on top of the 'setting.py' file:
<pre>
"import os"
"import dj_database_url"
<pre>if os.path.isfile('env.py'):
        import os</pre>
</pre>
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
<pre>
    1. 'cloudinary_storage'
    2. 'django.contrib.staticfiles'
    3. 'cloudinary'
    </pre>
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
<pre>
media
templates
static
</pre>
<details><summary>Heroku Deployment - Step 40:</summary>
<img src="readme/deployment/step-43.png" alt="step of deployment" style="width: 100%">
</details> 
<br>

41. In the application in Heroku in 'Config Vars'. Add 'CLOUDINARY_URL' and as value (the red area) add the url. Also, add the following keys and values:
<pre>
key: PORT - value: 8000
key: DISABLE_COLLECTSTATIC - value: 1
</pre>
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
<pre>
"web: gunicorn PROJECT_NAME.wsgi"
</pre>
<details><summary>Heroku Deployment - Step 43:</summary>
<img src="readme/deployment/step-45.png" alt="step of deployment" style="width: 100%">
</details>
<br>


Save all the files and add, commit and push the project to GitHub by writing these commands:
<pre>
"git add ."
"git commit -m "Deployment Commit""
"git push"
</pre>

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


# Cloning

1. Open the GitHub repository.
2. Click the green 'Code' button and copy the given URL.
<img src="readme/deployment/cloning.png" alt="step of deployment" style="width: 100%">

3. Open Git Bash and change directory to where you want the cloned directory.
4. Write:
<pre>
"git clone"
</pre> and paste the URL that was copied in Github and then click 'enter'.
5. In Git Bash locate the cloned directory.
6. Type:
<pre>
"code ."
</pre> this will launch the project in VSCode.
7. Now install the requirements needed to run the project by typing this command:
<pre>
"pip3 install -r requirements.txt"
</pre>
8. Create an 'env.py' file in the top level directory.
Add the os.environ as shown in the image with their respective values.
9. Add the variables from the env.py file in Herokus Config Vars when it is time for deployment.
<img src="readme/deployment/step-37.png" alt="step of deployment" style="width: 100%">
9. Now run this command:
<pre>
"python manage.py migrate"
</pre>
10. Run this command:
<pre>
"python manage.py runserver"
</pre>
If everything is working as expected the project will launch and be ready for development.

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

These pictures are included in the features pictures.

<br>

#### Fake profiles
<br>
Photo by Spencer Selover: https://www.pexels.com/sv-se/foto/affarsman-mode-man-person-428364/
<br>
Photo by Min An: https://www.pexels.com/sv-se/foto/person-kvinna-avslappning-flicka-1547971/
<br>
Photo by Andrea Piacquadio: https://www.pexels.com/sv-se/foto/person-kvinna-staende-kansla-774909/
<br>

#### Posts
Photo by: Element5 Digital: https://www.pexels.com/sv-se/foto/tra-lampor-skrivbord-lampa-1125136/
<br>
Photo by: Taryn Elliott: https://www.pexels.com/sv-se/foto/sovrum-interior-heminredning-skandinavisk-4440213/
<br>
Photo by: Polina Kovaleva: https://www.pexels.com/sv-se/foto/sang-sovrum-lampa-design-5644277/
<br>
Photo by: Emre Can Acer: https://www.pexels.com/sv-se/foto/tra-bocker-hus-bord-2079249/
<br>
Photo by: Maksim Goncharenok: https://www.pexels.com/sv-se/foto/tra-vagg-bord-lyx-4352247/
<br>
Photo by: Jean van der Meulen: https://www.pexels.com/sv-se/foto/hotell-hus-glas-lyx-1457847/
<br>
Photo by: PNW Production: https://www.pexels.com/sv-se/foto/sang-vaxt-vit-design-8251666/
<br>
Photo by: Maria Orlova: https://www.pexels.com/sv-se/foto/kreativ-vagg-hus-vaxt-4915834/
<br>
Photo by: Olena Bohovyk: https://www.pexels.com/sv-se/foto/romantisk-mork-vinter-hus-5686478/
<br>
Photo by: Zsófia Fehér: https://www.pexels.com/sv-se/foto/byggnad-arkitektur-resa-utomhus-14532811/
<br>
Photo by: Dilruba Sarıçimen: https://www.pexels.com/sv-se/foto/dryck-dricksglas-vertikalt-skott-narbild-8851505/
<br>
Photo by: Element5 Digital: https://www.pexels.com/sv-se/foto/tra-lampor-skrivbord-lampa-1125136/
<br>
Photo by: Max Vakhtbovych: https://www.pexels.com/sv-se/foto/mat-stad-restaurang-manniskor-6434622/
<br>
Photo by: Pixabay: https://www.pexels.com/sv-se/foto/barnkammare-dekor-design-golv-462235/
<br>
Photo by: Mathilde Langevin: https://www.pexels.com/sv-se/foto/dekoration-bage-spegel-vas-14320924/
<br>
Photo by: Vincent Rivaud: https://www.pexels.com/sv-se/foto/hus-lyx-lampa-hem-2227832/
<br>
Photo by: Victoria Akvarel : https://www.pexels.com/sv-se/foto/hotell-hus-arkitektur-lyx-3315291/
<br>
Photo by: cottonbro studio: https://www.pexels.com/sv-se/foto/ljus-konst-kontor-vagg-4067759/
<br>
Photo by Pixabay: https://www.pexels.com/sv-se/foto/ljus-skrivbord-vagg-bord-509922/

# Acknowledgement
This website has been made for my 4th Portfolio Project (Full-Stack Toolkit) - Diploma in Full Stack Software Development at [Code Institute](https://codeinstitute.net/).
I would like to thank my mentor Precious Ijege from Code Institute who helped me develop the website with feedback through the project.