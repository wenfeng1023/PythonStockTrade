from audioop import reverse
from threading import local
from django.shortcuts import render
from .forms import FileForm
from django.http.response import FileResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
import os
from django.utils.http import urlquote
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from astock.stock_bt.neo_run import run_bt
from pandas_datareader._utils import RemoteDataError




# Create your views here.
@csrf_exempt
def get_stock_name(request):
    if request.method=='POST':
        name = request.POST['fname']
    return name
    
@csrf_exempt
def index(request):
    """
    upload File
    :param request:
    :return:
    """
    if request.method == 'POST':
        name = request.POST['fname']
        start = request.POST['start']
        end = request.POST['end']
        strategy = request.POST['strategy']
        period = request.POST['period']
        period1 = request.POST['period1']
        period2 = request.POST['period2']
        selection = request.POST['flexRadioDefault']

        html = "<html><body><center><p> Please input correct Code of Stock</p> </center></body></html>"

        try:
            run_bt(name,strategy,period,period1,period2, selection,start,end)
        except RemoteDataError:        
            return HttpResponse(html)
        except IndexError:
            return HttpResponse('\n Please input correct Start time and End time')
              
        return render(request,'test.html',locals())
    else:
        return render(request, 'index.html', locals())
        
    #     form = FileForm(request.POST['fname'])
    #     if form.is_valid():
    #         #Get Files
    #         files = request.FILES.getlist('file')
    #         file_name = files[0].name.split('.')
            
    #         # request.session['file_name'] = file_name
            

    #         # save the file in database or local server
    #         for file in files:
    #             # save in database through the model
    #             #  file_model = FileModel(name=file.name,
    #             #                         path=os.path.join(
    #             #                             './upload', file.name))
    #             #  file_model.save()

    #             # Save the file in local server
    #             destination = open(os.path.join("./upload", file.name), 'wb+')
    #             for chunk in file.chunks():
    #                 destination.write(chunk)
    #             destination.close()

    #         #Using the Onnx_Connx Molde to get Connx File
    #         if not os.path.exists("./out"):
    #             path = "python -m onnx_connx "+ "./upload/"+file_name[0] +".onnx "
    #             subprocess.run(path, shell=True, check= True,capture_output=True,text=True)

    #             # Compressed Files 
    #             shutil.make_archive("out",'zip', "out")
    #         else:
    #             shutil.rmtree("./out")
    #             path = "python -m onnx_connx "+ "./upload/"+file_name[0] +".onnx"
    #             subprocess.run(path, shell=True, check= True,capture_output=True,text=True)

    #             # Compressed Files 
    #             shutil.make_archive("out",'zip', "out")         

    #         return redirect('download')
    # else:
    #     form = FileForm()
    #     return render(request, 'index.html', locals())

"""
Download the Connx Model
"""
def download_view(request):
    #file_name = request.session['file_name']
    name = "out.zip"  #file.name
    path = "./out.zip"  #file.path
    File_exists = os.path.exists(path)

    if File_exists == True:

        # Read the File
        file = open(path, 'rb')

        response = FileResponse(file)

        # Coding the File's name in  urlquote
        response[
            'Content-Disposition'] = 'attachment;filename="%s"' % urlquote(
                name)
        # Session.objects.all().delete()

        return response

    else:
        return HttpResponse('No Files')

