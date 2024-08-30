import sub
import server


# init
index = 1
server.CleanDir('./resource')

# read subs file
sub_list = sub.get_list()

# process sub
for item in sub_list:

    # download
    print('download:', item)
    content = sub.download(item)

    # process
    print('process:', item)
    server.Write(str(index), content)

    # add index
    index+=1

# unite sub?
if input('Unite File? (y/n)') == 'y':
    server.Unite()

# finish
print('Finish')