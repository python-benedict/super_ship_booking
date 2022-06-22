from typing_extensions import Required
from django.db import models

# Create your models here.


# Start of seat class

class HumanSeat(models.Model):
    total_seats = models.IntegerField()




class MartialSeat(models.Model):
    total_seats = models.IntegerField()

# End of seat class



# start of the abstract class we are having
class PassengerBaseModel(models.Model):
    name = models.CharField(max_length=100)
    age =  models.IntegerField()
    gender = models.CharField(max_length=10)
    human = models.BooleanField(default=False)
    martial = models.BooleanField(default=False)

    def __str__(self):
        return self.name




class SpaceShipBaseModel(models.Model):
    name = models.CharField(max_length=100)
    speed = models.IntegerField()
    capacity = models.IntegerField()
    engine_type = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    human_seat = models.ForeignKey(HumanSeat, on_delete=models.CASCADE)
    martial_seat = models.ForeignKey(MartialSeat, on_delete=models.CASCADE)
    class Meta: 
        abstract = True

# End of the abstract class we are having




# start of the ships we are having
class Stadelino(SpaceShipBaseModel):

    def __str__(self):
        return self.name




class Spacer(SpaceShipBaseModel):
    
    def __str__(self):
        return self.name




class BulletShip(SpaceShipBaseModel):
    
    def __str__(self):
        return self.name
# End of the ships we are having






