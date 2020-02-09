def main():
    c = int(input())
    d = input().split()
    d1 = list(map(int,d))
    d1.sort(reverse=True)
    stacks = [set([d1[0]])]
    for i in range(1,c):
        for j in range(len(stacks)):
            if d1[i] in stacks[j]:
                if(j+1==len(stacks)):
                    stacks = stacks + [set([d1[i]])] 
                continue
            else:
                stacks[j].add(d1[i])
                break
    print(len(stacks))
main()