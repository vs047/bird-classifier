# bird-classifier

# Important Points
1-> Please download mysql for accessing this project.If you do not have mysql then you will not be able to access this prject.
2->inside dist folder move the birdlogin folder in the path "C:\ProgramData\MySQL\MySQL Server 8.0\Data".

this project allows the classification of birds on the basis of length and width of various bones.
this project is divided into following segments:-

## 1) GUI for user interface and Database for accessing the UI
### GUI->
1. Tkinter is python in built library for developing GUI applications.
2. It is easy to use and understand since the  content for learning is available online.
3. This is ideal for creating system applications .eg=> Calculator.

### Database->
1. I have used MYSQL wokbench community edition which is a relational database.
2. It is the most basic and commonly used database in the field of development.
3. relational database means the data inside the tables is connected with certain relations.
4. Here i have created a table named as details with the schema described below:-

|ID           |email      |password|
|numeric      |varchar    |varchar |

5. The server is local host.
6. Only basic queries like select,insert into,create table has been used for this project.

#### Connecting the code to the Database
>Pyhon has a module known by the name of mysql.connector which connects sql server with the python editor.
>after establishing the connection ,we can write SQL queries in the code itself to perform the desired tasks.
>then we create console using the same connection.

#### commiting changes into the table
>After executing the queries  in the  code we commit those changes in table using console_name.commit method.

## 2) Working of the classifier
1. here we have to predict the type of bird based on the dimensions given,so it is a classification problem.
2. Before moving towards machine learnig algorithms we have to understand the dataset given.

### 1->Dataset description
* This dataset is taken from kaggle.com having one csv file with dimensions of 420 rows with 12 columns.
* the 12 columns were named as Id,huml,humw,nlnal,ulnaw,feml,femw,tibl,tibw,tarl,tarw,type.
* There are 6 types of birds in the dataset namely Swimming birds,Reptors,Wading birds,Terrestrial birds,Scansorial birds,Singing birds.

