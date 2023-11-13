#!/bin/bash

ITERATIONS=100  # 运行次数

for ((i=1; i<=ITERATIONS; i++))
do
    echo "运行第 $i 次排序程序"
    ./sorting $((ITERATIONS*11))  # 替换为您的排序程序的命令或路径
    echo "sort original..."
    ./sort_original $((ITERATIONS*11))
done