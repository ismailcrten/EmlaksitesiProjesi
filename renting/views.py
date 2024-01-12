from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from renting.models import Type, Feature, Renting, Image, Favorite, Tag
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt
from account.models import User
from renting.utils import MailHandler
from django.contrib.auth import logout


def check_user(user):
    return user.is_authenticated and (user.is_superuser or user.is_staff)


def is_owner(user, owner):
    return user.id == owner.id

# Create your views here.
@xframe_options_exempt
def apartDetailView(request, pk):
    '''
    Apart detail view class
    '''
    apart = Renting.objects.get(uuid=pk)
    images = apart.get_images()
    return render(request, 'renting/detail.html', {'apart': apart, 'images': images})
    

def homeView(request):
    # get page number
    type = Type.objects.all()
    feature = Feature.objects.all()
    meta = Tag.objects.get(id=1)

    if request.method == 'POST':
        # formdan gelen verilerin alınması,
        type_value = request.POST.getlist('type')
        feature_value = request.POST.getlist('feature')
        min_price = request.POST.get('price_min')
        max_price = request.POST.get('price_max')

        # filter data
        renting = Renting().filter_renting(type_value, feature_value, min_price, max_price)
        house_list = []
        for r in renting:
            map = {
                'house': r,
                'images': r.get_images()
            }
            house_list.append(map)

        # return data
        return render(request, 'renting/home.html', 
                    context={'type': type, 'feature': feature, 
                            'renting': house_list, 'tag': meta})
    else:
        page = request.GET.get('page')
        search = request.GET.get('search')
        # if page number is not exist, set 1
        if page is None:
            page = 1

        if search is not None:
            # get data from database
            renting = Renting().get_searched_renting(search)

            house_list = []
            for r in renting:
                map = {
                    'house': r,
                    'images': r.get_images()
                }
                house_list.append(map)
            return render(request, 'renting/home.html', 
                        context={'type': type, 'feature': feature, 
                                'renting': house_list, 'tag': meta})

        # get data from database
        renting = Renting().get_paginated_renting(int(page))
        rent_count = Renting().get_count_renting()
        count = rent_count // 6
        if rent_count % 6 != 0:
            count += 1 
        
        house_list = []
        for r in renting:
            map = {
                'house': r,
                'images': r.get_images()
            }
            house_list.append(map)
        return render(request, 'renting/home.html', 
                    context={'type': type, 'feature': feature, 
                            'renting': house_list, 'count': range(count), 
                            'page': int(page)})
    

@login_required(login_url='/account/login')
def createApartView(request):
    '''
    Create apart view class
    '''
    rent_type = Type.objects.all()
    rent_feature = Feature.objects.all()
    if request.method == 'POST':
        # formdan gelen verilerin alınması,
        title = request.POST.get('title')
        city = request.POST.get('city')
        state = request.POST.get('state')
        address = request.POST.get('address')
        description = request.POST.get('description')
        feature = request.POST.get('feature')
        type = request.POST.get('type')
        price = request.POST.get('price')
        phone = request.POST.get('phone')
        square_meter = request.POST.get('square_meter')
        files = request.FILES.getlist('picture__input')

        count = 0
        images = []
        for f in files:
            if f != '':
                images.append(f)

        # control every field is none or not
        if title == '' or city == '' or state == '' or address == '' or description == '' or feature == '' or type == '' or price == '' or phone == '' or square_meter == '' or len(images) < 3:
            msg = []
            if len(images) < 3:
                msg.append({
                    "message": "Lütfen en az üç resim yükleyiniz",
                    "tags": "danger"
                })
            else :
                msg.append({
                    "message": "Lütfen tüm alanları doldurunuz",
                    "tags": "danger"
                })
            return render(request, 'renting/create.html', {'type': rent_type, 'feature': rent_feature, 'messages': msg})
            
        # create apart
        apart = Renting().create_renting(title=title, description=description, price=price, type_id=type, feautes=feature, city=city, state=state, full_address=address,phone=phone, square_meter=square_meter, owner=request.user, images=images)
        # create apart
        # apart = Renting().create_renting(title, description, price, type, feature, image)
        return redirect('renting:home')
    else:
        return render(request, 'renting/create.html', {'type': rent_type, 'feature': rent_feature})
    

