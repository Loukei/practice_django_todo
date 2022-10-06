# Some tricks needs to records

## Class based view

- 一般基於函數的視圖可以處裡多數情況
  - endpoint必須處裡更多有關
    - 使用者是否登入
    - 使用者的權限控制
    - 針對不同的HTTP Method執行不同的回應
    - 頁面的邏輯較複雜，比如儀錶板等等
- 引入Class來處理會更好

[Class-based views | Django documentation | Django](https://docs.djangoproject.com/en/4.1/topics/class-based-views/)

## class base view and Login control

當使用基於函數的View時，有一個很方便的裝飾器可以使用[login_required decorator](https://docs.djangoproject.com/en/4.1/topics/auth/default/#the-login-required-decorator)，但在class view則需要不同的方式

[使用 Django 的验证系统 | Django 文档 | Django](https://docs.djangoproject.com/zh-hans/3.2/topics/auth/default/#the-loginrequired-mixin)

## Template with user

[Using the Django authentication system | Django documentation | Django](https://docs.djangoproject.com/en/4.1/topics/auth/default/#users)

## ListView

ListView用來顯示以列表出現的資料

[Django的ListView超详细用法（含分页paginate功能），文章有增加内容_HD243608836的博客-CSDN博客_django listview 多个model](https://blog.csdn.net/HD243608836/article/details/107182567)

## 良好的模板習慣

1. 在html開頭以註釋標明當前的檔案位置
2. 使用註釋明確標明每個段落的功能
3. 為每個`{% block %}`標明用途

## Relate work

- 基於GET與POST方法的實現
  - [Manage Your To-Do Lists Using Python and Django – Real Python](https://realpython.com/django-todo-lists/#step-4-add-your-sample-to-do-data)
  - [Develop a Simple Python Django ToDo App in 1 minute - DEV Community 👩‍💻👨‍💻](https://dev.to/nditah/develop-a-simple-python-django-todo-app-in-1-minute-4908)
