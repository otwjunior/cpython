import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers= 0
for questionNumber  in range(numberOfQuestions):
    #Pick two random numbers:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = '#%s: %s * %s =  ' %(questionNumber, num1,num2)

    try:
        # right answer are handled by allowregexs
        #wrong answer are handled by blockregex, with custom message.
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 *num2)],blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
            print('out of time')
    except pyip.RetryLimitException:
            print('Out of tries')
    else:
            #This block runs if no exception were raised  in the try block.
        print('Correct!')
        correctAnswers += 1
    time.sleep(1) #brief pause to let user see the result.
print('Score: %s / %s' %(correctAnswers, numberOfQuestions))