



import random



def hello():
    a = "Hello World"
    print a

hello()

def char_word():
     inp_1 = raw_input("Enter the word: ")
     inp_2 = raw_input("Enter the 2nd word: ")
     out_list = [inp_1]
     out_list.append(inp_2)
     out_list = "".join(out_list)
     out_final = list(out_list)
     out_final.pop()
     out_final.pop(0)
     out_final = "".join(out_final)
     return out_final

def less_than():

     # out_list = []
     # num = input("Enter the num to compare : ")
     # for i in list_1:
     #     if i < num:
     #         out_list.append(i)
     #         return out_list
    return [i for i in list_1 if i < num]





if __name__ == '__main__':
    list_1 = random.sample(range(100), 10)
    print list_1
    num = input("Enter the num : ")





#print char_word()
print less_than()
