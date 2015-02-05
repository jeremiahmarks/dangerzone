=================================================
==
==  Flags of note
==
==================================================

-n, --dry-run               show what would have been transferred
-u, --update                update only (don't overwrite newer files)
-z, --compress              compress file data
-r, --recursive             recurse into directories
-e, --rsh=COMMAND           specify rsh replacement
-P                          equivalent to --partial --progress

=================================================
==
==  rsync examples
==
==================================================

rsync -rzun -e "ssh" --progress 192.168.1.135:/home/jlmarks/jlmarks.org ~/jlmarks.org
    connects to lrm and syncs the jlmarks.org folders
    also, due to the --progress flag it updates me as it transfers each file.

rsync -iurtP /home/jlmarks/rem/gd/html /home/jlmarks/mycode/mysite
     -i turns on the itemized format, which shows more information than the default format
     -u makes rsync transfer skip files which are newer in dest than in src
     -r, --recursive             recurse into directories
     -t, --times                 preserve times
     -P                          equivalent to --partial --progress


rsync -abviuzP src/ dest/
     -i turns on the itemized format, which shows more information than the default format
     -b makes rsync backup files that exist in both folders, appending ~ to the old file. You can control this suffix with --suffix .suf
     -u makes rsync transfer skip files which are newer in dest than in src
     -z turns on compression, which is useful when transferring easily-compressible files over slow links
     -P turns on --partial and --progress
     --partial makes rsync keep partially transferred files if the transfer is interrupted
     --progress shows a progress bar for each transfer, useful if you transfer big files

=================================================
==
==  Flags
==
==================================================



 -v, --verbose               increase verbosity
 -q, --quiet                 decrease verbosity
 -c, --checksum              always checksum
 -a, --archive               archive mode
 -r, --recursive             recurse into directories
 -R, --relative              use relative path names
 -b, --backup                make backups (default ~ suffix)
     --backup-dir            make backups into this directory
     --suffix=SUFFIX         override backup suffix
 -u, --update                update only (don't overwrite newer files)
 -l, --links                 copy symlinks as symlinks
 -L, --copy-links            copy the referent of symlinks
     --copy-unsafe-links     copy links outside the source tree
     --safe-links            ignore links outside the destination tree
 -H, --hard-links            preserve hard links
 -p, --perms                 preserve permissions
 -o, --owner                 preserve owner (root only)
 -g, --group                 preserve group
 -D, --devices               preserve devices (root only)
 -t, --times                 preserve times
 -S, --sparse                handle sparse files efficiently
 -n, --dry-run               show what would have been transferred
 -W, --whole-file            copy whole files, no incremental checks
     --no-whole-file         turn off --whole-file
 -x, --one-file-system       don't cross filesystem boundaries
 -B, --block-size=SIZE       checksum blocking size (default 700)
 -e, --rsh=COMMAND           specify rsh replacement
     --rsync-path=PATH       specify path to rsync on the remote machine
 -C, --cvs-exclude           auto ignore files in the same way CVS does
     --existing              only update files that already exist
     --ignore-existing       ignore files that already exist on the receiving side
     --delete                delete files that don't exist on the sending side
     --delete-excluded       also delete excluded files on the receiving side
     --delete-after          delete after transferring, not before
     --ignore-errors         delete even if there are IO errors
     --max-delete=NUM        don't delete more than NUM files
     --partial               keep partially transferred files
     --force                 force deletion of directories even if not empty
     --numeric-ids           don't map uid/gid values by user/group name
     --timeout=TIME          set IO timeout in seconds
 -I, --ignore-times          don't exclude files that match length and time
     --size-only             only use file size when determining if a file should be transferred
     --modify-window=NUM     Timestamp window (seconds) for file match (default=0)
 -T  --temp-dir=DIR          create temporary files in directory DIR
     --compare-dest=DIR      also compare destination files relative to DIR
 -P                          equivalent to --partial --progress
 -z, --compress              compress file data
     --exclude=PATTERN       exclude files matching PATTERN
     --exclude-from=FILE     exclude patterns listed in FILE
     --include=PATTERN       don't exclude files matching PATTERN
     --include-from=FILE     don't exclude patterns listed in FILE
     --version               print version number
     --daemon                run as a rsync daemon
     --no-detach             do not detach from the parent
     --address=ADDRESS       bind to the specified address
     --config=FILE           specify alternate rsyncd.conf file
     --port=PORT             specify alternate rsyncd port number
     --blocking-io           use blocking IO for the remote shell
     --no-blocking-io        turn off --blocking-io
     --stats                 give some file transfer stats
     --progress              show progress during transfer
     --log-format=FORMAT     log file transfers using specified format
     --password-file=FILE    get password from FILE
     --bwlimit=KBPS          limit I/O bandwidth, KBytes per second
     --read-batch=PREFIX     read batch fileset starting with PREFIX
     --write-batch=PREFIX    write batch fileset starting with PREFIX
 -h, --help                  show this help screen
