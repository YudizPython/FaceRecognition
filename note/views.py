#AyazSaiyed
#yudiz - 2019
 # https://res.cloudinary.com/darkworldfacerecognition/image/upload/sample.jpg
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,JsonResponse


from django.shortcuts import render
from django.conf.urls.static import static
# Create your views here.
from django.http import HttpResponse

from django.core.files.storage import FileSystemStorage
import os
from django.http import HttpRequest
# from .models import users
# import urllib.requestsuest
# import request
# import requests
import time
from .models import UserImages
from rest_framework import serializers
from models import users,UserImages
from rest_framework import viewsets
import requests
from django.views.decorators.csrf import csrf_exempt
from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os

def home(request):
	return render(request,'AndroidFaceRecognitionApp/home.html')

def login(request):
	return render(request,'AndroidFaceRecognitionApp/login.html')

def loginvalidation(request):
	a = request.GET.get('username')
	# f = http://192.168.11.107:8080/api/users/?username=a
	# cc = requests.get('http://192.168.11.107:8080/api/users/username=?')
	# print("fc",cc)
	b = request.GET.get('password')
	# all = users.objects.filter(username=a)
	all = "ayaz"
	if a == all:
		ab = str(a)
		request.session['userid'] = ab
		print("login successful as ",ab)
		c = request.session.get('userid')
		print("***",c)
		return render(request,'AndroidFaceRecognitionApp/home.html')
	return render(request,'AndroidFaceRecognitionApp/login.html')

@csrf_exempt
def uploadimg(request):
	# response = requests.get("http://192.168.11.107:8080/api/usersimages/")
	# print(response.status_code)
	# request.session['userid'] = "ayazsaiyedahmed"
	img = request.FILES['userimg']
	imgname = str(img)
	# uid = 
	fs = FileSystemStorage()
	# a = request.session.get('last_visit')
	# user_id = "ayazsaiyed"
	# img_extension = os.path.splitext(img.name)[1]
	# user_folder = 'media/' + str(request.session['userid'])
	# # print(str(user_folder))
	# if not os.path.exists(user_folder):
	# 	os.mkdir(user_folder)

	# time.sleep(0.5)
	# img_save_path = (user_folder + img_extension)
	# with open(img_save_path, 'wb+') as f:
	# 	for chunk in img.chunks():
	# 		f.write(chunk)
	# # UserImages.objects.create(img=uploaded_file_url)
	# return HttpResponse("Uploaded")
	username = request.POST.get('username')

	# request.session['user'] = username

	# print("user",username)
	user_folder = username
	# dirpath = 'https://res.cloudinary.com/darkworldfacerecognition/image/upload/v1575031935/'+user_folder
	dirpath = '/Users/yudiz/Desktop/python-face-recognition/dataset/'+user_folder
	

	# print(user_folder)
	if not os.path.exists(dirpath):
		os.mkdir(dirpath)
		# os.move()
	time.sleep(0.10)
	# fs = FileSystemStorage()
	filename = fs.save(username+'.jpg',img)
	uploaded_file_url = fs.url(filename)
	UserImages.objects.create(img=uploaded_file_url)
	# moveimage(request)
	search_path = '/Users/yudiz/Desktop/python-face-recognition/dataset/'
	print(search_path)
	# username = request.POST.get('username')
	# username = request.session['userid']
	print("Session name !!!!!! ",username)
	for fname in os.listdir(search_path):
		if fname == username:
			print("Named Folder Found")
			os.rename("/Users/yudiz/Desktop/python-face-recognition/"+username+".jpg", '/Users/yudiz/Desktop/python-face-recognition/dataset/'+username+'/'+imgname)
		else:
			print("Not Found")
	# return render(request,'AndroidFaceRecognitionApp/train.html')
	# return JsonResponse("Image Uploaded",safe=False)
	return JsonResponse({'Status':'Image Uploaded'})

