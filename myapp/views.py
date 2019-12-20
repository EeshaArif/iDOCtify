from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Patient
from .forms import PatientHistory
from django.db.models import Q
import face_recognition
import cv2
import numpy as np
# Create your views here.

def home(request):
    return render(request,"home.html")

def profile(request):
    return render(request,"profile.html")

@login_required
def patienthistory(request):
    form = PatientHistory(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return render(request, 'profile.html')

    context = {'form': form}
    return render(request, 'newpatienthistory.html', context )

@login_required
def delete_patienthistory(request, patient_id):
    item_to_delete = Patient.objects.filter(pk = patient_id)
    if item_to_delete.exists():
        if request.user == item_to_delete[0].user:
            item_to_delete[0].delete()
    return redirect('/accounts/profile/display')

@login_required
def update_patienthistory(request, patient_id):
    unique_history = get_object_or_404(Patient, pk = patient_id)
    form = PatientHistory(request.POST or None, request.FILES or None, instance = unique_history)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return render(request, "profile.html")

    context = {'form': form}
    return render(request, 'newpatienthistory.html', context )

@login_required

def search(request):
    if request.method == 'POST':
        srch = request.POST['srch']
        if srch:
            match_patient = Patient.objects.filter(Q(first_name__icontains = srch)| Q(last_name__icontains = srch))
            for x in match_patient:
                list = [x.symptom1,x.symptom2,x.symptom3,x.symptom4,x.symptom5]
                list.sort(key=lambda x: x or 0)
                x.symptom1 = list[0]
                x.symptom2 = list[1]
                x.symptom3 = list[2]
                x.symptom4 = list[3]
                x.symptom5 = list[4]
                x.save()
            if match_patient:
                return render(request,"display.html",{'srch': match_patient})
            else:
                message = "No records Found"
                return render(request, "display.html", {'message': message})
        else:
            return render(request, 'profile.html')
    return render(request, 'profile.html')

def detect(request):
        context =  { 'patients': Patient.objects.all() }
        Patients=Patient.objects.all()
        #eesha_image=face_recognition.load_image_file(Eesha.image)
        video_capture = cv2.VideoCapture(0)

        # Load a sample picture and learn how to recognize it.
        """
        obama_image = face_recognition.load_image_file("obama.jpg")
        obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    
        # Load a second sample picture and learn how to recognize it.
        biden_image = face_recognition.load_image_file("biden.jpg")
        biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
        ayyan_image=face_recognition.load_image_file("ayyan.jpg")
        ayyan_face_encoding = face_recognition.face_encodings(ayyan_image)[0]
        eesha_image=face_recognition.load_image_file("eesha.jpg")"""
       # eesha_face_encoding = face_recognition.face_encodings(eesha_image)[0]
      #  arif_image=face_recognition.load_image_file("arif.jpg")
       # arif_face_encoding = face_recognition.face_encodings(arif_image)[0]


        # Create arrays of known face encodings and their names
        known_face_encodings = [
           # obama_face_encoding,
           # biden_face_encoding,
           # ayyan_face_encoding,
           # eesha_face_encoding
           # arif_face_encoding

            ]
        known_face_names = [
           # "Barack Obama",
          #  "Joe Biden",
            #"Ayyan Arif",
           # "Eesha Arif"
         #   "Arif Saleem"
        ]
        for patient in Patients:
            known_face_encodings.append(face_recognition.face_encodings(face_recognition.load_image_file(patient.image))[0])
            known_face_names.append(patient.first_name + patient.last_name)
            # Initialize some variables
       # known_face_encodings=[]
        #known_face_names=[]
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        while True:
            # Grab a single frame of video
            ret, frame = video_capture.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"

                    # # If a match was found in known_face_encodings, just use the first one.
                    # if True in matches:
                    #     first_match_index = matches.index(True)
                    #     name = known_face_names[first_match_index]

                    # Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]

                    face_names.append(name)

            process_this_frame = not process_this_frame


            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting image
            cv2.imshow('Video', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()
        return redirect('/')

