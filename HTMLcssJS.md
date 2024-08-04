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

- Pages with errors - widgets used give these errors.

registration page  (widget used to style it)
![regist](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/Htmlcssjs/registration_page_error.png)

new post page (summernote widget)
![newpost](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/Htmlcssjs/summernote_error.png)

Edit post page (summernote widget)
![editpage](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/Htmlcssjs/summernote_error.png)

Currently 11 out of 14 pages pass HTML checker.

# Bugs
- Currently 3 pages dont pass html checker and I think its because of the widgets I used.

- For registration page I used [django-widget-tweaks==1.5.0](https://github.com/jazzband/django-widget-tweaks) to style it. I tried to fix as many errors on the registration page as possible, but some of them Iam not able to edit out or its actually needed for page to work as intended. It was interresting experience to use this widget but unfortunately Iam not experienced enough to fix errors shown in HTML checker (if I do what HTML checker says then error will break app and give 500 error). I hope it wont be ground breaking error. I guess its just limitation of the widget and I would use different widget for future project, its still good to try something new.

- Create your new post and Edit your post page:  here I get lots of errors from [summernote widget](https://github.com/summernote/django-summernote). Its really hard to fix errors here, on stack I found Iam not only one who got these errors and cant fix them. Seems its limitation of the [summernote widget](https://github.com/summernote/django-summernote) same as [django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks).

[Back to readme](https://github.com/PeterSvk1/P4djangoSWfinalBlog/blob/main/README.md)