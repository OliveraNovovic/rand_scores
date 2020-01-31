

#communities_dec04
newfile = "filenames2.txt"
with open(newfile, 'w') as wf:
    #november
    for i in range(1, 31):
        if (i<10):
            wf.write("communities_nov0" + str(i) + "_v1.csv" + '\n')
        else:
            wf.write("communities_nov" + str(i) + "_v1.csv" + '\n')
    #december
    for i in range(1, 32):
        if (i<10):
            wf.write("communities_dec0" + str(i) + "_v1.csv" + '\n')
        else:
            wf.write("communities_dec" + str(i) + "_v1.csv" + '\n')
    #january
    wf.write("communities_jan01_v1.csv")
