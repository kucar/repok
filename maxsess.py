import subprocess
import re
from Tkinter import *
version=1.0
command1="snmpwalk -v 2c -c public "
command2=" iso.3.6.1.2.1.6.13.1.1 "

class TKclass:
   def __init__(self,parent):
      print "Welcome to GOOMS (Get Out Of My Switch) version %d" %version
      self.myParent =parent
      self.master=Frame(parent,width=500,height=500)
      self.master.pack(side=TOP,padx=100,pady=10)
      self.l = Label(self.master,text="Tell me Which Switch(ip?):")
      self.l.pack()
      self.e = Entry(self.master)
      self.e.pack()
      self.b = Button(self.master, text="Kick'em all", width=10, command=self.callback)
      self.b.pack()
      self.b2=Button(self.master,text="Quit",width=10,command=root.destroy)
      self.b2.pack()

   def callback(self):
       self.ip=self.e.get()
       self.snmpegetf()
   def snmpegetf(self):
      snempiset=[]  #command array
      counter=0
    #ip=str(raw_input("ip:?"))

      snempiget=command1+self.ip+command2
      print snempiget
      procget = subprocess.Popen(snempiget, \
                  shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

      for line in procget.stdout:
         if line.find('established') !=-1:
            print "found established connection"
            linesplit     =line.split(':')
            commandsetfull=linesplit[2].split()
            snempiset.append("snmpset -v 2c -c public " +self.ip+" "+commandsetfull[0]+" i 12")  #append to command list
            print snempiset[counter]
            counter+=1
         else:
             print "no established connection, counter :", counter
             """ procset = subprocess.Popen(snempiset, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)"""
             """for line in procset.stdout:
                print line"""
      print ( "found %d active connections"  %len(snempiset))
      self.snmpsetf(snempiset)
   def snmpsetf(self,commandlist):
      print "list length is : ", len(commandlist)
      for cmd in commandlist:
         procset = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
         for line in procset.stdout:
                print line
root=Tk()
root.title("    GOOMS   ")
app=TKclass(root)
root.mainloop()
print "Finished job"
