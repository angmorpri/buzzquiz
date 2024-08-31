# Python 3.10
# 27/08/2024


from buzzquiz import buzz
from buzzquiz.games import buzz_and_answer

if __name__ == "__main__":
    buzz.init(3)
    buzz_and_answer("blue", time_to_answer=8, chances=1, penalty=False)
