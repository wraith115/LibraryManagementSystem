# Library Management System 

## Note
This code is only meant for a small school project, I wouldn't recommend using this shit, it's bad.

this is a command-line program that allows you to control a database of books.
it allows you to view books and authors, add/remove books, and it has a borrowing system.


## instructions

1- use the data formation in the excel sample to put your books in an excel file.


ثم ادخلها في ملف اكسل, واستخدم نفس الشكل في ملف الاكسل الموجود في هذا المجلد

2-install packages in requirements.txt using `pip install -r requirements.txt`

قم بتنزيل الحزمات الموجودة في ملف
 requirements.txt

استخدم pip


3-run initiater.py  (creates the database file in using sqlite)

قم بتشغيل initiater.py
 (سيقوم بإنشاء قاعدة بيانات باستخدامsql)


4-run extractExcel.py (extracts data from the excel file into the database, make sure that the excel file name is identical to the one in extractExcel.py)

قم بتشغيل extractExcel.py

 ( ينقل المعلومات من ملف الاكسل إلى ملف قاعدة البيانات.تأكد أن اسم ملف الاكسل مطابق للكود)


5-run manipulater.py and control the database.

قم بتشغيل manipulater.py

ثم يصبح بإمكانك التحكم بقاعدة بيانات المكتبة

Note: you can use an sqlite db viewer to view the data.
ملحوظة: استخدام برنامج عارض قاعدات بيانات سيساعدك