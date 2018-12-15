import argparse
from os.path import join,basename
from glob import glob

parser = argparse.ArgumentParser()
parser.add_argument('--root',default='/mnt/d/baiyong/compile_code/evaluate/case/test1')
args = parser.parse_args()

root = args.root
output = join(args.root,'output')

files = glob(join(root,'tmp/*.txt'))

for file in files:
    with open(file,'r') as f:
        myout = f.readlines()
    myout = map(lambda line:line.rstrip('\r\n'),myout)
    myout = myout[1:]
    myout = filter(lambda line:line!='',myout)

    with open(join(output,basename(file)),'r') as f:
        standard = f.readlines()
    standard = map(lambda line:line.rstrip('\r\n'),standard)
    standard = filter(lambda line:line!='',standard)

    try:
        assert len(myout)==len(standard)
    except:
        #from IPython import embed
        #embed()
        print('ERROR',file,'too much or too few')

    for i in range(len(myout)):
        if myout[i].strip()!=standard[i].strip():
            #from IPython import embed
            #embed()
            print ('ERROR:',file,myout[i],standard[i])
            break

print ('Finished',basename(root))
