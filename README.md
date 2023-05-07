# theRetrieval_Zone@iiit

NOTE: This website must be run on the terminal using the command "python3 app.py". This starts the flask application. The link thus generated directs to the sign-in page from which the user can access all the functionalities of the website.  





Welcome to 'theRetrieval_Zone@iiit', where you can find what you lost, borrow what you need,and buy what what you want. It is IIIT Hyderabad's Hub for Campus Sharing.   
Our application provides a convenient and efficient way for users to connect and share resources, and helps build a stronger and more collaborative campus community.

Here are some guidelines for operating this app -
1. First the student has to sign in/up with their College Roll No. 
2. After signing in, the student gets redirected to the home page, from where they can select their purpose of visiting the website.
3. If the student has LOST something, they get redirected to the page where all the items found around the campus are listed. If the item they have lost is present in the list, they can contact the person who has found that item. Otherwise, they can click on the NOT HERE! button which redirects them to a form where they can enter the details of the lost item. If someone else finds the item, they can inform the student.
4. If a student wants to sell/lend something they doesn't use anymore, they can fill the form sharing the details of the item they have lost so that a person willing to buy/borrow it can contact them.
5. If a student has found something around the campus and wants to help return the item to it's owner, they are first redirected to the list of items people have lost. If the item they have found is already present, they can directly contact the owner from the details on the page. Else, they can click on the NOT HERE! button and fill the form by entering the details of the item they have found.
6. If a student wants to BUY/BORROW something they can click on the respective buttons to view the list of items up for selling/lending and contact the aforementioned person for the same.
7. If the student wants to view abut the items they have listed in the past, they can go to the profile page. They can also remove the items they have listed if the purpose of listing them is now fulfilled.


Contribution of Each Member:
Vasana Srinivasan (2022101023):
Contributed towards the idea behind the designing of the application and handled the Frontend. Also contributed towards creating the database as well as the backend of the Sell/Lend, Found, and Lost pages.  
Gargi Shroff (2022114009):
Contibuted towards managing the database and fitering out the information from the database, as well as the backend of the Sign-in/Sign-Out, Buy/Borrow, Found, Lost, and Home pages. 
Heamanth Sunkireddy (2022101005):
Contributed towards the Student Profile Page and Navigation bar, and managing the database. 
## All the members contributed for deciding the functionality of the application.

The detailed directory structure for our app is as follows:
```
.
└── ISS_Hackhaton-main
    ├── app.py
    ├── README.md
    ├── static
    │   ├── css
    │   │   ├── index.css
    │   │   └── navbar.css
    │   ├── js
    │   │   └── index.js
    │   └── logo.jpeg
    └── templates
        ├── borrow.html
        ├── buy.html
        ├── foundView.html
        ├── homepage.html
        ├── index.html
        ├── lostfoundAdd.html
        ├── lostView.html
        ├── sell.html
        └── studentProfile.html

5 directories, 16 files
```
