# implicit matrix recommender
import implicit
import pickle
import numpy as np
from scipy.sparse import load_npz
import os


class ImplicitRecommender():
    dimentions = 30
    user_items = load_npz(
        '/Users/vladyslavp/ML/git.com/Advanced_Django_CBV/reco_poc/cbv_reco/basic_app/reco_system/user_items.npz')
    print(os.path.dirname(os.path.abspath(__file__)))
    # duplicated with data loader
    # shoudl use only os.paths
    products_arr = np.genfromtxt(
        "/Users/vladyslavp/ML/git.com/Advanced_Django_CBV/reco_poc/cbv_reco/data/products_arr.csv")
    customers_arr = np.genfromtxt(
        "/Users/vladyslavp/ML/git.com/Advanced_Django_CBV/reco_poc/cbv_reco/data/customers_arr.csv")

    def __init__(self):
        filename = '/Users/vladyslavp/ML/git.com/Advanced_Django_CBV/reco_poc/cbv_reco/basic_app/reco_system/finalized_model.sav'
        self.loaded_model = pickle.load(open(filename, 'rb'))
        print('model loaded {}'.format(self.loaded_model))

    def recommend(self, user_id):
        #print('insde the recommend')
        #print(user_id)

        recommendations = self.loaded_model.recommend(
            user_id, ImplicitRecommender.user_items, N=ImplicitRecommender.dimentions)
        #print(recommendations)
        fast_recommended = []

        for index in recommendations:
            code = ImplicitRecommender.products_arr[index[0]]
            fast_recommended.append(code)

        print("recommened items : {}".format(fast_recommended))
        return fast_recommended
