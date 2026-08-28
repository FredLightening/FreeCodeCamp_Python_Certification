def rod_checker(last_num,rod_a,rod_b):
    if last_num%2==0:
        even=last_num
        odd=None

    else:
        odd=last_num
        even=None

    if even and rod_a and rod_a[-1]%2!=0 and even<rod_a[-1]:
        return rod_a
    elif even and rod_b and rod_b[-1]%2!=0 and even<rod_b[-1]:
        return rod_b
    
    elif odd and rod_a and rod_a[-1]%2==0 and odd<rod_a[-1]:
        return rod_a
    elif odd and rod_b and rod_b[-1]%2==0 and odd<rod_b[-1]:
        return rod_b
    elif not rod_a:
        return rod_a
    elif not rod_b:
        return rod_b


def hanoi_solver(number):
    # if number
    inital=[i for i in range(1,number+1)][::-1]
    # print(inital)
    rod_one=inital.copy()
    rod_two=[]
    rod_three=[]
    moves=f"{rod_one} {rod_two} {rod_three}"
    prev=None
    count=0

    if number%2==0:
        rod_two.append(rod_one[-1])
        del(rod_one[-1])
        moves+=f"\n{rod_one} {rod_two} {rod_three}"
        count+=1

    else:
        rod_three.append(rod_one[-1])
        del(rod_one[-1])
        moves+=f"\n{rod_one} {rod_two} {rod_three}"
        count+=1

        

    while not rod_three==inital:
        # print(rod_three==inital)
        if rod_one and rod_one[-1]!=prev and ((not rod_two or not rod_three) or (rod_one[-1]<rod_two[-1] or rod_one[-1]<rod_three[-1])):
            mover=rod_one[-1]
            right_rod=rod_checker(mover,rod_two,rod_three)

            if rod_two is right_rod:
                prev=mover
                rod_two.append(mover)
                del(rod_one[-1])
                moves+=f"\n{rod_one} {rod_two} {rod_three}"
                count+=1
            elif rod_three is right_rod:
                prev=mover
                rod_three.append(mover)
                del(rod_one[-1])
                moves+=f"\n{rod_one} {rod_two} {rod_three}"
                count+=1

            # print(moves)

        elif rod_two and rod_two[-1]!=prev and ((not rod_one or not rod_three) or (rod_two[-1]<rod_one[-1] or rod_two[-1]<rod_three[-1])):
            mover=rod_two[-1]
            right_rod=rod_checker(mover,rod_one,rod_three)

            if rod_one is right_rod:
                prev=mover
                rod_one.append(mover)
                del(rod_two[-1])
                moves+=f"\n{rod_one} {rod_two} {rod_three}"
                count+=1
                
            elif rod_three is right_rod:
                prev=mover
                rod_three.append(mover)
                del(rod_two[-1])
                moves+=f"\n{rod_one} {rod_two} {rod_three}"
                count+=1

            # print(moves)
        elif rod_three==inital :
            break
        elif rod_three and  rod_three[-1]!=prev and ((not rod_two or not rod_one) or (rod_three[-1]<rod_two[-1] or rod_three[-1]<rod_one[-1])):
            mover=rod_three[-1]
            right_rod=rod_checker(mover,rod_one,rod_two)

            if rod_one is right_rod:
                prev=mover
                rod_one.append(mover)
                del(rod_three[-1])
                moves+=f"\n{rod_one} {rod_two} {rod_three}"
                count+=1

            elif rod_two is right_rod:
                prev=mover
                rod_two.append(mover)
                del(rod_three[-1])
                moves+=f"\n{rod_one} {rod_two} {rod_three}"
                count+=1

            # print(moves)
    # print(count)
    return moves
