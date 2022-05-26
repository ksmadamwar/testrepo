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
	extra1  = models.IntegerField(null = True, default = None, blank = True)
	extra2  = models.IntegerField(null = True, default = None, blank = True)
	extra3  = models.CharField(max_length=200,null = True,default = None, blank = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	created_by = models.CharField(max_length=200)
	updated_by = models.CharField(max_length=200)



#This table woud be used to store cholinesterase type AChE/BChE related information
class CholinesteraseType(models.Model):
	class Meta:
		db_table = 'cholinesterase_type'
	cholinesterase_id = models.AutoField(primary_key=True)
	cholinesterase_name  = models.CharField(max_length=200)
	extra2  = models.IntegerField(null = True, default = None, blank = True)
	extra3  = models.CharField(max_length=200,null = True,default = None, blank = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	created_by = models.CharField(max_length=200)
	updated_by = models.CharField(max_length=200)


#This table woud be used to store biosensor test types
class BiosensorTestType(models.Model):
	class Meta:
		db_table = 'biosensor_test_type'
	biosensor_id = models.AutoField(primary_key=True)
	biosensor_test_name  = models.CharField(max_length=200)
	details  = models.CharField(max_length=200,null = True,default = None, blank = True)
	attributes_required = models.TextField()
	extra2  = models.IntegerField(null = True, default = None, blank = True)
	extra3  = models.CharField(max_length=200,null = True,default = None, blank = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	created_by = models.CharField(max_length=200)
	updated_by = models.CharField(max_length=200)

#This table woud be used to store data after proessing values from the device
class SensorData(models.Model):
	class Meta:
		db_table = 'sensor_data'
	sensor_id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(UserInformation, on_delete = models.CASCADE)
	biosensor_id = models.ForeignKey(BiosensorTestType, on_delete = models.CASCADE)
	cholinesterase_id = models.ForeignKey(CholinesteraseType,on_delete = models.CASCADE)
	test_time = models.DateTimeField()
	activity = models.FloatField()
	inhibition  = models.CharField(max_length=200,null = True,default = None, blank = True)
	baseline = models.FloatField()
	comments = models.TextField()	
	extra2  = models.IntegerField(null = True, default = None, blank = True)
	extra3  = models.CharField(max_length=200,null = True,default = None, blank = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	created_by = models.CharField(max_length=200)
	updated_by = models.CharField(max_length=200)

