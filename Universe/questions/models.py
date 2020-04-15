from django.db import models

class Questions(models.Model):
    question_1_titile=models.CharField(max_length=60,null=False,blank=False)
    question_1_description=models.TextField()
    question_1_input=models.CharField(max_length=500)
    question_1_output=models.CharField(max_length=400)
    question_1_sample_1=models.CharField(max_length=500)
    question_1_sample_output_1=models.CharField(max_length=10)
    question_1_sample_2=models.CharField(max_length=500, default="C")
    question_1_sample_output_2=models.CharField(max_length=10,default="C,E,G")
    question_1_sample_3=models.CharField(max_length=500,default="G")
    question_1_sample_output_3=models.CharField(max_length=10,default="G,B,D")
    question_1_sample_explain=models.CharField(max_length=500,null=True,blank=True,default="In Sample case #1, the combo for C-Major Chord is displayed according to gradual increase in note according to given pattern.")


    def __str__(self):
        return str(self.question_1_titile)