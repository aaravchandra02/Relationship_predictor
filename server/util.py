import pickle
import numpy as np

__model = None


def load_saved_models():
    global __model
    print(f"\n\nLoading saved Advanced Machine Learning Models...\n\n")
    if __model is None:
        with open("model/brain.pkl", "rb") as f:
            __model = pickle.load(f)
    print(__model)
    print(f"\n\nImport done successfully...\n\n\n")


def get_prediction(arr):
    return __model.predict(arr)


if __name__ == "__main__":
    load_saved_models()
    test_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    test_arr = np.asarray(test_list)
    print(test_arr.shape)
    test_arr = np.reshape(test_arr, newshape=(1, 54))
    print(test_arr.shape)
    print(get_prediction(test_arr))
