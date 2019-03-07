from django.shortcuts import render, redirect
from .models import Todo


def home(request):
    global lst
    #首先判断是否是POST请求
    if request.method == 'POST':
        #如果用户没输入就添加要给一个警告提示
        if request.POST["待办事项"] == "":
            content = {"Lists":Todo.objects.all(), "alert":"亲亲，请输入您的待办事项哦！"}
            return render(request, "todolist/home.html", content)
        #如果用户输入了就添加用户输入的事项
        else:
            a_row = Todo(thing=request.POST["待办事项"], done=False)
            a_row.save()
            content = {"Lists" : Todo.objects.all(), "alert_info":"添加成功！"}
            return render(request, "todolist/home.html", content)
    #如果刷新页面这时候没有这个字典直接返回页面
    elif request.method == "GET":
        content = {"Lists":Todo.objects.all()}
        return render(request, "todolist/home.html", content)

def about(request):
    return render(request, "todolist/about.html")

def edit(request, eve_list_id):
    if request.method == "POST":
        if request.POST["编辑页面"] == "":
            return render(request, "todolist/edit.html", {"alert":"亲亲，请输入您的修改哦！"})
        else:
            a = Todo.objects.get(id=eve_list_id)
            a.thing = request.POST["编辑页面"]
            a.save()
            return redirect("todolist:主页")
    elif request.method == "GET":
        content = {"待修改事项" : Todo.objects.get(id=eve_list_id).thing}
        return render(request, "todolist/edit.html", content)

def delete(request, eve_list_id):
    a = Todo.objects.get(id=eve_list_id)
    a.delete()
    return redirect("todolist:主页")

def cross(request, eve_list_id):
    if request.POST["完成状态"] == "已完成":
        a = Todo.objects.get(id=eve_list_id)
        a.done = True
        a.save()
        return redirect("todolist:主页")
    else:
        a = Todo.objects.get(id=eve_list_id)
        a.done = False
        a.save()
        return redirect("todolist:主页")
