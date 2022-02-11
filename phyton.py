workHours = 0
billableHours = 0

projectCode1 = ''
projectWork1 = 0

projectCode2 = ''
projectWork2 = 0

projectCode3 = ''
projectWork3 = 0

total = 0
avg = 0
#Employee enter the project code and hours worked for Day 1:
projectCode1 = str(input("Enter the 1st project code:  "))
projectWork1 = int(input("Enter the number of hours worked on 1st project: "))

projectCode2 = str(input("Enter the 2nd project code:  "))
projectWork2 = int(input("Enter the number of hours worked on 2nd project: "))

projectCode3 = str(input("Enter the 3rd project code:  "))
projectWork3 = int(input("Enter the number of hours worked on 3rd project: "))
# Calculate the total hours worked in  Day 1:
#workHours += hoursWorkedProject1 + hoursWorkedProject2 + hoursWorkedProject3
# Output the total hours:
print('Total hours worked in day 1 over the 3 projects is: ' ,workHours)


# Here you check if you have the project code
def projectCodeCompare(projectCode, workHours):
  if projectCode == projectCode1:
    projectWork1 += workHours
    return true

  if projectCode == projectCode2:
    projectCode2 += workHours
    return true

  if projectCode == projectCode3:
    projectWork3 += workHours
    return true

    return false

#Here you did not find the project code, so you search to replace existing codes

def projectCodeReplace(projectCode, workHours):
  if projectWork1 < workHours

    return

  if projectWork2 < workHours:
    projectCode2 = projectCode
    projectWork2 = workHours

    return

  if projectWork3 < workHours:
    projectCode3 = projectCode
    projectWork3 = workHours

    return

def initState():
  workHours = 0
  projectCode = ''
  projectWork = 0
  billableHours = 0
