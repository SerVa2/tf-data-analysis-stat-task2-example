import pandas as pd
import numpy as np

from scipy.stats import chi2

chat_id = 1633714108 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Определяем уровень значимости
    alpha = 1 - p
    
    # Определяем степень свободы
    df = len(x) - 1
    
    # Определяем квантиль распределения хи-квадрат со степенью свободы df 
    chi2_1 = chi2.ppf(1 - alpha/2, df)
    chi2_2 = chi2.ppf(alpha/2, df)
    
    # Определяем оценку для sigma
    var = np.sum(x**2) / (len(x) * 49) # Несмещенная оценка дисперсии
    sigma_1 = np.sqrt(var * df / chi2_1)
    sigma_2 = np.sqrt(var * df / chi2_2)
    
    # Возвращаем интервал
    return (sigma_1, sigma_2)
