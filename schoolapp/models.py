from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=200)

    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'

    def __str__(self):
        return self.name

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        ordering=('name',)
        verbose_name='course'
        verbose_name_plural='courses'

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FormSubmission(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    PURPOSE_CHOICES = [
        ('enquiry', 'Enquiry'),
        ('place_order', 'Place Order'),
        ('return', 'Return'),
    ]
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES)
    material = models.ForeignKey(Material, on_delete=models.CASCADE,default=True)

    def __str__(self):
        return self.name





