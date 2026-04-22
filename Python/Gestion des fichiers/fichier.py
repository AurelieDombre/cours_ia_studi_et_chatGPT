# ints = [1, 5, 8, 12, 42, 67]  # liste suggérée
# fileName = "ints.dat"
#
# try:
#     with open(fileName, "w") as f:
#         f.write(str(ints))
# except Exception as ex:
#     print(f"Exception : {ex}")

# try:
#     my_file = open("ints.dat","r")
#     my_data = my_file.readline()
#     print(my_data)
#     my_binary_file = open("ints.bin","wb")
#     my_binary_file.write(str.encode(my_data))
#     my_binary_file.close()
#     my_file.close()
# except Exception as e:
#     print(e)

ints = [1, 5, 8, 12, 42, 67]  # liste suggérée
fileName = "ints.txt"

try:
    with open(fileName, "w") as f:
        f.write(str(ints))
except Exception as ex:
    print(f"Exception : {ex}")

try:
    with open(fileName, "r") as f:
        intsList = f.readline().replace("[", '')
        intsList = intsList.replace("]", '')
        binaryInts = bytearray(map(int, list(intsList.split(","))))
        with open("ints.dat", 'wb') as fb:
            fb.write(binaryInts)
except Exception as ex:
    print(f"Exception : {ex}")