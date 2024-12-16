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
    return render(req,"admin/indexs.html")

def add_page(req):
    return render(req,"admin/add_page.html")

def view_page(req):
    # data=[dest for ]
    data=destinations.find()
    return render(req,"admin/view_page.html",{"data":data})

def del_page(req):
    return render(req,"admin/del_page.html")


def enter(req):
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
    destinations.insert_one(data).inserted_id
    print(id)
    return render(req,"admin/add_page.html")

def update(req,id):
    data=destinations.find_one({"title":id})
    return render(req,"admin/update.html",{"data": data})

def update_data(req):
    # path=""
    # if len(req.FILES)!=0:
    #     img=req.FILES['image']
    #     fs = FileSystemStorage()
    #     filename = fs.save(img.name, img)
    #     uploaded_file_url= fs.url(filename)
    #     path=uploaded_file_url
    
    title=req.POST['title']
    price=int(req.POST['price'])
    description=req.POST['description']
    data={
        "title":title,
        "price":price,
        "description":description,
    }
    id=destinations.update_one({"title":title},{"$set":{"price":price,"description":description}})
    print(id)
    return render(req,"admin/add_page.html")