@csrf_exempt
def training(request):
	user = request.POST.get('username')
	# user = "Pratesek"
	# print("111",user)

	# tempusername = "ChiragSir"
	print("[INFO] quantifying faces...")
	imagePaths = list(paths.list_images('/Users/yudiz/Desktop/python-face-recognition/'+user))
	for i in imagePaths:
		# print(imagePaths)
		 
		# initialize the list of known encodings and known names
		knownEncodings = []
		knownNames = []
		# username = request.POST.get('username')
		print("Training of ",user)
		for (i, imagePath) in enumerate(imagePaths):
			print("i",i)
			# extract the person name from the image path
			print("[INFO] processing image {}/{}".format(i + 1,
				len(imagePaths)))
			name = imagePath.split(os.path.sep)[-2]
		 
			# load the input image and convert it from BGR (OpenCV ordering)
			# to dlib ordering (RGB)
			image = cv2.imread(imagePath)
			rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

				# detect the (x, y)-coordinates of the bounding boxes
			# corresponding to each face in the input image
			boxes = face_recognition.face_locations(rgb,
				model='hog')
		 
			# compute the facial embedding for the face
			encodings = face_recognition.face_encodings(rgb, boxes)
		 
			# loop over the encodings
			for encoding in encodings:
				# add each encoding + name to our set of known names and
				# encodings
				knownEncodings.append(encoding)
				knownNames.append(name)


		# dump the facial encodings + names to disk
		print("Serializing encodings...")
		data = {"encodings": knownEncodings, "names": knownNames}
		f = open("/Users/yudiz/Desktop/python-face-recognition/encodings/"+user+".pickle", "wb")
		f.write(pickle.dumps(data))
		f.close()

		time.sleep(0.5)
		# return render(request,'AndroidFaceRecognitionApp/facerecognize.html')
		return JsonResponse({'Status':'Training has been Successfully Completed'})
	return HttpResponse("Sorry no user found with this name")

	# process = Subprocess.Popen(['python','encode_faces.py','-e -encodings.pickle','-i dataset'], stdout=PIPE, stderr=STDOUT)
	# output = process.stdout.read()
	# exitstatus = process.poll()
	# a = appscript.app('Terminal')
	# a.do_script('python encode_faces.py')
	# return HttpResponse("Training Started")
@csrf_exempt
def moveimage(request):
	search_path = '/Users/yudiz/Desktop/python-face-recognition/'
	print(search_path)
	username = request.session.get('userid')
	# username = request.session['userid']
	print("Session name !!!!!! ",username)
	for fname in os.listdir(search_path):
		if fname == username:
			print("Named Folder Found")
			os.rename("/Users/yudiz/Desktop/python-face-recognition/"+username+".jpg", '/Users/yudiz/Desktop/python-face-recognition/'+username+'/a.jpg')
		else:
			print("Not Found")


	# return HttpResponse("moveimage")
@csrf_exempt
def RecognizingImage(request):
	request.session['output'] = "Not Recognized"
	
	i = request.FILES['checkimage']
	fs = FileSystemStorage()
	fs.save('check.jpg',i)
	# os.rename('/Users/yudiz/Downloads/python-rest-api-djago-rest-framework/media/check.jpg', '/Users/yudiz/Downloads/python-rest-api-djago-rest-framework/check.jpg')
	recognize_faces(request)
	recognizedname = request.session.get('output')
	aaa = recognizedname
	id = 1
	# return HttpResponse("<html><h1>Face Recognized <b> "+ aaa+"</b></h1></html>")
	# return JsonResponse({'Status':id, 'Username':aaa})
	# loginuser = request.session.get('user')
	# print("login user",loginuser)
	myuserid = request.POST.get('usernametomatch')
	print("recognizedname",aaa)
	if recognizedname == myuserid:
		return JsonResponse({'Status':id, 'Username':aaa})
	else:
		return JsonResponse({'Status': ' No Match Found With this UserId'})






