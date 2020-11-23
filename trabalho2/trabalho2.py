
attribute_reference = [
    {'b': 0,'c': 1,'x': 2,'f': 3,'k': 4,'s':5},
    {'f': 0,'g': 1,'y': 2,'s': 3},
    {'n': 0,'b': 1,'c': 2,'g': 3,'r': 4,'p': 5,'u': 6,'e': 7,'w': 8,'y': 9},
    {'t': 0,'f': 1},
    {'a': 0,'l': 1,'c': 2,'y': 3,'f': 4,'m': 5,'n': 6,'p': 7,'s': 8},
    {'a': 0,'d': 1,'f': 2,'n': 3},
    {'c': 0,'w': 1,'d': 2},
    {'b': 0,'n': 1},
    {'k': 0,'n': 1,'b': 2,'h': 3,'g': 4,'r': 5,'o': 6,'p': 7,'u': 8,'e': 9,'w': 10,'y': 11},
    {'e': 0,'t': 1},
    {'b': 0,'c': 1,'u': 2,'e': 3,'z': 4,'r': 5,'?': 6},
    {'f': 0,'y': 1,'k': 2,'s': 3},
    {'f': 0,'y': 1,'k': 2,'s': 3},
    {'n': 0,'b': 1,'c': 2,'g': 3,'o': 4,'p': 5,'e': 6,'w': 7,'w': 8,'y': 9},
    {'n': 0,'b': 1,'c': 2,'g': 3,'o': 4,'p': 5,'e': 6,'w': 7,'w': 8,'y': 9},
    {'p': 0,'u': 1},
    {'n': 0,'o': 1,'w': 2,'y': 3},
    {'n': 0,'o': 1,'t': 2},
    {'c': 0,'e': 1,'f': 2,'l': 3,'n': 4,'p': 5,'s': 6,'z': 7},
    {'k': 0,'n': 1,'b': 2,'h': 3,'r': 4,'o': 5,'u': 6,'w': 7,'y': 8},
    {'a': 0,'c': 1,'n': 2,'s': 3,'v': 4,'y': 5},
    {'g': 0,'l': 1,'m': 2,'p': 3,'u': 4,'w': 5,'d': 6}
]

K = int(input())
Ntrain, Ntest = map(int, input().split())
D = 22

def vectorize(N):
    Xtotal = []
    for mushroom in range(N):
        attribute_translation = []
        Xtrain = input().split()
        for l in range(22):
            attribute_translation.append(attribute_reference[l][Xtrain[l]])

        Xtotal.append(attribute_translation)


    return Xtotal

Xtotal = vectorize(Ntrain)

Ytrain = []

for i in range(Ntrain):
   train_label = input()
   Ytrain.append(train_label)

Xtotal_test = vectorize(Ntest)

def calculate_u(Xtotal, N):
    u_list = []
    for i in range(22):
        sum_u = 0
        for j in range(N):
            sum_u += Xtotal[j][i]
        att_u = sum_u / N
        u_list.append(att_u)
    
    return u_list


def calculate_sigma(Xtotal, u_list,N):
    sigma_list = []
    for i in range(22):
        sum_sigma = 0
        for j in range(N):
            sum_sigma += (Xtotal[j][i] - u_list[i])**2
        sigma_list.append((sum_sigma / N)**0.5)
    
    return sigma_list


def calculate_normal(Xtotal, u_list,sigma_list,N):
    Xnorm = []

    for i in range(N):
        aux_list = []
        for j in range(22):
            aux_list.append(0)

        Xnorm.append(aux_list)

    for i in range(22):
        for j in range(N):
            if sigma_list[i] == 0:
                Xnorm[j][i] = 0
            else:
                Xnorm[j][i] = ((Xtotal[j][i] - u_list[i])/sigma_list[i])

    return Xnorm


u_list = calculate_u(Xtotal,Ntrain)
sigma_list = calculate_sigma(Xtotal,u_list,Ntrain)
Xnormal = calculate_normal(Xtotal,u_list,sigma_list,Ntrain)
Xnormal_test = calculate_normal(Xtotal_test,u_list,sigma_list,Ntest)


for i in range(Ntest):
    distance_list = []
    for k in range(Ntrain):
        distance = 0
        for j in range(22):
            distance += (Xnormal_test[i][j] - Xnormal[k][j])**2
        distance_list.append(distance**0.5)
        
    list_ = []

    for m in range(Ntrain):
        list_.append([distance_list[m], Ytrain[m]])

    list_.sort(key=lambda x: x[0])

    p = 0
    e = 0

    for m in range(K):
    
        if list_[m][1] == 'p':
            p += 1
        if list_[m][1] == 'e':
            e += 1

    if p > e:
        print('p')
    if e > p:
        print('e')