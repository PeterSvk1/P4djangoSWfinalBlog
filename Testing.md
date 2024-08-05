# Testing

- Here I tested functionality of my website. Beaware it mght be little bit chaotic.

### Navigation bar

- As a non-logged in user


| -- |Element| Action | wanted result | Score |
|  -- |   ---      | ---       |  ----   | ---- |
| 1 |  	 Logo| click | shows page with all posts | pass|
| 2 |    Search| click | user search for author, shows posts with author name | pass|
| 5 |    Search| click | shows no post message  if user search for random letters ex.:"dgdsfgd" |pass|
| 3 |    Register| click | redirect to registration page | pass|
| 4 |    Login| click | redirects to login page | pass|
| 5 |    Register| display |  	Render for non authenticated users | pass|
| 6 |    Login| display |  	Render for non authenticated users | pass|

### Page with posts

- As a non-logged in user


| -- |Element| Action | wanted result | Score |
|  -- |   ---      | ---       |  ----   | ---- |
| 1 |  	 Category| click | redirects to page which informs user to log in | pass|
| 2 |    Read more| click | redirects user to post which he wants to read | pass|
| 3 |    Edit| display | Render only if user is authenticated | pass|
| 4 |    likes| display | User can see how many likes post has | pass|
| 5 |    delete| display | Render only if user is authenticated | pass|
| 6 |    pagination| click | allows user to browse posts on website | pass|


- Inside post


| -- |Element| Action | wanted result | Score |
|  -- |   ---      | ---       |  ----   | ---- |
| 1 |  	 Category| click | redirects to page which informs user to log in | pass|
| 2 |    back| click | redirects user to home page with all posts | pass|
| 3 |    Edit| display | Render only if user is authenticated | pass|
| 4 |    delete| display | Render only if user is authenticated | pass|
| 4 |    profile| display | Render only if user is authenticated | pass|
| 5 |    login to comment| click | redirects to login page | pass|
| 6 |    login to like| click | redirects to login page | pass|
| 7 |    Comment section| display | user can read comments | pass|

- Inside Contact us page and About us page

| -- |Element| Action | wanted result | Score |
|  -- |   ---      | ---       |  ----   | ---- |
| 1 |  	 About us| click | "Redirect to Posts" return user to home page with all posts | pass|
| 2 |    Contact us| click | User fills up form and sends message to admin/admin receive it | pass|


### Footer

- As a non-logged in user


| -- |Element| Action | wanted result | Score |
|  -- |   ---      | ---       |  ----   | ---- |
| 1 |  	 Socials| click | opens social links in new window | pass|
| 2 |    Contact Us| click | redirects user to contact page | pass|
| 3 |    About us| click | redirects user to about us page |pass|