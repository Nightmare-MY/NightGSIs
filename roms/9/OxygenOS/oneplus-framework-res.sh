

LOCALDIR=`cd "$(dirname $0)" && pwd`
apppath=$1

find $apppath/res/ -type f -exec sed -i 's/@android/@*android/g' {} +
sed -i 's/<bool name="config_has_rounded_corner">true/<bool name="config_has_rounded_corner">false/' $apppath/res/values/bools.xml
