- [x] Create mysite `todo_awesome`
- [x] Create todo app
- [x] register todo app
- [x] Test project home page
- [ ] Craete a dashboard page
  - Show user's all todo list
  - [x] create and rigister a template folder
  - [x] create `base.html` and `index.html`
  - [x] craete `views.py` in todo_awesome
  - [ ] `class DashboardView`
  - [ ] modify `dashboard.html`
  - [x] `path('', DashboardView.as_view(), name="dashboard")`
  ~~- [x] `def dashboard(request)->response`~~
  ~~- [x] `path('', views.dashboard, name='dashboard')`~~
- [ ] Startapp `todo`
  - [x] add `todo/urls.py` to `urls.py`
  - [ ] design [`todo/models.py`](../src/todo_awesome/todo/models.py)
    - [ ] Todolist with user foreign key
  - [x] register todo, todolist model to admin