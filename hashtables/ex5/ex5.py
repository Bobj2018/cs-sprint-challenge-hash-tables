# Your code here



def finder(files, queries):
    hash_table = {}


    #hash files by storing the characters after the hash
    for i in files:
        curr_char = len(i) - 1

        while i[curr_char - 1] != "/":
            curr_char -= 1

        if i[curr_char:len(i)] in hash_table:
            hash_table[i[curr_char:len(i)]].append(i)
        else:
            hash_table[i[curr_char:len(i)]] = [i]



    #loops through queries and append to result if exists

    result = []
    for i in queries:
        if i in hash_table:
            for j in hash_table[i]:
                    result.append(j)


    return result


if __name__ == "__main__":
    files = [
    "/usr/local/share/foo.txt",
    "/usr/bin/ls",
    "/home/davidlightman/foo.txt",
    "/bin/su"
]

    queries = [
    "ls",
    "foo.txt",
    "nosuchfile.txt"
]
    print(finder(files, queries))
