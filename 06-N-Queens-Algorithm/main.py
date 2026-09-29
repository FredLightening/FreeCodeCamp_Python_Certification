def legal(num,length,path):
    result=[]
    index=len(path)
    # for i in range(length):
    #     if not (i==num or i==num+1 or i==num-1) and i not in path:
    #         result.append(i)

    #     if 
    if index==0:
        
        for i in range(length):
            if not (i==num or i==num+1 or i==num-1) and i not in path:
                result.append(i)
    if index==0:
        return result[::-1]

    for number in range(length):

        

        for i,j in enumerate(path):
            if (number==num or number==num+1 or number==num-1) or abs((index-i))==abs((number-j)) or number in path:
            # if not (number==num or number==num+1 or number==num-1) and abs((index-i))!=abs((number-j)) and number not in path:#index!=i and abs((index-i))!=abs((number-j)):
                # print(f'index-i is {abs((index-i))} and number - j is {abs((number-j))}')
                result.append(number)
    gen_set={i for i in range(length)}

    converted_result=set(result)
    correct=gen_set-converted_result
    return list(correct)[::-1]
    # pass
def keep_list_check(array):
    
    for j in array[::-1]:
        if j:
            return True

    return False
def list_checker(array):
    delete_list=[]
    length= len(array)-1
    for i,j in enumerate(array[::-1]):
        if not j:
            delete_list.append(length-i)
        if j:
            delete_list.append(length-i)
            return [length-i,delete_list]



def dfs_n_queens(number):
    if number<1:
        return []
    rand=[]
    keeping_list=[]
    for i in range(number):
        keeping_list.append(rand.copy())



    # print(keeping_list)
    # return matrix
    count=0
    result=[]
    paths=[]    
    visited=[]
    # available=[]
    current=0
    keeping_list[0]=[i for i in range(number)][::-1]
    b=0
    # return keeping_list
    while paths not in result  and (keep_list_check(keeping_list) or paths not in visited):
        # print(f'{b} paths at {count} is {paths} and current is {current} and keeping list is {keeping_list} and visited is {visited}')


        if len(paths)==number and paths not in result :
          
            result.append(paths.copy())
            visited.append(paths.copy())
            # paths.pop()
            # print(paths)
            if not keep_list_check(keeping_list):
                break
            checked=list_checker(keeping_list)
            ind=checked[0]
            for i in checked[1]:
                if i<len(paths):
                    del paths[i]
            current=keeping_list[ind].pop()
            paths.append(current)
      
        # current=paths[-1]
        legal_spaces=legal(current,number,paths)
        index=len(paths)
        # if not keep_list_check(keeping_list):
        #     break
        if not keeping_list[index]:
            keeping_list[index]=legal_spaces.copy()
        if paths in visited and index==1 and keeping_list[index-1]:
            paths.pop()

            current=keeping_list[index-1].pop()
        elif paths in visited: #and list_checker(keeping_list)==0:
            checked=list_checker(keeping_list)
            ind=checked[0]
            for i in checked[1]:
                if i<len(paths):
                    del paths[i]
            # print(f'keeping list is {keeping_list}')
            current=keeping_list[ind].pop()
            # print(f'ind is {ind} current is {current}')
            legal_spaces=legal(current,number,paths)
            paths.append(current)
            index=len(paths)
            # print(f'path is {paths} and index is {index}')
            if index<number:
                keeping_list[index]=legal_spaces.copy()


        
        if len(paths)==number and paths not in result :
         pass
        elif keeping_list[index] and keeping_list[index][-1] not in paths and paths not in visited: #and result_checker(paths):
            # print('if 1')
           
            current=keeping_list[index].pop()
            # keeping_list[index].append(current)
            paths.append(current)



        elif not legal_spaces or not keeping_list[index]:
            # print('if 3')
            b=3
            visited.append(paths.copy())
            if not keep_list_check(keeping_list):
                break
            checked=list_checker(keeping_list)
            ind=checked[0]
            for i in checked[1]:
                if i<len(paths):
                    del paths[i]
            current=keeping_list[ind].pop()
            paths.append(current)





    return result
