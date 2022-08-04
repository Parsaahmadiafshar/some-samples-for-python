import socket
print('1.sendig request via domain')
print('2.sendig request via IP & port')
print('========================================')
num1 = int(input('please choose number 1 or 2 ====>> '))
num2 = int(input('please Enter the request count'))
if num1 == 1:
   url = input('so now Enter your favorite Url ====>> ')
   ip = socket.gethostbyname(url)
   UDP_PORT = 80


   for i in range(1, num2+1):
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tcp connection
       s.connect((ip, UDP_PORT))
       print(f'succsessfully sent the request {i}')

   print('the process has succsessfully Done ')
   s.close()
if num1 == 2:
    ip1 = input('Enter ip ====> ')
    port1 = int(input('Enter port number ====>> '))


    for j in range(1, num2 + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tcp connection
        s.connect((ip1, port1))
        print(f'succsessfully sent the request {j}')

    print('the process has succsessfully Done ')
    s.close()
