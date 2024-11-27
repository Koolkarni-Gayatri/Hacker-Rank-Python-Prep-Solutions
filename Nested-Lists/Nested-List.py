if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    scores=[item[1] for item in records]
    min_scr=sorted(set(scores))
    
    names=sorted([item[0] for item in records if item[1]==min_scr[1]])
    [print(item) for item in names]
