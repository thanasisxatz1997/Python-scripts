def testRanked():
    ranked = [100, 90, 90, 80]
    print(ranked.count(90))
    dict = {}
    for rank in ranked:
        if rank not in dict.keys():
            dict[rank] = ranked.count(rank)
    for item in dict:
        print(item, dict[item])
    print(dict)


def rankedApproach1():
    ranked = [100, 90, 90, 80]
    player = [70, 80, 105]
    newRanked = ranked + player
    newRanked = sorted(newRanked, reverse=True)
    print(newRanked)
    dict = {}
    count = 0
    for score in newRanked:
        if score not in dict.keys():
            count += 1
            dict[score] = count
    print(dict)
    for score in player:
        print(dict[score])

def rankedApproach2():
    ranked = [100, 90, 90, 80]
    player = [70, 80, 105]
    dict={}
    res=[]
    count=0
    for rankedScore in ranked:
        if rankedScore not in dict.keys():
            count+=1
            dict[rankedScore]=count
    print(dict)
    for playerScore in player:
        if playerScore in dict:
            res.append(dict[playerScore])
        else:
            dict = {}
            count=0
            ranked.append(playerScore)
            ranked=sorted(ranked,reverse=True)
            for rankedScore in ranked:
                if rankedScore not in dict.keys():
                    count += 1
                    dict[rankedScore] = count
            res.append(dict[playerScore])
    return res

def rankedApproach3():
    ranked = [100, 90, 90, 80]
    player = [70, 80, 105]
    res = [1]*len(player)
    for k,playerScore in enumerate(player):
        i=0
        count = 1
        cur = ranked[0]
        while i<len(ranked) and playerScore<ranked[i]:
            if ranked[i] != cur:
                count += 1
                cur = ranked[i]
            i += 1
        if i==0:
            res[k]=1
        else:
            res[k]=count+1
    return res

def rankedApproach4():
    ranked = [100, 90, 90, 80]
    player = [70, 80, 105]
    numR=[1]*len(ranked)
    for i in range(1,len(ranked)):
        if ranked[i]==ranked[i-1]:
            numR[i]=numR[i-1]
        else:
            numR[i]=numR[i-1]+1
    print(numR)
    res=[1]*len(player)
    for i in range(len(player)):
        j=len()
        while j<len(ranked):
            if player[i]<ranked[j]:
                res[i]=numR[j]+1
                print(numR[j])
                break
            j+=1
    return res

if __name__ == '__main__':
    print(rankedApproach4())
