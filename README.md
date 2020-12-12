# bird-classifier

** Note-> Special thanks to @ theonlyjohnny for guiding me how to live host a database and the website 

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
* In these columns the number of non null values are 419.000000,419.000000,417.000000,418.000000,418.000000,419.000000,418.000000,419.000000,419.000000,419.000000 respectively.
* Since the number of null values is very less so dropping of such rows is performed.
* So the number of rows reduces to 413.

### 2->finding  out dependent and independent variables
* The main objective of this project is to identify the type of bird based on dimensions of bones.
* So dependent variable is type while huml,humw,nlnal,ulnaw,feml,femw,tibl,tibw,tarl,tarw are dependent variables.

### 3->Splitting data into test and train data
* Here I  have split data into test and train data.
* The data which is used to generate the model is called train data and the data  which is udes to test the model is called test data.
* The ratio of test to train data is 25:75.Random sampling is not performed.

### 4->Feature Scaling using StandardScaler
* Feature scaling means that the value of features are scaled according to certain crietrion depending upon the the type of algorithm used.
* In this case I have used Standard Scaler.
* In standard Scaler we use normalized value given by the nirmal distribuion i.e (x-u)/sigma

### 5->Applying suitable machine learning Algorithm
1. Logistic Regression
* train data accuracy:90.93851132686084%
* test data accuracy:90.38461538461539%

2. SVC algorithm
* train data accuracy:96.44012944983819%
* test data accuracy:92.30769230769231%

3. KNN algorithm
* train data accuracy:100%
* test data accuracy:87.5%

4. Naive Bayes Algorithm
* train data accuracy:52.75080906148867%
* test data accuracy:49.038461538461536%

5. Decision Tree
* train data accuracy:67.63754045307443%
* test data accuracy:53.84615384615384%

6. Random Forest Classifier
* train data accuracy:99.02912621359223%
* test data accuracy:81.73076923076923%
