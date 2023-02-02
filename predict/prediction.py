def my_predict(model,zip_code,area,bedrooms) :
    prediction = model.predict([[zip_code, bedrooms, area]])
    return prediction