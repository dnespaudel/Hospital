**Hospital Project using Django Rest Framework**

py manage.py makemigrations

py manage.py migrate

py manage.py createsuperuser (must for AdminUser and Admin role assignment)

py manage.py runserver

Register Using Email/Phone

**"USE POSTMAN"**

*api/v1/register/ -> ['POST'] request ->*

Otp is randomly generated and sent to your email for verification (using pyotp and bas32 verification)

role is automatically set to "P" i.e PATIENT after registration

*api/v1/register/all/ ->['GET'] request -> lists all users [only id's]*

*api/v1/register/pk/ -> ['PUT'] request Update ,Delete User's Info*

**OTP Verification**

*api/v1/verify/<int:otp>/ -> ['POST'] request -> sets is\_verified flag as True.*

**You are verified now!**

**NOTE: OTP is set to expire after 3 minutes (180 seconds). Once expired, you won’t be able to verify using that otp as "otp is expired" is shown. So, one would have to resend otp in their email for verification.**

**OTP Resend**

*api/v1/resend/pk/ - > ['POST'] request ->*

Resend another otp to your user, and a new mfa\_hash is generated for that otp.

Use the new obtained otp in your email for verification in the previous api.

**Assign Roles**

[Can only be done with SuperUser, Admin, and Manager Role] // login>get access token->use that bearer token in POSTMAN header and now you can assign roles to user

api/v1/roles/<pk> -> ['PUT'] request -> Assign roles to Doctor, Nurse, Receptionist, Manager.

**Note: User with patient, doctor, nurse and receptionist role can only retrieve, admin and manager can do everything CRUD functionality.**

**Login**

*api/v1/login/ - > login into the system using Patient\_Id/Password for the ‘patient’ user or Username/Password for the ‘doctor, nurse, and receptionist’ user.*

Generates simple jwt access and refresh token

**News App**

*api/v2/news-image - > ['POST'] request -> upload images for news article*

*api/v2/news-image/all - > [‘GET’] request -> list all images id*

*api/v2/news-image/<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete news image*

*api/v2/news-event- > ['POST'] request -> create new-event info*

*api/v2/news-event/all - > [‘GET’] request -> list all new-event id*

*api/v2/news-event/<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete news-event*

*api/v2/comment- > ['POST'] request -> create comment section on the news article*

*api/v2/comment/all - > [‘GET’] request -> list all comment id*

*api/v2/comment/<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete comment* 

*api/v2/reaction - > ['POST'] request -> create reaction on the news article*

*api/v2/reaction/all - > [‘GET’] request -> list all reaction id*

*api/v2/reaction/<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete reaction*

` `*api/v2/share - > ['POST'] request -> create share option on the news article*

*api/v2/share/all - > [‘GET’] request -> list all share id*

*api/v2/share/<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete share*

**About Us App**

*api/v3/hospital-image - > ['POST'] request -> upload hospital images* 

*api/v3/hospital-image/all - > [‘GET’] request -> list all hospital images id*

*api/v3/hospital-image/<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete hospital image*

*api/v3/about-hospital - > ['POST'] request -> create hospital description*

*api/v3/about-hospital/all - > [‘GET’] request -> list hospital description id*

*api/v3/about-hospital/<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete hospital description*

*api/v3/record - > ['POST'] request -> create hospital record*

*api/v3/record/all - > [‘GET’] request -> list hospital record id*

*api/v3/record/<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete hospital record*

*api/v3/department-image - > ['POST'] request -> upload department images* 

*api/v3/department-image/all - > [‘GET’] request -> list all department images id*

*api/v3/department-image/<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete department images*

*api/v3/department - > ['POST'] request -> create department*

*api/v3/department /all - > [‘GET’] request -> list all department id*

*api/v3/department /<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete department*

*api/v3/doctor-image - > ['POST'] request -> upload doctor images* 

*api/v3/doctor-image/all - > [‘GET’] request -> list all doctor images id*

*api/v3/doctor-image/<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete doctor image*

*api/v3/doctor - > ['POST'] request -> create doctor* 

*api/v3/doctor /all - > [‘GET’] request -> list all doctor id*

*api/v3/doctor /<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete doctor* 

*api/v3/doctor-details - > ['POST'] request -> create doctor details*

*api/v3/doctor-details/all - > [‘GET’] request -> list all doctor details id*

*api/v3/doctor-details/<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete doctor details*

*api/v3/about-doctor - > ['POST'] request -> create doctor detail description*

*api/v3/about-doctor/all - > [‘GET’] request -> list all doctor detail description id*

*api/v3/about-doctor/<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete doctor details description*

*api/v3/doctor-listing - > ['POST'] request -> create doctor listing*

*api/v3/doctor-listing/all - > [‘GET’] request -> list all doctor listing id*

*api/v3/doctor-listing/<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete doctor listing*

**Service App**

*api/v4/services - > ['POST'] request -> create service* 

*api/v4/services/all - > [‘GET’] request -> list all service id*

*api/v4/services/<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete service*

*api/v4/hospital-services - > ['POST'] request -> create hospital service* 

*api/v4/hospital-services/all - > [‘GET’] request -> list all hospital service id*

*api/v4/hospital-services/<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete hospital service*

**Contact App**

*api/v5/contact-us - > ['POST'] request -> create hospital contact* 

*api/v5/contact-us/all - > [‘GET’] request -> list all hospital contact id*

*api/v5/contact-us/<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete hospital contact*

*api/v5/get-connected - > ['POST'] request -> create get connected info* 

*api/v5/get-connected/all - > [‘GET’] request -> list all get connected info id*

*api/v5/get-connected/<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete get connected info*

*api/v5/social-media - > ['POST'] request -> create social media info* 

*api/v5/social-media/all - > [‘GET’] request -> list all social media info id*

*api/v5/social-media/<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete social media info*

**Extra App**

*api/v6/career - > ['POST'] request -> create vacancy info* 

*api/v6/career/all - > [‘GET’] request -> list all vacancy info id*

*api/v6/career/<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete vacancy info*

*api/v6/feedback - > ['POST'] request -> create feedback info* 

*api/v6/feedback/all - > [‘GET’] request -> list all feedback info id*

*api/v6/feedback/<pk> - > [‘PUT, DELETE, RETRIEVE’] request -> retrieve, update, delete feedback info*
