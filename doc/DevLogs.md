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