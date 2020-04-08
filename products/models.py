from django.db import models
class Product(models.Model):
                title=models.CharField(max_length=70)

                image=models.ImageField(upload_to='images/')
                price=models.IntegerField(default=0)
                body=models.TextField()

                AUTOMOTIVE=1
                BABY=2
                BEAUTY=3
                BOOKS=4
                COMPUTERS=5
                ELECTRONICS=6
                WOMEN=7
                MEN=8

                HOMEKITCHEN=9
                SPORTS=10
                TOYSGAME=11
                catagory = [
                       (AUTOMOTIVE, 'Automotive'),
                               (BABY, 'Baby'),
                       (BEAUTY, 'Beauty & personal care'),
                    (BOOKS, 'Books'),
                    (COMPUTERS,'Computers'),
                    (ELECTRONICS,'Electronics'),
                    (WOMEN,'Women\'fasion'),
                    (MEN,'Men\'fasion'),

                    (HOMEKITCHEN,'Home & kitchen'),
                    (SPORTS,'Sports & outdore'),
                    (TOYSGAME,'Toys & games'),
                  ]
                field = models.IntegerField(  choices=catagory,
                    default=COMPUTERS,

                )
                def __str__(self):
                     return self.title
