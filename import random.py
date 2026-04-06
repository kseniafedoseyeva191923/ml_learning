import random

def run_test():
    questions = [
        {
            "q": "Как расшифровывается CSV?",
            "a": ["Comma Separated Values", "Color System Video", "Central Save Volume"],
            "c": 0
        },
        {
            "q": "Какая библиотека основная для работы с таблицами?",
            "a": ["NumPy", "Pandas", "Matplotlib"],
            "c": 1
        },
        {
            "q": "Как обратиться к столбцу 'GR' в DataFrame df?",
            "a": ["df.get('GR')", "df['GR']", "Оба варианта вер