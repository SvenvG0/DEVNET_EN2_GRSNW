# Lab 2: EXPLORE REST APIs WITH API SIMULATOR AND POSTMAN
## Part 1: Explore API Documentation Using the API Simulator
### Task preparation and implementation:
- Study the API's formats:
    - Requests
    - Responses
    - Headers
    - Parameters

>[!TIP]
>Look in the school library: http://library.demo.local/api/v1/docs

>[!NOTE]
>Notice the downward arrow to the far right. Clicking anywhere on the /api/v1 bar will minimize the API list
and turn the arrow facing right. Click again on the same bar to re-display the API list.
Notice the lock to the far right of several of the APIs. The lock indicates that these APIs require a token to
be used. 

#### Get Books
Click on `GET /Books` to see the content of this API. Notice the different aspects:
- Parameters
- Response content type
- Code

Click `Try it out` to test the API.
Give the following parameters (try it with and without):
- includeISBN
    - true
- SortBy
    - id

Now click on `Execute`

>[!Important]
>The respons section has changed and now contains the respons based on your request. Depending on the parameters you filled, your results will change.

Take a look at the curl and the responsbody.
The responsbody contains the data in json format.

>[!Warning]
> if you changed the respons content type, this will differ.

The curl can be used in your terminal to get the same data.
To try this out, copy the curl into your terminal and hit enter.
> curl -X GET "http://library.demo.local/api/v1/books?includeISBN=true&sortBy=id" -H "accept: application/json"

Minimize `Get /Books`
 
#### POST loginViaBasic
Click on "POST /loginViaBasic to see the content of this API. Notice the different aspects:
- Parameters is empty

Click `Try it out` and then `Execute` to test the API.
Fill in the credentials:
- Username: cisco
- Password: Cisco123!

in the responsbody you'll find the token:
>{ \
  "token": "cisco|R3h4SSLs-7tl4kbAjyHBJ9NYmO8SBJ41MGRnX_ZUP-0" \
}

>[!Warning]
>Your token will be different!

Scroll up to the top of the page and locate the green `Authorize` button. Click on it and paste your token after `Value`. Click on `Authorize`.

>[!NOTE]
>Note that the **Name** is **X-API-KEY**. We'll use this later in POSTMAN along with the token.

Close the pop-up window and minimize `POST /loginViaBasic`.

#### POST books
Click the API POST /books to see the content of this API. Notice the different aspects:
- Under Parameters, the payload is required. 

>[!NOTE] 
>This means that this API requires information for
>this parameter in the format specified by the Parameter content type, which is JSON.

Click "Try it out".

Modify the id, title and author with the information shown below.
>{
 "id": 4, \
 "title": "IPv6 Fundamentals", \
 "author": "Rick Graziani" \
}

Click Execute.

>[!NOTE]
>You should see the book you added in the Response body along with a new id. You will also
see updated information for curl and the Request URL.

Try it again with another:
>{ \
 "id": 5, \
 "title": "31 Days Before Your CCNA Exam", \
 "author": "Allan Johnson" \
}

Click `Execute`.

Click the bar for the API POST /books to minimize.
Go to `Get /books` and try to see if you added the books succesfully.

#### GET /books{id}
- Click the `GET /books{id}` API.
- Enter 4 for the required id.
- Click `Execute`.

#### DELETE /books{id}
- Use what you have learned at `GET /books{id}` to delete the book with id 4
- Check the result with `GET /books` like you learned in previous exercises

### Task troubleshooting:
#### POST books
>[!Important]
>If you got a 401 code, check the Response body text. Most likely you received an "error": \
***"Invalid API key"*** response. This is because you did not enter all the characters for your API key. Or
possibly, you add an unnecessary space. Return to the previous step and repeat the authorization
process.

### Task verification:

>[!Tip]
>You can verify the books were added to the Our Books page. Return to the School Library tab in your
browser (http://library.demo.local) and refresh the page. Be careful not to close the School Library API
tab. If you do, then you will need to reauthenticate.

## Part 2: Use Postman to Make API Calls to the API Simulator
### Task preparation and implementation:
Locate the application Postman on your desktop and open it.

#### GET /books
- Click the plus icon "+" to create an Untitled Request (if not open yet).
- Default = GET
- Enter request URL.

#### POST /loginViaBasic
- Create a new Untitled Request.
- Select POST.
- Enter request URL.
- Authorization:
    - Type: API Key
    - Key: X-API-KEY
    - Value: `<token>` (cisco|R3h4SSLs-7tl4kbAjyHBJ9NYmO8SBJ41MGRnX_ZUP-0)
- Body:
    - Raw: on
    - JSON
    - `<JSON-Code>`

#### POST /books
- Follow similar steps as in the API documentation but use Postman's interface for entering request details and authorization.

### Task troubleshooting:

Take a look at the workings of postman via a video on `youtube`.

### Task verification:

#### GET /books
- Return to the first GET tab in Postman and click Send to see the updated list of books.
- Modify the GET request in Postman to include additional parameters like `includeISBN` and `sortBy`.

## Part 3: Use Python to Add 100 Books to the API Simulator
### Task preparation and implementation:

#### Open Visual Studio (VS) Code and navigate to the school-library directory.
- Open VS Code and navigate to the folder `~/labs/devnet-src/school-library`

#### Investigate the libraries used by the add100RandomBooks.py program.
- Review the Python script and its dependencies (Imports), by clicking on the script. 

>[!NOTE]You will use the Python requests library throughout this course. The requests library is required if you
want to use **Python** to make API requests using GET, POST, DELETE and other HTTP methods.

#### Practice generating random data using the faker library.
- Use Python's faker library to generate fake data for books.
    - Open a terminal window and start Python3.
    - From faker import the Faker() module.
    - Assign the Faker() module to fake.
    - To see all the methods, enter fake. and then press the tab key twice. 
    
>[!NOTE]
>Notice the method fake.name(),
which you will use in the next step. In the next step and later in this lab, you will also use the three
highlighted methods (prefaced with fake.).: catch_phrase(), isbn13(), and name().

Use the terminal with `python3` and the following command to get fake names:
```python 
print('My name is {}.'.format(fake.name()))
```

Now try to use these functions get the following result:
- fake.catch_phrase()
- fake.isbn13()
- fake.name()

>My name is Gary Castaneda and I wrote "Organic incremental neural-net" (ISBN 978-0-
669-01935-3).

Use a while loop to fill the library:
```python
for i in range(10):
    print(fake.name())
```

Quit the interpreter:
```python
quit()
```

#### Review the function variables.
- Examine the variables used in the Python script for adding books.
    - APIHOST
    - LOGIN
    - PASSWORD

#### Review the getAuthToken function.
- Understand how the script authenticates to the API.
>[!Tip]
>Look at the `request.post()` function.

#### Review the addBook function.
- Look at how books are added using the API in the script.

#### Review the code that invokes the two functions.
- Examine how the script uses functions to add books.

#### Run and verify the add100RandomBooks.py program.
- Execute the Python script and verify that books are added to the library

### Task troubleshooting:

>[!Warning]
>Make sure you fill out the POST request correctly in Postman. Otherwise you'll get an error. If the error persists, try to first `Authorize` in the browser.

>[!Important]
>If the call is unsuccessful (HTTP status code is not equal to 200), an exception is raised and printed to the
terminal window. Again, notice the use of an f-string to build the exception message. You can test the
exception code by changing the one of the variables in previous steps.

### Task verification:

Execute the Python script and verify that books are added to the library