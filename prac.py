def separate_small_large(number):
    small_number=[]
    large_number=[]
    for i in number:
        if i <=0:
            small_number.append(i)
        else:
            large_number.append(i)
    return small_number,large_number
if __name__=="__main__":
     number_list=[2,5,6,-1,-5,6,8,10]
     print("original number:-[2,5,-1,-5,6,8,10]")
     a,b=separate_small_large(number_list)
     print(f"\n The list for small number:-{a}\n The list for large number:-{b}\n")
   