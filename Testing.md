# Testing

- Here I tested functionality of my website. Beaware it might be little bit chaotic.

## Navigation bar

- As a non-logged in user

| -- |Element| Action | wanted result | Score |
|  -- |   ---      | ---       |  ----   | ---- |
| 1 |  	 Logo| click | shows page with all posts | pass|
| 2 |    Search| click | user search for author, shows posts with author name | pass|
| 3 |    Search| click | shows no post message  if user search for random letters ex.:"dgdsfgd" |pass|
| 4 |    Register| click | redirect to registration page | pass|
| 5 |    Login| click | redirects to login page | pass|
| 6 |    Register| display |  	Render for non authenticated users | pass|
| 7 |    Login| display |  	Render for non authenticated users | pass|
| 8 |    logout| display |  	does not render for non authenticated users | pass|

- As a logged in user

| -- |Element| Action | wanted result | Score |
|  -- |   ---      | ---       |  ----   | ---- |
| 1 |  	 Logo| click | shows page with all posts | pass|
| 2 |    Search| click | user search for author, shows posts with author name | pass|
| 3 |    Search| click | shows no post message  if user search for random letters ex.:"dgdsfgd" |pass|
| 4 |    LogOut| click | redirects to logout page | pass|
| 5 |    Register| display |  does not render if user is authenticated | pass|
| 6 |    Login| display |  does not render if user is authenticated | pass|
| 7 |    LogOut| display |  Render only if user is authenticated | pass|
| 8 |    Dropdown menu| display |  Render only if user is authenticated | pass|
| 9 |    Dropdown menus| click |  user can access links in drobdowm menu and use it to navigate website | pass|
| 10 |    Posts - New Post| click | when user clicks on new post link then its redirected to create post page | pass|
| 12 |    Posts - New Cat| click | when user clicks on new category link then its redirected to create new category page | pass|
| 13 |   Info - Contact | click | when user click on Contact link then its redirected to contact page | pass|
| 14 |   Info - About us | click | when user click on About us link then its redirected to about us page | pass|
| 15 |   User - Edit profile | click | when user click on Edit Profile link then its redirected to edit profile page | pass|
| 16 |   User - User profile | click | when user click on User Profile link then its redirected to User profile page | pass|
| 17 |   Blog - category menus| click | when user click on any category then only posts in category they selected are shown | pass|


## Page with posts

- As a non-logged in user

| -- |Element| Action | wanted result | Score |
|  -- |   ---      | ---       |  ----   | ---- |
| 1 |  	 Category| click | redirects to page which informs user to log in | pass|
| 2 |    Read more| click | redirects user to post which he wants to read | pass|
| 3 |    Edit| display | Render only if user is authenticated | pass|
| 4 |    Likes| display | User can see how many likes post has | pass|
| 5 |    Delete| display | Render only if user is authenticated | pass|
| 6 |    Pagination| click | allows user to browse posts on website | pass|
| 7 |    Sort option| click | Sorts post by likes or by date | pass|
| 8 |    All post ## | display | Shows ho many posts are currently on website | pass|

- As a logged in user

| -- |Element| Action | wanted result | Score |
|  -- |   ---      | ---       |  ----   | ---- |
| 1 |  	 Category| click | redirects to page with all posts in selected category | pass|
| 2 |    Read more| click | redirects user to post which he wants to read | pass|
| 3 |    Edit| display | Render only if user is authenticated and author of the post | pass|
| 4 |    Edit| click | Redirects to edit post page only if user is authenticated and author of the post| pass|
| 5 |    Likes| display | User can see how many likes post has | pass|
| 6 |    Delete| display | Render only if user is authenticated and author of the post | pass|
| 7 |    Delete| click | Redirects to delete page only if user is authenticated and author of the post | pass|
| 8 |    Pagination| click | allows user to browse posts on website | pass|
| 9 |    Sort option| click | Sorts post by likes or by date | pass|
| 10 |    All post ## | display | Shows ho many posts are currently on website | pass|



### Inside post
- Inside post: as a non logged in user