@login_required(login_url='/account/login')
def editApartView(request, pk):
    '''
    Create apart view class
    '''
    apart = Renting.objects.get(uuid=pk)
    check = is_owner(request.user, apart.owner)
    if check == False:
        return redirect('renting:notfound')

    rent_type = Type.objects.all()
    rent_feature = Feature.objects.all()
    if request.method == 'POST':
        # formdan gelen verilerin alınması,
        title = request.POST.get('title')
        city = request.POST.get('city')
        state = request.POST.get('state')
        address = request.POST.get('address')
        description = request.POST.get('description')
        feature = request.POST.get('feature')
        type = request.POST.get('type')
        price = request.POST.get('price')
        phone = request.POST.get('phone')
        square_meter = request.POST.get('square_meter')
        files = request.FILES.getlist('picture__input')

        
        images = []
        apart = Renting.objects.get(uuid=pk)
        images_data = apart.get_images()
        # merge images_data and images
        for img in images_data:
            # conver image to InMemoryUploadedFile
            img = img.image
            images.append(img)

        for f in files:
            if f != '':
                images.append(f)

        new_images = []
        for img in files:
            if img != '':
                new_images.append(img)


        # control every field is none or not
        if title == '' or city == '' or state == '' or address == '' or description == '' or feature == '' or type == '' or price == '' or phone == '' or square_meter == '' or len(images) < 3:
            msg = []
            if len(images) < 3:
                msg.append({
                    "message": "Lütfen en az üç resim yükleyiniz",
                    "tags": "danger"
                })
            else :
                msg.append({
                    "message": "Lütfen tüm alanları doldurunuz",
                    "tags": "danger"
                })
            return render(request, 'renting/edit.html', {'type': rent_type, 'feature': rent_feature, 'messages': msg, 'apart': apart, 'img': images})
            

        # create apart
        Renting().update_renting(
            title=title, 
            description=description, 
            price=price, type_id=type, 
            feautes=feature, city=city, 
            state=state, full_address=address,
            phone=phone, square_meter=square_meter, 
            owner=request.user, images=new_images, pk=pk)
        
        images_data = apart.get_images()
        return redirect("renting:edit", apart.uuid)
        #return render(request, 'renting/edit.html', {'type': rent_type, 'feature': rent_feature, 'apart': apart, 'img': images_data})
    else:
        images = apart.get_images()
        return render(request, 'renting/edit.html', {'type': rent_type, 'feature': rent_feature, 'apart': apart, 'img': images})
    

@login_required(login_url='/account/login')
def deleteImage(request, pk):
    apart = Renting.objects.get(uuid=pk)
    check = is_owner(request.user, apart.owner)
    if check == False:
        return redirect('renting:notfound')
    
    image = Image.objects.get(id=pk)
    renting = Renting.objects.get(id=image.renting_id)
    image.delete()
    return redirect('/edit/' + str(renting.uuid) + '/' + '#title-img')


@login_required(login_url='/account/login')
def panelView(request):
    '''
    Panel view class
    '''
    check = check_user(request.user)
    if check == False:
        return redirect('renting:notfound')
    renting = Renting.objects.filter(is_approve=False)
    return render(request, 'renting/panel.html', context={"renting": renting})

@login_required(login_url='/account/login')
def approveView(request, pk):
    '''
    Panel view class
    '''
    check = check_user(request.user)
    if check == False:
        return redirect('renting:notfound')
    renting = Renting.objects.get(uuid=pk)
    renting.is_approve = True
    renting.save()
    return redirect('renting:panel')

@login_required(login_url='/account/login')
def rejectView(request, pk):
    '''
    Panel view class
    '''
    check = check_user(request.user)
    if check == False:
        return redirect('renting:notfound')
    renting = Renting.objects.get(uuid=pk)
    renting.is_approve = False
    return redirect('renting:panel')

@login_required(login_url='/account/login')
def user_profile(request):
    '''
    requested user profile view
    '''
    username = request.user.username
    if request.method == 'POST':
        # formdan gelen verilerin alınması,
        new_username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        # control every field is none or not
        if first_name == '' or last_name == '' or new_username == '' or email == '':
            msg = []
            msg.append({
                "message": "Lütfen tüm alanları doldurunuz",
                "tags": "danger"
            })
            return render(request, 'renting/profile.html', context={'messages': msg})
            
        # update user
        User.objects.filter(username=username).update(username=new_username, first_name=first_name, last_name=last_name, email=email)
        return redirect('renting:profile', username=new_username)
    else:
        user = User.objects.get(username=username)
        renting = Renting.objects.filter(owner=user)
        favorite = Favorite.objects.filter(user=user)
        return render(request, 'renting/profile.html', context={'renting': renting, 'user': user})
    

