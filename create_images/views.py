from django.shortcuts import render
from create_images.forms import Upload_image_form
from create_images.models import Images
from django.views.generic import View
from PIL import Image, ImageFilter
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your views here.

class index(View):
	def get(self,request):
		return render(request,"create_images/home.html",{'form':Upload_image_form})
	
	def post(self,request):
		user_form = Upload_image_form(request.POST,request.FILES)
		if user_form.is_valid() :
			new_image=user_form.save()	
			
			im = Image.open( new_image.Image )
			f_image=None
			if new_image.Filter=='BLUR':
				f_image=im.filter( ImageFilter.BLUR )
			elif new_image.Filter=='CONTOUR':
				f_image=im.filter( ImageFilter.CONTOUR )
			elif new_image.Filter == 'DETAIL':
				f_image=im.filter( ImageFilter.DETAIL )
			else :
				f_image=im.filter( ImageFilter.EDGE_ENHANCE )
			
			thumb_io = StringIO.StringIO()

			f_image.save(thumb_io, format='JPEG')

			thumb_file = InMemoryUploadedFile(thumb_io, None, 'foooo.jpg', 'image/jpeg',thumb_io.len, None)

			isit=Images.objects.create(Image=thumb_file,Filter='Filterd')

			return render(request,"create_images/home.html",{'form':Upload_image_form,'image':isit,'uploaded_image':new_image})
		else :
			return render(request,"create_images/home.html",{'form':Upload_image_form,"message":user_form.errors})



