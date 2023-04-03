import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1633714108 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = len(x)
    s2 = np.var(x)
    chi2_left = chi2.ppf(alpha / 2, df=n-1)
    chi2_right = chi2.ppf(1 - alpha / 2, df=n-1)
    left = np.sqrt((n-1)*s2/chi2_right)
    right = np.sqrt((n-1)*s2/chi2_left)
    return left, right
