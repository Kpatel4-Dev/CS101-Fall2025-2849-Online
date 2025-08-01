
# Create a Carbon Footprint Calculation Program

_Learning Objectives: Demonstrate an understanding of how to write functions. Demonstrate effective use of console input and output._ 

## Introduction
[Greenhouse gases](https://www.epa.gov/ghgemissions/overview-greenhouse-gases) (GHG) are gases that trap heat in the atmosphere. Humans are contributing to the creation of more GHG every second. 

One of the first steps to reducing GHG is understanding how much of a footprint you are leaving on your planet.  
[Simple calculator for your carbon footprint](https://www.nature.org/en-us/get-involved/how-to-help/carbon-footprint-calculator/#:~:text=A%20carbon%20footprint%20is%20the,highest%20rates%20in%20the%20world.)

In this lab you are going to create a function in Python. [This spreadsheet](https://drive.google.com/file/d/1X2hB1dmH291D-Rtd6HE8lPt3YaH64IYb/view?usp=sharing) has all of the information you will need. 

## Directions
### Step 1
Fill in your names and the date at the top of the page. Note the three quotes ''' before and after this section. Those make a _block comment_, something useful for people to read but that the compiler should not use to run the program.

### Step 2
Write a **calc\_car\_emissions** function in the appropriate section of main.py. You will need to use the keyword _def_ which tells the compiler this is a function definition. After the name of the method are parentheses around words which we call _parameters_. These are inputs for the function, like the little orange variables in the Snap! custom block editor.
*	_mpg_: vehicle's average miles per gallon
*	_avg\_miles\_driven_: average number of miles driven per year

Inside the definition put you will calculate the annual carbon produced and return the result.

The formula is in [this spreadsheet](https://drive.google.com/file/d/1X2hB1dmH291D-Rtd6HE8lPt3YaH64IYb/view?usp=sharing) in the **Assumptions** tab cell C9 (*Please make sure you open the speadsheet in Google Sheets in order to view the equations*).  

The _return_ keyword is like report in Snap!, it gives the output of the function. Python requires lines of code to be positioned in a particular way to run properly. Be sure these two lines are indented one level (i.e. tab in) from where the header starts.

Click Run and fix any errors.

### Step 3
In the *main* section of the code at the bottom get values for mpg and average miles driven from the user using the _input_ keyword. 

Call the calc_car_emissions function with the user input and print the result to the console.

  Enter your average mpg: 30
  Enter your average yearly miles driven: 5000
  Your car produces 3311.37 pounds of CO2 per year.

### Step 4
Add to your program several more function calls to compare the user's vehicle use with others.

Tell the user what the average car produces by using the values from the spreadsheet.

Tell the user what their carbon production would be if they improved their mpg by 2.

  If your mpg was 32 mpg, then your car emissions would be 3104.4095286365937 pounds of CO2 per year. That's 206.96063524243937 pounds less!

Tell the user what their carbon production would be if they improved their average miles driven by 10%.

  If you drove 10% less miles, then your annual car emissions would be 2980.23314749113 pounds of CO2 per year. That's 331.13701638790326 pounds less!

### Step 5
Notice how in the output there are a lot of numbers after the decimal point. Let's clean that up by using formatted output.

The output should now look like:

  Enter your average mpg: 30
  Enter your average yearly miles driven: 5000

  Your car produces 3311.37 pounds of CO2 per year.

  The average US car produces 2417.30 pounds of CO2 per year.

  If your mpg was 32, then your car emissions would be 3104.41 pounds of CO2 per year. That's about 207 pounds less!

  If you drove 10% less miles, then your annual car emissions would be 2980.23 pounds of CO2 per year. That's about 331.1 pounds less!

Make sure that yours matches the expected output. To test it, click on the checkmark in the left menu. Select "run tests". Make any changes needed to get the tests to pass.

When you are all done, click Submit in the upper right corner.
