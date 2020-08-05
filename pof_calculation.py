# perceptron calculation
# approach: 
# k_c the pof of current layer
# k_u kernal size of last layer
# s stride of last layer
def perception(k_c,k_u,s):
    return k_c*k_u - (k_c-1)*(k_u-s)


def main():
    all_ks = [[7,2],[5,2],[3,2],[3,1],[3,2],[3,1],[1,1]]
    k_c = 1
    for ks in all_ks[::-1]:
        print(ks)
        k_c = perception(k_c,ks[0],ks[1])
        print(k_c)



if __name__ == '__main__':
    main()
       

