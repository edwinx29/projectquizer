from tkinter import *
import tkinter.messagebox as tm
import tkinter as tk
import sqlite3
import db
import os

with sqlite3.connect('quiz.db') as db:
			c = db.cursor()

db.commit()
            
class App(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		#Setup Menu
		#MainMenu(self)
		#Setup Frame
		container = Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F, geometry in zip((StartPage,SignUp, AyoMulai,PageSoal,PageScore,BuatSoal),('230x280','230x280','390x140','600x450','600x400','420x350')):
			context=F.__name__
			frame = F(container, self)
			self.frames[context] = (frame, geometry)
			frame.grid(row=0, column=0, sticky="nsew")
		self.show_frame("StartPage")
        
	def show_frame(self, context):
		frame, geometry = self.frames[context]
		self.update_idletasks()
		self.geometry(geometry)
		frame.tkraise()
	

class StartPage(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		
		c.execute('SELECT * FROM sesi')
		if c.fetchall():
			c.execute('DELETE FROM sesi')
			db.commit()
		
		self.login=Label(self, text="LOGIN")
		self.login.grid(padx=5,pady=5,row=0,column=1,sticky=W)
		self.login.config(font=("Courier", 15))
		self.label_username = Label(self, text="Username")
		self.label_password = Label(self, text="Password")
		self.entry_username = Entry(self)
		self.entry_password = Entry(self, show="*")
		self.label_username.grid(padx=10,pady=10,row=1, sticky=E)
		self.label_password.grid(padx=10,pady=10,row=2, sticky=E)
		self.entry_username.grid(padx=10,pady=10,row=1, column=1)
		self.entry_password.grid(padx=10,pady=10,row=2, column=1)
		self.logbtn = Button(self, text="Log in", bg="light grey",width=15,height=2, command=lambda:self._login_btn_clicked(controller))
		self.logbtn.grid(padx=10,pady=3,columnspan=2)
		self.signbtn = Button(self, text="Sign Up", bg="light grey",width=15,height=2, command=lambda:self._signup_btn_clicked(controller))
		self.signbtn.grid(padx=10,pady=3,columnspan=2)
		self.buatbtn = Button(self, text="Buat Soal", bg="light grey",width=15,height=2, command=lambda:self._buat_btn_clicked(controller))
		self.buatbtn.grid(padx=10,pady=3,columnspan=2)

	def _login_btn_clicked(self,controller):
		username = self.entry_username.get()
		password = self.entry_password.get()
			
		find_user = ('SELECT * FROM users WHERE username = ? and password = ?')
		c.execute(find_user,[(username),(password)])
		result = c.fetchall()
		if result:
			x=""
			for row in result:
				x=row[0]
				tm.showinfo("Login info", "Welcome "+ row[1])
			insert =('Insert Into sesi SELECT username,name,jumlahtes FROM users WHERE username = ?')
			c.execute(insert,[(x)])
			print(x)
			if db.commit:
				db.commit()
				print("OK")
				c.execute('Select * from sesi')
				print(c.fetchall())
			controller.show_frame("AyoMulai")
		else:
			tm.showerror("Login error", "Incorrect username")
			
	def _signup_btn_clicked(self,controller):
			controller.show_frame("SignUp")
	
	def _buat_btn_clicked(self,controller):
			controller.show_frame("BuatSoal")
    
	
class SignUp(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		
		self.login=Label(self, text="SIGN UP")
		self.login.grid(padx=5,pady=5,row=0,column=1,sticky=W)
		self.login.config(font=("Courier", 15))
		self.label_username = Label(self, text="Username")
		self.label_password = Label(self, text="Password")
		self.label_myname = Label(self, text="Full name")
		self.entry_username = Entry(self)
		self.entry_password = Entry(self, show="*")
		self.entry_myname = Entry(self)
		self.label_username.grid(padx=10,pady=10,row=1, sticky=E)
		self.label_password.grid(padx=10,pady=10,row=2, sticky=E)
		self.label_myname.grid(padx=10,pady=10,row=3, sticky=E)
		self.entry_username.grid(padx=10,pady=10,row=1, column=1)
		self.entry_password.grid(padx=10,pady=10,row=2, column=1)
		self.entry_myname.grid(padx=10,pady=10,row=3, column=1)
		self.signbtn = Button(self, text="Create Account", bg="light grey",width=15,height=2, command=lambda:self._signup_btn_clicked(controller))
		self.signbtn.grid(padx=10,pady=3,columnspan=2)
		self.bbtn = Button(self, text="Back", bg="light grey",width=15,height=2, command=lambda:self._back_btn_clicked(controller))
		self.bbtn.grid(padx=10,pady=3,columnspan=2)

	def _signup_btn_clicked(self,controller):

		find_user = ('SELECT * FROM users WHERE username = ?')
		c.execute(find_user,[(self.entry_username.get())])

		if c.fetchall():
			tm.showerror("Sign Up Error", "Username already used")
			#controller.show_frame(PageOne)
		else:
			add_user = ('INSERT INTO users (username, name, password) VALUES (?, ?, ?)')
			c.execute(add_user,[(self.entry_username.get()),(self.entry_myname.get()),(self.entry_password.get())])
			db.commit()
			c.execute("SELECT * from users")
			print(c.fetchall())
			tm.showinfo("Sign Up Info", "Account Created")
			controller.show_frame("StartPage")
	
	def _back_btn_clicked(self,controller):
			controller.show_frame("StartPage")
	

class AyoMulai(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.home(controller)
		
	def home(self,controller):
		
		c.execute('SELECT * FROM soalterpilih')
		if c.fetchall():
			c.execute('DELETE FROM soalterpilih')
			db.commit()
		
		filler=Label(self,bg="white",width=20,height=1, text="")
		filler.grid(row=0,column=0)
		filler=Label(self,bg="white",width=15,height=1, text="QUIZER X")
		filler.config(font=("Courier", 8))
		filler.grid(row=0,column=1)
		filler=Label(self,bg="white",width=2,height=1, text="")
		filler.grid(row=0,column=2)
		filler=Label(self,bg="white",width=15,height=1, text="")
		filler.grid(row=0,column=3)
		filler=Label(self,bg="white",width=20,height=1, text="")
		filler.grid(row=1,column=0)
		filler=Label(self,bg="white",width=15,height=1, text="")
		filler.grid(row=1,column=1)
		filler=Label(self,bg="white",width=2,height=1, text="")
		filler.grid(row=1,column=2)
		filler=Label(self,bg="white",width=15,height=1, text="")
		filler.grid(row=1,column=3)
		la=Label(self, text="Mata Pelajaran")
		la.grid(row=2,column=0)
		lb=Label(self, text="Tingkat Kesulitan")
		lb.grid(row=3,column=0)
		opt =["Matematika","IPA","BI"]
		dfc =["Mudah","Lumayan","Sulit"]
		self.drop1= StringVar()
		self.drop1.set("Matematika")
		self.drop2= StringVar()
		self.drop2.set("Mudah")
		e1 = tk.OptionMenu(self,self.drop1,*opt)
		e1.grid(row=2, column=1)
		e2 = tk.OptionMenu(self,self.drop2,*dfc)
		e2.grid(row=3, column=1)
		la=Label(self, text="",width=2)
		la.grid(row=2,column=2)
		la=Label(self, text="",width=2)
		la.grid(row=3,column=2)
		b1=Button(self,text="Start", bg="light grey", width=12,height=2,command=lambda:self._mulai_btn_clicked(controller))
		b1.grid(row=2,column=3)
		b1=Button(self,text="Score", bg="light grey", width=12,height=2,command=lambda:self._score_btn_clicked(controller))
		b1.grid(row=3,column=3)
		
	def _mulai_btn_clicked(self,controller):
		matpel=self.drop1.get()
		diff=self.drop2.get()
		diffrate = 0
		if diff=='Mudah':
			self.diffrate=1
		elif diff=='Lumayan':
			self.diffrate=2
		else :
			self.diffrate=3
		
		find_soal = ('Insert Into soalterpilih SELECT * FROM soal WHERE matpel = ? and tingkat_kesulitan = ? ORDER BY RANDOM() LIMIT 5')
		c.execute(find_soal,[(matpel),(self.diffrate)])
		db.commit()
		#c.execute('SELECT * FROM soalterpilih')
		#print(c.fetchall())
		controller.show_frame("PageSoal")
	
	def _score_btn_clicked(self,controller):
		controller.show_frame("PageScore")
		
class PageSoal(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		#self.frame=Frame(self)
		self.nilai = 0
		self.timer = 15
		self.timer_id = 0
		self.init(controller)
	
	def init(self,controller):
		self.label= tk.Label(self, text="",width=15)	
		self.label.grid(padx=10,pady=10,row=0,column=0, sticky=W)
		self.start = Button(self, text="Mari Kita Mulai !!", bg="light grey",width=40, height=4,command=lambda:self.started(controller))
		self.start.grid(padx=10,pady=10,row=0,column=1,columnspan=2,sticky=W+E)


	def started(self,controller):
		self.start.destroy()
			
		c.execute('SELECT * FROM soalterpilih')
		#print(c.fetchall())
		row = c.fetchone()
		rows=1
		i=0
		self.lbl=[]
		self.soal=[]
		self.val=[]
		self.timer=15
		self.diff=IntVar()
		self.matpel=StringVar()
		self.value=IntVar()
		self.cur=StringVar()
		self.var=tk.IntVar()
		self.var.set(5)
		self.labelscore= tk.Label(self,bg="white", text="Score= %s"%self.nilai,width=10)	
		self.labelscore.grid(padx=10,pady=10,row=0,column=0, sticky=W)
		self.labelscore.config(font=("Courier", 12))
		self.labeltimer= tk.Label(self,bg="white", text="Timer : %s"%self.timer,width=10)	
		self.labeltimer.grid(padx=200,pady=10,row=0,column=0, sticky=W)
		self.labeltimer.config(font=("Courier", 12))
		self.lbl.append(self.labelscore)
		self.lbl.append(self.labeltimer)
		self.countdown(controller)
		if row:
			self.cur.set(row[2])
			self.matpel.set(row[1])
			self.diff.set(row[3])
			self.label_soal = tk.Label(self, text="%s"%row[2],wraplength=550)
			self.label_soal.grid(padx=10,pady=10,row=rows,column=0, sticky="W")
			rows+=1
			find_pilihan = ('SELECT * FROM pilihan WHERE id_soal = ? ORDER by RANDOM()')
			c.execute(find_pilihan,[(row[0])])
			res = c.fetchall()
			for roww in res:
				lebar=20
				print(roww[1],roww[2])
				if len(roww[1])>20:
					self.pilihan= Radiobutton(self, text="%s"%roww[1], indicatoron =0, variable =self.var,command=self.cek, value=roww[2], bg="light grey",wraplength=300)
				else:
					self.pilihan= Radiobutton(self, text="%s"%roww[1], indicatoron =0, variable =self.var,command=self.cek, value=roww[2],width=lebar,height=2, bg="light grey")
				self.pilihan.grid(padx=10,pady=3,row=rows,column=0,sticky="W")
				self.val.append(self.pilihan)
				#print(var.get())
				rows+=1
			i+=1
			self.soal.append(self.label_soal)
			self.lbl.append(self.label)
		
		self.logbtn=Button(self, text="Submit Jawaban", bg="light grey",height=2, command=lambda:self._cek_btn_clicked(controller))
		self.logbtn.grid(padx=10,pady=10,row=rows,column=0,columnspan=2,sticky="W")
		#self.update_timer(controller)
		#self.logbtn = Button(self, text="Log in", command=lambda:self._cek_btn_clicked(controller))
		#self.logbtn.grid(padx=10,pady=10,columnspan=2)
		
			
	def update_timer(self,controller):
		#self.tick=500
		if self.timer!=0:
			self.timer-=1
		self.timeString=self.pattern.format(self.timer)
		self.timeText.configure(text=self.timeString)
		if self.timer==0:
			self.after(self.tick,self._cek_btn_clicked,controller)
		else:
			self.after(self.tick,self.update_timer,controller)
		
	def cek(self,event=None):
		self.value.set(self.var.get())
			
	def _cek_btn_clicked(self,controller):
		controller.after_cancel(self.timer_id)
		self.timer = 15
		diff=0
		cekk=self.value.get()
		query=('DELETE FROM soalterpilih WHERE soal=?')
		c.execute(query,[(self.cur.get())])
		db.commit()
		
		for widget in self.lbl:
			widget.destroy()
		for widget in self.soal:
			widget.destroy()
		for widget in self.val:
			widget.destroy()
		self.logbtn.destroy()
		
		if cekk==1:
			self.nilai+=2
		
		c.execute('SELECT * from soalterpilih')
		if c.fetchone():
			"""self.tick*=2
			if self.tick>2000:
				self.tick=500"""
			self.started(controller)
		else:
			teske=0
			user=""
			print(str(self.nilai))
			with sqlite3.connect('quiz.db') as dd:
				x = dd.cursor()
			x.execute('SELECT username,jumlahtes from sesi')
			row=x.fetchone()
			user=row[0]
			teske=row[1]+1
			diff=self.diff.get()
			matpel=self.matpel.get()
			print(teske,user,diff)
			query=('Insert into list_Nilai values(?,?,?,?,?)')
			x.execute(query,[(user),(teske),(matpel),(self.nilai),(diff)])
			#if self.ctr==0:
			dd.commit()
			query2=('Update users Set jumlahtes=? Where username=?')
			query3=('Update sesi Set jumlahtes=? Where username=?')
			x.execute(query2,[(teske),(user)])
			dd.commit()
			x.execute(query3,[(teske),(user)])
			dd.commit()
			#	self.ctr+=1
			self.nilai=0
			self.init(controller)
			nilai=StringVar()
			nilai.set(str(self.nilai))
			tm.showinfo("Nilai Akhir", "Nilai Akhir Anda : "+ nilai.get())
			#self.timer=15
			controller.show_frame("AyoMulai")
	
	def countdown(self, controller):
		self.timer= self.timer - 1
		#print(self.timer)
		if(self.timer>0):
			self.labeltimer.config(text=self.timer)
			print(self.timer)
			self.timer_id = controller.after(1000, self.countdown, controller)
		else:
			controller.after_cancel(self.timer_id)
			self.timer = 15
			diff=0
			cekk=self.value.get()
			query=('DELETE FROM soalterpilih WHERE soal=?')
			c.execute(query,[(self.cur.get())])
			db.commit()
			
			for widget in self.lbl:
				widget.destroy()
			for widget in self.soal:
				widget.destroy()
			for widget in self.val:
				widget.destroy()
			self.logbtn.destroy()
			
			if cekk==1:
				self.nilai+=2
			
			c.execute('SELECT * from soalterpilih')
			if c.fetchone():
				self.started(controller)
			else:
				teske=0
				user=""
				nilai=StringVar()
				nilai.set(str(self.nilai))
				print(self.nilai)
				with sqlite3.connect('quiz.db') as dd:
					x = dd.cursor()
				x.execute('SELECT username,jumlahtes from sesi')
				row=x.fetchone()
				user=row[0]
				teske=row[1]+1
				diff=self.diff.get()
				matpel=self.matpel.get()
				print(teske,user,diff)
				query=('Insert into list_Nilai values(?,?,?,?,?)')
				x.execute(query,[(user),(teske),(matpel),(self.nilai),(diff)])
				dd.commit()
				query2=('Update users Set jumlahtes=? Where username=?')
				query3=('Update sesi Set jumlahtes=? Where username=?')
				x.execute(query2,[(teske),(user)])
				dd.commit()
				x.execute(query3,[(teske),(user)])
				dd.commit()
				self.nilai=0
				tm.showinfo("Nilai Akhir", "Nilai Akhir Anda : "+ nilai.get())
				self.init(controller)
				controller.show_frame("AyoMulai")
            
			
class PageScore(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.show_score(controller)
		
	def show_score(self,controller):
		user=""
		with sqlite3.connect('quiz.db') as dd:
				x = dd.cursor()
		x.execute('SELECT username,jumlahtes from sesi')
		row=x.fetchone()
		if row:
			print(row[0])
			user=row[0]
		rows=2
		self.labels=[]
		self.a=Label(self,bg="white",text="Daftar 5 Nilai Tes Terakhir",height=2)
		self.a.grid(padx=10,pady=10,row=0,column=1,sticky=E)
		self.label_username = Label(self,bg="white", text="Username")
		self.label_teske = Label(self,bg="white", text="Tes ke")
		self.label_matpel = Label(self,bg="white", text="Mata Pelajaran")
		self.label_nilai = Label(self,bg="white", text="Nilai")
		self.label_tingkat = Label(self,bg="white", text="Level Kesulitan")
		self.label_username.grid(padx=10,pady=10,row=1,column=0,sticky=E)
		self.label_teske.grid(padx=10,pady=10,row=1,column=1,sticky=E)
		self.label_matpel.grid(padx=10,pady=10,row=1,column=2,sticky=E)
		self.label_nilai.grid(padx=10,pady=10,row=1,column=3,sticky=E)
		self.label_tingkat.grid(padx=10,pady=10,row=1,column=4,sticky=E)
		query2=('SELECT * FROM list_Nilai Where username=? ORDER BY teske DESC LIMIT 5')
		c.execute(query2,[(user)])
		res=c.fetchall()
		for row in res:
			x=StringVar()
			x.set(row[1])
			self.label_username = Label(self, text="%s"%row[0])
			self.label_teske = Label(self, text="%s"%row[1])
			self.label_matpel = Label(self, text="%s"%row[2])
			self.label_nilai = Label(self, text="%s"%row[3])
			self.label_tingkat = Label(self, text="%s"%row[4])
			self.label_username.grid(padx=10,pady=10,row=rows,column=0,sticky=E)
			self.label_teske.grid(padx=10,pady=10,row=rows,column=1,sticky=E)
			self.label_matpel.grid(padx=10,pady=10,row=rows,column=2,sticky=E)
			self.label_nilai.grid(padx=10,pady=10,row=rows,column=3,sticky=E)
			self.label_tingkat.grid(padx=10,pady=10,row=rows,column=4,sticky=E)
			rows+=1
			self.labels.append(self.label_username)
			self.labels.append(self.label_teske)
			self.labels.append(self.label_matpel)
			self.labels.append(self.label_nilai)
			self.labels.append(self.label_tingkat)
		self.bckbtn = Button(self, text="Back", bg="light grey",height=2,width=10, command=lambda:self._back_btn_clicked(controller))
		self.bckbtn.grid(padx=10,pady=10,columnspan=2)
		
	def _back_btn_clicked(self,controller):
		for widget in self.labels:
			widget.destroy()
		self.bckbtn.destroy()
		self.show_score(controller)
		controller.show_frame("AyoMulai")

class BuatSoal(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.home(controller)
		
	def home(self,controller):
		
		intro=Label(self,bg="white", text="Buat Soal",width=20,height=2)
		intro.grid(row=0,column=0, sticky=W)
		intro=Label(self,bg="white", text="",width=20,height=2)
		intro.grid(row=0,column=1, sticky=W)
		intro=Label(self,bg="white", text="",width=20,height=2)
		intro.grid(row=0,column=2, sticky=W)
		la=Label(self, text="Mata Pelajaran")
		la.grid(padx=10,pady=10,row=1,column=0, sticky=W)
		lb=Label(self, text="Tingkat Kesulitan")
		lb.grid(padx=10,pady=10,row=2,column=0, sticky=W)
		opt =["Matematika","IPA","BI"]
		dfc =["Mudah","Lumayan","Sulit"]
		self.drop1= StringVar()
		self.drop1.set("Matematika")
		self.drop2= StringVar()
		self.drop2.set("Mudah")
		e1 = tk.OptionMenu(self,self.drop1,*opt)
		e1.grid(row=1, column=1)
		e2 = tk.OptionMenu(self,self.drop2,*dfc)
		e2.grid(row=2, column=1)
		self.labelsoal = Label(self, text="Soal")
		self.labelbenar = Label(self, text="Jawaban Benar")
		self.soal = Entry(self)
		self.benar = Entry(self)
		self.labelsoal.grid(padx=10,pady=10,row=3, sticky=W)
		self.labelbenar.grid(padx=10,pady=10,row=4, sticky=W)
		self.soal.grid(padx=10,pady=10,row=3, column=1)
		self.benar.grid(padx=10,pady=10,row=4, column=1)
		
		self.labelsalah1 = Label(self, text="Jawaban Salah 1")
		self.salah1 = Entry(self)
		self.labelsalah2 = Label(self, text="Jawaban Salah 2")
		self.salah2 = Entry(self)
		self.labelsalah3 = Label(self, text="Jawaban Salah 3")
		self.salah3 = Entry(self)
		self.labelsalah1.grid(padx=10,pady=10,row=5, sticky=W)
		self.salah1.grid(padx=10,pady=10,row=5, column=1)
		self.labelsalah2.grid(padx=10,pady=10,row=6, sticky=W)
		self.salah2.grid(padx=10,pady=10,row=6, column=1)
		self.labelsalah3.grid(padx=10,pady=10,row=7, sticky=W)
		self.salah3.grid(padx=10,pady=10,row=7, column=1)
		
		b1=Button(self,text="Buat", bg="light grey", width=12,height=2, command=lambda:self._buat_btn_clicked(controller))
		b1.grid(row=5,column=2)
		b1=Button(self,text="Back", bg="light grey", width=12,height=2, command=lambda:self._back_btn_clicked(controller))
		b1.grid(row=6,column=2)
		
	def _buat_btn_clicked(self,controller):
		id=0
		matpel=self.drop1.get()
		diff=self.drop2.get()
		self.diffrate = 0
		if diff=='Mudah':
			self.diffrate=1
		elif diff=='Lumayan':
			self.diffrate=2
		else :
			self.diffrate=3
		soal=self.soal.get()
		benar=self.benar.get()
		salah1=self.salah1.get()
		salah2=self.salah2.get()
		salah3=self.salah3.get()
		
		insert_soal = ('Insert Into soal (matpel,soal,tingkat_kesulitan) VALUES(?,?,?)')
		c.execute(insert_soal,[(matpel),(soal),(self.diffrate)])
		db.commit()
		
		select_id=('SELECT * from soal WHERE soal=?')
		c.execute(select_id,[(soal)])
		row=c.fetchone()
		if row:
			print("A")
			id=row[0]
		
		insert_pilihan1 = ('Insert Into pilihan (id_soal, pilihan, value) VALUES(?,?,?)')
		c.execute(insert_pilihan1,[(id),(benar),(1)])
		db.commit()
		
		insert_pilihan2 = ('Insert Into pilihan (id_soal, pilihan, value) VALUES(?,?,?)')
		c.execute(insert_pilihan2,[(id),(salah1),(2)])
		db.commit()
		
		insert_pilihan3 = ('Insert Into pilihan (id_soal, pilihan, value) VALUES(?,?,?)')
		c.execute(insert_pilihan3,[(id),(salah2),(3)])
		db.commit()
		
		insert_pilihan4 = ('Insert Into pilihan (id_soal, pilihan, value) VALUES(?,?,?)')
		c.execute(insert_pilihan4,[(id),(salah3),(4)])
		db.commit()
		
		#c.execute('SELECT * FROM soalterpilih')
		#print(c.fetchall())
		controller.show_frame("StartPage")
	
	def _back_btn_clicked(self,controller):
		controller.show_frame("StartPage")

app = App()
app.mainloop()