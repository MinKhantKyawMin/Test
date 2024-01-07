 from tkinter import*
import Modulemodel
from tkinter import messagebox

class CourseEntry():
    def getCType(self):
        CT=self.rdoCType.get()
        return CT

    def btnSave_Click(self):
        if(self.txtCourseName.get()=="" or self.getCType()=="" or self.txtFGees.get()==""):
            messagebox.showwarning("Program Say","Please Try again after Fill all Record!")
        else:
            bn=Modulemodel.Fun_Select("SELECT CourseName From course WHERE CourseName='"+self.txtCourseName.get()+"';")
            print(bn)
            if(len(bn)>0)
              messagebox.showerror("This program say","This Course Name is Already have.");
              self.txtCourseName.delete(0,END)
              self.Fees.delete(0,END)
              self.rdoCType.Set(None)
              self.txtcourseName.focous()
            else:
                CourseName=self.txtCourseName.get();
                print(CourseName)
                CourseType=self.getCType()
                Fees=self.txtFees.get()
                sql="INSERT INTO course(CourseName,CourseType,Fees)VALUES('"+CourseName+"','"+CourseType+"',"+Fees+");"

                Modulemodel.Fun_Execude(sql)
                messagebox.showinfo("Saving","Successfully Save Record")
                self.txtCourseName.delete(0,END)
                self.txtFees.delete(0,END)
                self.rdoCType.set(None)
                self.txtCourseName.focus()
                
    def __init__(self):
        global rdoCType
        self.rdoCType=StringVar()

        lf=Toplevel()
        lf.title("Course Entry")
        lf.geometry("600x400")

        Label(lf,text="Enter Course Name;").grid(row=0,column=0,pady="0.5c",padx="1c")
        self.txtCourseName=Entry(lf)
        self.txtCourseName["width"]=40
        self.txtCourseName.grid(row=0,column=1,pady="0.5c")
        self.txtCourseName.focus()
        Label(lf,text="Choose Course Type:").grid(row=1,column=0,pady="0.5c",padx="1c")

        frame=Frame(lf)
        frame.grid(row=1,column=1)

        self.ty=Radiobutton(frame,text="Application",variable=self.rdoCType,value="Application",command=self.getCType)
        self.ty.grid(row=0,column=0,pady="0.5c")

        self.ty=Radiobutton(frame,text="Programming",variable=self.rdoCType,value="Programming",command=self.getCType)
        self.ty.grid(row=0,column=1,pady="0.5c")

        self.ty=Radiobutton(frame,text="Networking",variable=self.rdoCType,value="Networking",command=self.getCType)
        self.ty.grid(row=0,column=2,pady="0.5c")
        self.rdoCType.set(None)

        Label(lf,text="Enter Fees:").grid(row=2,column=0,pady="0.5c",padx="1c")
        self.txtFees=Entry(lf)
        self.txtFees["width"]=40
        self.txtFees.grid(row=2,column=1,pady="0.5c")

        self.btnSave=Button(lf,text="Save")
        self.btnSave.grid(row=3,column=1,pady="0.5c",padx="1c",columnspan=2)
        self.btnSave["command"]=self.btnSave_Click

        self.btnSaveButton(lf,text="close")
        self.btnSave.grid(row=3,column=0,pady="0.5c",padx="2.5c)
        
        

        
        
        
        


    
                
                 
