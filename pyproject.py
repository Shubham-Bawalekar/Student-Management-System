from tkinter import *
from tkinter.scrolledtext import *
from tkinter.messagebox import *
from sqlite3 import *
import matplotlib.pyplot as plt
import requests
import bs4

#location
try:
	web_address = "https://ipinfo.io/"
	res = requests.get(web_address)
	data = res.json()
	your_city = data['city']
	your_region = data['region']
except Exception as e:
	print("issue", e)

#temperature
try:
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=" + your_city
	a3 = "&appid=c6e315d09197cec231495138183954bd"
	web_add = a1 + a2 + a3
	result = requests.get(web_add)
	datas = result.json()
	main = datas['main']
	temp = main['temp']
except Exception as e:
	print(e)

#quote
try:
	web = "https://www.brainyquote.com/quote_of_the_day"
	resu = requests.get(web)
	data = bs4.BeautifulSoup(resu.text, "html.parser")
	info = data.find('img', {'class':'p-qotd'})
	quote = info['alt']
except Exception as e:
	print("issue ", e)


def f1():
	root.withdraw()
	add_stu.deiconify()

def f2():
	add_stu.withdraw()
	root.deiconify()

def f3():
	root.withdraw()
	view_stu.deiconify()
	view_stu_data.delete(1.0, END)
	con = None
	try:
		con = connect("shubham.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data:
			info = info + "rno = " + str(d[0]) + " name = " + str(d[1]) + " marks = "  + str(d[2]) + "\n"
		view_stu_data.insert(INSERT,info)
	except Exception as e:
		showerror("Issue ", str(e))
	finally:
		if con is not None:
			con.close()


def f4():
	view_stu.withdraw()
	root.deiconify()

def f5():
	con = None
	try:
		con = connect("shubham.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		numbersss = []

		for d in data:
			info = info + "rno = " + str(d[0]) + " name = " + str(d[1]) + " marks = "  + str(d[2])
			numbersss.append(d[0])
		if add_stu_entRno.get() == "":
			showerror("Issue", "Rno cannot be empty.")
		elif add_stu_entName.get() == "":
			showerror("Issue", "Name cannot be empty.")
		elif len(add_stu_entName.get()) < 2:
			showerror("Issue", "Name should contain atleast 2 letters.")
		elif add_stu_entMarks.get() == "":
			showerror("Issue", "Marks cannot be empty.")
		else:
			try:
				if int(add_stu_entRno.get()) > 0:

					if int(add_stu_entRno.get()) not in numbersss:
						rno = int(add_stu_entRno.get())
					else:
						showerror("Issue", "Record already exists.")

				else:
					showerror("Issue", "Rno should be integer greater than 0.")
			except ValueError:
				showerror("Issue", "Rno should be integer greater than 0.")
			name = add_stu_entName.get()
			try:
				if int(add_stu_entMarks.get()) > 0 and int(add_stu_entMarks.get()) < 100:
					marks = int(add_stu_entMarks.get())
				else:
					showerror("Issue", "Marks should be an integer within range of 0 to 100.")
			except ValueError:
				showerror("Issue", "Marks should be an integer within range of 0 to 100.")
			sql = "insert into student values('%d', '%s', '%d')"
			cursor.execute(sql % (rno, name, marks))
			con.commit()
			showinfo("Success", "Record added.")
	except UnboundLocalError:

		con.rollback()
	finally:
		if con is not None:
			con.close()




def f6():
	root.withdraw()
	update_stu.deiconify()

def f7():
	update_stu.withdraw()
	root.deiconify()

def f8():
	con = None
	try:
		con = connect("shubham.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		numberss = []
		for d in data:
			info = info + "rno = " + str(d[0]) + " name = " + str(d[1]) + " marks = "  + str(d[2])
			numberss.append(d[0])
		if update_stu_entRno.get() == "":
			showerror("Issue", "Rno cannot be empty.")
		# elif type(update_stu_entRno.get()) == str:
		# 	showerror("Issue", "Enter correct roll number.")
		elif update_stu_entName.get() == "":
			showerror("Issue", "Name cannot be empty.")
		elif len(update_stu_entName.get()) < 2:
			showerror("Issue", "Name should contain atleast 2 letters.")
		elif update_stu_entMarks.get() == "":
			showerror("Issue", "Marks cannot be empty.")
		else:
			try:
				if int(update_stu_entRno.get()) > 0 and int(update_stu_entRno.get()) in numberss:
					r = int(update_stu_entRno.get())
				else:
					showerror("Issue", "Enter correct rno which you want to update.")
			except ValueError:
				showerror("Issue", "Rno should be integer greater than 0.")
			n = update_stu_entName.get()
			try:
				if int(update_stu_entMarks.get()) > 0 and int(update_stu_entMarks.get()) < 100:
					m = int(update_stu_entMarks.get())
				else:
					showerror("Issue", "Marks should be an integer within range of 0 to 100.")
			except ValueError:
				showerror("Issue", "Marks should be an integer within range of 0 to 100.")
			sql = "update student set name = '%s', marks = '%s' where rno = '%s'"%(n,m,r)
			cursor.execute(sql)
			con.commit()
			showinfo("Success", "Record updated.")
	except UnboundLocalError:

		con.rollback()
	finally:
		if con is not None:
			con.close()

def f9():
	root.withdraw()
	delete_stu.deiconify()

def f10():
	con = None
	try:
		con = connect("shubham.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		number = []

		for d in data:
			info = info + "rno = " + str(d[0]) + " name = " + str(d[1]) + " marks = "  + str(d[2])
			number.append(d[0])
		if delete_stu_entRno.get() == "":
			showerror("Issue", "Rno cannot be empty.")
		else:

			if int(delete_stu_entRno.get()) > 0 and int(delete_stu_entRno.get()) in number:
				r = int(delete_stu_entRno.get())
			else:
				showerror("Issue", "Enter correct rno.")
		sql = "delete from student where rno = '%s'"%(r)
		cursor.execute(sql)
		con.commit()
		showinfo("Success", "Record deleted.")
	except UnboundLocalError:
		pass
	except ValueError:
		showerror("Issue ", "Enter correct roll number.")
		con.rollback()
	finally:
		if con is not None:
			con.close()

def f11():
	delete_stu.withdraw()
	root.deiconify()

def f12():
	con = None
	try:
		con = connect("shubham.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		names = []
		marks = []
		for d in data:
			info = info + "rno = " + str(d[0]) + " name = " + str(d[1]) + " marks = "  + str(d[2])
			# storing all names in a list
			names.append(d[1])
			marks.append(d[2])

		plt.bar(names, marks, color=['red', 'green', 'blue', 'black', 'orange', 'purple', 'grey'])
		plt.title("Batch Information")
		plt.xlabel("Names")
		plt.ylabel("Marks")
		#ax = plt.axes()
		#ax.set_facecolor("#caf0f8")
		plt.show()
		#view_stu_data.insert(INSERT,info)
	except Exception as e:
		showerror("Issue ", str(e))
	finally:
		if con is not None:
			con.close()



root = Tk()
root.title("S.M.S")
root.geometry("600x350+600+180")
root.configure(background='#caffbf')


btnAdd = Button(root, text='Add', width=16, font=('Georgia'), command=f1)
btnView = Button(root, text='View', width=16, font=('Georgia'), command=f3)
btnUpdate = Button(root, text='Update', width=16, font=('Georgia'), command=f6)
btnDelete = Button(root, text='Delete',width=16, font=('Georgia'), command=f9)
btnCharts = Button(root, text='Charts',width=16, font=('Georgia'), command=f12)

location_label = "Location: " + your_city + ", " + your_region + "       Temp: " + str(temp)
my_loc = StringVar()
my_loc.set(location_label)
lblLoc = Label(root, textvariable=my_loc, font=('Georgia'))


my_quote = StringVar()
my_quote.set(quote)

lblQOTD = Label(root, textvariable=my_quote, font=('Georgia', 10))

btnAdd.pack(pady=7)
btnView.pack(pady=7)
btnUpdate.pack(pady=7)
btnDelete.pack(pady=7)
btnCharts.pack(pady=7)
lblLoc.pack()
lblQOTD.pack(pady=7)



add_stu = Toplevel(root)
add_stu.title("Add St.")
add_stu.geometry("300x370+600+180")
add_stu.configure(background='#ade8f4')

add_stu_lblRno = Label(add_stu, text="Enter rno", font=('Georgia'))
add_stu_entRno = Entry(add_stu, bd=5, font=('Georgia'))
add_stu_lblName = Label(add_stu, text="Enter Name", font=('Georgia'))
add_stu_entName = Entry(add_stu, bd=5, font=('Georgia'))
add_stu_lblMarks = Label(add_stu, text="Enter Marks", font=('Georgia'))
add_stu_entMarks = Entry(add_stu, bd=5, font=('Georgia'))
add_stu_btnSave = Button(add_stu, text='Save', width=16, font=('Georgia'), command=f5)
add_stu_btnBack = Button(add_stu, text='Back', width=16, font=('Georgia'), command=f2)

add_stu_lblRno.pack(pady=7)
add_stu_entRno.pack(pady=7)
add_stu_lblName.pack(pady=7)
add_stu_entName.pack(pady=7)
add_stu_lblMarks.pack(pady=7)
add_stu_entMarks.pack(pady=7)
add_stu_btnSave.pack(pady=7)
add_stu_btnBack.pack(pady=7)

add_stu.withdraw()


view_stu = Toplevel(root)
view_stu.title("View St.")
view_stu.geometry("320x270+600+180")
view_stu.configure(background='#ffcad4')

view_stu_data = ScrolledText(view_stu, width=27, height=10, font=('Georgia'))
view_stu_btnBack = Button(view_stu, text='Back', width=16, font=('Georgia'), command=f4)
view_stu_data.pack(pady=7)
view_stu_btnBack.pack(pady=7)

view_stu.withdraw()



update_stu = Toplevel(root)
update_stu.title("Update St.")
update_stu.geometry("300x360+600+180")
update_stu.configure(background='#fff4af')

update_stu_lblRno = Label(update_stu, text="Enter rno", font=('Georgia'))
update_stu_entRno = Entry(update_stu, bd=5, font=('Georgia'))
update_stu_lblName = Label(update_stu, text="Enter Name", font=('Georgia'))
update_stu_entName = Entry(update_stu, bd=5, font=('Georgia'))
update_stu_lblMarks = Label(update_stu, text="Enter Marks", font=('Georgia'))
update_stu_entMarks = Entry(update_stu, bd=5, font=('Georgia'))
update_stu_btnSave = Button(update_stu, text='Save', width=16, font=('Georgia'), command=f8)
update_stu_btnBack = Button(update_stu, text='Back', width=16, font=('Georgia'), command=f7)

update_stu_lblRno.pack(pady=7)
update_stu_entRno.pack(pady=7)
update_stu_lblName.pack(pady=7)
update_stu_entName.pack(pady=7)
update_stu_lblMarks.pack(pady=7)
update_stu_entMarks.pack(pady=7)
update_stu_btnSave.pack(pady=7)
update_stu_btnBack.pack(pady=7)

update_stu.withdraw()

delete_stu = Toplevel(root)
delete_stu.title("Delete St.")
delete_stu.geometry("300x200+600+180")
delete_stu.configure(background='#d0bef2')

delete_stu_lblRno = Label(delete_stu, text="Enter rno", font=('Georgia'))
delete_stu_entRno = Entry(delete_stu, bd=5, font=('Georgia'))
delete_stu_btnSave = Button(delete_stu, text='Save', width=16, font=('Georgia'), command=f10)
delete_stu_btnBack = Button(delete_stu, text='Back', width=16, font=('Georgia'), command=f11)

delete_stu_lblRno.pack(pady=7)
delete_stu_entRno.pack(pady=7)
delete_stu_btnSave.pack(pady=7)
delete_stu_btnBack.pack(pady=7)

delete_stu.withdraw()

root.mainloop()
