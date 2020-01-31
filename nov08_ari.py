import pandas as pd
from sklearn.metrics.cluster import adjusted_rand_score

def community_count(option, file):
    df = pd.read_csv(file)
    comm_num = df['community'].nunique()
    print("Number of communities for filtering " + option + " is ", comm_num)

def fileprep(option, file, wfile):
    df = pd.read_csv(file)
    list = []
    for pid in range(1, 301):
        com = df.loc[df['poly_id1'] == pid]['community']
        list.append(com.item())

    wfile.write(option + "; " + str(list) + '\n')

def makelist(line):
    el = line[2:-2].split(",")
    listel = []
    for e in el:
        listel.append(int(e.strip()))
    return listel

def avg_ari_fn(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        line1 = lines[0]  # ground truth line no filtering
        gt_option = line1.split(";")[0]
        gt_list = makelist(line1.split(";")[1])
        for line in lines[1:]:
            line2 = line
            option = line2.split(";")[0]
            list2 = makelist(line2.split(";")[1])
            ari = adjusted_rand_score(gt_list, list2)
            print("ARI between " + gt_option + " and " + option + " is " + str(ari))






def main():
    # path = "/home/olivera/Documents/communities_november08_filtering/"
    # options = ["nofilter", "filter005", "filter001", "filter0001"]
    # wf = open("nov08_filtering_commlist.txt", 'w')
    # for option in options:
    #     filename = path + "communities_nov08_" + option + ".csv"
    #     community_count(option, filename)
    #     fileprep(option, filename, wf)
    #
    # wf.close()

    avg_ari_fn("nov08_filtering_commlist.txt")





if __name__ == '__main__':
    main()