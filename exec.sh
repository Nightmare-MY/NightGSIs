#export CURPRO=/storage/emulated/0/MTOOLKIT/Rom/GSI测试
export PATH=/data/data/com.termux/files/usr/bin/:$PATH
#./url2GSI.sh miui_MI8_20.5.14_8988f38447_10.0.zip miui
cd $(dirname $0)
./make.sh ./system MIUI AB ./output