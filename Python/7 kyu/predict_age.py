import math

def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    return math.sqrt(sum(list(map(lambda x: x * x, locals().values())))) // 2
    

if __name__ == "__main__":
    predict_age(65,60,75,55,60,63,64,45) == 86
    print("All tests passed")