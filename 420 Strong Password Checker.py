import random

#Directly from leetcode if you input an invalid test case
valid_test_case_characters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '!']

#With regular random generation, strong passwords are too common for useful testcases
#A random one of these lists is assigned to "character_set_to_use"
all_letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
all_letters_lower=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
all_letters_upper=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
all_numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
weird_characters=['.', '!']
all_character_sets=[valid_test_case_characters,all_letters,all_numbers,weird_characters,all_letters_lower,all_letters_upper]

test_case_count=""

try:
    while test_case_count!="exit":
        test_case_count=input("Enter number of test cases to generate, or type 'exit' to exit. 😎 \n")
        
        if test_case_count=="exit":
            print("Exiting ❗")
            break
        
        custom_test_cases=input("Input number desired generation cases\n1:All Random\n2:All Letters\n3:All Numbers\n4:All Dot and Exclamations\n5:All Letters Lowercase\n6:All Leeters Uppercase\n")

        if custom_test_cases=="exit":
            print("Exiting ❗")
            break
        
        
        
        else:
            array_length=random.randrange(1,50)
            for i in range(int(test_case_count)):
                
                if custom_test_cases=="1":
                    character_set_to_use=random.choice(all_character_sets)
                else:
                    character_set_to_use=all_character_sets[int(custom_test_cases)-1]

                #Start with atleast one value for the string
                test_case_string=random.choice(character_set_to_use)
                
                #Max character limit is 50, so 0 to 49 characters to add randomly
                array_length=random.randrange(0,49)
                

                for k in range(array_length):
                    #With regular random generation, no triple repeating characters are very uncommon
                    repating_character_increaser=random.randrange(1,100)
                    #Can change chance of a repeating character here
                    if repating_character_increaser>=60:
                        test_case_string+=test_case_string[-1]


                    else:
                        test_case_string+=random.choice(character_set_to_use)
                
                print(f'"{test_case_string}"')
except:
    print("Error with inputs, exiting ❗")