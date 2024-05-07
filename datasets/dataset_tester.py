from conll04_typed import CONLL04
from self_relations import PERSONAL
if __name__ == '__main__':
    print("DEBUGGING")
    
    dataset_name = 'E:/CodesRepos/MGR_Gaming/Model/rebel/datasets/conll04_typed.py'
    train_file = "E:/CodesRepos/MGR_Gaming/Model/rebel/datasets/data/conll04/conll04_train.json"
    validation_file = 'E:/CodesRepos/MGR_Gaming/Model/rebel/datasets/data/conll04/conll04_test.json'
    test_file = 'E:/CodesRepos/MGR_Gaming/Model/rebel/datasets/data/conll04/conll04_test.json'
    
    
    #ds = CONLL04()
    # copy in here what  print("Cached PATHS -- copy into STEP 5:", filepaths) printed on the terminal
    # mind [], [[]] to match original implementation
    #listed = [i for i in ds._generate_examples([train_file])]
    #print(listed[0])
    
    
    train_file = "E:/CodesRepos/MGR_Gaming/Model/rebel/datasets/data/self_made/self_test.json"
    ms = PERSONAL()
    
    listed = [i for i in ms._generate_examples([train_file])]
    print(listed[0])
    print(listed[1])
    print(listed[500])

    #('3255', {'title': '3255', 'context': "Newspaper ` Explains ' U.S. Interests Section Events FL1402001894 Havana Radio Reloj Network in Spanish 2100 GMT 13 Feb 94", 'id': '3255', 'triplets': '<triplet> Radio Reloj Network <org> Havana <loc> headquarters location'})