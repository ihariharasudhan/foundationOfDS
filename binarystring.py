def bstoi(binary):
    binaryint = int(binary,2)
    return binaryint

def main():
    binary = input("Enter a binary input :")
    res=bstoi(binary)
    print(binary," is ",res)
    binary = input("Enter password :")
    bins  = bstoi(binary)
    print(binary," is ",bins)
    mask = input("Enter mask :")
    mas = bstoi(mask)
    print(mask," is ",mas)
    for i in range(len(mask)):
        if mask[i] == '1':
            print(binary[i],end=" ")
        else:
            print("_",end=" ")



if __name__ == "__main__":
    main()