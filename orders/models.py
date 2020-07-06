from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class Meal(models.Model):

    CATEGORIES = [
        ('RP', 'Regular Pizza'),
        ('SP', 'Sicilian Pizza'),
        ('TO', 'Topping'),
        ('SU', 'Sub'),
        ('PA', 'Pasta'),
        ('SA', 'Salad'),
        ('DP', 'Dinner Plate')
    ]

    category = models.CharField(max_length=64, choices=CATEGORIES)

    name = models.CharField(max_length=64)

    small_price = models.FloatField(blank=True, null=True, default=None)
    large_price = models.FloatField(blank=True, null=True, default=None)
    unique_price = models.FloatField(blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.category} - {self.name}"

# class Pizza(models.Model):
#
#     PIZZA_STYLE = [
#         ('R', 'Regular'),
#         ('S', 'Sicilian')
#     ]
#
#     style = models.CharField(max_length=1, choices=PIZZA_STYLE)
#
#     PIZZA_TYPE = [
#         ('C', 'Cheese'),
#         ('1', '1 Topping'),
#         ('2', '2 Toppings'),
#         ('3', '3 Toppings'),
#         ('S', 'Special')
#     ]
#
#     type = models.CharField(max_length=1, choices=PIZZA_TYPE)
#
#     PIZZA_SIZE = [
#         ('S', 'Small'),
#         ('L', 'Large')
#     ]
#
#     size = models.CharField(max_length=1, choices=PIZZA_SIZE)
#

    # PIZZA_TOPPINGS = [
    #     (0, 'Pepperoni'),
    #     (1, 'Sausage'),
    #     (2, 'Mushrooms'),
    #     (3, 'Onions'),
    #     (4, 'Ham'),
    #     (5, 'Canadian Bacon'),
    #     (6, 'Pineapple'),
    #     (7, 'Eggplant'),
    #     (8, 'Tomato & Basil'),
    #     (9, 'Green Peppers'),
    #     (10, 'Hamburger'),
    #     (11, 'Spinach'),
    #     (12, 'Artichoke'),
    #     (13, 'Buffalo Chicken'),
    #     (14, 'Barbeque Chicken'),
    #     (15, 'Anchovies'),
    #     (16, 'Black Olives'),
    #     (17, 'Fresh Garlic'),
    #     (18, 'Zucchini')
    # ]
    #
    # toppings = MultiSelectField(choices=PIZZA_TOPPINGS, max_choices=5, max_length=5)
