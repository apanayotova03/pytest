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

## Member:  Ana Alexandra Cornea 

### Function 1: fullwidth() 



#### Coverage results with our implementation: 



### Patch image of modified code: 

![image](https://github.com/apanayotova03/pytest/assets/156092269/ae1c1a16-426e-4971-b2ae-a6e36fd0278d)
![image](https://github.com/apanayotova03/pytest/assets/156092269/139f172b-e23d-4699-9932-7997fb8404c4)
![image](https://github.com/apanayotova03/pytest/assets/156092269/928653f0-3663-450f-bc89-65f08a2d2e54)



### Function 2:markup()
![Screenshot 2024-06-27 210504](https://github.com/apanayotova03/pytest/assets/156057178/56d347ab-74a6-4885-afc3-e84d45265f8c)



### Patch image of modified code: 
![Screenshot 2024-06-27 215350](https://github.com/apanayotova03/pytest/assets/156057178/784dfa9e-9293-4688-949c-1fa35f702649)
![Screenshot 2024-06-27 215533](https://github.com/apanayotova03/pytest/assets/156057178/17bf91a8-bf07-46f0-a932-6a0779a35a5d)


#### Coverage results with our implementation: 

 ![Screenshot 2024-06-27 215042](https://github.com/apanayotova03/pytest/assets/156057178/14d8f6bb-4338-4415-89b0-597d18c7e112)

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

## Member:  Ana Alexandra Cornea

### Test 1
![Screenshot 2024-06-27 215942](https://github.com/apanayotova03/pytest/assets/156057178/fbfa596b-95e1-4f51-ba0c-ddda460ca119)
![Screenshot 2024-06-27 220012](https://github.com/apanayotova03/pytest/assets/156057178/3ae252b4-f04e-4176-8b70-146de30496e2)

#### Old coverage results: 

  ![Screenshot 2024-06-27 212450](https://github.com/apanayotova03/pytest/assets/156057178/3fe740eb-a8d8-4b1a-8b37-f6e044805e80)
  
### New coverage results: 
 ![image](https://github.com/apanayotova03/pytest/assets/156057178/a277b960-5452-41f2-9a14-56b9910b4c5b)


<State the coverage improvement with a number and elaborate on why the coverage is improved>
From the images above, we can see that the initial coverage was only 50% due to the “If” statement not being executed. However, I successfully increased the coverage to 83%, achieving an improvement of 33%











#### Patch image of modified code: 

  ![Screenshot 2024-06-27 222452](https://github.com/apanayotova03/pytest/assets/156057178/bb347c21-0045-4fd3-995c-63f3174d0a0b)
![Screenshot 2024-06-27 222631](https://github.com/apanayotova03/pytest/assets/156057178/835609ca-5553-47ea-b223-352410592ffa)
  
#### Coverage results with our implementation: 
![Screenshot 2024-06-27 221143](https://github.com/apanayotova03/pytest/assets/156057178/290aae94-31b6-4c2e-b684-b3ff0c23d2e4)
### New coverage results: 
  ![image](https://github.com/apanayotova03/pytest/assets/156057178/2f54e02e-5955-4f5a-afde-8668894bfe42)


<State the coverage improvement with a number and elaborate on why the coverage is improved>
From the images above, we can see that the initial coverage was only 61% due to two of the “If” statements not being executed. However, I successfully increased the coverage to 100%, achieving an improvement of  39%.












## Your own coverage tool

## Member:  Liang Laura Moragues Hincapie

### Function 1: get_terminal_width()

#### Patch image of modified code: 


![Screenshot 2024-06-27 at 20 52 00](https://github.com/apanayotova03/pytest/assets/122705116/7e518922-3e79-497f-b7ac-b6c4a35af2a7)


#### Coverage results with our implementation: 


![Screenshot 2024-06-27 at 20 28 22](https://github.com/apanayotova03/pytest/assets/122705116/80f3e018-1ed5-46e0-bcdb-12e7ce8e6806)


### Function 2: _highlight

#### Patch image of modified code: 

![Screenshot 2024-06-27 at 22 32 22](https://github.com/apanayotova03/pytest/assets/122705116/22929e68-caa8-43f5-82d5-d12183d1b9d9)

#### Coverage results with our implementation: 

![Screenshot 2024-06-27 at 23 20 07](https://github.com/apanayotova03/pytest/assets/122705116/1387eba5-48d9-4482-898e-58a12bd929c6)


## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

## Member:  Liang Laura Moragues Hincapie

### Test 1

#### Patch with enhanced test: 

![Screenshot 2024-06-27 at 20 52 23](https://github.com/apanayotova03/pytest/assets/122705116/6fcf0773-a25b-4744-93e0-43f76fc5ac45)


#### Old coverage results: 

![Screenshot 2024-06-27 at 21 12 50](https://github.com/apanayotova03/pytest/assets/122705116/6138f1d1-6bf5-4dbb-98d9-548d4861d592)


### New coverage results: 

![WhatsApp Image 2024-06-27 at 20 23 12](https://github.com/apanayotova03/pytest/assets/122705116/da1fec93-531d-4838-936d-16f45096b7da)

<State the coverage improvement with a number and elaborate on why the coverage is improved>

The coverage improvement is 100% as full branch coverage for the get_width function. This means that every possible execution path 
within the function has been systematically tested. Various scenarios, such as when the terminal width is greater than or less than 40 pixels, 
have been specifically designed to ensure thorough validation. The coverage improvement is 100% since we managed to test every test possible so it goes through all branches.

### Test 2

#### Patch with enhanced test: 

![Screenshot 2024-06-27 at 22 32 22](https://github.com/apanayotova03/pytest/assets/122705116/c829617e-8b2a-4c17-ad76-efe8c54ce5a3)


#### Old coverage results: 


![Screenshot 2024-06-27 at 22 45 38](https://github.com/apanayotova03/pytest/assets/122705116/94127838-632c-4f40-9761-41e266192cb1)


### New coverage results: 

 ![WhatsApp Image 2024-06-27 at 20 23 12](https://github.com/apanayotova03/pytest/assets/122705116/544eeddd-e0ac-4b7c-b0fc-b114997e97d5)


<State the coverage improvement with a number and elaborate on why the coverage is improved>

The coverage improvement is 100% because thorough testing has ensured complete branch coverage in the _highlight method of the TerminalWriter class. This means that every possible path through the method's logic has been tested, including scenarios where hasmarkup and code_highlight are both true, when one or both are false and cases where the Pygments lexer or formatter is unavailable. By designing test cases that cover these conditions and using mocking to isolate dependencies like _get_pygments_lexer and _get_pygments_formatter, the tests verify that _highlight behaves as expected in all situations.




## Your own coverage tool
### Member:  Anda Gabriela Barbu

### Function 1: should_do_markup()

#### Patch image of modified code: 
![image](https://github.com/apanayotova03/pytest/assets/156002940/37edd183-00d6-4a73-82d8-34cfe61e73ee)

![image](https://github.com/apanayotova03/pytest/assets/156002940/7870477a-f208-4092-bec0-4a5bff1ff884)


#### Coverage results with our implementation: 
![image](https://github.com/apanayotova03/pytest/assets/156002940/29e30760-02c2-4675-844e-a93ff19d27be)













### Function 2: wcwidth()

#### Patch image of modified code: 
![image](https://github.com/apanayotova03/pytest/assets/156002940/c011ee33-d3ac-496c-84ba-83b1fefb685e)
![image](https://github.com/apanayotova03/pytest/assets/156002940/785be5b5-f059-43e3-99c2-7f4939247991)



#### Coverage results with our implementation: 

![image](https://github.com/apanayotova03/pytest/assets/156002940/f6d25146-d5dc-47a2-9c30-dab9e587b1b5)



## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

## Member: Anda Barbu

### Test 1

#### Patch with enhanced test: 
![image](https://github.com/apanayotova03/pytest/assets/156002940/32cf2056-d10a-4ee3-a629-f9986a2c14fc)
![image](https://github.com/apanayotova03/pytest/assets/156002940/94afda0a-03a0-40b3-a9e4-d88eb65d6020)

#### Old coverage results: 
![image](https://github.com/apanayotova03/pytest/assets/156002940/618fd389-12f9-49e7-ac15-456ba22aa794)

### New coverage results: 
![image](https://github.com/apanayotova03/pytest/assets/156002940/0c9af461-3b83-4a12-9b59-2907cbb742dc)

<State the coverage improvement with a number and elaborate on why the coverage is improved>
The new coverage is 93%, the new test takes in consideration all possible cases, for example “if os.environ.get(“NO_COLOR”)” is not tested for the branch where the return is false

 ### Test 2

#### Patch with enhanced test: 
![image](https://github.com/apanayotova03/pytest/assets/156002940/8017d213-0a73-4ed4-aa0b-cd741b549698)
![image](https://github.com/apanayotova03/pytest/assets/156002940/7b3c9d91-fb70-4204-a89d-1889f7112728)

#### Old coverage results: 
![image](https://github.com/apanayotova03/pytest/assets/156002940/10a1ca01-67e8-43c1-86de-a05c0302c576)

### New coverage results: 
![image](https://github.com/apanayotova03/pytest/assets/156002940/4a63bc95-6f9d-410d-9aef-b3ee2a579b6c)

<State the coverage improvement with a number and elaborate on why the coverage is improved>
The new coverage is 100%, the new test takes all the cases for the ifs, for example “if category == “Cc”) is not covered at all in the initial test










### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

![WhatsApp Image 2024-06-27 at 23 52 50](https://github.com/apanayotova03/pytest/assets/122705116/6f22a5e0-ee53-49ce-8f4c-b8bb96ee60db)


## Statement of individual contributions

<Write what each group member did>
