import random

test_case_count=""

try:
    while test_case_count!="exit":
        test_case_count=input("Enter number of test cases to generate, or type 'exit' to exit. \n")

        array_length=random.randrange(3,50)

        if test_case_count=="exit":
            break
        
        else:
            for i in range(int(test_case_count)):
                test_case_array=random.sample(range(1,50),array_length)
                print(test_case_array)
except:
    print("Error with inputs, exiting")