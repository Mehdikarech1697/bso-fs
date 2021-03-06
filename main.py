from fs_data import FSData

if __name__=="__main__":

    # RL 

    alhpa = 0.1
    gamma = 0.99
    epsilon = 0.01

    # BSO

    flip = 5
    maxChance = 3
    nbrBees = 10
    maxIterations = 10
    locIterations = 10

    # Test type

    typeOfAlgo = 1
    nbr_exec = 1
    dataset = "Glass"
    data_loc_path = "./datasets/"
    location = data_loc_path + dataset + ".csv"
    method = "qbso_simple"
    test_param = "rl"
    param = "gamma"
    val = str(locals()[param])
    classifier = "knn"

    instance = FSData(typeOfAlgo,location,nbr_exec,method,test_param,param,val,classifier,alhpa,gamma,epsilon)
    instance.run(flip,maxChance,nbrBees,maxIterations,locIterations)