# Report for Assignment 1

## Project chosen

Name: Pytest

URL: https://github.com/pytest-dev/pytest/tree/main

Number of lines of code and the tool used to count it: 77.686 - lizard
![Screenshot 2024-06-27 at 22 16 31](https://github.com/apanayotova03/pytest/assets/122705116/d227c09a-97b9-4d79-a9f8-93f7f5c58616)

Programming language: Python

## Coverage measurement

### Existing tool

<Inform the name of the existing tool that was executed and how it was executed>

We used tox to run the tests and measured their coverage using coverage.py. The specific commands that were used are:

$ tox

$ coverage html

This allowed us to run all tests in the repository and summarised the coverage of each test in an html file. Here is a screenshot of the results:



The results indicate that the tests have a branch coverage of 38% on the program.

<Show the coverage results provided by the existing tool with a screenshot>

 ![Screenshot 2024-06-27 at 22 18 22](https://github.com/apanayotova03/pytest/assets/122705116/74aedda1-54a4-4a50-bd9b-8af833493ef8)

## Your own coverage tool
# Member:  Anastasia
## Function 1: create_terminal_writer()
### Patch image of modified code: 

![image](https://github.com/apanayotova03/pytest/assets/156092269/07e74987-cd23-4525-9388-8a96281119cd)
![image](https://github.com/apanayotova03/pytest/assets/156092269/76bb2404-7b2f-4229-a896-13cc93a1c480)





### Coverage results with our implementation: 
New branch coverage: 100%

 ![Screenshot 2024-06-27 at 22 20 47](https://github.com/apanayotova03/pytest/assets/122705116/e2c5a548-2373-4c05-9710-31666b811296)


## Function 2: def _strtobool()

### Patch image of modified code: 

![image](https://github.com/apanayotova03/pytest/assets/156092269/ae1c1a16-426e-4971-b2ae-a6e36fd0278d)
![image](https://github.com/apanayotova03/pytest/assets/156092269/139f172b-e23d-4699-9932-7997fb8404c4)
![image](https://github.com/apanayotova03/pytest/assets/156092269/928653f0-3663-450f-bc89-65f08a2d2e54)




### Coverage results with our implementation: 

New branch coverage: 100%
![image](https://github.com/apanayotova03/pytest/assets/156092269/f4264791-b691-45e4-b21d-c2adb41bf993)


## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

# Member:  Anastasia

### Test 1

### Patch with enhanced test: 
![image](https://github.com/apanayotova03/pytest/assets/156092269/8b508bbb-5b7c-471b-a558-2513689713d5)



### Old coverage results: 

Previous branch coverage: 50%

![image](https://github.com/apanayotova03/pytest/assets/156092269/64ad6395-7688-452a-ba9a-5cef40d23889)



### New coverage results: 

New branch coverage: 100%
![image](https://github.com/apanayotova03/pytest/assets/156092269/aa841d25-e253-4285-ae90-83ddd731e9eb)


<State the coverage improvement with a number and elaborate on why the coverage is improved>

The branch coverage has doubled from 50% to 100%. The reason is because the previous tests did not check every case, for example the case when the colour option was either set to “yes” or “no”. However, the new test checks for all four different cases.


### Test 2

### Patch with enhanced test: 

![image](https://github.com/apanayotova03/pytest/assets/156092269/6d73bccb-8e4b-4f97-b372-41d95145e3d6)



### Old coverage results: 
Previous branch coverage: 0%
![image](https://github.com/apanayotova03/pytest/assets/156092269/e1626aaa-fb84-409e-b720-d4739a813340)


### New coverage results: 
![image](https://github.com/apanayotova03/pytest/assets/156092269/ee6221ba-318c-492f-8b68-507aaec23fe3)


<State the coverage improvement with a number and elaborate on why the coverage is improved>

The branch coverage has improved from 0% to 100%. In the original test, neither of the branches were covered, possibly due to the fact that the function was not called. However, the new test checks all 3 different branches, creating a branch coverage of 100%.
























## Your own coverage tool

# Member:  Ana Alexandra Cornea 

## Function 1: fullwidth() 

### Patch image of modified code: 
 


### Coverage results with our implementation: 


## Function 2:

<Provide the same kind of information provided for Function 1>

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

# Member:  Ana Alexandra Cornea

### Test 1



### Old coverage results: 

### New coverage results: 

<State the coverage improvement with a number and elaborate on why the coverage is improved>

### Test 2

<Provide the same kind of information provided for Test 1>













### Patch image of modified code: 

### Coverage results with our implementation: 

### New coverage results: 

<State the coverage improvement with a number and elaborate on why the coverage is improved>











## Your own coverage tool

# Member:  Liang Laura Moragues Hincapie

## Function 1: get_terminal_width()

### Patch image of modified code: 


![Screenshot 2024-06-27 at 20 52 00](https://github.com/apanayotova03/pytest/assets/122705116/7e518922-3e79-497f-b7ac-b6c4a35af2a7)


### Coverage results with our implementation: 


![Screenshot 2024-06-27 at 20 28 22](https://github.com/apanayotova03/pytest/assets/122705116/80f3e018-1ed5-46e0-bcdb-12e7ce8e6806)


## Function 2: _highlight
### Patch image of modified code: 
### Coverage results with our implementation: 


## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

# Member:  Liang Laura Moragues Hincapie

### Test 1

### Patch with enhanced test: 

![Screenshot 2024-06-27 at 20 52 23](https://github.com/apanayotova03/pytest/assets/122705116/6fcf0773-a25b-4744-93e0-43f76fc5ac45)


### Old coverage results: 

![Screenshot 2024-06-27 at 21 12 50](https://github.com/apanayotova03/pytest/assets/122705116/6138f1d1-6bf5-4dbb-98d9-548d4861d592)


### New coverage results: 

![WhatsApp Image 2024-06-27 at 20 23 12](https://github.com/apanayotova03/pytest/assets/122705116/da1fec93-531d-4838-936d-16f45096b7da)

<State the coverage improvement with a number and elaborate on why the coverage is improved>

New branch coverage is 100% DEVELOP


### Test 2

### Patch with enhanced test: 

![Screenshot 2024-06-27 at 22 32 22](https://github.com/apanayotova03/pytest/assets/122705116/c829617e-8b2a-4c17-ad76-efe8c54ce5a3)


### Old coverage results: 


![Screenshot 2024-06-27 at 22 45 38](https://github.com/apanayotova03/pytest/assets/122705116/94127838-632c-4f40-9761-41e266192cb1)


### New coverage results: 

 ![WhatsApp Image 2024-06-27 at 20 23 12](https://github.com/apanayotova03/pytest/assets/122705116/544eeddd-e0ac-4b7c-b0fc-b114997e97d5)


<State the coverage improvement with a number and elaborate on why the coverage is improved>

The coverage is 100%


## Your own coverage tool
## Member:  Anda Gabriela Barbu

## Function 1: should_do_markup()

### Patch image of modified code: 
The code of the new test after creating a branch array


def test():
    # Branch Id 1
    os.environ["PY_COLORS"] = "1"
    test = should_do_markup(None)
    del os.environ["PY_COLORS"]
    assert test == True


    os.environ["PY_COLORS"] = "0"
    test = should_do_markup(None)
    del os.environ["PY_COLORS"]
    assert test == False


    # Branch Id 3
    os.environ["NO_COLOR"] = "1"
    test = should_do_markup(None)
    del os.environ["NO_COLOR"]
    assert test == False


    # Branch Id 4
    os.environ["FORCE_COLOR"] = "1"
    test = should_do_markup(None)
    del os.environ["FORCE_COLOR"]
    assert test == True


    # Branch Id 5
    test = should_do_markup(None)
    assert test == False


    os.environ["PY_COLORS"] = "1"
if __name__ == "__main__":
    test()




### Coverage results with our implementation: 













## Function 2:

<Provide the same kind of information provided for Function 1>

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

# Member: 

### Test 1

### Patch with enhanced test: 

### Old coverage results: 

### New coverage results: 

<State the coverage improvement with a number and elaborate on why the coverage is improved>

### Test 2

### Patch with enhanced test: 

### Old coverage results: 

### New coverage results: 

<State the coverage improvement with a number and elaborate on why the coverage is improved>



















### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>
