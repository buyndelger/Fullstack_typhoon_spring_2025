import os
 
if os.path.exists('exaple.txt'):
    size = os.path.getsize('advanced.txt')
    print(size)



    mod_time =os.path.getmtime('advanced.txt')
    print(mod_time)
    os.rename('advanced.txt', 'new_advanced.txt')
    print('renamed')
    os.rename('new_advanced.txt')
    print('renamed')