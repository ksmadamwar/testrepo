from django.db import models

# Create your models here.


#This table woud be used to store all user related information

class UserInformation(models.Model):
	class Meta:
		db_table = 'user_information'
	user_id = models.AutoField(primary_key=True)
	gender  = models.CharField(max_length=200)
	pesticide_applied_last_x_days = models.CharField(max_length=200)
	pesticide_brand = models.CharField(max_length=200)
	crops  = models.CharField(max_length=200)
	location  = models.CharField(max_length=200)
	age  = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	created_by = models.CharField(max_length=200)
	updated_by = models.CharField(max_length=200)



#This table woud be used to store data after proessing values from the device
class SensorData(models.Model):
	class Meta:
		db_table = 'sensor_data'
	sensor_id = models.AutoField(primary_key=True)
	user_id = models.IntegerField()
	biosensor_name = models.CharField(max_length=200, default = None,null = True)
	cholinesterase_name = models.CharField(max_length=200, default = None,null = True)
	test_time = models.DateTimeField()
	activity = models.FloatField()
	inhibition  = models.CharField(max_length=200,null = True,default = None, blank = True)
	baseline = models.FloatField()
	comments = models.TextField()	
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	created_by = models.CharField(max_length=200)
	updated_by = models.CharField(max_length=200)


	

