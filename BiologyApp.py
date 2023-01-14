from Question import Question

question_prompts = [
    """2. One of the differences between bookkeeping and accounting is that the former __.  
    A. records data while the latter interprets 
    B. is regarded as the language of the business while the latter ascertains its strength 
    C. interprets data while the latter records it  
    D. summarises information while the latter communicates it""",
    """3. The concept which states that revenue should be recognized at the point when the sale is deemed to have been made is  
    A. matching 
    B. consistency 
    C. realization 
    D. going concern""",
    """4. A cheque of ₦5,000 paid to Sulieman had been correctly entered in the cash book but had not been entered in Sulieman's account. To correct this error, debit Sulieman's account and credit  
    A. cash account 
    B. bank account 
    C. suspense account 
    D. purchases account""",
    """5. Aduke Motors bought three Toyota Hilux vans on cash at the cost of₦6,000,000, on debiting the vehicle account, the corresponding credit for the purchase will appear in the __.  
    A. sales day book 
    B. purchases day book 
    C. sales subsidiary book 
    D. cash book"""
]

questions = [
    Question(question_prompts[0],"A"),
    Question(question_prompts[1],"C"),
    Question(question_prompts[2],"B"),
    Question(question_prompts[3],"D")
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        answer=answer.upper()
        if answer == question.answer:
            score+=1
    print("you got" + str(score) + "/" + str(len(questions))+ " correct")
run_test(questions)

