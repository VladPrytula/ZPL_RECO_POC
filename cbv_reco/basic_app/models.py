from django.db import models
import datetime
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=256)
    # weight = models.PositiveIntegerField()

    # below fields are mirroring the DB extract
    art_c_prod_nubmer = models.IntegerField(default=-1)
    art_n_key_article = models.IntegerField(default=-1)
    ppr_n_key_phys_product = models.IntegerField(default=-1)
    tdt_t_key_order_date = models.DateField(
        default=datetime.datetime(2000, 1, 1))
    art_v_art_description = models.CharField(
        max_length=1024, default='no_description')
    # above fields are mirroring the DB extract

    # this will contain the url derived from the image name (see reco sytem notebook)
    image_url = models.URLField(
        default='https://images.pexels.com/photos/35435/pexels-photo.jpg')

    lookup_product_idx = models.IntegerField(null=True)

    # buyer = models.ForeignKey(
    #    PetOwner, related_name='products', on_delete=models.CASCADE)

    """  
    @classmethod
    def create(cls, name, art_c_prod_nubmer, art_v_art_description, lookup_product_idx):
        product = cls(name=name, art_c_prod_nubmer=art_c_prod_nubmer,
                    art_v_art_description=art_v_art_description, lookup_product_idx=lookup_product_idx)
        # do something with the product
        print(name)
        return product
    """

    def __str__(self):
        return self.name


class PetOwner(models.Model):
    name = models.CharField(max_length=256)
    # below fields are mirroring the DB extract
    cus_n_key_customer = models.IntegerField(default=-1)
    # above fields are mirroring the DB extract

    # this field is used to map the current customer to the
    # corresponding entry in the customers_arr from the reco system.
    lookup_customers_idx = models.IntegerField(null=True)

    # product = models.ForeignKey(
    #    Product, related_name='customers', on_delete=models.CASCADE, null=True)
    # it seems like we need many to many
    products = models.ManyToManyField(Product)

    """
    @classmethod
    def create(cls, name, cus_n_key_customer, lookup_customers_idx, product):
        owner = cls(name=name, cus_n_key_customer=cus_n_key_customer,
                    lookup_customers_idx=lookup_customers_idx)
        # do something with the book
        return owner
    """

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    owner = models.ForeignKey(
        PetOwner, related_name='pets', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
