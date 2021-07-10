from django.db import models

# Create your models here.
class User_Database(models.Model):
	name = models.CharField(max_length=64)
	email = models.EmailField(max_length=200)

	def __str__(self):
		return f'Name: {self.name}---- Email: {self.email}'


class Tag(models.Model):
	name = models.CharField(max_length=64, null=True)

	def __str__(self):
		return self.name



class Customer(models.Model):
	name = models.CharField(max_length=64, null=True)
	email = models.EmailField(max_length=200,null=True)
	phone = models.IntegerField()
	date_registered = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Product(models.Model):
	CATEGORY = (
		("Indoor", "Indoor"),
		('Outdoor', "Outdoor"),
		)

	name = models.CharField(max_length=64)
	price = models.FloatField()
	category = models.CharField(max_length=200 , choices=CATEGORY)
	description = models.CharField(max_length=200)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name



class Order(models.Model):
	STATUS = (
		('Pending','Pending'),
		('Out for delivery','Out for delivery'),
		('Delivered','Delivered'),
		)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200 , choices=STATUS, null=True)

	def __str__(self):
		return f'{self.product} ordered from {self.customer}'


class Passenger(models.Model):
	name = models.CharField(max_length=300)
	email = models.EmailField(max_length=200)

	def __str__(self):
		return f'Name : {self.name}, Email : {self.email}'


class Airport(models.Model):
	initial = models.CharField(max_length=3)
	place = models.CharField(max_length=300)

	def __str__(self):
		return f'{self.place} ({self.initial})'


class Flight(models.Model):
	origin = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True ,related_name='departure')
	destination = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name="arrivals") 
	duration = models.IntegerField()
	date = models.DateTimeField(auto_now_add=True, null=True)
	passengers = models.ManyToManyField(Passenger)
	def __str__(self):
		return f'Flight number {self.id}: from {self.origin} to {self.destination}.'


class Chapiteau_customer(models.Model):
	first_name = models.CharField(max_length=300, null=True)
	last_name = models.CharField(max_length=300, null=True)
	email = models.EmailField(max_length=200, null=True)
	date_created= models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

class Chapiteau_activity(models.Model):
	REFERENCES = (
		('indoor','indoor'),
		('outdoor','outdoor'),
		('chill','chill'),
		)

	name = models.CharField(max_length=200)
	type_of_activity = models.CharField(max_length=200, choices=REFERENCES)


	def __str__(self):
		return f'{self.name}'


class Chapiteau_coordinator(models.Model):
	customer_name = models.ForeignKey(Chapiteau_customer, null=True , on_delete= models.SET_NULL , related_name='customer')
	activity_name = models.ManyToManyField(Chapiteau_activity, related_name='activity')


	def __str__(self):
		return f'{self.customer_name}:{self.activity_name.name}'









