- CSS:
![css](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/Htmlcssjs/css_validation.png)

- Js:
![js](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/Htmlcssjs/jscript_validator.png)

- HTML Checker:

home page
![home](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/Htmlcssjs/htmlchecker_detail.png)

add category page
![add](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/Htmlcssjs/htmlchecker_detail.png)

contact page
![contact](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/Htmlcssjs/htmlchecker_detail.png)

Edit profile page
![edit](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/Htmlcssjs/htmlchecker_detail.png)

Profile page
![profile](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/Htmlcssjs/htmlchecker_detail.png)

Category page   
![cats](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/Htmlcssjs/htmlchecker_detail.png)

log out page
![logout](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/Htmlcssjs/htmlchecker_detail.png)

log IN
![log in](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/Htmlcssjs/htmlchecker_detail.png)

Page with a post
![post](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/Htmlcssjs/htmlchecker_detail.png)

search page:  post nothing found
![search](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/Htmlcssjs/htmlchecker_detail.png)

Delete page
![delete](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/Htmlcssjs/htmlchecker_detail.png)

registration page
![regist](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/Htmlcssjs/htmlchecker_detail.png)

- Pages with errors - widget used give these errors.

new post page (summernote widget)
![newpost](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/Htmlcssjs/summernote_error.png)

Edit post page (summernote widget)
![editpage](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/Htmlcssjs/summernote_error.png)

Currently 12 out of 14 pages pass HTML checker.

# Bugs
- Currently 2 pages dont pass html checker and it is because of the widgets I used.

- Create your New post and Edit your post page:  here I get lots of errors from [summernote widget](https://github.com/summernote/django-summernote). Its really hard to fix errors here, on stack I found Iam not only one who got these errors and cant fix them. Seems its limitation of the [summernote widget](https://github.com/summernote/django-summernote).

- For registration I tried to use [django widgets tweaks](https://github.com/jazzband/django-widget-tweaks) but HTML validator gave me error with password input required = True. It was this widget which cause error and I decided to use crispy forms for registration page, now registration page passes [w3validator](https://validator.w3.org/)


[Back to readme](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/README.md)