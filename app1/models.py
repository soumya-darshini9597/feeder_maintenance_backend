from django.db import models

class Feeder(models.Model):
    mesuredHeight = models.CharField(max_length=250,help_text="mesuredHeight in cm",null=True,blank=True)
    stepCount = models.PositiveIntegerField(help_text="Number of stepCount",null=True,blank=True)
    # targetHeight = models.PositiveIntegerField(help_text="target in mm",null=True,blank=True)
    conformationHeight = models.PositiveIntegerField(help_text="conformationheight",null=True,blank=True)


    def __str__(self):
        return f"Feeder - mesuredHeight: {self.mesuredHeight} m, stepCount: {self.stepCount},conformationHeight: {self.conformationHeight}"

