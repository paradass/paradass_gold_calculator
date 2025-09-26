#Baisc gold calculator with python by Burak "paradass" Görez

import requests

class GoldCalculator:
    def __init__(self):
        self.url = "https://malatyakuyumcular.net/"
    
    def get_gold_price(self,url):
        response = requests.get(url,timeout=3)
        html_code = response.text.split("\n")
        gram_gold = html_code[135].split(">")[3].split("<")[0]
        gram_gold = gram_gold.replace(".","")
        gram_gold = gram_gold.replace(",",".")
        gram_gold_price = float(gram_gold)
        return gram_gold_price

    def calculate(self):
        try:
            gold_amount = float(input("Kaç gram altının var? "))
            gram_gold_price = self.get_gold_price(self.url)
            gold_value = gold_amount * gram_gold_price
            print(f"{gold_amount} gram altini satarsan \033[32m{gold_value:,.2f}\033[0m₺ ediyor.")
            print(f"{gold_amount} gram altının {gold_amount/40} gramı zekat olarak \033[32m{gold_value/40:,.2f}\033[0m₺ ediyor.")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    gold_calculator = GoldCalculator()
    gold_calculator.calculate()