S = int(input(' enter your score: '))
if S >= 0 and S < 10:
    print('your score is bad')
elif S >= 10 and S < 14:
    print('your score is not  bad')
elif S >= 14 and S <18:
    print('your score is good')
elif S >= 18 and S <= 20:
    print('your score is great')
elif S < 0 :
    print('wrong score')
elif S > 20 :
    print('wrong score')

