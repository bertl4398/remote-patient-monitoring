#!/usr/bin/env python3

import os
import fs
from fs import open_fs
import gnupg

gpg = gnupg.GPG(gnupghome="/home/benjamin/.gnupg")
home_fs = open_fs(".")

if os.path.exists("encrypted/"):
    print("Encrypt directory exists")
else:
    home_fs.makedir(u"encrypted")
    print("Created encrypted directory")

files_dir = []

files = [f for f in os.listdir(".") if os.path.isfile(f)]
for f in files:
    files_dir.append(f)

print(files_dir)

for x in files_dir:
    with open(x, "rb") as f:
        status = gpg.encrypt_file(f,recipients=["doctor@test.org"],output= files_dir[files_dir.index(x)]+".gpg")
        print("ok: ", status.ok)
        print("status: ", status.status)
        print("stderr: ", status.stderr)
        os.rename(files_dir[files_dir.index(x)] + ".gpg", "encrypted/" +files_dir[files_dir.index(x)] + ".gpg")

files_dir = []
files_dir_clean = []

if os.path.exists("decrypted/"):
    print("Decrypted directory already exists")
else:
    home_fs.makedir(u"decrypted/")
    print("Created decrypted directory")

files = [f for f in os.listdir(".") if os.path.isfile(f)]
for f in files:
    files_dir.append(f)
