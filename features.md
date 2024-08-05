# Features

### Navbar
- Navigation bar with website logo at the top of the website allows users access different pages such as Posts, Info , Login/logout, Registration/Profile, search bar.

![navbar](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/navbar.png)

- From the navigation bar menu user can also access all categories available, adding new blog post or contact admin, search for posts. Navbar has multyple drop down menus for user to explore.

![navbar](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/navbar2.png)

- For smaller devices navbar is collapsible

![navbar](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/navbar3.png)

### Footer

- Footer section at the bottom of the website include social links with effect and contact/about us page, so people who are not registered can read and contact owner of the website

![footer](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/footer.png)

### Main Pages

- Home Page its greets users upon their login/registration. so they can start reading posts.

![home](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/home_page.png)

- About us page lets user know little bit about website.

![about](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/about_us.png)

- Contact us page lets user contact owner on their mail and also they get notification if their email was received.

![contact](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/contact_us.png)

![contact](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/email_notification.png)
- its using django email system

- User gets notification when he sends messsage, creates posts, edit posts, login and such. Here is an example:
![contact](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/notification.png)
- messages use django message system.

### User registration and authentication pages
- This pages allow users to create an account, log in and access additional features of the website such as commenting and liking or profile view.

1. Login
![contact](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/login.png)

2. Registration
![contact](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/registration.png)

3. Log Out
![contact](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/log_out.png)

### User profile pages

- If Users created posts they are able to see them in the profile box with their published or draft posts with ability to change them or delete them.
- This page allow users to view their profile with additional details such username, date registered, created posts.

Profile page

![contact](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/profile.png)

Edit profile page

![contact](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/editprofile.png)

### Blog pages
- On this page users can view all latest blog posts sorted by a date or by likes.
- Every post has a featured image or a default image if author won't upload an image.
- Every post has also additional details such as Title of the post, author, date created, category, num. of likes, update or delete post button if user is author of the post or superuser.

![page](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/blog_page.png)

- After clicking on one of the post image, title or "Read More link in the excerpt text" user is redirected to a post detail page where he can read more about the post.

![page](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/detail_page.png)

- Users can also view posts sorted by category.

![page](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/category.png)

### Blog post managment

- If user is authenticated they can add blog posts.
![page](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/new_post.png)

- If user is authenticated they can edit blog posts which they created.
![page](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/edit_post.png)

- If user is authenticated they can delete blog posts which they created.
![page](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/delete.png)

### Search
- Search bar in the navbar enables users to find blog posts by title or their author.
- Once searched page will redirect to the search results page and show all the relevant posts.

![page](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/search.png)

- If search post is not found, relevant text is displayed.
![page](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/search2.png)

# Extra Features

- Includes: Pagination, Likes, Upvotes and downvotes, comment section.
1. User cannot upvote and downvote comment at the same time.
2. User can like once post or unlike it if he previously liked it ( user cannot like/unlike posts multiple times).
3. User can add comment and also delete comment which they made.
4. Blog shows 4 posts per page.
![page](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/like.png)

- If Post has no comment and no like then like button is yellow and comment section says no comment.
![page](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/features/like2.png)

[Back to Readme](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/README.md)