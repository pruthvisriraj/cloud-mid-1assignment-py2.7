# cloud-mid-1assignment-py2.7
It need python2.7 to run
first we need upload our code.py, app.yaml and requments.txt in git
Next we need to go to google cloud sdk shell
which is confirged eailer.
in that we have to follow these stepts


$gcloud projects create mid1-assig --set-as-default 
--->to create the project 

$gcloud app create --project=mid1-assig
--->to create the app in the project

now we have to link the project to billing account 

$ git clone https://github.com/pruthvisriraj/cloud-mid-1assignment-py2.7.git

to clone the gepositry in the g-cloud. The repostory conotains 3files: 1) code.py(in python2.7) 2) app.yaml and 3) requments
  
$ gcloud app deploy 

---> To deploy the the app

$ gcloud app browse

---> We will get the link to bowser https://mid1-assig.el.r.appspot.com/
