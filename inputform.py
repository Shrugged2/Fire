from tkinter import *
fields = ('Property Name', 'Address', 'City', 'State', 'Zipcode', 'Smoking Habits',
    'Year Built', 'Sprinklers', 'Suppression', 'Electrical', 'Construction',
    'Fire Alarm/Smoke Detectors', 'Per Capita Income', 'Square Feet', 'Annual Rent Income',
    'Habitational Stories', 'Rentable Square Feet', 'Max Square Feet between Structures')

def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text))

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=25, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

if __name__ == '__main__':
   root = Tk()
   root.title("Give Me All Your Data")
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))
   b1 = Button(root, text='Run',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
