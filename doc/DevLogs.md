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

當使用基於函數的View時，有一個很方便的裝飾器可以使用[login_required decorator](https://docs.djangoproject.com/en/4.1/topics/auth/default/#the-login-required-decorator)，但在`ClassView`則需要不同的方式

- [使用 Django 的验证系统 | Django 文档 | Django](https://docs.djangoproject.com/zh-hans/3.2/topics/auth/default/#the-loginrequired-mixin)

## Template with user

[Using the Django authentication system | Django documentation | Django](https://docs.djangoproject.com/en/4.1/topics/auth/default/#users)

## ListView

ListView用來顯示以列表出現的資料

[Django的ListView超详细用法（含分页paginate功能），文章有增加内容_HD243608836的博客-CSDN博客_django listview 多个model](https://blog.csdn.net/HD243608836/article/details/107182567)

## 良好的模板習慣

1. 在html開頭以註釋標明當前的檔案位置
2. 使用註釋明確標明每個段落的功能
3. 為每個`{% block %}`標明用途

## ModelFrom

建立模型後，常需要透過前端的表單來輸入相對應的表單資料。

新手的方式:
- 在HTML模板撰寫表單，一邊參考models的格式一邊撰寫HTML模板
- 撰寫Views，依照Model的欄位撰寫對應的檢查邏輯
  - 如果使用者輸入合法，則透過(ORM/SQL)語法建立對應的資料

Django的ModelForm:
- 根據開發者所選擇的欄位與欄位型態自動提供對應的`<input type=>`選項
- 生成對應的`<label>`
- 可以提供基本的輸入檢查邏輯，也可以自行撰寫
- 使用`save()`函數就可以自動存入資料庫

ModelForm的
- 優點
  - 當模型的內容出現變化，開發者無須來回修正template與views的部分，而是集中在處理Model與ModelForm上面
- 缺點
  - 要套用CSS樣式的時候必須回到對應的ModelForm修改對應的html widgets，而非在模板修改
    - 想要在模板層處理也不是不行
      - 安裝套件
      - 在模板拆分對應的field內容

- [从模型创建表单 | Django 文档 | Django](https://docs.djangoproject.com/zh-hans/4.1/topics/forms/modelforms/)
- [[Django教學7]善用Django ModelForm快速開發CRUD應用程式教學](https://www.learncodewithmike.com/2020/03/django-modelform.html)

## ClassView with Model CRUD

對於常見的任務，Django提供一套便捷的方式來處理，開發者只要繼承並修改對應的參數

### CreateView

新增模型
- [通用编辑视图 | Django 文档 | Django](https://docs.djangoproject.com/zh-hans/4.1/ref/class-based-views/generic-editing/#createview)
- [Createview - Class Based Views Django - GeeksforGeeks](https://www.geeksforgeeks.org/createview-class-based-views-django/)

### DetailView

- 查詢
- [通用显示视图 | Django 文档 | Django](https://docs.djangoproject.com/zh-hans/4.1/ref/class-based-views/generic-display/#detailview)

### ListView

- 查詢列表
- [通用显示视图 | Django 文档 | Django](https://docs.djangoproject.com/zh-hans/4.1/ref/class-based-views/generic-display/#listview)

### UpadteView

- 更新
- [使用基于类的视图处理表单 | Django 文档 | Django](https://docs.djangoproject.com/zh-hans/4.1/topics/class-based-views/generic-editing/#model-forms)

### DeleteView

- 刪除
- [通用编辑视图 | Django 文档 | Django](https://docs.djangoproject.com/zh-hans/4.1/ref/class-based-views/generic-editing/#deleteview)

### Class view with custom ModelForm

如果想要使用預設好的`ClassView`，並且套用自訂的`ModelForm`

- [使用基于类的视图处理表单 | Django 文档 | Django](https://docs.djangoproject.com/zh-hans/4.1/topics/class-based-views/generic-editing/#model-forms)

## CreateView 不使用 template

當View的行為作為API命令使用，類似"按下新增/修改/刪除等按鈕"的行為，預期的結果不是返回一個新的頁面，而是回應一個JSON之類的回覆的時候，View就不需要渲染頁面，更無須指定template

- [Django CreateView without template rendering](https://copyprogramming.com/howto/django-how-to-create-view-function-without-template#django-how-to-create-view-function-without-template:~:text=template%20without%20model-,Django%20CreateView%20without%20template%20rendering,-Question%3A)

## 一些頁面設計的資源

- [W3Schools How TO - Code snippets for HTML, CSS and JavaScript](https://www.w3schools.com/howto/default.asp)
- [W3.CSS Home](https://www.w3schools.com/w3css/default.asp)

## UI: inline form

#TODO
- [How To Create a Responsive Inline Form With CSS](https://www.w3schools.com/HOWTO/howto_css_inline_form.asp)

## Relate work

- 基於`GET`與`POST`方法的實現
  - [Manage Your To-Do Lists Using Python and Django – Real Python](https://realpython.com/django-todo-lists/#step-4-add-your-sample-to-do-data)
  - [Develop a Simple Python Django ToDo App in 1 minute - DEV Community 👩‍💻👨‍💻](https://dev.to/nditah/develop-a-simple-python-django-todo-app-in-1-minute-4908)
