# Boot2Root WriteUp 1
## Step 1

We need a shell to run our exploit so we use the first part of `writeup1`.

We can start with the `www-data` reverse shell but its easier if we have a ssh access with `laurie` or `zaz`.

## Step 2

We upload the one of the dirtycow exploit to /tmp folder, compile it and run it.
DirtyCow is quite unstable and not reliable so sometime we have to try multiples implementations.

    $> scp `exploit_code.c` laurie@192.168.56.101:/tmp/
    $> gcc `exploit_code.c`
    $> ./a.out

## Step 3
Done !
