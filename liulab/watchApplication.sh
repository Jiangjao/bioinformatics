#! /bin/sh
while true;
do
        server=`ps aux | grep 进程名称| grep -v grep`
        if [ ! "$server" ]; then
            # 执行的语句
           nohup /usr/bin/php /test.php &
        fi
        sleep 5
done

# ########## source from ############
# https://junyiseo.com/linux/1032.html