## first make .o file
```bash
cc -c libex29.c -o libex29.o
```

## nm to see .o file
```bash
nm libex29.o
```

## make shared library
```bash
# on Linux VM-8-15-ubuntu 4.15.0-159-generic #167-Ubuntu SMP
cc -shared -o libex29.so libex29.o
```

## complie
```bash
cc -Wall -g -DNDEBUG ex29.c -ldl -o ex29
```

## excute
```bash
./ex29 ./libex29.so print_a_message "hello there"
./ex29 ./libex29.so uppercase "hello there"
```