| -- |Element| Action | wanted result | Score |
|  -- |   ---      | ---       |  ----   | ---- |
| 1 |  	 Category| click | redirects to page which informs user to log in | pass|
| 2 |    Back| click | redirects user to home page with all posts | pass|
| 3 |    Edit| display | Render only if user is authenticated | pass|
| 4 |    Delete| display | Render only if user is authenticated | pass|
| 5 |    Profile| display | Render only if user is authenticated | pass|
| 6 |    Login to comment| click | redirects to login page | pass|
| 7 |    Login to like| click | redirects to login page | pass|
| 8 |    Comment section| display | user can read comments | pass|
| 9 |    upvote comment| display |Render only if user is authenticated | pass|
| 10 |    downvote comment| display |Render only if user is authenticated | pass|
| 11 |    Comment section| display | user can see number of comments | pass|

- Inside post: as a logged in user ( is authenticated )

| -- |Element| Action | wanted result | Score |
|  -- |   ---      | ---       |  ----   | ---- |
| 1 |  	 Category| click | redirects to page with all posts in selected category | pass|
| 2 |    Back| click | redirects user to home page with all posts | pass|
| 3 |    Edit| display | Render only if user is authenticated and author of the post| pass|
| 4 |    Edit| click | Redirects to edit post page only if user is authenticated and author of the post| pass|
| 5 |    Delete| display | Render only if user is authenticated and author of the post | pass|
| 6 |    Delete| click | Redirects to delete page only if user is authenticated and author of the post | pass|
| 7 |    Profile| display | Render only if user is authenticated | pass|
| 8 |    Profile| click | Redirects to profile page only if user is authenticated and author of the post  | pass|
| 9 |    add comment here| display |Render only if user is authenticated | pass|
| 10 |    add comment here| click | redirects to page where user can write comment and post it | pass|
| 11 |    like| click |add like to post "+1" | pass|
| 12 |    Unlike| click |reduce like to post "-1" | pass|
| 13 |    Comment section| display | user can read comments | pass|
| 14 |    Comment section| display | Number of comments | pass|
| 15 |    upvote comment| click | user can upvote comment | pass|
| 16 |   downvote comment| click | user can downvote comment | pass|
| 17 |    Comment delete| click | user can delete comments only if user is authenticated and author of the comment | pass|


## Registration page and login page.

| -- |Element| Action | wanted result | Score |
|  -- |   ---      | ---       |  ----   | ---- |
| 1 |  	 Registration page| click | Lets user register on website after he fills up all fields | pass|
| 2 |  	 Registration page| click | Wont let user to use same name as other users | pass|
| 3 |    Login page| click | If user is not registered then login page wont let him logIn | pass|
| 4 |    Login page| click | If user is registered then login page will let him logIn | pass|
| 5 |    Login/registration page| click | both forms have to be correctly filled out in order to work | pass|

## miscellaneous

- Inside Contact us page and About us page : as a non logged in user and logged in user (works for both)

| -- |Element| Action | wanted result | Score |
|  -- |   ---      | ---       |  ----   | ---- |
| 1 |  	 About us| click | "Redirect to Posts" return user to home page with all posts | pass|
| 2 |    Contact us| click | User fills up form and sends message to admin/admin receive it | pass|

- As a logged in user

| -- |Element| Action | wanted result | Score |
|  -- |   ---      | ---       |  ----   | ---- |
| 1 |  	 New post page| click | Lets user create new post and shows it on home page | pass|
| 2 |    New category page| click | Lets user create new category but its working after database restarts | pass|
| 3 |    Edit profile page | click | Lets user edit bio | pass|
| 4 |    User profile page | click | Lets user see all his posts, bio, link to edit profile | pass|
| 5 |    Delete post page | click | Lets user delete selected post if he is the author of the post | pass|
| 6 |    Notifications | Display | when user log in, log out, create post and such user gets notification | pass|


## Footer

- As a non-logged in user and also as a logged in user. (works for both)

| -- |Element| Action | wanted result | Score |
|  -- |   ---      | ---       |  ----   | ---- |
| 1 |  	 Socials| click | opens social links in new window | pass|
| 2 |    Contact Us| click | redirects user to contact page | pass|
| 3 |    About us| click | redirects user to about us page |pass|


[Back to Readme](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/README.md)