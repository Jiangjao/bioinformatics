# !/usr/bin/python3
# <!--encoding=utf-8-->
from time import sleep
# thus read it into mysql and then output it into fasta-ref



def transformEMblToFasta(line_descr,line_block):
    try:
        line = True
        print("---")
        while line:
            line = inputfile.readline()
            # print(line.find("Sequence"))
            if line.find("ID") == 0:
                pre = line.split(' ')[3]
                line_descr.append(pre)
                # sleep(0.000001)
            elif line.find("Sequence") == 2:
                
                line_descr.append(line)

                # if len(line_descr) >= 2:
                #     block_begin =  ' '.join(i for i in line_descr) 
                block_begin = "> " + ' '.join(i for i in line_descr)
                line_descr = []
                print(block_begin,file=outputfile)
                # sleep(0.00001)
                # line_block = []
            else:
                line_code = line.lstrip(' ')
                if line_code == r"//":
                    continue            
                # sleep(0.00001)   
                print(line_code,file=outputfile)
        # sleep(0.00001)
    except Exception as error:
        print(error)


if __name__ == "__main__":
    print("waiting")
    line_descr = []
    line_block = []
    inputfile = open("../notes/RMRBSeqs.embl",'r', encoding='utf-8')
    outputfile = open("test2",'w+', encoding='utf-8')
    transformEMblToFasta(line_descr,line_block)
    print("finishing")
    