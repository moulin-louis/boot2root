# Boot2Root WriteUp 1
## Step 1

We need a shell to run our exploit so we use the first part of `writeup1`.

We can start when we have the `www-data` reverse shell but its easier whit user `zaz` cause we have an ssh access.

## Step 2

We upload the one of the dirtycow exploit to /tmp folder, compile it and run it.
DirtyCow is quite a unstable, not reliable exploit so sometime we have to try multiple implementation.

    $> scp `exploit_code.c` laurie@192.168.56.101:/tmp/
    $> gcc `exploit_code.c`
    $> ./a.out


## Step 3
Done !
