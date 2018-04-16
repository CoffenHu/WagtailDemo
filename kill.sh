for i in `ps -ef|grep mysite.wsgi|grep -v grep|awk '{print $2}'`
do
kill -9 $i
done