@login_required(login_url='/account/login')
def profile(request, username):
    '''
    user profile view
    '''
    if request.method == 'POST':
        # formdan gelen verilerin alınması,
        new_username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        # control every field is none or not
        if first_name == '' or last_name == '' or new_username == '' or email == '':
            msg = []
            msg.append({
                "message": "Lütfen tüm alanları doldurunuz",
                "tags": "danger"
            })
            return render(request, 'renting/profile.html', context={'messages': msg})
            
        # update user
        User.objects.filter(username=username).update(username=new_username, first_name=first_name, last_name=last_name, email=email)
        return redirect('renting:profile', username=new_username)
    else:
        try:
            user = User.objects.get(username=username)
            renting = Renting.objects.filter(owner=user)
            favorite = Favorite.objects.filter(user=user)
            return render(request, 'renting/profile.html', context={'renting': renting, 'user': user})
        except User.DoesNotExist:
            return redirect('renting:notfound')


@login_required(login_url='/account/login')
def favorite(request):
    '''
    favorite view
    '''
    user = request.user
    favorite = Favorite.objects.filter(user=user)
    house_list = []
    for f in favorite:
        map = {
            'house': f.renting,
            'images': f.renting.get_images()
        }
        house_list.append(map)

    return render(request, 'renting/favorite.html', context={'renting': house_list})

@login_required(login_url='/account/login')
def addFavorite(request, pk):
    '''
    add favorite view
    '''
    user = request.user
    renting = Renting.objects.get(uuid=pk)
    Favorite().create_favorite(user, renting)
    return redirect('renting:home')

@login_required(login_url='/account/login')
def removeFavorite(request, pk):
    '''
    remove favorite view
    '''
    user = request.user
    renting = Renting.objects.get(uuid=pk)
    Favorite().delete_favorite(user, renting)
    return redirect('renting:favorite')


@login_required(login_url='/account/login')
def ilanlarim(request):
    '''
    ilanlarim view
    '''
    user = request.user
    renting = Renting.objects.filter(owner=user)

    house_list = []
    for r in renting:
        map = {
            'house': r,
            'images': r.get_images()
        }
        house_list.append(map)
    
    return render(request, 'renting/ilanlarim.html', context={'renting': house_list})

@login_required(login_url='/account/login')
def deleteRenting(request, pk):
    '''
    delete renting view
    '''
    renting = Renting().delete_renting(pk, request.user.id)
    if (renting == False):
        return redirect('renting:home')
    return redirect('renting:ilanlarim')


@login_required(login_url='/account/login')
def metaView(request):
    '''
    meta view
    '''
    check = check_user(request.user)
    if check == False:
        return redirect('renting:notfound')
    
    if request.method == "POST":
        # formdan gelen verilerin alınması,
        author = request.POST.get('author')
        description = request.POST.get('description')
        keywords = request.POST.get('keywords')

        # control every field is none or not
        if author == '' or description == '' or keywords == '':
            msg = []
            msg.append({
                "message": "Lütfen tüm alanları doldurunuz",
                "tags": "danger"
            })
            return render(request, 'renting/meta.html', context={'messages': msg, 'meta': Tag.objects.get(id=1)})
            
        # update meta
        tag = Tag.objects.filter(id=1)
        tag.update(author=author, meta_description=description, meta_keywords=keywords)
        return redirect('renting:meta')
    else:
        meta = Tag.objects.get(id=1)
        return render(request, 'renting/meta.html', context={'meta': meta})
    

def contactView(request):
    '''
    contact view
    '''
    if request.method == "POST":

        # formdan gelen verilerin alınması,
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        subject = request.POST.get('subject')

        # control every field is none or not
        if email == '' or phone == '' or message == '' or subject == '' or name == '':
            msg = []
            msg.append({
                "message": "Lütfen tüm alanları doldurunuz",
                "tags": "danger"
            })
            return render(request, 'renting/contact.html', context={'messages': msg})
        
        MailHandler.contact_send_mail(name, email, phone, subject, message)
        msg = []
        msg.append({
            "message": "Mesajınız başarıyla gönderildi, en kısa sürede size dönüş yapılacaktır.",
            "tags": "success"
        })
        return render(request, 'renting/contact.html', context={'messages': msg})
    else:
        return render(request, 'renting/contact.html')
    

def not_found(request):
    return render(request, 'renting/404.html')

def about(request):
    return render(request, 'renting/about.html')