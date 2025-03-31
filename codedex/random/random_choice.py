def main():
    import random
    
    list = ["Yes - deinitely", "It is decidely so", "Without a doubt", "Reply hazy, try again.", "Ask again later", "Better not tell you now"]

    rand_ans = random.choice(list)

    input("What is your question?")
    print(rand_ans)

main()

