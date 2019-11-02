import os, sys

print ("\033[1;32mPlease Enter Your Username & Password")

print ("\033[1;32mor please contact +923135409492 ")


print ("\033[1;32mThis script is now not free ")

username = 'igamerpk'      

password = 'XXXxxxXXX'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[1;32mAlready Entered", 

			sys.exit()



		else:

			print "\033[1;32mSorry you Entered Wrong username [?]\033[00m"

			print "Please log in again...!!\n"

			restart()



	else:

		print "\033[1;32mMaaf Masukkan Username Anda salah... [?]\033[00m"

		print "Silahkan segera log-in kembali...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
