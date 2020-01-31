import os
from sklearn.metrics.cluster import adjusted_rand_score


def test():
    #tralalalala
    c1 = [0, 0, 0, 1, 1, 2, 2, 3]
    c2 = [0, 0, 1, 1, 2, 2, 2, 3]
    c3 = [0, 0, 0, 2, 2, 2, 3, 3]
    #ari = adjusted_rand_score([0, 0, 1, 2], [0, 0, 1, 1])
    ari1 = adjusted_rand_score(c1, c2)
    ari2 = adjusted_rand_score(c1, c3)
    ari3 = adjusted_rand_score(c2, c3)
    print(ari1, ari2, ari3)

def makelist(line):
    el = line[2:-2].split(",")
    listel = []
    for e in el:
        listel.append(int(e.strip()))
    return listel

# Python program to get average of a list
def Average(lst):
    return sum(lst) / len(lst)

def avg_ari_fn(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        line1 = lines[0]  # ground trouth line
        gt_list = makelist(line1.split(";")[1])
        ari_list = []
        for line in lines[1:]:
            line2 = line
            list2 = makelist(line2.split(";")[1])
            ari = adjusted_rand_score(gt_list, list2)
            ari_list.append(ari)

        return Average(ari_list)



def main():
    # curdir = os.getcwd()
    # filenames = open("files/filenames.txt", 'r')
    # wf = open(curdir + "/files/ari_per_month.txt", 'w')
    # wf.write("month,avg_ARI" + '\n')
    # # for each month calculate ari between iterations
    # for fn in filenames:
    #     month = fn[12:18].strip()
    #     file = curdir + "/files/" + month + '.txt'
    #     avg_ari = avg_ari_fn(file)
    #     wf.write(month + ',' + str(avg_ari) + '\n')
    #
    # wf.close()

    curdir = os.getcwd()
    #wf = open(curdir + "/files/ari_between_months.txt", 'w')
    #wf.write("month1,month2,ari" + '\n')
    ari_list = []
    with open("files/all_months.txt", 'r') as fn:
        lines = fn.readlines()
        for i in range(0, 61):
            month1 = lines[i].split(";")[0][:-1]
            list1 = makelist(lines[i].split(";")[1])
            month2 = lines[i+1].split(";")[0][:-1]
            list2 = makelist(lines[i+1].split(";")[1])
            ari = adjusted_rand_score(list1, list2)
            ari_list.append(ari)

    avg_ari = Average(ari_list)
    print("Average ARI between sequential days is ", avg_ari)
            #wf.write(month1 + "," + month2 + "," + str(ari) + '\n')

    #wf.close()



if __name__ == '__main__':
    main()