# @csrf_exempt
def recognize_faces(request):
	request.session['output'] = "No Match Found"

	user = request.POST.get('usernametomatch')
	print("user name to check ",user)
	request.session['output'] = "No Match Found"
	import face_recognition
	import argparse
	import pickle
	import cv2
	if os.path.exists('/Users/yudiz/Desktop/python-face-recognition/encodings/'+user+'.pickle'):
	# x = pickle.loads('/Users/yudiz/Desktop/python-face-recognition/encodings/'+user+'.pickle')

		data = pickle.loads(open('/Users/yudiz/Desktop/python-face-recognition/encodings/'+user+'.pickle', "rb").read())
		c = '/Users/yudiz/Desktop/python-face-recognition/encodings/'+user+'.pickle'
		print("[INFO] loading encodings...",c)

		# print(str(data))
		# convert it from BGR to RGB
		image = cv2.imread('check.jpg')
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		# detect the (x, y)-coordinates of the bounding boxes corresponding
		# to each face in the input image, then compute the facial embeddings
		# for each face
		print("Ready to Recognize faces...")
		boxes = face_recognition.face_locations(rgb,
			model='hog')
		encodings = face_recognition.face_encodings(rgb, boxes)

		# initialize the list of names for each face detected
		names = []

		# loop over the facial embeddings
		for encoding in encodings:
			# attempt to match each face in the input image to our known
			# encodings
			matches = face_recognition.compare_faces(data["encodings"],
				encoding)
			name = "Unknown"
			print(matches)
			perfectmatch = 0
			for i in matches:
				# print(i)
				a = i
				if a == True:
					print("Matched")
					perfectmatch += 1
				else:
					print("Better luck next time")
			print(perfectmatch)

			# check to see if we have found a match
			if True in matches:

				# find the indexes of all matched faces then initialize a
				# dictionary to count the total number of times each face
				# was matched
				matchedIdxs = [i for (i, b) in enumerate(matches) if b]
				counts = {}
				# print("matches",matchedIdxs)
				# loop over the matched indexes and maintain a count for
				# each recognized face face
				for i in matchedIdxs:
					name = data["names"][i]
					counts[name] = counts.get(name, 0) + 1

				# for j in str(counts[name]):
				# 	print("Number of Counts",j)
				# determine the recognized face with the largest number of
				# votes (note: in the event of an unlikely tie Python will
				# select first entry in the dictionary)
				name = max(counts, key=counts.get)

				# print(name)
				# names.append(name)
				
			# update the list of names
			# names.append(name)
			# for j in str(counts[name]):
			# 	print("Number of Counts",j)

				a = str(matchedIdxs)

				# for x in a:
				# 	print(len(x))
				# print("Number of Matches",a)
				# if perfectmatch >= 3:
			if perfectmatch >=5:
				names.append(name)
			else:
				print("Better luck next time")

			# print(names)
			# else:
			# 	print("Unknow Person")

		# loop over the recognized faces
		for ((top, right, bottom, left), name) in zip(boxes, names):
			# draw the predicted face name on the image
			cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
			y = top - 15 if top - 15 > 15 else top + 15
			print("The Person in the image is ", name)
			cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
				0.75, (0, 255, 0), 2)
			request.session['output'] = name
		# time.sleep(0.1)
		os.remove('check.jpg')
	else:
		# return JsonResponse("Sorry Pickle File doesn't exisit")
		return JsonResponse({'Status':'Sorry Pickle File doesnt exisit'})

	# show the output image
	# cv2.imshow("Image", image)
	# cv2.waitKey(0)

@csrf_exempt
def directrecognize(request):
	return render(request,'AndroidFaceRecognitionApp/facerecognize.html')


# class UserSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:

#         model = users
#         fields = '__all__'



# class UserViewSet(viewsets.ModelViewSet):
	
	
# 	queryset = users.objects.all()
# 	serializer_class = UserSerializer

# # def get_queryset(self):
# #     longitude = self.request.query_params.get('username')
# #     # latitude= self.request.query_params.get('latitude')
# #     # radius = self.request.query_params.get('radius')

# #     # location = Point(longitude, latitude)

# #     queryset = users.objects.filter(username=longitude)

# #     return queryset


# class UserImageSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = UserImages
# 		fields = '__all__'


# class UserImageViewSet(viewsets.ModelViewSet):

#     queryset = UserImages.objects.all()
#     # print("query set is ",qu)
#     serializer_class = UserImageSerializer


def temp(request):
    response = requests.get('http://192.168.11.107:8080/uploadimg')
    geodata = response.json()
    return render(request, 'core/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })


#HOG is faster and accurate 
#CNN is more accurate
