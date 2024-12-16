from django.shortcuts import render
from . models import destinations
from django.core.files.storage import FileSystemStorage
# Create your views here.
def home(req):
    return render(req,"index.html")

def dashboard(req):
    return render(req,"admin/indexs.html")

def about(req):
    return render(req,"about.html")

def admin(req):
    return render(req,"admin/login.html")

def add_page(req):
    return render(req,"admin/add_page.html")

def view_page(req):
    # data=[dest for ]
    data=destinations.find()
    return render(req,"admin/view_page.html",{"data":data})

def del_page(req):
    data=destinations.find()
    return render(req,"admin/del_page.html",{"data":data})

def delete(req,id):
    data=destinations.find_one({"title":id})
    if data:
        destinations.delete_one(data)
    remain_data=destinations.find()
    return render(req,"admin/del_page.html",{"data":remain_data})



def enter(req):
    path=""
    if len(req.FILES)!=0:
        img=req.FILES['image']
        print(img)
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        print(filename)
        uploaded_file_url= fs.url(filename)
        path=uploaded_file_url
        print(path)
    
    title=req.POST['title']
    price=req.POST['price']
    description=req.POST['description']
    data={
        "title":title,
        "price":price,
        "description":description,
        "path":path
    }
    destinations.insert_one(data).inserted_id
    print(id)
    return render(req,"admin/add_page.html")

def update(req,id):
    data=destinations.find_one({"title":id})
    return render(req,"admin/update.html",{"data": data})

def update_data(req):
    path=""
    if len(req.FILES)!=0:
        img=req.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        uploaded_file_url= fs.url(filename)
        path=uploaded_file_url
    
    title=req.POST['title']
    price=int(req.POST['price'])
    description=req.POST['description']
    data={
        "title":title,
        "price":price,
        "description":description,
        "path":path
    }
    destinations.update_one({"title":title},{"$set":{"price":price,"description":description,"path":path}})
    return render(req,"admin/add_page.html")