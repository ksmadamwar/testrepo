1. Install Python 3 https://www.python.org/downloads/ version used for deveopment 3.10.4
2. Install Django https://docs.djangoproject.com/en/4.0/topics/install/
3. Go to the cloned git folder and run command - "pip install -m requirements.txt"
4. Install node https://nodejs.org/en/download/
5. Go to Biosensorproject/biosensorapp/templates, run "npm install"
6. Get firebase account service file using this link, https://clemfournier.medium.com/how-to-get-my-firebase-service-account-key-file-f0ec97a21620
	a. Select python from the options and download the file
	b. Save the downloaded file in "biosensorproject/biosensorproject" folder where settings.py
		is present and name it as "services.json"
	c. Add the environment path for the firebase admin setup, follow this document to update the
		same referring this link - https://firebase.google.com/docs/admin/setup#windows
		for windows just run below command from the shell 
		$env:GOOGLE_APPLICATION_CREDENTIALS=<PATH TO SERVICES JSON FILE>(the one downloaded from step above)
6. go to "biosensorproject/biosensorapp/templates/src/constants/AppConstants.js" file and update the "API_URL" as your local machine ip(to run locally)
7. open terminal and go to the folder where the codebase is cloned, open "biosensorproject" folder, you
should see "manage.py" run the command as "python manage.py runserver yourapp:8000"
8. go to the browser and open the above URL, you should see the app running
9. Whenever any changes are made to the frontend/react js side, just run the below command to update those changes on server side. 
	a. go to "biosensorproject/biosensorapp/templates
	b. run "npm run-script build"