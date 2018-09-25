# data population script
# pupulates models based on the data prepared for the reco system notebook
# Script populates only those customer that are present in the cleaned data set, i.e.
# the ones that are present in the 'customers_arr'

"""
 In the Notebook we have the following mapping between the cus_n_key_customer
 and the positional index in the 'customers_arr' array
    # Get our unique customers
    customers = list(np.sort(df_lim.CUS_N_KEY_CUSTOMER.unique()))
    # Get our unique products that were purchased
    products = list(df_lim.ART_C_PROD_NUMBER.unique())
    # All of our purchases
    quantity = list(df_lim.SCM_D_QUANTITY)

    customers_arr = np.array(customers) # Array of customer IDs from the ratings matrix
    products_arr = np.array(products)   # Array of product IDs from the ratings matrix

    so to get the values for 
    lookup_product_array and lookup_customers_array we have to get the positional index
    of the ART_C_PROD_NUMBER and CUS_N_KEY_CUSTOMER respectively
"""
import numpy as np
import pandas as pd
import os


def read_customers_array(file):
    customers_arr = np.genfromtxt(file)
    return customers_arr


def read_products_array(file):
    products_arr = np.genfromtxt(file)
    return products_arr


def read_user_data(file):
    grouped_purchased = pd.read_csv(file, sep='\t', encoding='utf-8')
    return grouped_purchased


def read_item_lookup(file):
    item_lookup = pd.read_csv(file, sep='\t', encoding='utf-8')
    print("First three rows of the data frame:")
    print(item_lookup.iloc[:3])
    return item_lookup


def populate_users(grouped_purchased, customers_arr):
    """
        I will use grouped_purchased data frame to load customers for now, and will skip names
        the name will be the cus_n_key_customer
        !!! TODO: this is to be reconsidered !!!!
        this DF gives mapping between products and customers, not customers.
        It looks like I have to get the customers from the initial table,
        restricted to the customers_arr
        On the other hand , coudl be from this table also... there is not so much info in the
        raw_df
    """
    #grouped_purchased = pd.read_csv(file, sep='\t', encoding='utf-8')
    #grouped_purchased_restricted = grouped_purchased[grouped_purchased['CUS_N_KEY_CUSTOMER'].isin(customers_arr)]
    #print("First three rows of the data frame:")
    # print(grouped_purchased_restricted.iloc[:3])

    # should be done with bulk_create()
    ###############################
    PetOwner.objects.all().delete()
    # >>> o2 = PetOwner(name='owner2', cus_n_key_customer=12345, lookup_customers_idx=1, product=Product.objects.filter(art_c_prod_nubmer=111).first())
    # >>> o2.save()
    ###############################

    for index, x in np.ndenumerate(customers_arr):
        #print(index[0], x.astype(int))
        owner = PetOwner(name=x.astype(str), cus_n_key_customer=x.astype(
            int), lookup_customers_idx=index[0])

        owner.save()

        # we hve to get the list of products that were bought by this user (should it be unique?)
        bought_products_prod_numbers = grouped_purchased[grouped_purchased['CUS_N_KEY_CUSTOMER'] == x.astype(
            int)]['ART_C_PROD_NUMBER'].unique()
        bought_products_qset = Product.objects.filter(
            art_c_prod_nubmer__in=bought_products_prod_numbers)

        owner.products.add(*bought_products_qset)


def populate_products(products_arr, item_lookup):
    Product.objects.all().delete()

    for idx, x in np.ndenumerate(products_arr):
        description = item_lookup[item_lookup['ART_C_PROD_NUMBER'] == x.astype(
            int)].iloc[0]['ART_V_ART_DESCRIPTION']

        product = Product(name=x.astype(str), art_c_prod_nubmer=x.astype(
            int), lookup_product_idx=idx[0])
        product.save()  # it should be unique...


if __name__ == "__main__":
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'cbv_reco.settings')
    django.setup()
    from basic_app.models import PetOwner, Product

    customers_arr_file = "data/customers_arr.csv"
    products_arr_file = "data/products_arr.csv"
    item_lookup_file = "data/item_lookup.csv"
    grouped_purchased_file = "data/grouped_purchased.csv"

    customers_arr = read_customers_array(customers_arr_file)
    products_arr = read_products_array(products_arr_file)

    item_lookup = read_item_lookup(item_lookup_file)
    grouped_purchased = read_user_data(grouped_purchased_file)
    populate_products(products_arr=products_arr, item_lookup=item_lookup)
    populate_users(grouped_purchased=grouped_purchased,
                   customers_arr=customers_arr)

    print("Script finished running")
