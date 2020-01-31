import pandas as pd

# file preparation for ari calculation between iteration for same day
def fileprep_multiple():
    path = "/home/olivera/Documents/communities_multiple_all/all/"
    #file name communities_dec04_v6.csv
    filenames = open("files/filenames.txt", 'r')
    for fn in filenames:
        month = fn[12:18]
        wf = open("files/" + month.strip() + ".txt", 'w')
        for i in range(1, 11):
            file = fn.strip('\n') + "_v" + str(i) + ".csv"
            #print(file)
            df = pd.read_csv(path + file)
            list = []
            for pid in range(1, 301):
                #poly_id1,community
                com = df.loc[df['poly_id1'] == pid]['community']
                #print(file)
                #print("this is pid ", pid, com.item())
                list.append(com.item())
            print(file, list)
            wf.write(str(i) + "; " + str(list) + '\n')

        wf.close()


def main():
    path = "/home/olivera/Documents/communities_multiple_all/all/"
    #file name communities_dec19_v1.csv
    filenames = open("files/filenames2.txt", 'r')
    wf = open("files/all_months.txt", 'w')
    for fn in filenames:
        month = fn[12:18]
        df = pd.read_csv(path + fn.strip('\n'))
        list = []
        for pid in range(1, 301):
            com = df.loc[df['poly_id1'] == pid]['community']
            list.append(com.item())

        wf.write(month + "; " + str(list) + '\n')

    wf.close()






if __name__ == '__main__':
    main()