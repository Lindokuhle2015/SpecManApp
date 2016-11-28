from django.db import models
from django.contrib.auth.models import User
from registration.signals import user_registered
#from django.db.models.Model import models


# Create your models here.


class UserProfile(models.Model) :
    #Links UserProfile to User Model Instance
    #Models the Interested and Affected Register Parameters for the SutherLand Astronomy Advantage Area
    user = models.OneToOneField(User)
    #Additional Attributes
    FullNames = models.CharField(max_length =60)
    CityTown = models.CharField(max_length =100)
    PostalAddress = models.CharField(max_length=100)
    PostalCode = models.IntegerField()
    CellphoneNumber = models.IntegerField()
    TelNumber = models.IntegerField()
    YearSubmitted = models.IntegerField()
    CommunicationMethod = models.CharField(max_length =10)
    picture = models.ImageField(upload_to ='profile_images', blank= True)
    Landline = models.IntegerField()
    Fax  = models.IntegerField()
    #email = models.CharField(max_length =50)
    StatusRelation = models.CharField(max_length=50)
    Other = models.CharField(max_length = 50)
    AdvantageArea= models.CharField(max_length=100)
    AffectedParty = models.CharField(max_length = 100)
    PhysicalAddress =models.CharField(max_length=100)
    PropertyFarm = models.CharField(max_length =50)
    DeedNumber = models.CharField(max_length =30)
    FarmName = models.CharField(max_length=50)
    Radio = models.CharField(max_length=60)
    Radio_Other = models.CharField(max_length =60)
    TVSignal = models.CharField(max_length=30)
    OtherTV = models.CharField(max_length = 100)
    TVLicence = models.CharField(max_length =30)
    ElectronicComm = models.CharField(max_length=50)
    IcasaLicence = models.CharField(max_length =50)
    OtherElectronicComm = models.CharField(max_length =50)
    state = models.CharField(max_length = 30)
    OtherInterest = models.CharField(max_length =100)
    AdditionalInfo = models.CharField(max_length =150)
    Certify = models.CharField(max_length =15)
    
    def __unicode__(self) :
        return self.user.username
    class Meta :
        db_table = "userprofile"
        

    #Models the Interested and Affected Stake holders
   # user = models.OneToOneField(User)
    #FirstName = models.CharField(max_length =60)
    #LastName =models.CharField(max_length=60)
    #PostalAddress =models.CharField(max_length=60)

    #CellphoneNumber = models.IntegerField()

    #CommunicationMethod = models.CharField(max_length=50)
    
    
    