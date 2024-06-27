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

### Your own coverage tool

<The following is supposed to be repeated for each group member>
<Group member name> Anastasia
<Function 1 name> create_terminal_writer()
<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>
![Screenshot 2024-06-27 at 22 19 26](https://github.com/apanayotova03/pytest/assets/122705116/b4933dba-97e4-4337-acc1-1d77c9afb250)

<Provide a screenshot of the coverage results output by the instrumentation>
New branch coverage: 100%
![Screenshot 2024-06-27 at 22 20 47](https://github.com/apanayotova03/pytest/assets/122705116/e2c5a548-2373-4c05-9710-31666b811296)


<Function 2 name> def _strtobool()

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

<Provide a screenshot of the coverage results output by the instrumentation>

New branch coverage: 100%


## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name> Anastasia

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>
![Screenshot 2024-06-27 at 22 21 40](https://github.com/apanayotova03/pytest/assets/122705116/9ef88a09-957d-4a18-90cc-b7ae1c855155)


<Provide a screenshot of the old coverage results (the same as you already showed above)>

Previous branch coverage: 50%

![Screenshot 2024-06-27 at 22 22 09](https://github.com/apanayotova03/pytest/assets/122705116/372df057-4d83-4435-abdd-2a5669de463a)


<Provide a screenshot of the new coverage results>

New branch coverage: 100%


<State the coverage improvement with a number and elaborate on why the coverage is improved>

The branch coverage has doubled from 50% to 100%. The reason is because the previous tests did not check every case, for example the case when the colour option was either set to “yes” or “no”. However, the new test checks for all four different cases.


<Test 2>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>




<Provide a screenshot of the old coverage results (the same as you already showed above)>
Previous branch coverage: 0%


<Provide a screenshot of the new coverage results>


<State the coverage improvement with a number and elaborate on why the coverage is improved>

The branch coverage has improved from 0% to 100%. In the original test, neither of the branches were covered, possibly due to the fact that the function was not called. However, the new test checks all 3 different branches, creating a branch coverage of 100%.

























<Group member name> Ana Alexandra Cornea 

<Function 1 name> fullwidth() 

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

![Screenshot 2024-06-27 210356](https://github.com/apanayotova03/pytest/assets/156057178/4f5a7560-c200-4f0d-b553-93755a86344f)
![Screenshot 2024-06-27 210441](https://github.com/apanayotova03/pytest/assets/156057178/c162d918-39ce-4b13-b2d0-51b5f75fb1c8)


<Provide a screenshot of the coverage results output by the instrumentation>


 ![Screenshot 2024-06-27 210504](https://github.com/apanayotova03/pytest/assets/156057178/56d347ab-74a6-4885-afc3-e84d45265f8c)


<Function 2 name> markup()

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>
![Screenshot 2024-06-27 215350](https://github.com/apanayotova03/pytest/assets/156057178/784dfa9e-9293-4688-949c-1fa35f702649)
![Screenshot 2024-06-27 215533](https://github.com/apanayotova03/pytest/assets/156057178/17bf91a8-bf07-46f0-a932-6a0779a35a5d)


<Provide a screenshot of the coverage results output by the instrumentation>

 ![Screenshot 2024-06-27 215042](https://github.com/apanayotova03/pytest/assets/156057178/14d8f6bb-4338-4415-89b0-597d18c7e112)

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name> Ana Alexandra Cornea

<Test 1>
<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>
![Screenshot 2024-06-27 215942](https://github.com/apanayotova03/pytest/assets/156057178/fbfa596b-95e1-4f51-ba0c-ddda460ca119)
![Screenshot 2024-06-27 220012](https://github.com/apanayotova03/pytest/assets/156057178/3ae252b4-f04e-4176-8b70-146de30496e2)

<Provide a screenshot of the old coverage results (the same as you already showed above) & a screenshot of the new coverage results>

![Screenshot 2024-06-27 212450](https://github.com/apanayotova03/pytest/assets/156057178/3fe740eb-a8d8-4b1a-8b37-f6e044805e80)



<Provide a screenshot of the new coverage results>
 
![image](https://github.com/apanayotova03/pytest/assets/156057178/a277b960-5452-41f2-9a14-56b9910b4c5b)

<State the coverage improvement with a number and elaborate on why the coverage is improved>
From the images above, we can see that the initial coverage was only 50% due to the “If” statement not being executed. However, I successfully increased the coverage to 83%, achieving an improvement of 33%

<Test 2>
<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>
![Screenshot 2024-06-27 222452](https://github.com/apanayotova03/pytest/assets/156057178/bb347c21-0045-4fd3-995c-63f3174d0a0b)
![Screenshot 2024-06-27 222631](https://github.com/apanayotova03/pytest/assets/156057178/835609ca-5553-47ea-b223-352410592ffa)

<Provide a screenshot of the old coverage results (the same as you already showed above) & a screenshot of the new coverage results>
![Screenshot 2024-06-27 221143](https://github.com/apanayotova03/pytest/assets/156057178/290aae94-31b6-4c2e-b684-b3ff0c23d2e4)

<Provide a screenshot of the new coverage results>
 
![image](https://github.com/apanayotova03/pytest/assets/156057178/2f54e02e-5955-4f5a-afde-8668894bfe42)

<State the coverage improvement with a number and elaborate on why the coverage is improved>
From the images above, we can see that the initial coverage was only 61% due to two of the “If” statements not being executed. However, I successfully increased the coverage to 100%, achieving an improvement of  39%.
















<Group member name> Liang Laura Moragues Hincapie

<Function 1 name> get_terminal_width()

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>


<Provide a screenshot of the coverage results output by the instrumentation>


<Function 2 name> _highlight

<Provide the same kind of information provided for Function 1>

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name> Liang Laura Moragues Hincapie

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>


<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>


<State the coverage improvement with a number and elaborate on why the coverage is improved>

New branch coverage is 100%

<Test 2>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>






<Group member name> Anda Gabriela Barbu

<Function 1 name> should_do_markup()

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>
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




<Provide a screenshot of the coverage results output by the instrumentation>













<Function 2 name>

<Provide the same kind of information provided for Function 1>

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name>

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>



















### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>
