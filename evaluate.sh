id=$1

root=`pwd`
tmp_output="/mnt/d/baiyong/compile_code/output"
case_output=$root/case/test$id


test_root="D:/baiyong/compile_code/evaluate/c0/test$id.txt"
echo $test_root > tmp
"/mnt/d/baiyong/compile_code/compile_tmp/cmake-build-debug/compile_tmp.exe" < tmp > $case_output/log.txt
rm -r tmp

cp $tmp_output/result.asm $root/mips/result$id.asm

cd $case_output

mkdir -p tmp

inputs=$(ls input)

for file in $inputs
do
    java -jar $root/mars_compile.jar $root/mips/result$id.asm < input/$file > tmp/$file
done

python $root/cmp.py --root `pwd`





